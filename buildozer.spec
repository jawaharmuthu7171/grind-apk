[app]
title = Grind
package.name = grind
package.domain = org.jawaharmuthu
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf
version = 1.0
requirements = python3,kivy,pyjnius,android
orientation = portrait
fullscreen = 0
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,VIBRATE
android.api = 31
android.minapi = 21
android.ndk = 25b
android.sdk = 31
android.ndk_api = 21
android.build_tools_version = 30.0.3
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
