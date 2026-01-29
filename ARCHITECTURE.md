# Camera Module Architecture Diagram

## System Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    APK Builder Studio                        │
│                                                              │
│  ┌────────────────────────────────────────────────────┐    │
│  │  buildozer.py                                       │    │
│  │                                                      │    │
│  │  1. detect_camera_requirement()                     │    │
│  │     └─> Parse buildozer.spec                        │    │
│  │     └─> Find "camera" in requirements               │    │
│  │                                                      │    │
│  │  2. load_module_config("camera")                    │    │
│  │     └─> Read modules/camera/module.json             │    │
│  │                                                      │    │
│  │  3. apply_spec_edits()                              │    │
│  │     └─> android.api = 34                            │    │
│  │     └─> android.permissions = CAMERA,RECORD_AUDIO   │    │
│  │     └─> android.gradle_dependencies = CameraX libs  │    │
│  │                                                      │    │
│  │  4. sync_module_folders()                           │    │
│  │     └─> Copy java_sources/ to project               │    │
│  │                                                      │    │
│  │  5. Set needs_java = True                           │    │
│  │                                                      │    │
│  │  6. _compose_wsl_build_script()                     │    │
│  │     └─> Add P4A_EXTRA_ARGS="--add-source=..."       │    │
│  │                                                      │    │
│  └────────────────────────────────────────────────────┘    │
│                            │                                 │
│                            ▼                                 │
│  ┌────────────────────────────────────────────────────┐    │
│  │  Buildozer Build Process                            │    │
│  │  • Compiles Python app                              │    │
│  │  • Includes Java sources via P4A                    │    │
│  │  • Downloads CameraX from Gradle                    │    │
│  │  • Packages APK with camera support                 │    │
│  └────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                      Generated APK                           │
│                                                              │
│  ┌────────────────────────────────────────────────────┐    │
│  │  Python Side (Kivy/KivyMD)                          │    │
│  │                                                      │    │
│  │  • Request permissions via android.permissions      │    │
│  │  • Load CameraHelper via pyjnius                    │    │
│  │  • Call startCamera() method                        │    │
│  │  • Handle UI/events                                 │    │
│  └────────────────────────────────────────────────────┘    │
│                            │                                 │
│                            │ pyjnius bridge                  │
│                            ▼                                 │
│  ┌────────────────────────────────────────────────────┐    │
│  │  Java Side (Android)                                │    │
│  │                                                      │    │
│  │  CameraHelper.java                                  │    │
│  │  • startCamera()                                    │    │
│  │    └─> Create PreviewView                           │    │
│  │    └─> Bind CameraX lifecycle                       │    │
│  │    └─> Display overlay                              │    │
│  │                                                      │    │
│  │  • takePhoto(path)                                  │    │
│  │    └─> ImageCapture.takePicture()                   │    │
│  │    └─> Save to file                                 │    │
│  │                                                      │    │
│  │  • closeCamera()                                    │    │
│  │    └─> Remove PreviewView                           │    │
│  └────────────────────────────────────────────────────┘    │
│                            │                                 │
│                            ▼                                 │
│  ┌────────────────────────────────────────────────────┐    │
│  │  Android System                                     │    │
│  │  • CameraX Framework (androidx.camera)              │    │
│  │  • Camera HAL                                       │    │
│  │  • Device Camera Hardware                           │    │
│  └────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

## Module Directory Structure

```
modules/camera/
│
├── module.json                          # Configuration metadata
│   ├── description                      # Module description
│   ├── activate_java_sources: true      # Enable Java integration
│   ├── spec_edits[]                     # Buildozer spec patches
│   │   ├── android.api = 34
│   │   ├── android.minapi = 24
│   │   ├── android.permissions = ...
│   │   ├── android.gradle_dependencies = ...
│   │   ├── android.build_tools = 34.0.0
│   │   └── android.ndk_api = 26
│   ├── required_dirs[]                  # Directories that must exist
│   └── folder_sync[]                    # Files to copy to project
│       └── src: java_sources -> dest: java_sources
│
├── java_sources/                        # Java implementation
│   └── org/test/camera/
│       └── CameraHelper.java
│           ├── startCamera()            # Display preview
│           ├── takePhoto(String path)   # Capture image
│           └── closeCamera()            # Cleanup
│
├── README.md                            # User documentation
├── example_main.py                      # Python integration example
└── buildozer.spec.example              # Configuration example
```

## Data Flow: Taking a Photo

```
User clicks "Take Photo" button
         │
         ▼
┌──────────────────────────┐
│ Python: on_release()     │
│ photo_btn.on_release     │
└──────────────────────────┘
         │
         ▼
┌──────────────────────────┐
│ Python: Method call      │
│ cam_helper.takePhoto()   │
└──────────────────────────┘
         │
         │ pyjnius bridge
         ▼
┌──────────────────────────┐
│ Java: CameraHelper       │
│ public void takePhoto()  │
└──────────────────────────┘
         │
         ▼
┌──────────────────────────┐
│ CameraX API              │
│ imageCapture.takePicture │
└──────────────────────────┘
         │
         ▼
┌──────────────────────────┐
│ Android Camera HAL       │
│ Capture image sensor data│
└──────────────────────────┘
         │
         ▼
┌──────────────────────────┐
│ File System              │
│ Save JPEG to path        │
└──────────────────────────┘
         │
         ▼
┌──────────────────────────┐
│ Callback                 │
│ onImageSaved() or        │
│ onError()                │
└──────────────────────────┘
```

## Permission Flow

```
App Start
    │
    ▼
┌─────────────────────────────┐
│ User clicks "Start Camera"  │
└─────────────────────────────┘
    │
    ▼
┌─────────────────────────────┐
│ Check if Android            │
│ platform == 'android'       │
└─────────────────────────────┘
    │
    ▼ Yes
┌─────────────────────────────┐
│ Request Permissions         │
│ request_permissions()       │
│ - Permission.CAMERA         │
│ - Permission.RECORD_AUDIO   │
└─────────────────────────────┘
    │
    ▼
┌─────────────────────────────┐
│ Android System Dialog       │
│ "Allow camera access?"      │
│ [Deny]  [Allow]             │
└─────────────────────────────┘
    │
    ├─ Deny ──> on_permissions_result(grants=[False])
    │           └─> Show error message
    │
    └─ Allow ──> on_permissions_result(grants=[True])
                 │
                 ▼
            ┌─────────────────────────────┐
            │ Initialize Camera           │
            │ CameraHelper(activity)      │
            │ .startCamera()              │
            └─────────────────────────────┘
                 │
                 ▼
            ┌─────────────────────────────┐
            │ Camera Preview Displayed    │
            └─────────────────────────────┘
```

## Build Process Flow

```
User clicks "Build APK" in APK Builder Studio
    │
    ▼
┌──────────────────────────────────────┐
│ buildozer.py: apply_intelligent_fixes│
└──────────────────────────────────────┘
    │
    ├─> detect_camera_requirement()
    │   └─> "camera" found in requirements? ──No──> Skip module
    │                                                    │
    │   └─> Yes                                         │
    │       │                                           │
    ├─────────> load_module_config("camera")           │
    │           └─> Parse module.json                   │
    │                                                   │
    ├─────────> apply_spec_edits()                     │
    │           └─> Update buildozer.spec               │
    │                                                   │
    ├─────────> sync_module_folders()                  │
    │           └─> Copy java_sources/ to project      │
    │                                                   │
    └─────────> Set needs_java = True                  │
                │                                       │
                ▼                                       │
         ┌────────────────────────────┐                │
         │ _compose_wsl_build_script()│                │
         │ if needs_java:             │                │
         │   P4A_EXTRA_ARGS="..."     │                │
         └────────────────────────────┘                │
                │                                       │
                ▼                                       │
         ┌────────────────────────────┐                │
         │ Execute Buildozer          │<───────────────┘
         │ buildozer android debug    │
         └────────────────────────────┘
                │
                ▼
         ┌────────────────────────────┐
         │ Python-for-Android         │
         │ • Compile Java sources     │
         │ • Download Gradle deps     │
         │ • Package APK              │
         └────────────────────────────┘
                │
                ▼
         ┌────────────────────────────┐
         │ APK Ready!                 │
         │ With camera support ✅     │
         └────────────────────────────┘
```

## Key Integration Points

1. **Detection**: `buildozer.py` scans requirements for "camera" keyword
2. **Configuration**: `module.json` provides all necessary settings
3. **File Sync**: Java sources copied from module to project
4. **Build Flag**: `needs_java` flag controls P4A_EXTRA_ARGS inclusion
5. **Runtime**: pyjnius bridges Python to Java CameraHelper class

## Module Activation Logic

```python
# In buildozer.py

def apply_intelligent_fixes(self):
    self.needs_java = False  # Default: no Java
    
    if self.detect_camera_requirement():
        config = self.load_module_config('camera')
        
        if config.get('activate_java_sources'):
            self.needs_java = True  # Enable Java integration
    
    # Later in build script generation:
    if self.needs_java:
        script += f'export P4A_EXTRA_ARGS="--add-source={project}/java_sources"\n'
```

## Security Model

```
User App (Python)
    │
    │ Runtime permission check
    ▼
Android System
    │
    │ User grants permission
    ▼
CameraHelper (Java)
    │
    │ Uses granted permission
    ▼
CameraX Framework
    │
    │ Hardware access
    ▼
Camera Hardware
```

No permissions = App cannot access camera
Permission granted = Full camera access via CameraX

## Dependencies Hierarchy

```
User's APK
    │
    ├─> Python 3.x
    │   └─> Kivy 2.x
    │       └─> KivyMD
    │
    ├─> pyjnius (Python-Java bridge)
    │
    └─> Android Dependencies
        ├─> androidx.camera:camera-core:1.2.2
        ├─> androidx.camera:camera-camera2:1.2.2
        ├─> androidx.camera:camera-lifecycle:1.2.2
        └─> androidx.camera:camera-view:1.2.2
            └─> Android Camera2 API
                └─> Camera HAL
                    └─> Device Camera
```

All dependencies automatically included when "camera" is in requirements!
