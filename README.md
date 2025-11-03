# 🖐️ Gesture Virtual Mouse using Python

<p align="center">
  <img src="assets/preview.png" alt="Project Preview" width="800"/>
</p>

<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.8%2B-blue.svg?style=flat-square"></a>
  <a href="https://opencv.org/"><img src="https://img.shields.io/badge/OpenCV-Enabled-green.svg?style=flat-square"></a>
  <a href="https://mediapipe.dev/"><img src="https://img.shields.io/badge/MediaPipe-Hand_Tracking-orange.svg?style=flat-square"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square"></a>
  <a href="#"><img src="https://img.shields.io/github/last-commit/<your-username>/gesture-virtual-mouse?style=flat-square"></a>
</p>

> 🎓 Built by **Honey**, MCA Student at CGC College of Engineering, Landran  
> 💡 "Control your system without touching it — just your hands and AI magic!"

---

## 🚀 Overview

This project turns your webcam into a **gesture-controlled virtual mouse** 🖱️  
It uses **MediaPipe** for hand tracking, **OpenCV** for real-time video processing, and **PyAutoGUI** to control mouse movements and actions.

Perform actions like:
- Move the mouse with your index finger  
- Click with thumb + index  
- Scroll with two fingers  
- Drag and drop with gesture holding  

All this, hands-free!

---

## 🧰 Tech Stack

| Library | Purpose |
|----------|----------|
| `OpenCV` | Webcam feed & image processing |
| `MediaPipe` | Hand detection and tracking |
| `PyAutoGUI` | Mouse automation and system control |
| `NumPy`, `Math` | Distance and gesture logic |

---

## 🧩 Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/gesture-virtual-mouse.git
cd gesture-virtual-mouse
````

### 2️⃣ Create and Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate     # Windows
# or
source venv/bin/activate  # Mac/Linux
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the App

```bash
python gesture_mouse.py
```

---

## 🎮 Gesture Controls

| Gesture                     | Action         |
| --------------------------- | -------------- |
| ☝️ Move Index Finger        | Move Mouse     |
| 👍 Thumb + Index Touch      | Click          |
| 👍 Double Touch             | Double Click   |
| 🤚 Thumb-Index Close (Hold) | Drag           |
| ✌️ Index + Middle Close     | Scroll Up/Down |

> Press **ESC** to exit safely.

---

## ⚙️ Performance Tips

* Ensure **good lighting** for best tracking accuracy.
* Use a **30+ FPS webcam** for smoother performance.
* Adjust:

  ```python
  smooth_factor = 5
  click_cooldown = 0.3
  ```

  to tune responsiveness.

---

## 📂 Project Structure

```
gesture-virtual-mouse/
│
├── gesture_mouse.py        # Main script
├── requirements.txt        # Dependencies
├── README.md               # Documentation
└── assets/
    └── preview.mp4          # Screenshot/Preview videos
```

> 🖼️ Place a screenshot or demo GIF inside the `assets/` folder and name it `preview.png`.

---

## 🧑‍💻 Author

**Honey**
🎓 MCA Student | CGC College of Engineering, Landran
💡 Passionate about **AI, Computer Vision, and Intelligent Systems**

---

## 📜 License

This project is licensed under the **MIT License**.
You are free to use, modify, and distribute it with attribution.

---

## ⭐ Support

If you like this project:

* ⭐ Star this repo on GitHub
* 🪄 Share it with your friends or classmates
* 💬 Contribute or suggest new features!

---

<p align="center">
  Made with ❤️ using Python, OpenCV & MediaPipe
</p>
```

---

