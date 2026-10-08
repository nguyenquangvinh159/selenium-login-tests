# Selenium Python - Kiểm thử đăng nhập

Bài thực hành Buổi 8: Selenium 4, Page Object Model, Explicit Wait và Headless.
Website: https://automationexercise.com/login. Mục tiêu hoàn thiện: 20 test case, 21 commit gồm commit khởi tạo có sẵn.

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

## Tài liệu

- Đề bài: buoi8.pdf, đặc biệt trang 47, 60–63.
- https://automationexercise.com/test_cases
- https://automationexercise.com/api_list
- https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/
