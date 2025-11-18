
````markdown
# 💧 Water Reminder App (Python Desktop App)

A simple **Water Reminder** desktop app built with **Python** for Windows 11, featuring:

- Periodic hydration reminders
- Desktop notifications using **Windows 11 toast notifications**
- Minimal, easy-to-use **GUI** with Start/Stop buttons
- Runs standalone as `.exe` using PyInstaller

---

## 🛠 Features

- Reminds you to drink water every configurable interval (default 1 minute for testing)
- Desktop toast notifications with friendly message
- Simple **Tkinter GUI**
- Works standalone as `.exe` on Windows 11

---

## 📦 Installation & Setup

### Requirements

Make sure you have **Python 3.10+** installed and the following package:

```bash
pip install win11toast
````

### Clone the repository

```bash
git clone https://github.com/naeemcodemaster/Water-Reminder-Python.git Water-Reminder-App
cd Water-Reminder-App
```

### Run in development mode

```bash
python app.py
```

### Build standalone executable

```bash
pyinstaller --onefile --windowed app.py
```

This will generate a standalone `.exe` file in the `dist/` folder.

---

## 🎯 Usage

1. Open the app (`app.py` in development mode or the `.exe` in `dist/`).
2. Click **Start Reminder** to begin.
3. Click **Stop Reminder** to stop notifications.

---

## 🤝 Contributing

Contributions, suggestions, and bug reports are welcome! Please create a pull request or issue in this repository.

---

## ⚡ License

MIT License

```

✅ Notes:  
- Clone this repository to get started:
- The interval is set in the code (currently 1 minute for testing).  
- Instructions include running in dev mode and building `.exe`.  
```
