import pyautogui
import time

# Danh sách các tọa độ X và Y bạn muốn nhấp.
# Mỗi cặp (X, Y) là một điểm.
# Bạn có thể thêm bao nhiêu điểm tùy ý vào danh sách này.
CLICK_POINTS = [
    (1911, 591),  # Điểm 1
    (1911, 739),  # Điểm 2
    # Thêm các điểm khác nếu cần
]

# Khoảng thời gian chờ giữa mỗi chu kỳ nhấp chuột (tính bằng giây)
# 3 phút = 180 giây
INTERVAL = 300

def click_multiple_points(points):
    """
    Di chuyển chuột đến từng điểm trong danh sách và thực hiện một cú nhấp chuột.
    """
    for x, y in points:
        print(f"Đang nhấp tại tọa độ: ({x}, {y})")
        pyautogui.click(x, y)
        time.sleep(5)  # Thêm một chút độ trễ giữa các lần nhấp liên tiếp
                          # để đảm bảo hệ thống nhận diện đúng
                          # Bạn có thể điều chỉnh hoặc bỏ qua nếu không cần

def main():
    print("Bắt đầu tự động nhấp chuột vào nhiều điểm. Nhấn Ctrl+C để dừng.")
    try:
        while True:
            click_multiple_points(CLICK_POINTS)
            print(f"Đã hoàn thành một chu kỳ nhấp chuột. Chờ {INTERVAL} giây trước chu kỳ tiếp theo...")
            time.sleep(INTERVAL)
    except KeyboardInterrupt:
        print("\nĐã dừng tự động nhấp chuột.")

if __name__ == "__main__":
    main()