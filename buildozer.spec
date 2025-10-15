[app]
# =============================
# 📱 Загальні налаштування
# =============================
title = XT-ScalperPro
package.name = xtscalperpro
package.domain = org.xt.scalper

# =============================
# 📂 Джерела
# =============================
source.dir = .
source.main = main.py
source.include_exts = py,png,jpg,kv,txt,md

# =============================
# ⚙️ Версія
# =============================
version = 1.0

# =============================
# 🧩 Іконка та заставка
# =============================
icon.filename = assets/icon.png
presplash.filename = assets/splash.png

# =============================
# 🧠 Залежності (лише стабільні)
# =============================
requirements = python3,kivy==2.2.1,ccxt,pandas,numpy,pandas_ta,cython

# =============================
# 🤖 Android
# =============================
p4a.bootstrap = sdl2
android.archs = arm64-v8a
orientation = portrait

# API і SDK — стабільна зв’язка для Buildozer 1.5.0
android.api = 33
android.minapi = 28
android.ndk = 25b
android.sdk = 33
android.build_tools_version = 34.0.0

# =============================
# 📡 Дозволи
# =============================
android.permissions = INTERNET,ACCESS_NETWORK_STATE,WAKE_LOCK
android.enable_androidx = True
android.allow_backup = True
android.hardware = touchscreen
android.unicode = True

# =============================
# 🪶 Інше
# =============================
fullscreen = 0
log_level = 2
android.accept_sdk_license = True
android.enable_internet = True

# =============================
# ⚙️ Prebuild (створює assets при потребі)
# =============================
[buildozer]
prebuild = python3 -c "import os; os.makedirs('assets', exist_ok=True); open('assets/icon.png','ab').close(); open('assets/splash.png','ab').close()"