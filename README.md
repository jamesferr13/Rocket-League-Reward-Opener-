# Rocket League Reward Opener (Automated)

This project is an automated tool for opening rewards in Rocket League. It simulates the necessary actions to open a user-defined number of rewards, helping speed up the process for players.

## 🚀 Features

- Automatically opens rewards in Rocket League
- Requires ZERO user interaction
- Easily configurable number of openings via code

## ⚙️ Requirements

- Rocket League must be running in a **1920x1080 resolution** window
- Python (pyautogui)
- Screen must remain active during execution

## 🧑‍💻 Usage

1. **Set up your Rocket League window:**
   - Resolution must be **1920x1080**
   - Window must be focused and visible on screen

2. **Configure the script:**
   - Open the script file
   - Change the value in the `for` loop to match how many rewards you want to open:
     ```python
     for i in range(DESIRED_AMOUNT):
         # DESIRED_AMOUNT = automated actions here
     ```

3. **Run the script:**
   - Execute the script and watch your inventory grow

## ⚠️ Disclaimer

This tool interacts with Rocket League’s interface and may violate terms of service. Use at your own risk.
