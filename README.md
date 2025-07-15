## Auto-Clicker Python Script
- Đây là một script Python đơn giản được thiết kế để tự động nhấp chuột vào các vị trí cụ thể trên màn hình máy tính của bạn theo chu kỳ và với thời gian chờ tùy chỉnh cho từng điểm nhấp.

## Tính năng
- **Nhấp chuột đa điểm**: Hỗ trợ nhấp vào nhiều tọa độ khác nhau theo một trình tự đã định.
- **Thời gian chờ tùy chỉnh**: Mỗi điểm nhấp có thể có thời gian chờ riêng biệt sau khi được nhấp, cho phép kiểm soát linh hoạt luồng công việc tự động.
- **Chu kỳ lặp lại**: Script sẽ tự động lặp lại toàn bộ chuỗi nhấp chuột sau một khoảng thời gian xác định.

## Yêu cầu
Để chạy script này, bạn cần cài đặt:
- Python 3.x
- Thư viện `pyautogui`

## Cài đặt

### Cài đặt Python:
- Nếu bạn chưa có Python, hãy tải xuống và cài đặt từ trang web chính thức: [python.org](https://www.python.org/downloads/)

### Cài đặt thư viện `pyautogui`:
- Mở Terminal (trên macOS/Linux) hoặc Command Prompt/PowerShell (trên Windows) và chạy lệnh sau:
  ```
  pip install pyautogui
  ```

## Cách sử dụng
### Bước 1: Cấu hình `click.py`
- Mở tệp `click.py` trong một trình soạn thảo văn bản và chỉnh sửa phần `CLICK_POINTS` và `INTERVAL_BETWEEN_CYCLES`.
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
- Thay thế các cặp tọa độ mẫu bằng tọa độ thực tế bạn đã lấy ở Bước 1.
- Mỗi phần tử phải là một tuple gồm 3 giá trị `(X, Y, sleep_time)`.
- `sleep_time` là số giây script sẽ chờ *sau khi* nhấp vào điểm đó và *trước khi* chuyển sang điểm tiếp theo. Nếu bạn không muốn chờ sau một điểm, hãy đặt `sleep_time` là `0`.
#### **`INTERVAL_BETWEEN_CYCLES`**:
- Đây là khoảng thời gian (tính bằng giây) mà script sẽ chờ *sau khi hoàn thành tất cả các lần nhấp trong `CLICK_POINTS`* và *trước khi bắt đầu lại chu kỳ mới*. Mặc định là 300 giây (5 phút).
- 
### Bước 2: Chạy script
- Mở Terminal hoặc Command Prompt/PowerShell, điều hướng đến thư mục chứa tệp `click.py` và chạy lệnh sau:
```
python click.py
```

### Dừng script
- Để dừng script, bạn chỉ cần nhấn `Ctrl+C` trong cửa sổ Terminal/Command Prompt nơi script đang chạy.

## Lưu ý quan trọng
- **Tỷ lệ hiển thị màn hình (Display Scaling)**: Nếu bạn đang sử dụng Windows và có cài đặt tỷ lệ hiển thị khác 100% (ví dụ: 125% hoặc 150%), `pyautogui` có thể gặp vấn đề về ánh xạ tọa độ. Hãy thử đặt về 100% nếu bạn gặp sự cố.
- **Môi trường ảo hóa/Từ xa**: Script có thể hoạt động không ổn định khi chạy trên máy ảo (VM) hoặc qua các kết nối từ xa (như RDP, TeamViewer) do cách chúng xử lý tương tác chuột.
- **Kiểm soát**: Sử dụng script này một cách cẩn thận. Đảm bảo bạn đã cấu hình đúng tọa độ và thời gian chờ để tránh các hành động không mong muốn. Luôn kiểm tra kỹ trước khi sử dụng trong các tác vụ quan trọng.
- **Quyền truy cập**: Trên một số hệ điều hành (ví dụ: macOS), bạn có thể cần cấp quyền truy cập/điều khiển cho ứng dụng Terminal hoặc IDE của bạn trong phần cài đặt bảo mật và quyền riêng tư.
- **Độ phân giải màn hình**: Đảm bảo độ phân giải màn hình không thay đổi giữa lúc bạn lấy tọa độ và lúc bạn chạy script.

## 📩 Contact me on Discord:
- Username: migu_2008

## 🎬 VIDEO WILL HELP YOU SET UP
-

## 🎉 HAVE FUN!
- Follow my GitHub profile for more :3
