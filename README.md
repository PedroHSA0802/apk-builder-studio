<p align="center">
  <img src="https://github.com/user-attachments/assets/dbd808ae-6e6a-4921-9d12-2bff1c00b582" width="600" alt="APK Builder Studio Main Interface">
</p>

> ### 📢 Current Status: Production-Ready Beta
> **APK Builder Studio** is fully functional. The current Beta phase is used to verify compatibility across diverse Windows hardware environments. 
> **All core features (WSL setup, SDK management, APK building) are 100% operational.**
>
> ## 📥 Download & Quick Start
The latest version is ready for use! 
- **Current Version:** [v1.0.0-beta](https://github.com/PedroHSA0802/apk-builder-studio/releases/latest)
- **Direct Download:** https://github.com/PedroHSA0802/apk-builder-studio/releases/tag/v1.0.0-beta

🛡️ Security & Trust (Verified by Microsoft)

I have personally submitted the installer to Microsoft Security Intelligence for a manual review to resolve initial "False Positive" alerts.

The Official Result: Microsoft has audited the application and officially whitelisted it. The security warning has been removed.

Status: ✅ Officially Verified & Safe (Whitelisted)

Analyst Result: Manual review confirmed the app contains no malware or unwanted software.

Submission ID: 41e5748c-5ed7-4e2b-9043-fbfd7d767957

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

Why this is a game-changer:

Instead of manually hunting for compatible NDK versions or fixing Gradle errors, you simply click Update, select your version, and let the app handle the complex background configuration.
## 📺 Video Tutorial
Check out the tool in action:




https://github.com/user-attachments/assets/497ae25b-6aae-416f-bcd9-86588e7f29a3




Watch on YouTube:
[https://youtu.be/DQ5Ox1PAafc](https://youtu.be/Dr0fThHWPxs)


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

🔥 Coming Soon: The Integrated USB Debugger

I'm already working on the next big update:
One-Click Debugging: 
Just plug your phone into your PC via USB.

Live Logcat: See exactly why your app is crashing on the device.

Python Error Filter: No more digging through thousands of lines of system logs. The app will highlight the specific Python error causing the crash.

🔒 License & Connectivity
Activation: Requires a one-time internet connection to link your key to an anonymous hardware-hash (valid for up to 2 devices).

Setup: Internet access is needed during the first run to automatically download the required Android components (WSL, SDK, NDK).
