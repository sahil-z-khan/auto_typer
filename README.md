Here is a **more concise, clean, professional README**:

---

# 📄 Auto Typer — Human-Like Typing Script

A simple Python script that types text into any application (Word, Google Docs, Notes) with **human-like typing delays**.

---

## 🚀 Features

* Simulates natural typing (random delays per character)
* Handles punctuation and newlines realistically
* 5-second countdown before typing begins
* Emergency stop: **move mouse to the top-left corner**

---

## 📦 Installation

### 1. Install dependencies

Using Pipenv:

```bash
pipenv install
pipenv shell
```

Or with pip:

```bash
python3 -m pip install pyautogui
python3 -m pip install pyobjc-core pyobjc pillow   # macOS only
```

---

## ▶️ Usage

### 1. Add your text

Edit `TEXT_TO_TYPE` in `main.py`:

```python
TEXT_TO_TYPE = """
Paste your text here.
"""
```

### 2. Run the script

```bash
python main.py
```

You will get a 5-second window to click into Word (or any typing app).

### 3. Let it type

The script will type everything character-by-character.

### ⛔ Stop typing

Move your mouse to the **top-left corner** of the screen.

---

## ⚙️ Customizing Typing Speed

```python
human_type(TEXT_TO_TYPE, base_min=0.02, base_max=0.10)
```

Lower values → faster typing
Higher values → slower, more human-like

---

That's it — clean, simple, and ready to use.
If you'd like, I can also generate a minimal logo, a GUI version, or a CLI tool.
