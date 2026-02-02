# Nhật ký thay đổi

Tất cả các thay đổi đáng chú ý đối với EdgeAI for Beginners được ghi lại tại đây. Dự án này sử dụng các mục nhập theo ngày và phong cách Keep a Changelog (Thêm mới, Thay đổi, Sửa lỗi, Loại bỏ, Tài liệu, Di chuyển).

## 2025-10-30

### Thêm mới - Nâng cấp toàn diện Module06 AI Agents
- **Tích hợp Microsoft Agent Framework** (`Module06/01.IntroduceAgent.md`):
  - Phần hoàn chỉnh về Microsoft Agent Framework để phát triển agent sẵn sàng cho sản xuất
  - Các mẫu tích hợp chi tiết với Foundry Local cho triển khai tại edge
  - Ví dụ về điều phối đa-agent với các mô hình SLM chuyên biệt
  - Các mẫu triển khai doanh nghiệp với quản lý tài nguyên và giám sát
  - Các tính năng bảo mật và tuân thủ cho hệ thống agent tại edge
  - Ví dụ triển khai thực tế (bán lẻ, chăm sóc sức khỏe, dịch vụ khách hàng)

- **Chiến lược triển khai SLM Agent trong sản xuất**:
  - **Foundry Local**: Tài liệu runtime AI edge cấp doanh nghiệp hoàn chỉnh với hướng dẫn cài đặt, cấu hình và mẫu sản xuất
  - **Ollama**: Triển khai tập trung vào cộng đồng với giám sát toàn diện và quản lý mô hình
  - **VLLM**: Công cụ suy luận hiệu suất cao với các kỹ thuật tối ưu hóa tiên tiến và tính năng doanh nghiệp
  - Danh sách kiểm tra triển khai sản xuất và bảng so sánh cho cả ba nền tảng

- **Nâng cấp Framework SLM tối ưu hóa cho edge**:
  - **ONNX Runtime**: Phần mới toàn diện cho triển khai agent SLM đa nền tảng
  - Các mẫu triển khai phổ quát trên Windows, Linux, macOS, iOS và Android
  - Tùy chọn tăng tốc phần cứng (CPU, GPU, NPU) với phát hiện tự động
  - Các tính năng sẵn sàng sản xuất và tối ưu hóa dành riêng cho agent
  - Ví dụ triển khai hoàn chỉnh với tích hợp Microsoft Agent Framework

- **Tài liệu tham khảo và đọc thêm**:
  - Thư viện tài nguyên toàn diện với hơn 100 nguồn uy tín
  - Các bài nghiên cứu cốt lõi về AI agents và Small Language Models
  - Tài liệu chính thức cho tất cả các framework và công cụ lớn
  - Báo cáo ngành, phân tích thị trường và các tiêu chuẩn kỹ thuật
  - Tài nguyên giáo dục, hội nghị và diễn đàn cộng đồng
  - Các tiêu chuẩn, thông số kỹ thuật và framework tuân thủ

### Thay đổi - Hiện đại hóa nội dung Module06
- **Mục tiêu học tập nâng cao**: Thêm khả năng làm chủ Microsoft Agent Framework và triển khai tại edge
- **Tập trung vào sản xuất**: Chuyển từ hướng dẫn khái niệm sang hướng dẫn sẵn sàng triển khai với các ví dụ sản xuất
- **Ví dụ mã**: Cập nhật tất cả các ví dụ để sử dụng các mẫu SDK hiện đại và thực hành tốt nhất
- **Mẫu kiến trúc**: Thêm các kiến trúc agent phân cấp và phối hợp edge-to-cloud
- **Tối ưu hóa hiệu suất**: Nâng cao với các khuyến nghị quản lý tài nguyên và tự động mở rộng

### Tài liệu - Nâng cấp cấu trúc Module06
- **Phạm vi toàn diện về Agent Framework**: Từ các khái niệm cơ bản đến triển khai doanh nghiệp
- **Chiến lược triển khai sản xuất**: Hướng dẫn hoàn chỉnh cho Foundry Local, Ollama và VLLM
- **Tối ưu hóa đa nền tảng**: Thêm ONNX Runtime cho triển khai phổ quát
- **Thư viện tài nguyên**: Các tài liệu tham khảo phong phú để học tập và triển khai liên tục

### Thêm mới - Cập nhật tài liệu Model Context Protocol (MCP) cho Module06
- **Hiện đại hóa phần giới thiệu MCP** (`Module06/03.IntroduceMCP.md`):
  - Cập nhật với các thông số MCP mới nhất từ modelcontextprotocol.io (phiên bản 2025-06-18)
  - Thêm phép ẩn dụ USB-C chính thức cho các kết nối ứng dụng AI tiêu chuẩn hóa
  - Cập nhật phần kiến trúc với thiết kế hai lớp chính thức (Lớp Dữ liệu + Lớp Vận chuyển)
  - Nâng cao tài liệu về các nguyên thủy cốt lõi với nguyên thủy máy chủ (Công cụ, Tài nguyên, Gợi ý) và nguyên thủy khách hàng (Lấy mẫu, Khai thác, Ghi nhật ký)

- **Tài liệu tham khảo và tài nguyên MCP toàn diện**:
  - Thêm liên kết **MCP for Beginners** (https://aka.ms/mcp-for-beginners)
  - Tài liệu và thông số MCP chính thức (modelcontextprotocol.io)
  - Tài nguyên phát triển bao gồm MCP Inspector và các triển khai tham khảo
  - Tiêu chuẩn kỹ thuật (JSON-RPC 2.0, JSON Schema, OpenAPI, Server-Sent Events)

### Thêm mới - Tích hợp Qualcomm QNN cho Module04
- **Phần mới 7: Bộ tối ưu hóa Qualcomm QNN** (`Module04/05.QualcommQNN.md`):
  - Hướng dẫn toàn diện hơn 400 dòng về framework suy luận AI thống nhất của Qualcomm
  - Phạm vi chi tiết về tính toán dị thể (Hexagon NPU, Adreno GPU, Kryo CPU)
  - Tối ưu hóa nhận thức phần cứng cho nền tảng Snapdragon với phân phối khối lượng công việc thông minh
  - Các kỹ thuật lượng hóa tiên tiến (INT8, INT16, độ chính xác hỗn hợp) cho triển khai di động
  - Tối ưu hóa suy luận tiết kiệm năng lượng cho các thiết bị chạy pin và ứng dụng thời gian thực
  - Hướng dẫn cài đặt hoàn chỉnh với thiết lập SDK QNN và cấu hình môi trường
  - Ví dụ thực tế: Chuyển đổi PyTorch sang QNN, tối ưu hóa đa backend, tạo nhị phân ngữ cảnh
  - Các mẫu sử dụng nâng cao: cấu hình backend tùy chỉnh, lượng hóa động, phân tích hiệu suất
  - Phần khắc phục sự cố toàn diện và tài nguyên cộng đồng

- **Cấu trúc Module04 nâng cao**:
  - Cập nhật README.md để bao gồm 7 phần tiến bộ (trước đây là 6)
  - Thêm Qualcomm QNN vào bảng điểm chuẩn hiệu suất (cải thiện tốc độ 5-15 lần, giảm bộ nhớ 50-80%)
  - Kết quả học tập toàn diện cho triển khai AI di động và tối ưu hóa năng lượng

### Thay đổi - Cập nhật tài liệu Module04
- **Nâng cao tài liệu Microsoft Olive** (`Module04/03.MicrosoftOlive.md`):
  - Thêm phần "Kho công thức Olive" toàn diện bao gồm hơn 100 công thức tối ưu hóa được xây dựng sẵn
  - Phạm vi chi tiết về các họ mô hình được hỗ trợ (Phi, Llama, Qwen, Gemma, Mistral, DeepSeek)
  - Ví dụ sử dụng thực tế cho tùy chỉnh công thức và đóng góp cộng đồng
  - Nâng cao với các điểm chuẩn hiệu suất và hướng dẫn tích hợp

- **Sắp xếp lại các phần trong Module04**:
  - Apple MLX chuyển sang Phần 5 (trước đây là Phần 6)
  - Workflow Synthesis chuyển sang Phần 6 (trước đây là Phần 7)
  - Qualcomm QNN được đặt ở Phần 7 (tập trung vào di động/edge chuyên biệt)
  - Cập nhật tất cả các tham chiếu tệp và liên kết điều hướng tương ứng

### Sửa lỗi - Xác thực mẫu Workshop
- **Xác thực và sửa lỗi chat_bootstrap.py**:
  - Sửa lỗi câu lệnh import bị hỏng (`util.util.workshop_utils` → `util.workshop_utils`)
  - Tạo `__init__.py` bị thiếu trong gói util để giải quyết mô-đun Python đúng cách
  - Cài đặt các phụ thuộc cần thiết (openai, foundry-local-sdk) trong môi trường conda
  - Xác thực thành công việc thực thi mẫu với cả gợi ý mặc định và tùy chỉnh
  - Xác nhận tích hợp với dịch vụ Foundry Local và tải mô hình (phi-4-mini với tối ưu hóa CUDA)

### Tài liệu - Cập nhật hướng dẫn toàn diện
- **Cấu trúc lại hoàn chỉnh README.md của Module04**:
  - Thêm Qualcomm QNN như framework tối ưu hóa chính cùng với OpenVINO, Olive, MLX
  - Cập nhật kết quả học tập của chương để bao gồm triển khai AI di động và tối ưu hóa năng lượng
  - Nâng cao bảng so sánh hiệu suất với các chỉ số QNN và trường hợp sử dụng di động/edge
  - Duy trì tiến trình logic từ giải pháp doanh nghiệp đến tối ưu hóa nền tảng cụ thể

- **Tham chiếu chéo và điều hướng**:
  - Cập nhật tất cả các liên kết nội bộ và tham chiếu tệp cho số phần mới
  - Nâng cao mô tả tổng hợp quy trình để bao gồm môi trường di động, máy tính để bàn và đám mây
  - Thêm các liên kết tài nguyên toàn diện cho hệ sinh thái nhà phát triển Qualcomm

## 2025-10-08

### Thêm mới - Cập nhật toàn diện Workshop
- **Viết lại hoàn chỉnh README.md của Workshop**:
  - Thêm phần giới thiệu toàn diện giải thích giá trị của Edge AI (bảo mật, hiệu suất, chi phí)
  - Tạo 6 mục tiêu học tập cốt lõi với các năng lực chi tiết
  - Thêm bảng kết quả học tập với các sản phẩm và ma trận năng lực
  - Bao gồm phần kỹ năng sẵn sàng cho nghề nghiệp để phù hợp với ngành
  - Thêm hướng dẫn bắt đầu nhanh với các yêu cầu và thiết lập 3 bước
  - Tạo bảng tài nguyên cho các mẫu Python (8 tệp với thời gian chạy)
  - Thêm bảng Jupyter notebooks (8 notebooks với xếp hạng độ khó)
  - Tạo bảng tài liệu (7 tài liệu chính với hướng dẫn "Sử dụng khi nào")
  - Thêm các khuyến nghị lộ trình học tập cho các cấp độ kỹ năng khác nhau

- **Hạ tầng xác thực và kiểm tra Workshop**:
  - Tạo `scripts/validate_samples.py` - Công cụ xác thực toàn diện cho cú pháp, import và thực hành tốt nhất
  - Tạo `scripts/test_samples.py` - Trình chạy kiểm tra nhanh cho tất cả các mẫu Python
  - Thêm tài liệu xác thực vào `scripts/README.md`

- **Tài liệu toàn diện**:
  - Tạo `SAMPLES_UPDATE_SUMMARY.md` - Hướng dẫn chi tiết hơn 400 dòng bao gồm tất cả các cải tiến
  - Tạo `UPDATE_COMPLETE.md` - Tóm tắt điều hành về việc hoàn thành cập nhật
  - Tạo `QUICK_REFERENCE.md` - Thẻ tham chiếu nhanh cho Workshop

### Thay đổi - Hiện đại hóa mẫu Python của Workshop
- **Cập nhật tất cả 8 mẫu Python với thực hành tốt nhất**:
  - Nâng cao xử lý lỗi với các khối try-except xung quanh tất cả các hoạt động I/O
  - Thêm gợi ý kiểu và docstrings toàn diện
  - Triển khai mẫu ghi nhật ký nhất quán [INFO]/[ERROR]/[RESULT]
  - Bảo vệ các import tùy chọn với gợi ý cài đặt
  - Cải thiện phản hồi người dùng trong tất cả các mẫu

- **session01/chat_bootstrap.py**:
  - Nâng cao khởi tạo client với các thông báo lỗi toàn diện
  - Cải thiện xử lý lỗi streaming với xác thực chunk
  - Thêm xử lý ngoại lệ tốt hơn cho trường hợp dịch vụ không khả dụng

- **session02/rag_pipeline.py**:
  - Thêm bảo vệ import cho sentence-transformers với gợi ý cài đặt
  - Nâng cao xử lý lỗi cho các hoạt động nhúng và tạo
  - Cải thiện định dạng đầu ra với kết quả có cấu trúc

- **session02/rag_eval_ragas.py**:
  - Bảo vệ các import tùy chọn (ragas, datasets) với thông báo lỗi thân thiện với người dùng
  - Thêm xử lý lỗi cho các chỉ số đánh giá
  - Nâng cao định dạng đầu ra cho kết quả đánh giá

- **session03/benchmark_oss_models.py**:
  - Triển khai suy giảm nhẹ nhàng (tiếp tục khi mô hình gặp lỗi)
  - Thêm báo cáo tiến trình chi tiết và xử lý lỗi từng mô hình
  - Nâng cao tính toán thống kê với khả năng phục hồi lỗi toàn diện

- **session04/model_compare.py**:
  - Thêm gợi ý kiểu (kiểu trả về Tuple)
  - Nâng cao định dạng đầu ra với kết quả JSON có cấu trúc
  - Triển khai xử lý lỗi từng mô hình với khả năng phục hồi

- **session05/agents_orchestrator.py**:
  - Nâng cao Agent.act() với docstrings toàn diện
  - Thêm xử lý lỗi pipeline với ghi nhật ký từng giai đoạn
  - Cải thiện quản lý bộ nhớ và theo dõi trạng thái

- **session06/models_router.py**:
  - Nâng cao tài liệu chức năng cho tất cả các thành phần định tuyến
  - Thêm ghi nhật ký chi tiết trong hàm route()
  - Cải thiện đầu ra kiểm tra với kết quả có cấu trúc

- **session06/models_pipeline.py**:
  - Thêm xử lý lỗi vào hàm trợ giúp chat()
  - Nâng cao pipeline() với ghi nhật ký từng giai đoạn và báo cáo tiến trình
  - Cải thiện main() với khả năng phục hồi lỗi toàn diện

### Tài liệu - Nâng cao tài liệu Workshop
- Cập nhật README.md chính với phần Workshop làm nổi bật lộ trình học tập thực hành
- Nâng cao STUDY_GUIDE.md với phần Workshop toàn diện bao gồm:
  - Mục tiêu học tập và các lĩnh vực tập trung nghiên cứu
  - Câu hỏi tự đánh giá
  - Các bài tập thực hành với ước tính thời gian
  - Phân bổ thời gian cho học tập tập trung và bán thời gian
  - Thêm Workshop vào mẫu theo dõi tiến độ
- Cập nhật hướng dẫn phân bổ thời gian từ 20 giờ lên 30 giờ (bao gồm Workshop)
- Thêm mô tả mẫu Workshop và kết quả học tập vào README

### Sửa lỗi
- Giải quyết các mẫu xử lý lỗi không nhất quán trong các mẫu Workshop
- Sửa lỗi import phụ thuộc tùy chọn với các bảo vệ thích hợp
- Sửa lỗi thiếu gợi ý kiểu trong các chức năng quan trọng
- Khắc phục phản hồi người dùng không đủ trong các tình huống lỗi
- Sửa các vấn đề xác thực với hạ tầng kiểm tra toàn diện

---

## 2025-09-23

### Thay đổi - Hiện đại hóa lớn Module 08
- **Căn chỉnh toàn diện với các mẫu repository Microsoft Foundry-Local**:
  - Cập nhật tất cả các ví dụ mã để sử dụng `FoundryLocalManager` hiện đại và tích hợp SDK OpenAI
  - Thay thế các cuộc gọi `requests` thủ công đã lỗi thời bằng cách sử dụng SDK đúng cách
  - Căn chỉnh các mẫu triển khai với tài liệu và mẫu chính thức của Microsoft

- **Hiện đại hóa 05.AIPoweredAgents.md**:
  - Cập nhật điều phối đa-agent để sử dụng các mẫu SDK hiện đại
  - Nâng cao triển khai điều phối viên với các tính năng tiên tiến (vòng phản hồi, giám sát hiệu suất)
  - Thêm xử lý lỗi toàn diện và kiểm tra sức khỏe dịch vụ
  - Tích hợp các tham chiếu phù hợp với các mẫu cục bộ (`samples/05/multi_agent_orchestration.ipynb`)
  - Cập nhật các ví dụ gọi hàm để sử dụng tham số `tools` hiện đại thay vì `functions` đã lỗi thời
  - Thêm các mẫu triển khai sẵn sàng sản xuất với giám sát và theo dõi thống kê

- **Viết lại hoàn chỉnh 06.ModelsAsTools.md**:
  - Thay thế đăng ký công cụ cơ bản bằng triển khai định tuyến mô hình thông minh
  - Thêm lựa chọn mô hình dựa trên từ khóa cho các loại nhiệm vụ khác nhau (chung, lý luận, mã, sáng tạo)
  - Tích hợp cấu hình dựa trên môi trường với phân bổ mô hình linh hoạt
  - Nâng cao với giám sát sức khỏe dịch vụ toàn diện và xử lý lỗi
  - Thêm các mẫu triển khai sản xuất với giám sát yêu cầu và theo dõi hiệu suất
  - Căn chỉnh với triển khai cục bộ trong `samples/06/router.py` và `samples/06/model_router.ipynb`

- **Cải tiến cấu trúc tài liệu**:
  - Thêm các phần tổng quan làm nổi bật hiện đại hóa và căn chỉnh SDK
  - Nâng cao với biểu tượng cảm xúc và định dạng tốt hơn để cải thiện khả năng đọc
  - Thêm các tham chiếu phù hợp với các tệp mẫu cục bộ trong toàn bộ tài liệu
  - Bao gồm hướng dẫn triển khai sẵn sàng sản xuất và thực hành tốt nhất

### Thêm mới
- Các phần tổng quan toàn diện trong các tệp Module 08 làm nổi bật tích hợp SDK hiện đại
- Điểm nổi bật về kiến trúc giới thiệu các tính năng tiên tiến (hệ thống đa-agent, định tuyến thông minh)
- Các tham chiếu trực tiếp đến các triển khai mẫu cục bộ để trải nghiệm thực hành
- Hướng dẫn triển khai sản xuất với các mẫu giám sát và xử lý lỗi
- Ví dụ Jupyter notebook tương tác với các tính năng tiên tiến và điểm chuẩn

### Sửa lỗi
- Các điểm không khớp giữa tài liệu và các triển khai mẫu thực tế
- Các mẫu sử dụng SDK lỗi thời trong toàn bộ Module 08
- Thiếu các tham chiếu đến thư viện mẫu cục bộ toàn diện
- Các cách tiếp cận triển khai không nhất quán giữa
  - Các mẫu có thể chạy trong `Module08/samples/01`–`06` với hướng dẫn cmd trên Windows
    - `01` REST trò chuyện nhanh (`chat_quickstart.py`)
    - `02` SDK khởi động nhanh với OpenAI/Foundry Local và hỗ trợ Azure OpenAI (`sdk_quickstart.py`)
    - `03` CLI danh sách và kiểm tra (`list_and_bench.cmd`)
    - `04` Demo Chainlit (`app.py`)
    - `05` Điều phối đa tác nhân (`python -m samples.05.agents.coordinator`)
    - `06` Bộ định tuyến Models-as-Tools (`router.py`)
- Hỗ trợ Azure OpenAI trong mẫu SDK Phiên 2 với cấu hình biến môi trường
- `.vscode/settings.json` trỏ đến `Module08/.venv` để cải thiện phân tích Python
- `.env` với gợi ý `PYTHONPATH` để VS Code/Pylance nhận diện

### Đã thay đổi
- Cập nhật mô hình mặc định thành `phi-4-mini` trong tài liệu và mẫu của Module 08; loại bỏ các đề cập còn lại đến `phi-3.5` trong Module 08
- Cải tiến bộ định tuyến (`Module08/samples/06/router.py`):
  - Phát hiện điểm cuối qua `foundry service status` với phân tích regex
  - Kiểm tra sức khỏe `/v1/models` khi khởi động
  - Đăng ký mô hình có thể cấu hình qua môi trường (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Cập nhật yêu cầu: `Module08/requirements.txt` hiện bao gồm `openai` (cùng với `requests`, `chainlit`)
- Làm rõ hướng dẫn mẫu Chainlit và thêm phần khắc phục sự cố; giải quyết nhập khẩu qua cài đặt workspace

### Đã sửa
- Giải quyết vấn đề nhập khẩu:
  - Bộ định tuyến không còn phụ thuộc vào module `utils` không tồn tại; các hàm được tích hợp trực tiếp
  - Điều phối viên sử dụng nhập khẩu tương đối (`from .specialists import ...`) và được gọi qua đường dẫn module
  - Cấu hình VS Code/Pylance để giải quyết nhập khẩu `chainlit` và các gói
- Sửa lỗi chính tả nhỏ trong `STUDY_GUIDE.md` và thêm nội dung Module 08

### Đã xóa
- Xóa `Module08/infra/obs.py` không sử dụng và loại bỏ thư mục `infra/` trống; các mẫu quan sát được giữ lại như tùy chọn trong tài liệu

### Đã di chuyển
- Hợp nhất các demo của Module 08 vào `Module08/samples` với các thư mục đánh số theo phiên
  - Di chuyển ứng dụng Chainlit vào `samples/04`
  - Di chuyển các tác nhân vào `samples/05` và thêm các tệp `__init__.py` để giải quyết gói

### Tài liệu
- Tài liệu phiên Module 08 và tất cả README mẫu được bổ sung với các tham chiếu từ Microsoft Learn và các nhà cung cấp đáng tin cậy
- Cập nhật `Module08/README.md` với Tổng quan về Mẫu, cấu hình bộ định tuyến, và mẹo xác thực
- Phần Foundry Local trên Windows trong `Module07/README.md` được xác thực với tài liệu Learn
- Cập nhật `STUDY_GUIDE.md`:
  - Thêm Module 08 vào tổng quan, lịch trình, trình theo dõi tiến độ
  - Thêm phần Tham khảo toàn diện (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Lịch sử (tóm tắt)
- Kiến trúc khóa học và các module được thiết lập (Modules 01–07)
- Hiện đại hóa nội dung theo từng bước, chuẩn hóa định dạng, và thêm các nghiên cứu điển hình
- Mở rộng phạm vi các khung tối ưu hóa (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Chưa phát hành / Đang chờ xử lý (đề xuất)
- Kiểm tra nhanh tùy chọn cho từng mẫu để xác thực tính khả dụng của Foundry Local
- Xem xét các bản dịch để đồng bộ hóa tham chiếu mô hình (ví dụ: `phi-4-mini`) khi phù hợp
- Thêm cấu hình pyright tối thiểu nếu các nhóm muốn áp dụng độ nghiêm ngặt trên toàn workspace

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.