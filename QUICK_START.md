# 📷 Camera Module Quick Start

Get camera functionality in your Android app in 3 easy steps!

## Step 1: Add to Requirements

Edit your `buildozer.spec` file and add `camera` to requirements:

```ini
requirements = python3,kivy,kivymd,pyjnius,camera
```

## Step 2: Build Your APK

Build your APK using APK Builder Studio. The camera module will be automatically configured:
- ✅ Permissions added
- ✅ CameraX libraries included  
- ✅ Java sources integrated
- ✅ API 34 configured

## Step 3: Use Camera in Your App

Copy this minimal example to your `main.py`:

```python
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import platform
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton


class CameraApp(MDApp):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        btn = MDRaisedButton(
            text="Start Camera",
            on_release=self.start_camera,
            size_hint=(1, None),
            height="56dp"
        )
        layout.add_widget(btn)
        return layout
    
    def start_camera(self, instance):
        if platform == 'android':
            from android.permissions import request_permissions, Permission
            request_permissions([Permission.CAMERA], self.on_permission)
    
    def on_permission(self, permissions, grants):
        if all(grants):
            from jnius import autoclass, cast
            
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            activity = cast('android.app.Activity', PythonActivity.mActivity)
            
            CameraHelper = autoclass('org.test.camera.CameraHelper')
            self.cam_helper = CameraHelper(activity)
            self.cam_helper.startCamera()


if __name__ == '__main__':
    CameraApp().run()
```

## That's It! 🎉

Your app now has camera functionality. The preview will appear as an overlay on your app.

## Need More?

- **Full Example**: See `modules/camera/example_main.py` for photo capture
- **Documentation**: See `modules/camera/README.md` for advanced features
- **Troubleshooting**: See README.md troubleshooting section

## What You Get

- 📸 Camera preview overlay
- 📷 Photo capture capability
- 🔄 Lifecycle management
- ✅ Permission handling
- 📱 Works on Android 7.0+
- 🏪 Google Play Store ready (API 34)

## Common Next Steps

**Capture a photo:**
```python
# Define where to save
path = "/sdcard/DCIM/photo.jpg"
self.cam_helper.takePhoto(path)
```

**Close camera:**
```python
self.cam_helper.closeCamera()
```

**Check module files:**
```bash
modules/camera/
├── README.md              # Full documentation
├── example_main.py        # Complete working example
└── buildozer.spec.example # Configuration example
```

---

**Having issues?** Check `modules/camera/README.md` troubleshooting section!
