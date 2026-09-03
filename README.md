<img width="1869" height="947" alt="SamAI" src="https://github.com/user-attachments/assets/92032eeb-31e1-4d64-8b80-d61e5a26c102" />
## 🤖 New: SamAI — Your Built-in Build Assistant

**What is SamAI?** SamAI is an AI-powered diagnostic assistant built directly into the browser-based IDE. Instead of digging through cryptic Buildozer output or Android logcat traces yourself, you just ask SamAI what's wrong — and it reads your project for you.

**What it's for:** SamAI helps with two kinds of problems, each with its own quick-select button:
- **"Build Problem (APK/AAB)"** — your build fails? Just click it. SamAI analyzes why the build isn't going through and gives you the right change to apply.
- **"App doesn't start on the device or behaves incorrectly"** — your app crashes on the device? SamAI analyzes the logcat and tells you why it's not starting.

**What about a silent bug** — the app runs fine, but something behaves wrong (a button click doesn't do what it should)? There's no dedicated button for that, so here's the workflow:
1. Clear the logcat on Screen 4 first, so nothing old gets mixed in
2. Start the logcat and reproduce the bug (click the button, test it)
3. In the IDE's file tree, check the checkbox on the affected file so SamAI can see it
4. In the prompt, briefly describe what's not working
5. Send the request — SamAI reviews the selected file and reasons about the logic

**How it works:** Whichever of the three paths you use — when SamAI finds a fix, it proposes concrete changes, whether to `buildozer.spec` or to project files like `.py`/`.kv`. Click **"Apply"** and the suggestion is written directly into the file automatically. An automatic checkpoint is created before every apply, so you can always roll back.

**This is a beta — and I need your help improving it.** SamAI is actively being trained on real bugs. If it gets something wrong or can't solve your case, use the **"No solution"** button in the IDE — it sends me your description plus a zipped snapshot of your project, so I can add your case to SamAI's knowledge base and make it smarter for everyone. The more real cases I collect, the better SamAI gets.

**How to get access:** SamAI requires a free beta key (separate from your regular Studio access — Studio itself works without any key at all). You'll find the key request built right into the IDE — just follow the prompt when you try SamAI for the first time.

**Why are the keys limited?** I build and maintain APK Builder Studio alone. Every SamAI request costs real API compute, and during this beta phase I want to be able to give each case my personal attention instead of drowning in requests. That's why there's only a limited number of keys for now — first come, first served.




<p align="center"><img width="1234" height="857" alt="apkbuilderstudio2" src="https://github.com/user-attachments/assets/c6016c3b-9330-48b5-959a-073482f7aef3" />
</p>
<img width="1236" height="861" alt="apkbuilderstudioscreen2" src="https://github.com/user-attachments/assets/b7565202-ec03-4c9e-a7fc-e6b113ebd585" />
<img width="1236" height="857" alt="apkbuilderstudioscreen3" src="https://github.com/user-attachments/assets/aaf2e7e4-3a5b-4866-849e-f9861e2e292a" />

> ### 📢 Current Status: Production-Ready Beta
> **APK Builder Studio** is fully functional. The current Beta phase is used to verify compatibility across diverse Windows hardware environments. 
> **All core features (WSL setup, SDK management, APK building) are 100% operational.**


> ## 📥 Download & Quick Start
The latest version is ready for use! 

> [!CAUTION]
> ### ⚠️ WRONG BUTTON?
> If you clicked the **green "Code" button** above, you only downloaded the documentation.
> **The actual App is located below!**
# 📥 [DOWNLOAD INSTALLER (.ZIP) HERE](https://github.com/PedroHSA0802/apk-builder-studio/releases/download/v1.0.0-beta/APK-Builder-Studio.zip)

- **Direct Download:** https://github.com/PedroHSA0802/apk-builder-studio/releases/tag/v1.0.0-beta

🛡️ Security & Trust (Verified by Microsoft)

I have personally submitted the installer to Microsoft Security Intelligence for a manual review to resolve initial "False Positive" alerts.

The Official Result: Microsoft has audited the application and officially whitelisted it. The security warning has been removed.

Status: ✅ Officially Verified & Safe (Whitelisted)

Analyst Result: Manual review confirmed the app contains no malware or unwanted software.

Submission ID: a9dc272e-a353-4c33-9296-63dcac7762c3 

How this benefits you:

Seamless Installation: Windows Defender now recognizes the installer as safe and will not block the process.

Verified Integrity: The manual check confirms the app only performs its intended tasks (setting up your Android environment).

Verify it Yourself: You can right-click the .exe after downloading and select "Scan with Microsoft Defender" to see the "No threats found" result yourself.

Developer's Note: I chose this verification path to ensure you can use APK Builder Studio with full confidence, free from confusing security warnings.
## 🚀 Features

### 🔧 Fully Automated Setup
*No terminal, no prompts.* **APK Builder Studio** sets up the entire Android build environment automatically — without requiring the user to open a terminal or enter any commands:

* **Automatic Installation:** Configuration of WSL (Windows Subsystem for Linux).
* **Toolchain Setup:** Full installation of Android SDK, NDK, and Build-tools.
* **Environment:** Automatic creation and activation of a Python virtual environment (`venv`).
* **Structure:** Intelligent placement of all required folders in the correct hierarchy.
* **Sync:** Automatic synchronization between the Windows file system and WSL.

> **Note:** The user does not need to perform any manual installations. Everything runs seamlessly in the background.

### 📁 Project & Structure Management
* **Create & Manage:** Easily start new Kivy/KivyMD projects with the correct folder structure.
* **Smart Detection:** Automatically detect and repair missing or incorrect project folders.
* **Path Optimization:** Synchronize files between Windows and WSL to avoid build errors caused by incorrect file paths.

---

### 🧩 Template-Based Configuration
* **Smart Templates:** Assign pre-defined build templates to your projects.
* **Customization:** Save your own templates for repeated builds.
* **Ease of Use:** Edit templates as simple text files directly within the interface.

---

### 📦 APK Build with Buildozer
* **GUI-Driven:** Automatically runs Buildozer inside WSL without the need for terminal commands.
* **Real-time Monitoring:** Displays build logs and progress directly in the app.
* **Organized Output:** Stores generated APKs in a clean and structured output folder.

### 🧩 Module System — Extend Your App with One Click
APK Builder Studio includes a built-in **Module Manager**. With a simple checkmark, you can integrate powerful native Android features into your KivyMD project — no manual Java code.

Currently Available Modules:

* 📷 **CameraX** — Adds a ready-to-use camera widget to your KivyMD app. Access the device camera directly from a custom KivyMD widget without writing any platform-specific code.
* 🧠 **ML Kit Face Detection** — Enables real-time face detection powered by Google's ML Kit. Simply activate the module to add face recognition capabilities to your app.
* 🔍 **ML Kit Barcode Scanning** — High-speed recognition and decoding of 1D and 2D barcodes (QR codes, EAN, UPC, Data Matrix) directly from the camera feed.
* 🔤 **ML Kit Text Recognition (OCR)** — Real-time optical character recognition to extract and process text from images or the live camera stream.
* 🗣️ **Text-to-Speech (TTS)** — Converts Python string data into natural-sounding spoken audio directly through Android's native speech engine.
* 🎙️ **Speech-to-Text (STT)** — High-accuracy voice recognition that captures user speech and converts it into Python string variables for seamless voice commands.

> **How it works:** Open the Module Manager in APK Builder Studio, check the modules you need.

#### 📱 Demo App: VisionPro Droid Widget
A fully functional demo app called **visionpro_droid_widget** has been built using these modules, showcasing CameraX and ML Kit Face Detection working together in a KivyMD app. The demo is available on GitHub with full source code, `buildozer.spec`, and a pre-built APK.
---
🛠 Troubleshooting & Self-Healing

APK Builder Studio is designed to be resilient. If you encounter issues during the build process, the app provides built-in tools to fix the environment without manual intervention:

🔍 Structure Check: Before building, use the integrated folder check. It identifies missing main.py files or incorrect project hierarchies that would typically cause Buildozer to fail silently.

🧹 Safe Reset ("The Broom"): If your build hangs or shows weird Python errors, use the Safe Reset. It clears the python-for-android platform caches and local Buildozer temporary files while keeping your project settings intact.

💣 Deep Reset ("The Bomb"): In case the WSL environment becomes corrupted or an SDK update fails, the Deep Reset allows you to unregister and wipe the entire Ubuntu/WSL instance. The app will then guide you through a fresh, automated setup.

  🔑 Permission Fix: Our automated script automatically configures sudo access within WSL (passwordless), eliminating the "Permission Denied" errors that frequently plague manual Kivy/Buildozer setups.
---

🔄 KivyMD Update Engine

The integrated update button ensures your build environment stays current without needing to reinstall the application:

Profile Synchronization: Downloads the latest configuration files (.txt) directly from our server to your local AppData directory.

Dynamic Toolchain Adaptation: Each profile contains specific instructions for the required Android SDK, NDK, and Gradle versions, as well as the exact Python requirements for that KivyMD version.

Automated Reconfiguration: Once a new profile is selected, the app automatically adjusts the entire WSL environment to the new specifications during the next installation or build process.

Version Switching: Allows you to switch seamlessly between different KivyMD generations (e.g., from 1.x to 2.x). The app reloads all build parameters in real-time based on the active profile.

🔥 **Integrated Wireless & USB Debugger + One-Click Installer**

No more guessing why your app crashes! APK Builder Studio now features a built-in Debugger and Direct Deployment Manager:

* 📶 & 🔌 **Wireless & USB Debugging:** Connect via Wi-Fi ADB (Auto-Detection) or standard USB cable in seconds.
* 📜 **Live Logcat Stream:** Real-time logs streamed directly inside the desktop interface.
* 🐍 **Smart Python Error Filter:** Automatically filters out thousands of irrelevant system logs and highlights the exact Python traceback / `ModuleNotFoundError` causing the crash.
* 📲 **Direct APK & AAB Installation:** Install both generated `.apk` files AND Google Play `.aab` bundles directly onto your connected Android device with a single click — no manual terminal or ADB commands needed!

Why this is a game-changer:

Instead of manually hunting for compatible NDK versions or fixing Gradle errors, you simply click Update, select your version, and let the app handle the complex background configuration.


✍️ A Note from the Developer (Why Beta Access?)

Hi! I’m the developer of this tool. I built it because the APK build process used to give me massive headaches, and I wanted a solution that just works for everyone.

Why a Beta Access Key? Even though the app is 100% free, I’ve included a simple access system. This is not for profit, but for community management:

Controlled Growth: It helps me track how many people are using the tool so I can prioritize features like the USB Debugger.

Support Quality: It prevents "bot-spam" and ensures that feedback comes from real users, helping me fix bugs faster.

Will it cost money later? I haven't decided yet. But here is my promise: If you get your key during this beta phase, APK Builder Studio stays free for you forever. No subscriptions, no hidden costs — you are a "Founding Member" of this project.
🔑 Get your Lifetime Beta Access

To secure your lifetime free access, simply claim your unique key here: 👉 Get your Beta Access Key (No registration, no email, no data collection. Just one click.)


https://PedroSamuel.pythonanywhere.com/get_beta_key
(No registration or email required. Just one click, copy, and paste into the app.)

⚡ Performance & Expectations

To be transparent about your workflow:

1. The One-Time Setup (~40-60 Min): The app downloads and configures the entire Android Toolchain (~5GB), including WSL, SDK, and NDK. You only do this once!

2. The First Build of a Project (~10-15 Min): When you build a specific project for the first time, Buildozer needs to compile the Python distribution and requirements.

3. Subsequent Builds (2 - 5 Minutes): 🚀 This is the magic part! After your first successful build, any changes you make to your Python code or UI will be compiled in just a few minutes. This allows for incredibly fast testing and iteration.

🔒 License & Connectivity
Activation: Requires a one-time internet connection to link your key to an anonymous hardware-hash (valid for up to 2 devices).

Setup: Internet access is needed during the first run to automatically download the required Android components (WSL, SDK, NDK).
