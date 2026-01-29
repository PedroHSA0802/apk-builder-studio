"""
Example Python code for integrating CameraX with Kivy/KivyMD

This file demonstrates how to use the CameraHelper Java class
from Python using pyjnius after the camera module is set up.

Prerequisites:
1. Add 'camera' to your requirements in buildozer.spec
2. The APK Builder Studio will automatically set up the module
3. Build and run on Android device

Usage:
- Call start_camera() to display the camera preview
- Call take_photo() to capture an image
- Call close_camera() to remove the preview
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.utils import platform
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton


class CameraApp(MDApp):
    """Example KivyMD app with CameraX integration"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cam_helper = None
    
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Start Camera Button
        start_btn = MDRaisedButton(
            text="Start Camera",
            on_release=self.start_camera_clicked,
            size_hint=(1, None),
            height="56dp"
        )
        
        # Take Photo Button
        photo_btn = MDRaisedButton(
            text="Take Photo",
            on_release=self.take_photo_clicked,
            size_hint=(1, None),
            height="56dp"
        )
        
        # Close Camera Button
        close_btn = MDRaisedButton(
            text="Close Camera",
            on_release=self.close_camera_clicked,
            size_hint=(1, None),
            height="56dp"
        )
        
        layout.add_widget(start_btn)
        layout.add_widget(photo_btn)
        layout.add_widget(close_btn)
        
        return layout
    
    def start_camera_clicked(self, instance):
        """Handle start camera button click"""
        if platform == 'android':
            from android.permissions import request_permissions, Permission
            request_permissions([Permission.CAMERA, Permission.RECORD_AUDIO], 
                              self.on_permissions_result)
        else:
            print("Camera is only available on Android!")
    
    def on_permissions_result(self, permissions, grants):
        """Callback after permission request"""
        if all(grants):
            print("Permissions granted, starting camera...")
            self.start_camera_java()
        else:
            print("Camera permissions denied!")
    
    def start_camera_java(self):
        """Initialize and start the CameraX preview"""
        try:
            from jnius import autoclass, cast
            
            # Get the current Android Activity
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            currentActivity = cast('android.app.Activity', PythonActivity.mActivity)
            
            # Load our CameraHelper Java class
            CameraHelper = autoclass('org.test.camera.CameraHelper')
            
            # Create instance and start camera
            self.cam_helper = CameraHelper(currentActivity)
            self.cam_helper.startCamera()
            
            print("Camera preview started successfully!")
        except Exception as e:
            print(f"Error starting camera: {e}")
    
    def take_photo_clicked(self, instance):
        """Handle take photo button click"""
        if self.cam_helper:
            # Define path for the photo
            # On Android, use app-specific directory to avoid storage permissions
            from android import mActivity
            context = mActivity.getApplicationContext()
            external_dir = context.getExternalFilesDir(None).getAbsolutePath()
            photo_path = f"{external_dir}/photo.jpg"
            
            self.cam_helper.takePhoto(photo_path)
            print(f"Photo will be saved to: {photo_path}")
        else:
            print("Camera not started yet!")
    
    def close_camera_clicked(self, instance):
        """Handle close camera button click"""
        if self.cam_helper:
            self.cam_helper.closeCamera()
            self.cam_helper = None
            print("Camera closed")
        else:
            print("Camera not running")


if __name__ == '__main__':
    CameraApp().run()
