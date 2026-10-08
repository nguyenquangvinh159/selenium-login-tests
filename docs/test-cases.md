# Đặc tả test case đăng nhập

Website: https://automationexercise.com/login. Công cụ: Selenium Python + pytest.
Phạm vi: form đăng nhập và vòng đời phiên đăng nhập; không kiểm thử form đăng ký.

## Quy ước

- Mỗi test dùng một phiên Chrome mới. Những ca cần tài khoản tồn tại tự tạo dữ liệu qua API và dọn trong teardown.
- Dữ liệu tài khoản là giả, email UUID thuộc example.com. Không dùng tài khoản cá nhân.
- API chỉ chuẩn bị/dọn dữ liệu. Các bước đăng nhập và assertion của test chạy qua UI.
- Test không phụ thuộc thứ tự, không retry tự động để che lỗi, không dùng time.sleep().
- Kết quả thực tế nằm trong báo cáo HTML/XML, không đồng nhất kết quả kỳ vọng với thực tế.
- 1 commit khởi tạo có sẵn + 20 commit TC01–TC20; mỗi commit thêm một test riêng.

## TC01 - Đăng nhập hợp lệ

- Nhóm / ưu tiên: Positive / Cao.
- Tiền điều kiện: tài khoản thử nghiệm được tạo thành công; trình duyệt sạch mở /login.
- Dữ liệu: email và mật khẩu của tài khoản vừa tạo.
- Bước: nhập email → nhập mật khẩu → bấm Login.
- Kỳ vọng: chuyển về /, hiển thị chính xác tên tài khoản và link Logout.
- Tự động hóa: tests/test_tc01_valid_login.py.

## TC02 - Bỏ trống mật khẩu

- Nhóm / ưu tiên: Validation / Cao; ca bắt buộc của đề bài trang 63.
- Tiền điều kiện: trình duyệt sạch mở /login; không cần tài khoản vì validation chạy trước khi gửi.
- Dữ liệu: email validation@example.com, mật khẩu rỗng.
- Bước: nhập email → để trống mật khẩu → bấm Login.
- Kỳ vọng: password có valueMissing=true, valid=false, thông báo không rỗng; focus vào mật khẩu; vẫn ở /login.
- Tự động hóa: tests/test_tc02_missing_password.py.

## TC03 - Bỏ trống email

- Nhóm / ưu tiên: validation / Cao.
- Tiền điều kiện: Không cần tài khoản; mở /login trong trình duyệt sạch.
- Dữ liệu: Email rỗng, mật khẩu DummyPass9!.
- Bước: Để trống email → nhập mật khẩu → bấm Login.
- Kỳ vọng: Email có valueMissing=true, valid=false, thông báo không rỗng; focus vào email; vẫn ở /login.
- Tự động hóa: tests/test_tc03_missing_email.py.

## TC04 - Bỏ trống cả email và mật khẩu

- Nhóm / ưu tiên: validation / Cao.
- Tiền điều kiện: Không cần tài khoản; mở /login trong trình duyệt sạch.
- Dữ liệu: Cả hai trường rỗng.
- Bước: Bấm Login khi chưa nhập dữ liệu.
- Kỳ vọng: Cả hai trường báo thiếu; email nhận focus trước; vẫn ở /login.
- Tự động hóa: tests/test_tc04_both_fields_empty.py.
