# Camera Module Integration Guide for APK Builder Studio

## Overview

This document explains how the camera module integrates with APK Builder Studio's build system. The module provides automatic CameraX setup when users add `camera` to their project requirements.

## Module System Architecture

### Directory Structure

```
modules/
└── camera/
    ├── module.json                      # Module configuration
    ├── README.md                        # User documentation
    ├── buildozer.spec.example          # Example configuration
    ├── example_main.py                 # Python integration example
    └── java_sources/
        └── org/
            └── test/
                └── camera/
                    └── CameraHelper.java
```

### How APK Builder Studio Processes This Module

When a user includes `camera` in their buildozer.spec requirements:

```ini
requirements = python3,kivy,kivymd,camera
```

The APK Builder Studio should:

1. **Detect the requirement**: Parse `buildozer.spec` and identify `camera` in the requirements list
2. **Load module configuration**: Read `modules/camera/module.json`
3. **Apply spec edits**: Patch the buildozer.spec with the values from `spec_edits` array
4. **Sync folders**: Copy `java_sources/` to the project's `java_sources/` directory
5. **Set build flag**: Set `needs_java = True` to enable Java source integration
6. **Configure build**: Add `--add-source=java_sources` to P4A_EXTRA_ARGS

## Implementation in buildozer.py

### Required Methods

#### 1. Requirement Detection

```python
def detect_camera_requirement(self, spec_content: str) -> bool:
    """
    Detect if 'camera' is in requirements.
    Handle variations: camera, camera==1.0, camera>=1.0, etc.
    """
    import re
    
    for line in spec_content.split('\n'):
        if line.strip().startswith('requirements'):
            # Extract requirements list
            req_line = line.split('=', 1)[1] if '=' in line else ''
            
            # Split by comma and normalize
            requirements = [r.strip().split('#')[0] for r in req_line.split(',')]
            
            # Check each requirement
            for req in requirements:
                # Remove version specifiers
                pkg_name = re.split(r'[=<>!~]', req)[0].strip()
                if pkg_name.lower() == 'camera':
                    return True
    
    return False
```

#### 2. Module Configuration Loading

```python
def load_module_config(self, module_name: str) -> dict:
    """Load module.json configuration"""
    import json
    import os
    
    module_path = os.path.join('modules', module_name, 'module.json')
    
    if not os.path.exists(module_path):
        raise FileNotFoundError(f"Module not found: {module_name}")
    
    with open(module_path, 'r') as f:
        return json.load(f)
```

#### 3. Spec Patching

```python
def apply_spec_edits(self, spec_path: str, edits: list):
    """
    Apply spec_edits from module.json to buildozer.spec
    
    Args:
        spec_path: Path to buildozer.spec
        edits: List of {key, value} pairs from module.json
    """
    with open(spec_path, 'r') as f:
        lines = f.readlines()
    
    for edit in edits:
        key = edit['key']
        value = edit['value']
        
        # Find and update the line
        found = False
        for i, line in enumerate(lines):
            if line.strip().startswith(f'{key} ='):
                lines[i] = f'{key} = {value}\n'
                found = True
                break
        
        # If not found, append it
        if not found:
            lines.append(f'{key} = {value}\n')
    
    with open(spec_path, 'w') as f:
        f.writelines(lines)
```

#### 4. Folder Synchronization

```python
def sync_module_folders(self, module_name: str, sync_configs: list, project_path: str):
    """
    Sync folders from module to project
    
    Args:
        module_name: Name of the module (e.g., 'camera')
        sync_configs: List of {src, dest} pairs from module.json
        project_path: Target project directory
    """
    import shutil
    import os
    
    module_base = os.path.join('modules', module_name)
    
    for sync in sync_configs:
        src = os.path.join(module_base, sync['src'])
        dest = os.path.join(project_path, sync['dest'])
        
        # Create destination directory
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        
        # Copy directory tree
        if os.path.exists(src):
            if os.path.exists(dest):
                shutil.rmtree(dest)
            shutil.copytree(src, dest)
            print(f"[Module] Synced {sync['src']} -> {sync['dest']}")
```

#### 5. Build Script Integration (CRITICAL FIX)

```python
def _compose_wsl_build_script(self, project_path: str, bz_command: str) -> str:
    """
    Compose the WSL build script.
    
    IMPORTANT: Only add P4A_EXTRA_ARGS when needs_java is True
    """
    p = project_path
    cfg_pkgs = self._config_python_packages()
    pkgs = self._sanitize_pip_packages(cfg_pkgs)
    lower = [x.lower() for x in pkgs]

    if not any(x.startswith("buildozer") for x in lower):
        pkgs.append("buildozer>=1.5.0")
    if not any(x.startswith("cython") for x in lower):
        pkgs.append("cython<3")

    def _sh_quote(s: str) -> str:
        return "'" + s.replace("'", "'\"'\"'") + "'"

    pip_install = " ".join(_sh_quote(x) for x in pkgs) if pkgs else ""

    # --- CRITICAL: Only enable Java integration when flag is set ---
    java_integration_cmd = ""
    if getattr(self, "needs_java", False):
        java_integration_cmd = (
            "echo '[Studio] Activating CameraX/Java Source Integration...'\n"
            f"export P4A_EXTRA_ARGS=\"--add-source={p}/java_sources\"\n"
        )
    # --- END CRITICAL SECTION ---

    return (
        "#!/usr/bin/env bash\n"
        "set -e\n"
        "set -x\n"
        "export LANG=C.UTF-8\n"
        # ... other environment setup ...
        "ANDROIDSDK=\"${ANDROIDSDK:-$HOME/.buildozer/android/platform/android-sdk}\"\n"
        "export ANDROID_SDK_ROOT=\"$ANDROIDSDK\"\n"
        "export ANDROID_HOME=\"$ANDROIDSDK\"\n"
        "\n"
        f"{java_integration_cmd}"
        "\n"
        f"\"$HOME/.buildozer_venv/bin/buildozer\" -v {bz_command} 2>&1 | tee \"$HOME/apk_builder_last_build.log\"\n"
    )
```

### Integration Flow

```python
def apply_intelligent_fixes(self, project_path: str):
    """
    Main method to apply module-based fixes
    Called before building the APK
    """
    spec_path = os.path.join(project_path, 'buildozer.spec')
    
    if not os.path.exists(spec_path):
        return
    
    with open(spec_path, 'r') as f:
        spec_content = f.read()
    
    # Reset flag
    self.needs_java = False
    
    # Detect camera requirement
    if self.detect_camera_requirement(spec_content):
        print("[Studio] Camera module detected in requirements")
        
        try:
            # Load module configuration
            config = self.load_module_config('camera')
            
            # Apply spec edits
            if 'spec_edits' in config:
                self.apply_spec_edits(spec_path, config['spec_edits'])
                print("[Studio] Applied camera module spec edits")
            
            # Sync folders
            if 'folder_sync' in config:
                self.sync_module_folders('camera', config['folder_sync'], project_path)
                print("[Studio] Synced camera module files")
            
            # Set Java flag
            if config.get('activate_java_sources', False):
                self.needs_java = True
                print("[Studio] Java source integration enabled")
                
        except Exception as e:
            print(f"[Studio] Error applying camera module: {e}")
            # Continue build anyway, user might have manual setup
```

## Testing the Integration

### Test Case 1: Basic Detection

1. Create a test buildozer.spec with `requirements = python3,kivy,camera`
2. Verify `detect_camera_requirement()` returns `True`
3. Verify module.json is loaded successfully

### Test Case 2: Spec Patching

1. Start with minimal buildozer.spec
2. Run `apply_spec_edits()`
3. Verify these keys are added/updated:
   - `android.api = 34`
   - `android.minapi = 24`
   - `android.permissions` includes CAMERA
   - `android.gradle_dependencies` includes CameraX libs

### Test Case 3: Folder Sync

1. Verify `java_sources/org/test/camera/CameraHelper.java` is copied to project
2. Verify directory structure is preserved

### Test Case 4: Build Flag

1. Verify `needs_java` is set to `True` when camera is detected
2. Verify `P4A_EXTRA_ARGS` is added to build script
3. Build an APK and verify Java classes are included

### Test Case 5: No Camera Requirement

1. Create buildozer.spec without camera
2. Verify `needs_java` remains `False`
3. Verify `P4A_EXTRA_ARGS` is NOT added to build script
4. Verify build succeeds without Java sources

## User Experience

### Before (Manual Setup)

User had to manually:
1. Add permissions to buildozer.spec
2. Configure gradle dependencies
3. Create Java source files
4. Set up directory structure
5. Configure buildozer with --add-source
6. Research CameraX documentation

### After (Automated)

User only needs to:
1. Add `camera` to requirements
2. Click "Build APK" button
3. Use the camera in Python (following example_main.py)

## Compatibility

- **Android API**: 24-34 (Android 7.0 to Android 14)
- **CameraX**: 1.2.2 (stable)
- **Kivy**: 2.0+
- **KivyMD**: Any version
- **Python**: 3.8+
- **Buildozer**: 1.5.0+

## Known Limitations

1. **Java Only**: This module uses Java (not Kotlin) for maximum compatibility
2. **Lifecycle**: The camera preview requires Activity lifecycle support
3. **Overlay**: Camera appears as an overlay, not integrated in Kivy widget tree
4. **Device Only**: Testing requires real Android device (emulator camera may not work)

## Future Enhancements

Potential improvements for future versions:

1. **Configuration Options**: Allow users to customize CameraX settings in module.json
2. **Front/Back Toggle**: Add Python API to switch cameras
3. **Video Recording**: Extend module to support video capture
4. **QR/Barcode**: Add ML Kit for code scanning
5. **Custom Package**: Allow users to customize Java package name
6. **Multiple Modules**: Support combining camera with other modules (e.g., location, sensors)

## Security Considerations

1. **Permissions**: Camera permission must be requested at runtime (example included)
2. **Storage**: Uses app-specific directories to avoid broad storage permissions
3. **Privacy**: No data is collected by the module itself
4. **Dependencies**: All dependencies are from official Google/AndroidX repositories

## Support Matrix

| Feature | Supported | Notes |
|---------|-----------|-------|
| Photo Capture | ✅ | Full support |
| Video Recording | ❌ | Not yet implemented |
| QR Scanning | ❌ | Not yet implemented |
| Front Camera | ⚠️ | Requires code modification |
| Image Processing | ⚠️ | User can extend Java code |
| Portrait Mode | ✅ | Supported |
| Landscape Mode | ✅ | Supported |
| Android 7-14 | ✅ | Full support |
| Google Play Store | ✅ | API 34 compliant |

## Troubleshooting

See `modules/camera/README.md` for user-facing troubleshooting guide.

For APK Builder Studio developers:

1. **Module Not Detected**: Check requirement parsing regex
2. **Spec Not Patched**: Verify file write permissions
3. **Java Files Missing**: Check folder sync logic
4. **Build Fails**: Verify P4A_EXTRA_ARGS is set correctly
5. **Wrong API**: Ensure API 34 is being applied from module.json

## References

- [CameraX Documentation](https://developer.android.com/training/camerax)
- [Android API Levels](https://developer.android.com/studio/releases/platforms)
- [Buildozer Documentation](https://buildozer.readthedocs.io/)
- [Python-for-Android](https://python-for-android.readthedocs.io/)
