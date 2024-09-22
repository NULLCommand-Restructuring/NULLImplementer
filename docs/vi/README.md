# NULL Implementer
## Tổng quan
**NULL Implementer** là một chương trình trợ lý trí tuệ nhân tạo được phát triển để hoạt động tương thích với môi trường dòng lệnh CMD Windows. Nó có khả năng tạo phản hồi văn bản cho các tác vụ trả lời câu hỏi, nghiên cứu các tài nguyên (có thể là tệp mã lập trình, tệp văn bản .pdf, .docx, tệp bảng tính .xlsx hay thậm chí là nội dung từ một URL trang web bất kỳ), tạo hình ảnh tức thì dựa trên ý tưởng văn bản mà người dùng cung cấp. Ngoài ra nó còn tích hợp thêm một trình mở khóa cực kỳ hữu ích dành cho người dùng sử dụng công cụ ChatGPT, giúp mở khóa các chức năng Plus trên tài khoản ChatGPT thông thường một cách nhanh chóng. **NULL Implementer** cung cấp một trải nghiệm sử dụng linh hoạt ngay trên nền tảng chỉ hỗ trợ dòng lệnh.

![NULL Implementer](https://nullcommand-restructuring.github.io/NULLCommand-Restructuring/NULLImplementer-DemoResources/main.jpg)

**NULL Implementer** hoạt động dựa trên nền tảng vững chắc là kho lưu trữ GitHub phổ biến [xtekky/gpt4free](https://github.com/xtekky/gpt4free). Kho lưu trữ này đóng vai trò là hạt nhân cực kỳ quan trọng, trái tim của chương trình, cung cấp các mô-đun quan trọng để chương trình hoạt động và phát triển lâu dài. Để tìm hiểu thêm về kho lưu trữ này, vui lòng tham khảo [tại đây](https://github.com/xtekky/gpt4free)

## Tính năng
- **Cấu hình linh hoạt**: Cho phép bạn tự cấu hình các thiết lập dữ liệu mà chương trình sẽ sử dụng để cung cấp dịch vụ cho bạn. Điều này bao gồm cấu hình loại trình duyệt sẽ được sử dụng để thu thập cookie cho AI tạo sinh sử dụng, cookie _U của site .bing.com cho AI tạo hình ảnh sử dụng, ngôn ngữ được AI tạo sinh sử dụng để tạo phản hồi văn bản và cuối cùng là địa chỉ email tài khoản ChatGPT được sử dụng để mở khóa các tính năng Plus cho tài khoản đó.
- **AI tạo sinh văn bản**: Cho phép xử lý nhiều tác vụ tạo sinh văn bản khác nhau như trả lời câu hỏi, nghiên cứu mã lập trình, nghiên cứu nội dung trong các tệp văn bản .docx, .pdf, các tệp bảng tính .xlsx hoặc thậm chí là xử lý nội dung một trang web.
- **AI tạo sinh hình ảnh**: Cho phép bạn gửi ý tưởng hình ảnh bạn muốn tạo dưới dạng một văn bản, sau đó tạo hình ảnh dựa vào ý tưởng của bạn và trả về kết quả dưới dạng một liên kết hình ảnh trên đám mây.
- **Trình mở khóa tính năng Plus cho ChatGPT**: Cho phép bạn mở khóa và sử dụng các tính năng của ChatGPT Plus trên một tài khoản thông thường (mỗi lần thực hiện có thời hạn sử dụng từ 10 - 15 phút), chỉ cần cung cấp địa chỉ email tài khoản ChatGPT của bạn và chương trình sẽ thực hiện phần còn lại.

![Features](https://nullcommand-restructuring.github.io/NULLCommand-Restructuring/NULLImplementer-DemoResources/features.png)

## Bắt đầu
Để nhanh chóng bắt đầu sử dụng **NULL Implementer**, hãy làm theo các bước sau:
1. Tải xuống phiên bản cuối cùng và thêm nó vào path environment của hệ thống Windows như mô tả trong phần [Cài đặt](#installation).
2. Mở CMD, chạy lệnh sau để cấu hình nhanh cho chương trình, bạn có thể thay đổi bất kỳ giá trị nào nếu bạn đã hiểu rõ về chúng:
    ```bash
    null-implementer config --browser firefox --bingcookie "" --lang "Việt Nam"
    ```
    ![Features](https://nullcommand-restructuring.github.io/NULLCommand-Restructuring/NULLImplementer-DemoResources/demo_3_getting_started.png)
3. Hãy thử đặt câu hỏi đầu tiên của bạn:
    ```bash
    null-implementer research --prompt "Bạn là ai?"
    ```
    ![Features](https://nullcommand-restructuring.github.io/NULLCommand-Restructuring/NULLImplementer-DemoResources/demo_4_getting_started.png)

[Click vào đây để xem video demo cho phần này.](https://nullcommand-restructuring.github.io/NULLCommand-Restructuring/NULLImplementer-DemoResources/demo_2_getting_started.mp4)

## Cài đặt
Để cài đặt NULL Implementer, hãy làm theo các bước sau:
1. **Tải xuống Bản phát hành**:
- Truy cập trang [Bản phát hành](https://github.com/NULLCommand-Restructuring/NULLImplementer/releases) của kho lưu trữ này.
- Tải xuống tệp `null-implementer.exe` phiên bản mới nhất.
2. **Thêm `null-implementer.exe` vào Path Environment**:
- Di chuyển tệp `null-implementer.exe` đã tải xuống đến thư mục có trong biến môi trường PATH của hệ thống.
- Để thêm tệp này vào PATH cho tất cả người dùng:
    - Mở **Control Panel**.
    - Truy cập **System and Security** > **System**.
    - Nhấp vào **Advanced system settings**.
    - Trong cửa sổ **System Properties**, nhấp vào nút **Environment Variables**.
    - Trong **System Variables**, tìm biến **Path** và nhấp vào **Edit**.
    - Nhấp vào **New** và thêm đường dẫn đến thư mục nơi bạn đặt tệp `null-implementer.exe`.
    - Nhấp vào **OK** để đóng tất cả các hộp thoại.
3. **Xác minh cài đặt**:
- Mở cửa sổ CMD trong Windows và nhập `null-implementer --version`, nếu nó hiển thị thông tin phiên bản thì có nghĩa là mọi thứ đã hoạt động.
![Version](https://nullcommand-restructuring.github.io/NULLCommand-Restructuring/NULLImplementer-DemoResources/version.png)

## Yêu cầu hệ thống:
- **Hệ điều hành**: Windows 10 hoặc phiên bản mới hơn.

## Cấu hình
- **NULL Implementer** có 4 tham số cần thực hiện cấu hình cho hoạt động của nó. Đầu tiên là `--browser` là tham số cung cấp thông tin loại trình duyệt nào sẽ được sử dụng để thu thập dữ liệu cookie phục vụ trình AI tạo sinh văn bản. Tiếp theo là `--bingcookie` là tham số được sử dụng để cung cấp thông tin cookie _U của site .bing.com, phục vụ trình AI tạo sinh hình ảnh. Tiếp theo là `--lang` là tham số cung câp thông tin ngôn ngữ nào sẽ được sử dụng để trình AI tạo sinh văn bản phản hồi các yêu cầu. Cuối cùng là `--gptemail` là tham số cung cấp thông tin địa chỉ email tài khoản ChatGPT mặc định sẽ được mở khóa các tính năng Plus khi bạn sử dụng option `gptunlocker` mà không cung cấp tham số `--email`.
- Nếu bạn muốn nhanh chóng sử dụng **NULL Implementer** mà không cần tìm hiểu cấu hình phức tạp, bạn có thể chạy câu lệnh sau đây trên CMD để sử dụng cấu hình mặc định (`--browser`: `firefox`, `--bingcookie`: `empty`, `--lang`: `English` và `--gptemail`: `project.someone@hotmail.com`):
    ```bash
    null-implementer config
    ```
    ![Config Default](https://nullcommand-restructuring.github.io/NULLCommand-Restructuring/NULLImplementer-DemoResources/config_default.png)
- Nếu bạn muốn sử dụng **NULL Implementer** với cấu hình tùy chỉnh của riêng mình (đảm bảo bạn đã hiểu rõ nó và biết mình đang làm gì), chỉ cần truyền các đối số tương ứng:
    ```bash
    null-implementer config --browser [your_browser_type] --bingcookie [your_bing_cookie] --lang [your_language] --gptemail [your_email_gpt_account]
    ```
    ![Config Detail](https://nullcommand-restructuring.github.io/NULLCommand-Restructuring/NULLImplementer-DemoResources/config_detail.png)
- Lưu ý: Bạn cần phải cấu hình đầy đủ cho **NULL Implementer** trước khi sử dụng nó để thực hiện điều gì đó. Hoặc là chạy lệnh sử dụng cấu hình mặc định nhanh, hoặc là cấu hình đầy đủ theo ý của riêng mình.

## Cách sử dụng
### Tùy chọn `research`
- Nếu chỉ đơn giản là bạn đang có một câu hỏi, một thắc mắc cần được giải đáp, hãy mở CMD Windows và gõ lệnh sau để yêu cầu AI tạo sinh văn bản giải quyết nó. AI tạo sinh văn bản sẽ sử dụng cơ sở kiến thức khổng lồ mà nó được đào tạo kết hợp khả năng truy cập dữ liệu internet thời gian thực để giúp bạn:
    ```bash
    null-implementer research --prompt "questions_you_need_answered"
    ```
    ![Simple Resesarch](https://nullcommand-restructuring.github.io/NULLCommand-Restructuring/NULLImplementer-DemoResources/simple_research.png)
[Click vào đây để xem video demo cho phần này.](https://nullcommand-restructuring.github.io/NULLCommand-Restructuring/NULLImplementer-DemoResources/simple_research.mp4)
- Bạn có thể cung cấp một tệp văn bản (.txt, .docx, .pdf, ...) hoặc mã lập trình (.html, .js, .py, ...) dưới dạng địa chỉ của nó tại máy tính local hoặc liên kết của nó trên đám mây bằng cách sử dụng `--resource` sau option `research`, sau đó yêu cầu AI tạo sinh giải quyết một yêu cầu liên quan đến tài nguyên mà bạn đã cung cấp như sau:
    ```bash
    null-implementer research --resource [your_path_pdf] [your_path_docx] ... --prompt "questions_you_need_answered"
    ```
    ![Resource Resesarch](https://nullcommand-restructuring.github.io/NULLCommand-Restructuring/NULLImplementer-DemoResources/resource_research.png)

    [Click vào đây để xem video demo cho phần này.](https://nullcommand-restructuring.github.io/NULLCommand-Restructuring/NULLImplementer-DemoResources/resource_research.mp4)
- Bạn cũng có thể cung cấp một tài nguyên từ đám mây, chẳng hạn một trang web, một liên kết trên đám mây, miễn là nó có thể truy cập được từ trình duyệt, sau đó yêu câu AI giải quyết một yêu cầu liên quan đến tài nguyên từ đám mây đó như sau:
    ```bash
    null-implementer research --resource [your_url_1] [your_url_2] ... --prompt "questions_you_need_answered"
    ```
    ![Web Resesarch](https://nullcommand-restructuring.github.io/NULLCommand-Restructuring/NULLImplementer-DemoResources/web_research.png)

    [Click vào đây để xem video demo cho phần này.](https://nullcommand-restructuring.github.io/NULLCommand-Restructuring/NULLImplementer-DemoResources/web_research.mp4)
- Một trường hợp chung có thể áp dụng cho các trường hợp sử dụng ở trước đã đề cập, khi câu hỏi của bạn khá phức tạp và không thể biểu diễn trực tiếp thành một hàng trong CMD của Windows, lúc này bạn có thể nhập câu hỏi đó vào một tệp văn bản .txt (ở đây ví dụ là `question.txt`) sau đó thực hiện câu lệnh như sau:
    ```bash
    null-implementer research --resource [your_url_1] [your_url_2] ... --prompt "your_path_question_txt"
    ```
    ![Question File](https://nullcommand-restructuring.github.io/NULLCommand-Restructuring/NULLImplementer-DemoResources/question_file.png)

    [Click vào đây để xem video demo cho phần này.](https://nullcommand-restructuring.github.io/NULLCommand-Restructuring/NULLImplementer-DemoResources/question_file.mp4)
### Tùy chọn `imager`
- Bạn có thể cung cấp ý tưởng cho bức ảnh bạn muốn tạo và để trình AI tạo ảnh của **NULL Implementer** thực hiện phần còn lại:
    ```bash
    null-implementer imager --prompt "your_image_idea"
    ```
    ![Imager Demo](https://nullcommand-restructuring.github.io/NULLCommand-Restructuring/NULLImplementer-DemoResources/imager_demo.png)
    [Click vào đây để xem video demo cho phần này.](https://nullcommand-restructuring.github.io/NULLCommand-Restructuring/NULLImplementer-DemoResources/imager_demo.mp4)
### Tùy chọn `gptunlocker`
- Bạn có một tài khoản ChatGPT thông thường, bạn mong muốn được sử dụng các tính năng Plus của công cụ này nhưng điều kiện kinh tế không cho phép. Hãy đưa cho **NULL Implementer** địa chỉ email tài khoản ChatGPT của bạn và để nó thực hiện việc mở khóa các tính năng Plus cho bạn, thực hiện lệnh sau:
    ```bash
    null-implementer gptunlocker --email "your_email_gpt_account"
    ```
    ![GPT Plus Unlocker](https://nullcommand-restructuring.github.io/NULLCommand-Restructuring/NULLImplementer-DemoResources/gptunlocker_demo.png)
    [Click vào đây để xem video demo cho phần này.](https://nullcommand-restructuring.github.io/NULLCommand-Restructuring/NULLImplementer-DemoResources/gptunlocker_demo.mp4)
- Bạn có thể không cần cung cấp tham số `--email`, lúc này **NULL Implementer** sẽ lấy giá trị mặc định được cấu hình trong tùy chọn `config`. Thực hiện lệnh sau:
    ```bash
    null-implementer gptunlocker 
    ```
    ![GPT Plus Unlocker](https://nullcommand-restructuring.github.io/NULLCommand-Restructuring/NULLImplementer-DemoResources/gptunlocker_demo_1.png)
    [Click vào đây để xem video demo cho phần này.](https://nullcommand-restructuring.github.io/NULLCommand-Restructuring/NULLImplementer-DemoResources/gptunlocker_demo_1.mp4)