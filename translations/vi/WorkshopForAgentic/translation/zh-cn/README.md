<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aa775a734bda4590ecbe3a94a3b62197",
  "translation_date": "2026-01-05T17:48:25+00:00",
  "source_file": "WorkshopForAgentic/translation/zh-cn/README.md",
  "language_code": "vi"
}
-->
# 🎙️ AI Phòng Thu Podcast Workshop

![logo](../../../../../translated_images/vi/logo.8711e39dc8257d7b.png)

## Nhiệm vụ của bạn

Chào mừng đến với **AI Phòng Thu Podcast**! Bạn sắp ra mắt podcast công nghệ riêng của mình "Tương Lai Số" — nhưng có một bước ngoặc: bạn sẽ xây dựng một đội ngũ sản xuất do AI điều khiển để giúp bạn tạo ra nó. Không còn phải nghiên cứu, viết kịch bản và chỉnh sửa âm thanh không ngừng. Thay vào đó, bạn sẽ trở thành nhà sản xuất podcast siêu năng lực AI thông qua lập trình.

## Bối cảnh câu chuyện

Hãy tưởng tượng: bạn và bạn bè muốn bắt đầu một podcast về những xu hướng công nghệ thú vị nhất, nhưng mọi người đều bận học, làm việc hoặc cuộc sống. Nếu bạn có thể xây dựng một đội ngũ AI thông minh để làm công việc nặng nhọc thì sao? Một AI nghiên cứu chủ đề, một AI khác viết kịch bản hấp dẫn, và một AI thứ ba biến văn bản thành cuộc đối thoại tự nhiên và mượt mà. Nghe như phim khoa học viễn tưởng? Hãy biến nó thành hiện thực.

## Những gì bạn sẽ học

Sau khi hoàn thành workshop này, bạn sẽ biết cách:
- 🤖 Triển khai mô hình AI tại chỗ của riêng bạn (không phí API, không phụ thuộc đám mây!)
- 🔧 Xây dựng hệ thống AI chuyên nghiệp có thể phối hợp làm việc thực tế
- 🎬 Tạo quy trình sản xuất podcast hoàn chỉnh từ sáng tạo đến âm thanh

## Hành trình của bạn: Ba màn

Giống như bất kỳ câu chuyện hay nào, chúng ta có ba màn. Mỗi màn sẽ dần xây dựng phòng thu podcast AI của bạn:

| Chương | Nhiệm vụ của bạn | Điều gì xảy ra | Kỹ năng mở khóa |
|---------|-----------|--------------|----------------|
| **Màn một** | [Làm quen với trợ lý AI của bạn](01.BuildAIAgentWithSLM.md) | Bạn sẽ khám phá cách tạo ra AI có thể trò chuyện, tìm kiếm web và thậm chí giải quyết vấn đề. Hãy tưởng tượng chúng như thực tập sinh nghiên cứu không bao giờ ngủ. | 🎯 Xây dựng AI đầu tiên của bạn<br>🛠️ Trang bị siêu năng lực cho nó (công cụ!)<br>🧠 Dạy nó cách suy nghĩ<br>🌐 Kết nối internet |
| **Màn hai** | [Xây dựng đội ngũ sản xuất của bạn](02.AIAgentOrchestrationAndWorkflows.md) | Giờ thì thú vị rồi! Bạn sẽ điều phối nhiều AI phối hợp như một đội podcast thực thụ. Một người nghiên cứu, một người viết, bạn duyệt — hợp tác để thành công. | 🎭 Điều phối nhiều AI<br>🔄 Xây dựng quy trình duyệt<br>🖥️ Dùng giao diện DevUI kiểm thử<br>✋ Duy trì quyền kiểm soát con người |
| **Màn ba** | [Mang podcast của bạn đến sự sống](03.Multi-SpeakerPodcastGenerationWithVibeVoice.md) | Kết thúc hoành tráng! Biến kịch bản văn bản thành âm thanh podcast thật với giọng nói sống động và đối thoại tự nhiên. Podcast "Tương Lai Số" của bạn đã sẵn sàng phát hành! | 🎤 Ma thuật chuyển văn bản thành giọng nói<br>👥 Đa giọng người nói<br>⏱️ Âm thanh định dạng dài<br>🚀 Hoàn toàn tự động hóa |

Mỗi màn sẽ mở khóa khả năng mới. Nếu bạn đủ can đảm, có thể xem nhảy màn, nhưng chúng tôi khuyên nên học theo thứ tự!

## Yêu cầu môi trường

Workshop hỗ trợ nhiều cấu hình phần cứng:
- **CPU**: phù hợp để thử nghiệm và dùng quy mô nhỏ
- **GPU**: khuyến nghị cho môi trường sản xuất, tăng tốc đáng kể việc suy luận
- **NPU**: hỗ trợ tăng tốc bằng bộ xử lý thần kinh thế hệ mới

## Những gì bạn cần

### Danh sách phần mềm ✅
- **Python 3.10+** (ngôn ngữ lập trình của bạn)
- **Ollama** (chạy mô hình AI trên máy của bạn)
- **VS Code** (trình chỉnh sửa mã của bạn)
- **Mở rộng Python** (làm VS Code thông minh hơn)
- **Git** (để lấy mã)

### Kiểm tra phần cứng 💻
- **Tôi có chạy được không?**: 8GB RAM, 10GB dung lượng trống (dùng được, nhưng có thể hơi chậm)
- **Cấu hình lý tưởng**: RAM 16GB+, một GPU khá tốt (chạy mượt!)
- **Có NPU không?**: Càng tốt hơn! Mở khóa hiệu năng thế hệ tiếp theo 🚀

## Thiết lập phòng thu của bạn 🎬

### Bước 1: Nâng cấp Python

Đảm bảo bạn có Python 3.10 hoặc mới hơn:

```bash
python --version
# Nên hiển thị Python 3.10.x hoặc phiên bản mới hơn
```

Chưa có Python? Vào [python.org](https://python.org) tải về — miễn phí mà!

### Bước 2: Lấy Ollama (trình chạy mô hình AI của bạn)

Đến [ollama.ai](https://ollama.ai) tải Ollama phù hợp hệ điều hành của bạn. Hãy coi nó như động cơ chạy AI tại chỗ.

Kiểm tra đã sẵn sàng chưa:

```bash
ollama --version
```

### Bước 3: Tải về bộ não AI của bạn 🧠

Đã đến lúc tải model Qwen-3-8B (như tuyển người trợ lý AI đầu tiên):

```bash
ollama pull qwen3:8b
```

*Điều này có thể mất vài phút. Thời gian pha cà phê hoàn hảo! ☕*

### Bước 4: Cài đặt VS Code

Nếu chưa có, lấy [Visual Studio Code](https://code.visualstudio.com/). Đây là trình soạn thảo mã tốt nhất (không tin cứ thử 😄).

### Bước 5: Mở rộng Python

Trong VS Code:
1. Nhấn `Ctrl+Shift+X` (hoặc `Cmd+Shift+X` trên Mac)
2. Tìm "Python"
3. Cài đặt mở rộng Python chính thức của Microsoft

### Bước 6: Hoàn tất! 🎉

Thật đấy, bạn đã sẵn sàng. Hãy tạo ra vài phép thuật AI thôi!

### Bước 7: Cài đặt Microsoft Agent Framework và các gói liên quan 📦

Cài tất cả dependencies cần thiết cho workshop:

```bash
pip install -r ./Installations/requirements.txt -U
```

*Điều này sẽ cài Microsoft Agent Framework và mọi gói cần thiết. Pha cho mình một ly cà phê — lần đầu cài có thể lâu đấy! ☕*

## Hướng dẫn workshop

Cấu trúc dự án chi tiết, các bước cấu hình và cách chạy sẽ được giải thích dần trong quá trình workshop.

## Xử lý sự cố (khi có vấn đề) 🔧

### "Ôi, tải model chậm quá!"
**Giải pháp**: Dùng VPN hoặc cấu hình nguồn mirror cho Ollama. Đôi khi mạng không ổn định.

### "Máy tớ sắp sập rồi! Hết RAM!"
**Giải pháp**: Chuyển sang model nhỏ hơn hoặc điều chỉnh `num_ctx` để dùng ít bộ nhớ hơn. Hãy coi đó như chế độ ăn kiêng cho AI của bạn.

### "Tôi có thể dùng GPU để tăng tốc không?"
**Giải pháp**: Ollama tự động nhận GPU! Chỉ cần đảm bảo driver GPU của bạn là mới nhất. Tăng tốc miễn phí! 🏎️

## Tài liệu bổ sung (dành cho bạn thích tìm hiểu) 📚

- [Tài liệu Ollama](https://github.com/ollama/ollama) — Hiểu sâu về AI mô hình tại chỗ
- [Microsoft Agent Framework](https://microsoft.github.io/autogen/) — Tìm hiểu về xây dựng đội AI
- [Thông tin model Qwen](https://qwenlm.github.io/) — Hiểu về bộ não trợ lý AI của bạn

## Giấy phép

Giấy phép MIT — Hãy xây dựng thứ hay ho, chia sẻ nó và làm cho thế giới đẹp hơn! 🌍

## Muốn đóng góp?

Phát hiện bug? Có ý tưởng? Hãy gửi Issue hoặc PR! Chúng tôi thích không khí cộng đồng. ✨

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc thông tin không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn tham khảo chính thức. Đối với những thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp của con người. Chúng tôi không chịu trách nhiệm đối với bất kỳ sự hiểu nhầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->