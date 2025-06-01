import pyautogui
import time

# Danh sách các tọa độ X, Y và thời gian chờ sau khi nhấp vào điểm đó (tính bằng giây).
# Mỗi phần tử trong danh sách là một tuple (x, y, sleep_time).
# sleep_time là thời gian chờ sau khi nhấp vào điểm đó, TRƯỚC KHI nhấp vào điểm tiếp theo.
CLICK_POINTS = [
    (1911, 591, 5),  # Điểm 1: nhấp tại (1911, 591), sau đó chờ 10 giây
    (1911, 739, 1),  # Điểm 2: nhấp tại (1911, 739), sau đó chờ 15 giây
    # Thêm các điểm khác với thời gian chờ tùy chỉnh
]

# Khoảng thời gian chờ giữa mỗi chu kỳ nhấp chuột (tức là sau khi đã nhấp qua tất cả các điểm trong CLICK_POINTS)
# 3 phút = 180 giây (đã cập nhật từ 300 giây của bạn thành 180s để khớp với yêu cầu ban đầu)
# Nếu bạn muốn 5 phút, hãy giữ 300.
INTERVAL_BETWEEN_CYCLES = 300 # Giữ nguyên 5 phút như trong file bạn đã cung cấp

def click_multiple_points(points):
    """
    Di chuyển chuột đến từng điểm trong danh sách và thực hiện một cú nhấp chuột,
    sau đó chờ một khoảng thời gian được chỉ định cho điểm đó.
    """
    for i, (x, y, sleep_time) in enumerate(points):
        print(f"Đang nhấp tại tọa độ: ({x}, {y})")
        pyautogui.click(x, y)

        # Chờ thời gian được chỉ định cho điểm hiện tại
        print(f"Đã nhấp. Chờ {sleep_time} giây trước lần nhấp tiếp theo...")
        time.sleep(sleep_time)

def main():
    print("Bắt đầu tự động nhấp chuột vào nhiều điểm với thời gian chờ tùy chỉnh. Nhấn Ctrl+C để dừng.")
    try:
        while True:
            click_multiple_points(CLICK_POINTS)
            print(f"Đã hoàn thành một chu kỳ nhấp chuột qua tất cả các điểm. Chờ {INTERVAL_BETWEEN_CYCLES} giây trước chu kỳ tiếp theo...")
            time.sleep(INTERVAL_BETWEEN_CYCLES)
    except KeyboardInterrupt:
        print("\nĐã dừng tự động nhấp chuột.")

if __name__ == "__main__":
    main()