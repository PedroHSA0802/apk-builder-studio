from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.utils import platform
from kivy.properties import ListProperty
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line
import os

if platform == 'android':
    from android.permissions import request_permissions, Permission
    from jnius import autoclass, PythonJavaClass, java_method
    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    CameraXHelper = autoclass('org.kivy.camerax.CameraXHelper')
else:
    PythonActivity = None
    CameraXHelper = None


class FaceOverlay(Widget):
    boxes = ListProperty([])  # normalized 0..1

    def on_boxes(self, instance, value):
        self._redraw()

    def on_size(self, *args):
        self._redraw()

    def on_pos(self, *args):
        self._redraw()

    def _redraw(self):
        self.canvas.after.clear()
        if not self.boxes:
            return
        w, h = self.width, self.height
        with self.canvas.after:
            Color(0, 1, 0, 0.6)
            for i in range(0, len(self.boxes), 4):
                nx1, ny1, nx2, ny2 = self.boxes[i:i + 4]
                x1, y1, x2, y2 = nx1 * w, ny1 * h, nx2 * w, ny2 * h
                Line(rectangle=(x1, y1, x2 - x1, y2 - y1), width=2)


class FaceCallback(PythonJavaClass):
    __javainterfaces__ = ['org/kivy/camerax/CameraXHelper$FaceListener']
    __javacontext__ = 'app'

    def __init__(self, app):
        super().__init__()
        self.app = app

    @java_method('([F)V')
    def onFaces(self, boxes):
        b = list(boxes)  # normalized 0..1
        Clock.schedule_once(lambda dt: self.app.update_faces(b), 0)


class CameraScreen(Screen):
    pass


class VisionApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"

        self.sm = ScreenManager()
        kv_path = os.path.join(os.path.dirname(__file__), "main.kv")
        Builder.load_file(kv_path)
        self.camera_screen = CameraScreen(name='camera')
        self.sm.add_widget(self.camera_screen)

        self.overlay = None

        Clock.schedule_once(self.request_android_permissions, 1)
        return self.sm

    def request_android_permissions(self, dt):
        if platform == 'android':
            request_permissions([Permission.CAMERA], self.on_permission_result)

    def on_permission_result(self, permissions, grants):
        if all(grants):
            self.init_camera_hardware()
        else:
            print("Permission denied by user.")

    def init_camera_hardware(self):
        if platform != 'android':
            return
        try:
            activity = PythonActivity.mActivity
            helper = CameraXHelper.getInstance()

            self.overlay = self.camera_screen.ids.face_overlay

            self.face_callback = FaceCallback(self)  # starke Referenz
            helper.setFaceListener(self.face_callback)

            activity.runOnUiThread(lambda: helper.init(activity))
            print("CameraX successfully started")
        except Exception as e:
            print(f"Hardware Init Error: {e}")

    def update_faces(self, boxes):
        if self.overlay:
            self.overlay.boxes = boxes

    def on_stop(self):
        if platform == 'android':
            activity = PythonActivity.mActivity
            helper = CameraXHelper.getInstance()
            activity.runOnUiThread(lambda: helper.stop(activity))


if __name__ == "__main__":
    VisionApp().run()