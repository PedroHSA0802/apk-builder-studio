[app]
title = VisionPro Droid
package.name = visionpro
package.domain = org.pedro

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,xml,json

version = 0.1

requirements = python3, kivy==2.3.1, https://github.com/kivymd/KivyMD/archive/master.zip, materialyoucolor, pillow, filetype, asynckivy, asyncgui, numpy, gestures4kivy, pyjnius

android.api = 34
android.minapi = 29
android.targetsdk = 34
android.ndk = 25b
android.ndk_api = 29
android.archs = arm64-v8a

orientation = portrait
fullscreen = 0

android.enable_androidx = True
android.enable_multidex = True

android.gradle_repositories = https://maven.google.com
android.gradle_dependencies = androidx.camera:camera-core:1.3.0,androidx.camera:camera-camera2:1.3.0,androidx.camera:camera-lifecycle:1.3.0,androidx.camera:camera-view:1.3.0,androidx.camera:camera-extensions:1.3.0,com.google.mlkit:face-detection:16.1.5

android.permissions = CAMERA,WRITE_EXTERNAL_STORAGE

android.add_src = ./java_sources

android.copy_libs = 1
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
