"""
HƯỚNG DẪN CHI TIẾT CÁC HUGGING FACE SKILLS
VỚI MẪU CÂU HỎI/PROMPT MẪU

File thamchieu.py chứa 8 skills để làm việc với Hugging Face Hub.
Dưới đây là giải thích chi tiết và các câu hỏi/mẫu prompt mẫu cho từng skill.
"""

# ============================================================
# 1. hugging-face-model-trainer
# ============================================================
"""
CHỨC NĂNG: Huấn luyện/fine-tune các mô hình ngôn ngữ (LLM)
CÔNG NGHỆ: Sử dụng TRL (Transformer Reinforcement Learning)
HỖ TRỢ: SFT, DPO, GRPO, Reward Modeling, GGUF conversion

CÁC TÍNH NĂNG CHÍNH:
- Supervised Fine-Tuning (SFT): Huấn luyện giám sát cơ bản
- DPO (Direct Preference Optimization): Tối ưu hóa trực tiếp dựa trên sở thích
- GRPO (Group Relative Policy Optimization): Tối ưu hóa chính sách nhóm
- Reward Modeling: Huấn luyện mô hình phần thưởng
- GGUF Conversion: Chuyển đổi sang định dạng GGUF để chạy local (llama.cpp)
- Hardware selection: Tự động chọn phần cứng phù hợp
- Cost estimation: Ước tính chi phí huấn luyện
- Trackio monitoring: Theo dõi quá trình huấn luyện
- Hub persistence: Lưu trữ tự động lên Hugging Face Hub

MẪU CÂU HỎI/PROMPT:
---------------------------------------------
1. "Train a Llama-3-8B model on my custom dataset for sentiment analysis"
   → Huấn luyện model Llama-3-8B trên dataset tùy chỉnh cho phân tích cảm xúc

2. "Fine-tune mistral-7b using DPO method with the help command dataset"
   → Fine-tune mistral-7b sử dụng phương pháp DPO với dataset help command

3. "Convert my fine-tuned model to GGUF format for local inference"
   → Chuyển đổi model đã fine-tune sang định dạng GGUF để chạy local

4. "Estimate the cost to train a 70B model on 10000 steps"
   → Ước tính chi phí huấn luyện model 70B trên 10000 bước

5. "Set up tracking for my training job with Trackio"
   → Thiết lập theo dõi cho job huấn luyện với Trackio
"""


# ============================================================
# 2. hugging-face-paper-publisher
# ============================================================
"""
CHỨC NĂNG: Xuất bản và quản lý paper nghiên cứu trên Hugging Face Hub
HỖ TRỢ: Tạo trang paper, liên kết models/datasets, claim authorship

CÁC TÍNH NĂNG CHÍNH:
- Tạo trang paper trên Hub: Hiển thị như một repo riêng
- Liên kết paper với models: Kết nối paper với model đã publish
- Liên kết paper với datasets: Kết nối paper với dataset đã share
- Claim authorship: Xác nhận quyền tác giả
- Tạo markdown: Viết bài báo dạng markdown chuyên nghiệp

MẪU CÂU HỎI/PROMPT:
---------------------------------------------
1. "Publish my research paper about LLM optimization on Hugging Face"
   → Xuất bản paper nghiên cứu về tối ưu LLM lên Hugging Face

2. "Link my paper to the model I trained"
   → Liên kết paper của tôi với model đã huấn luyện

3. "Create a paper page for my new dataset"
   → Tạo trang paper cho dataset mới của tôi

4. "Claim authorship of the paper 'Attention is All You Need'"
   → Xác nhận quyền tác giả cho paper 'Attention is All You Need'

5. "Generate a professional research article in markdown format"
   → Tạo bài nghiên cứu chuyên nghiệp dạng markdown
"""


# ============================================================
# 3. hugging-face-datasets
# ============================================================
"""
CHỨC NĂNG: Tạo và quản lý datasets trên Hugging Face Hub
HỖ TRỢ: Initialize repos, configs, streaming, SQL queries

CÁC TÍNH NĂNG CHÍNH:
- Initialize repos: Tạo repository cho dataset mới
- Define configs: Định nghĩa cấu hình và system prompts
- Streaming row updates: Cập nhật dữ liệu streaming
- SQL-based queries: Query và transform dữ liệu bằng SQL

MẪU CÂU HỎI/PROMPT:
---------------------------------------------
1. "Create a new dataset repository for Vietnamese text classification"
   → Tạo repository dataset mới cho phân loại văn bản tiếng Việt

2. "Initialize the dataset with config and system prompt"
   → Khởi tạo dataset với config và system prompt

3. "Upload new rows to my dataset using streaming"
   → Upload các row mới vào dataset sử dụng streaming

4. "Query my dataset to filter samples with label='positive'"
   → Query dataset để lọc các mẫu có label='positive'

5. "Transform the dataset by converting text to lowercase"
   → Transform dataset bằng cách chuyển text thành chữ thường
"""


# ============================================================
# 4. hugging-face-evaluation
# ============================================================
"""
CHỨC NĂNG: Thêm và quản lý kết quả đánh giá trong model cards
HỖ TRỢ: Extract eval tables, import scores, custom evaluations

CÁC TÍNH NĂNG CHÍNH:
- Extract eval tables: Trích xuất bảng đánh giá từ README
- Import scores: Import điểm số từ Artificial Analysis API
- Custom evaluations: Chạy đánh giá tùy chỉnh
- vLLM/lighteval integration: Sử dụng vLLM hoặc lighteval để đánh giá

MẪU CÂU HỎI/PROMPT:
---------------------------------------------
1. "Extract evaluation results from my model card"
   → Trích xuất kết quả đánh giá từ model card của tôi

2. "Import evaluation scores from Artificial Analysis API"
   → Import điểm đánh giá từ Artificial Analysis API

3. "Run MMLU evaluation on my fine-tuned model"
   → Chạy đánh giá MMLU trên model đã fine-tune

4. "Evaluate my model using lighteval on benchmark datasets"
   → Đánh giá model sử dụng lighteval trên các benchmark datasets

5. "Add evaluation results to my model README"
   → Thêm kết quả đánh giá vào README của model
"""


# ============================================================
# 5. hugging-face-tool-builder
# ============================================================
"""
CHỐC NĂNG: Xây dựng các script tái sử dụng cho Hugging Face API
HỖ TRỢ: Chain API calls, automate tasks

CÁC TÍNH NĂNG CHÍNH:
- Build reusable scripts: Tạo script có thể tái sử dụng
- Chain API calls: Kết nối nhiều API calls với nhau
- Automate tasks: Tự động hóa các task lặp đi lặp lại

MẪU CÂU HỎI/PROMPT:
---------------------------------------------
1. "Create a script to download and merge LoRA adapters"
   → Tạo script để download và merge LoRA adapters

2. "Build an automation script for model uploading pipeline"
   → Xây dựng script tự động cho pipeline upload model

3. "Write a script that chains dataset download → preprocessing → upload"
   → Viết script kết nối download dataset → tiền xử lý → upload

4. "Create a reusable tool for batch model evaluation"
   → Tạo công cụ tái sử dụng cho đánh giá model hàng loạt
"""


# ============================================================
# 6. hugging-face-cli
# ============================================================
"""
CHỨC NĂNG: Thực thi các thao tác HF Hub bằng hf CLI
HỖ TRỢ: Download, upload, manage repos, cloud jobs

CÁC TÍNH NĂNG CHÍNH:
- Download models/datasets: Tải models và datasets
- Upload files: Upload files lên Hub
- Manage repos: Quản lý repositories
- Run cloud compute jobs: Chạy jobs tính toán trên cloud

MẪU CÂU HỎI/PROMPT:
---------------------------------------------
1. "Download the llama-3-8b model to local"
   → Download model llama-3-8b về local

2. "Upload my fine-tuned model to Hugging Face"
   → Upload model đã fine-tune lên Hugging Face

3. "Create a new model repository"
   → Tạo repository model mới

4. "List all models in my organization"
   → Liệt kê tất cả models trong organization của tôi

5. "Run a inference job on GPU using hf CLI"
   → Chạy job inference trên GPU sử dụng hf CLI
"""


# ============================================================
# 7. hugging-face-jobs
# ============================================================
"""
CHỨC NĂNG: Chạy compute jobs trên hạ tầng Hugging Face
HỖ TRỢ: Python scripts, scheduled jobs, monitoring

CÁC TÍNH NĂNG CHÍNH:
- Execute Python scripts: Thực thi Python scripts trên HF infrastructure
- Manage scheduled jobs: Quản lý các jobs theo lịch
- Monitor job status: Theo dõi trạng thái job

MẪU CÂU HỎI/PROMPT:
---------------------------------------------
1. "Run a Python training script on Hugging Face infrastructure"
   → Chạy script training Python trên hạ tầng HF

2. "Schedule a weekly model evaluation job"
   → Lên lịch job đánh giá model hàng tuần

3. "Check the status of my running training job"
   → Kiểm tra trạng thái của job training đang chạy

4. "Cancel the pending inference job"
   → Hủy job inference đang chờ

5. "Get logs from my completed training job"
   → Lấy logs từ job training đã hoàn thành
"""


# ============================================================
# 8. hugging-face-trackio
# ============================================================
"""
CHỨC NĂNG: Theo dõi và trực quan hóa ML training experiments với Trackio
HỖ TRỢ: Log metrics, CLI retrieval, real-time dashboards

CÁC TÍNH NĂNG CHÍNH:
- Log metrics: Ghi log metrics qua Python API
- Retrieve metrics: Lấy metrics qua CLI
- Real-time dashboards: Dashboard realtime sync tới HF Spaces

MẪU CÂU HỎI/PROMPT:
---------------------------------------------
1. "Set up Trackio for tracking my training metrics"
   → Thiết lập Trackio để theo dõi metrics training

2. "Log the loss and accuracy during training"
   → Ghi log loss và accuracy trong quá trình training

3. "Retrieve training metrics from the last experiment"
   → Lấy metrics từ experiment gần nhất

4. "Create a real-time dashboard for my experiments"
   → Tạo dashboard realtime cho các experiments của tôi

5. "Compare metrics across different training runs"
   → So sánh metrics giữa các lần training khác nhau
"""


# ============================================================
# TỔNG KẾT - BẢNG SO SÁNH
# ============================================================

"""
+----------------------------+------------------------------------------+
| SKILL                      | MỤC ĐÍCH CHÍNH                           |
+----------------------------+------------------------------------------+
| model-trainer              | Huấn luyện/fine-tune LLM                 |
| paper-publisher            | Xuất bản paper nghiên cứu                |
| datasets                   | Quản lý datasets                         |
| evaluation                 | Đánh giá mô hình                         |
| tool-builder               | Tạo script tự động hóa                   |
| cli                        | Thao tác với HF qua command line        |
| jobs                       | Chạy jobs trên cloud HF                 |
| trackio                    | Theo dõi experiments                     |
+----------------------------+------------------------------------------+

VÍ DỤ SỬ DỤNG THỰC TẾ:
1. Train → Evaluate → Publish paper
2. Create dataset → Train model → Convert to GGUF → Upload
3. Track training → Monitor jobs → Download results

Cần giải thích thêm phần nào? Hãy cho tôi biết!
"""
