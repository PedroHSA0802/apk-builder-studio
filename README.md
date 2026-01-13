<p align="center">
  <img src="https://github.com/user-attachments/assets/dbd808ae-6e6a-4921-9d12-2bff1c00b582" width="600" alt="APK Builder Studio Main Interface">
</p>

🛡️ Security & Trust: Is this tool safe?

Building Android APKs requires deep system integration (installing WSL, configuring Android SDK/NDK, and managing environment variables).

Because of these powerful features, some security filters might be extra cautious.

Here are the facts regarding your security:

Verified by Industry Leaders: I submitted the application to VirusTotal, where it was analyzed by over 70 different security engines.

The Result: 68 out of 71 scanners (including world leaders like Kaspersky, BitDefender, ESET, and Sophos) confirmed the file is 100% clean.

The 3 minor flags are "False Positives." These occur because the app is designed to download the Android SDK and interact with the WSL system.

Verify it yourself: I encourage transparency. If you have any concerns, please feel free to upload the .exe to VirusTotal.com yourself before running it.

You will see the same results from the world's most trusted security providers.

Compatibility Testing: To ensure a smooth experience, I specifically tested the app against popular antivirus software like Avast.

The tool was correctly identified as safe and was not blocked during operation.

Why does Windows show a warning? Since the app is not digitally signed with an expensive corporate certificate, Windows SmartScreen may show an "Unknown Publisher" warning.

You can safely run the app by clicking "More info" and then "Run anyway."

Privacy First: The app only connects to our server to verify your license key using an anonymous hardware hash. No personal data, emails, or private files are ever collected or transmitted.

💡 Verification Tip: > Don't just take my word for it. You can take the VirusTotal "Behavior Report" and paste it into any AI like ChatGPT, Copilot, or Gemini. Ask the AI: "Is this behavior typical for a software installer?" > The AI will confirm that activities like writing registry keys, creating temporary folders, and updating the icon cache are standard procedures for tools built with Inno Setup and Nuitka.

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


✍️ A Note from the Developer (License & Future)

Hi! I’m the developer of this tool. I built it because the APK build process used to give me massive headaches, and I wanted a solution that just works for everyone.

Why a license key? Even though the app is currently free, I’ve included a license system to help me manage the community and growth while I’m still refining the software.

Will it cost money later? To be honest: I don't know yet. Maybe it will always be free, maybe there will be a small fee for new users later. But here’s the deal: If you get a key during this beta phase, the app stays free for you forever. No subscriptions, no hidden costs – even for all future updates and "Pro" features.
🔑 Get your Lifetime Access Key

To secure your lifetime free access, simply claim your unique key here:


https://PedroSamuel.pythonanywhere.com/get_beta_key
(No registration or email required. Just one click, copy, and paste into the app.)

🔥 Coming Soon: The Integrated USB Debugger

I'm already working on the next big update:
One-Click Debugging: 
Just plug your phone into your PC via USB.

Live Logcat: See exactly why your app is crashing on the device.

Python Error Filter: No more digging through thousands of lines of system logs. The app will highlight the specific Python error causing the crash.

🔒 License & Connectivity
Activation: Requires a one-time internet connection to link your key to an anonymous hardware-hash (valid for up to 2 devices).

Setup: Internet access is needed during the first run to automatically download the required Android components (WSL, SDK, NDK).
