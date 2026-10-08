# Selenium Python - Kiểm thử đăng nhập

Bài thực hành Buổi 8: Selenium 4, Page Object Model, Explicit Wait và Headless.
Website: https://automationexercise.com/login. Gồm 20 test case và 21 commit: commit khởi tạo có sẵn + một commit cho mỗi TC01–TC20.

## Cài đặt trên Windows

Yêu cầu Python 3.11+ và Google Chrome. Các phiên bản thư viện được chốt trong requirements.txt.

```powershell
cd D:\TestingProjects\selenium-login-tests
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Chạy kiểm thử

```powershell
# Mặc định chạy headless, tạo báo cáo HTML độc lập và JUnit XML
.\.venv\Scripts\python.exe -m pytest --html=reports/report.html --self-contained-html --junitxml=reports/junit.xml

# Hiển thị Chrome để xem thao tác
.\.venv\Scripts\python.exe -m pytest --headed

# Chạy riêng một ca
.\.venv\Scripts\python.exe -m pytest tests/test_tc01_valid_login.py

# Đếm các test được thu thập
.\.venv\Scripts\python.exe -m pytest --collect-only -q

# Chạy một nhóm, ví dụ validation hoặc session
.\.venv\Scripts\python.exe -m pytest -m validation
```

Không cần nhập tài khoản cá nhân. Fixture tạo tài khoản thử nghiệm UUID qua API createAccount và xóa chính tài khoản đó qua deleteAccount sau mỗi test cần tài khoản. Nếu API tạo/dọn dữ liệu lỗi, pytest báo ERROR; không bỏ qua âm thầm. Cần Internet cho website, API và lần tải ChromeDriver đầu tiên. Selenium Manager lưu driver trong .selenium-cache/ trên cùng ổ với project.

## Thiết kế theo bài học

- pages/: BasePage, LoginPage và HomePage; locator được đóng gói với tiền tố _, test không truy cập trực tiếp locator.
- tests/: mỗi tệp ứng với một TC; assertion nghiệp vụ đặt tại đây.
- tests/conftest.py: fixture theo từng test, cấu hình Chrome, WebDriverWait timeout, teardown và ảnh chụp khi lỗi.
- support/accounts.py: tạo/dọn dữ liệu giả, không dùng API để thay thế bước đăng nhập UI.
- docs/test-cases.md: tiền điều kiện, dữ liệu, bước và kỳ vọng cho từng test.
- reports/: kết quả chạy, ảnh lỗi (không commit).

Ưu tiên data-qa/CSS, XPath tương đối cho tên tài khoản. Dùng Explicit Wait, implicit wait bằng 0. Mỗi test đóng Chrome bằng quit(), kể cả khi thất bại. Mật khẩu không lưu trong Git; không lưu HTML nguồn trang có thể chứa dữ liệu nhạy cảm vào báo cáo.

## Phạm vi và giới hạn

Bao gồm đăng nhập và duy trì/kết thúc phiên đăng nhập. Không bao gồm kiểm thử đăng ký, quên mật khẩu, CAPTCHA, hiệu năng hoặc dò mật khẩu. Website công cộng có thể chậm hoặc thay đổi; ảnh lỗi và báo cáo giúp phân biệt lỗi ứng dụng với lỗi mạng/locator. Chạy tuần tự để hạn chế tải.

## Danh mục 20 test

| Nhóm | Mã | Số ca |
|---|---|---:|
| Đăng nhập thành công, Enter, sửa dữ liệu sau lỗi | TC01, TC12, TC14 | 3 |
| Trường bắt buộc và định dạng email | TC02, TC03, TC04, TC07, TC08 | 5 |
| Thông tin sai, email chưa có, hoa/thường, khoảng trắng | TC05, TC06, TC09, TC10 | 4 |
| Che mật khẩu và điều hướng bàn phím | TC11, TC13 | 2 |
| Đăng xuất, refresh, chuyển trang, tab và profile độc lập | TC15–TC20 | 6 |

Đọc đặc tả chi tiết trong [docs/test-cases.md](docs/test-cases.md).
Xem kết quả lần kiểm tra bàn giao trong [docs/verification.md](docs/verification.md).

## Lịch sử Git

```powershell
git log --reverse --oneline
git rev-list --count HEAD
```

Kết quả đếm là 21 tại thời điểm bàn giao. Commit đầu giữ nguyên c9f767d (Initial commit). Commit TC01 thêm bộ khung + ca đầu tiên; mỗi commit tiếp theo thêm đúng một tệp test cùng phần hỗ trợ/tài liệu cần thiết. Tệp .venv, driver cache và báo cáo sinh tự động không nằm trong Git.

## Tài liệu

- Đề bài: buoi8.pdf, đặc biệt trang 47, 60–63.
- https://automationexercise.com/test_cases
- https://automationexercise.com/api_list
- https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/
