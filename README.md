## 🎉 Auto-Clicker Python Script
- This is a simple Python script designed to automatically click at specific locations on your computer screen in cycles and with custom delays for each click point.

## 🎮 Features
- **Multi-point clicking**: Supports clicking at multiple different coordinates in a defined sequence.
- **Customizable delays**: Each click point can have its own specific delay after being clicked, allowing for flexible control over the automated workflow.
- **Repeat cycles**: The script will automatically repeat the entire click sequence after a specified interval.

## 🚀 Requirements
To run this script, you need to install:
- Python 3.x
- The `pyautogui` library

## ⚙️ Installation

### Install Python:
- If you don't have Python, download and install it from the official website: [python.org](https://www.python.org/downloads/)

### Install the `pyautogui` library:
- Open Terminal (on macOS/Linux) or Command Prompt/PowerShell (on Windows) and run the following command:
  ```
  pip install pyautogui
  ```

## 📚 How to Use
### ✅ Step 1: Configure `click.py`
- Open the `click.py` file in a text editor and edit the `CLICK_POINTS` and `INTERVAL_BETWEEN_CYCLES` sections.
```
# Danh sách các tọa độ X, Y và thời gian chờ sau khi nhấp vào điểm đó (tính bằng giây).
# Mỗi phần tử trong danh sách là một tuple (x, y, sleep_time).
# sleep_time là thời gian chờ sau khi nhấp vào điểm đó, TRƯỚC KHI nhấp vào điểm tiếp theo.
CLICK_POINTS = [
    (1911, 591, 10),  # Điểm 1: nhấp tại (1911, 591), sau đó chờ 10 giây
    (1911, 739, 15),  # Điểm 2: nhấp tại (1911, 739), sau đó chờ 15 giây
    # Thêm các điểm khác với thời gian chờ tùy chỉnh
    # Ví dụ: (x_diem_moi, y_diem_moi, thoi_gian_cho_sau_diem_moi)
]

# Khoảng thời gian chờ giữa mỗi chu kỳ nhấp chuột (tức là sau khi đã nhấp qua tất cả các điểm trong CLICK_POINTS)
# 5 phút = 300 giây (ví dụ)
INTERVAL_BETWEEN_CYCLES = 300
````
#### **`CLICK_POINTS`**:
- Replace the sample coordinate pairs with the actual coordinates you obtained in Step 1.
- Each element must be a tuple of 3 values: `(X, Y, sleep_time)`.
- `sleep_time` is the number of seconds the script will wait *after* clicking that point and *before* moving to the next point. If you don't want to wait after a point, set `sleep_time` to `0`.
#### **`INTERVAL_BETWEEN_CYCLES`**:
- This is the duration (in seconds) the script will wait *after completing all clicks in `CLICK_POINTS`* and *before starting the new cycle again*. The default is 300 seconds (5 minutes).

### ⬇️ Step 2: Run the script
- Open Terminal or Command Prompt/PowerShell, navigate to the directory containing the `click.py` file, and run the following command:
```
python click.py
```

### Stopping the script
- To stop the script, simply press `Ctrl+C` in the Terminal/Command Prompt window where the script is running.

## 📌 Important Notes
- **Display Scaling**: If you are using Windows and have a display scaling setting other than 100% (e.g., 125% or 150%), `pyautogui` may encounter issues with coordinate mapping. Try setting it to 100% if you experience problems.
- **Virtualization/Remote Environments**: The script may not work stably when run on a virtual machine (VM) or via remote connections (like RDP, TeamViewer) due to how they handle mouse interactions.
- **Control**: Use this script carefully. Ensure you have correctly configured the coordinates and delays to avoid unintended actions. Always double-check before using it for critical tasks.
- **Permissions**: On some operating systems (e.g., macOS), you may need to grant accessibility/control permissions to your Terminal application or IDE in the security and privacy settings.
- **Screen Resolution**: Ensure that the screen resolution does not change between when you obtain the coordinates and when you run the script.

## 📩 Contact me on Discord:
- Username: migu_2008

## 🎬 VIDEO WILL HELP YOU SET UP
-

## 🎉 HAVE FUN!
- Follow my GitHub profile for more :3
