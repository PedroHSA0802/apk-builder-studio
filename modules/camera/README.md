# Camera Module for APK Builder Studio

This module provides automatic CameraX integration for Kivy/KivyMD Android applications built with APK Builder Studio.

## What This Module Does

When you add `camera` to your requirements, this module automatically:

1. ✅ Sets up all required Android permissions (CAMERA, RECORD_AUDIO, etc.)
2. ✅ Configures Gradle dependencies for CameraX libraries
3. ✅ Sets Android API to 34 (required for Play Store)
4. ✅ Provides Java source code for native camera integration
5. ✅ Configures buildozer to include Java sources in the APK

## Quick Start

### Step 1: Add Camera to Requirements

In your `buildozer.spec` file, add `camera` to the requirements line:

```ini
requirements = python3,kivy,kivymd,camera
```

### Step 2: Build Your APK

When you build your APK through APK Builder Studio, it will automatically:
- Detect the `camera` requirement
- Copy the Java sources to your project
- Patch your buildozer.spec with necessary configurations
- Build with CameraX support

### Step 3: Use Camera in Your Python Code

See `example_main.py` for a complete working example. Here's the basic pattern:

```python
from kivy.utils import platform

def start_camera():
    if platform == 'android':
        from android.permissions import request_permissions, Permission
        request_permissions([Permission.CAMERA], on_permissions_result)

def on_permissions_result(permissions, grants):
    if all(grants):
        from jnius import autoclass, cast
        
        # Get Android Activity
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        activity = cast('android.app.Activity', PythonActivity.mActivity)
        
        # Load CameraHelper
        CameraHelper = autoclass('org.test.camera.CameraHelper')
        cam_helper = CameraHelper(activity)
        cam_helper.startCamera()
```

## Module Configuration

The `module.json` file contains all configuration:

- **Android API**: 34 (required for Google Play Store as of 2024)
- **Min API**: 24 (Android 7.0)
- **Permissions**: CAMERA, RECORD_AUDIO, WRITE_EXTERNAL_STORAGE, READ_MEDIA_IMAGES
- **CameraX Version**: 1.2.2 (stable)
- **Build Tools**: 34.0.0
- **NDK API**: 26

## File Structure

```
modules/camera/
├── module.json                          # Configuration file
├── README.md                            # This file
├── example_main.py                      # Complete Python example
└── java_sources/
    └── org/
        └── test/
            └── camera/
                └── CameraHelper.java    # CameraX implementation
```

## Java API Reference

### CameraHelper Class

Located at: `org.test.camera.CameraHelper`

#### Methods

**`CameraHelper(Activity activity)`**
- Constructor
- Parameters: Android Activity instance

**`void startCamera()`**
- Starts the camera preview overlay
- Displays camera view on top of Kivy interface
- Must be called from UI thread (handled automatically)

**`void takePhoto(String filePath)`**
- Captures a photo to the specified file path
- Parameters: Full path where photo should be saved
- Example: `/storage/emulated/0/DCIM/photo.jpg`

**`void closeCamera()`**
- Removes camera preview overlay
- Cleans up camera resources

## Important Notes

### Permissions

Always request permissions at runtime:
```python
from android.permissions import request_permissions, Permission
request_permissions([Permission.CAMERA, Permission.RECORD_AUDIO], callback)
```

### File Storage

For Android 10+ (API 29+), prefer app-specific directories to avoid storage permission issues:

```python
from android import mActivity
context = mActivity.getApplicationContext()
external_dir = context.getExternalFilesDir(None).getAbsolutePath()
photo_path = f"{external_dir}/photo.jpg"
```

### Lifecycle

The camera preview is overlaid on top of your Kivy app. Make sure to:
1. Call `closeCamera()` when switching screens
2. Keep a reference to the `cam_helper` object (store in `App` instance)
3. Handle app pause/resume events appropriately

## Troubleshooting

### Build Fails with "Cannot resolve androidx.camera"

- Ensure you have internet connection during build
- Check that `android.gradle_dependencies` is set correctly in buildozer.spec
- The first build may take longer as Gradle downloads dependencies

### Camera Preview Not Showing

1. Check permissions were granted
2. Ensure you're testing on a real device (emulators may not have camera)
3. Check Logcat for Java exceptions: `adb logcat | grep CameraHelper`

### App Crashes on Launch

- Verify `android.api = 34` in buildozer.spec
- Check that Java package name matches: `org.test.camera`
- Ensure all CameraX dependencies are included

### Photo Not Saving

- Check file path permissions
- Use app-specific directory instead of external storage
- Verify WRITE_EXTERNAL_STORAGE permission (for API < 29)

## Advanced Usage

### Switch Between Front/Back Camera

Modify `CameraHelper.java`:
```java
// For front camera:
CameraSelector cameraSelector = CameraSelector.DEFAULT_FRONT_CAMERA;
```

### Adjust Image Quality

Modify `ImageCapture` builder in `CameraHelper.java`:
```java
imageCapture = new ImageCapture.Builder()
    .setCaptureMode(ImageCapture.CAPTURE_MODE_MAXIMIZE_QUALITY)
    .build();
```

### Add Video Recording

Extend `CameraHelper.java` with `VideoCapture` use case:
```java
VideoCapture videoCapture = new VideoCapture.Builder().build();
cameraProvider.bindToLifecycle(activity, cameraSelector, preview, videoCapture);
```

## Version History

### v1.0.0
- Initial release
- CameraX 1.2.2 integration
- API 34 support
- Basic photo capture functionality

## License

This module is part of APK Builder Studio and follows the same license terms.

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Review the example code in `example_main.py`
3. Open an issue on the APK Builder Studio repository

## Credits

Built for APK Builder Studio by the community.
CameraX is developed by Google and licensed under Apache 2.0.
