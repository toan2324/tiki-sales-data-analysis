# 🛒 Phân tích Hiệu suất Kinh doanh & Chiến lược Giá - Tiki Vietnam

## 📌 Giai đoạn 1: Business Understanding (Thấu hiểu bài toán kinh doanh)

> **Mục tiêu:** Chuyển đổi dữ liệu thô từ sàn TMĐT Tiki thành các hiểu biết kinh doanh (Actionable Insights) nhằm tối ưu hóa doanh thu và hành vi khách hàng.

---

### 1. Bối cảnh dự án (Context)
Trong kỷ nguyên Data-driven, việc hiểu rõ các chỉ số vận hành là yếu tố sống còn của doanh nghiệp. Dự án này tập trung vào phân tích bộ dữ liệu thực tế từ ngành hàng **Balo & Túi xách** trên Tiki. 

Với tư cách là một Data Analyst, tôi thực hiện dự án này để giải quyết bài toán: **"Làm sao để tăng trưởng GMV bền vững mà không làm xói mòn lợi nhuận do chiết khấu?"**

### 2. Xác định vấn đề (Problem Statement)
* **Tối ưu hóa chiết khấu:** Xác định ngưỡng giảm giá tối ưu để kích cầu mà không gây lỗ vốn.
* **Sức mạnh thương hiệu:** So sánh lợi thế cạnh tranh giữa các Official Brands (Mall) và các shop nhỏ lẻ.
* **Điểm chạm niềm tin:** Định lượng hóa mối tương quan giữa đánh giá người dùng và tốc độ tiêu thụ sản phẩm.

### 3. Hệ thống chỉ số đo lường (Metric Tree)
Dự án bám sát cấu trúc các chỉ số (KPIs) dựa trên nền tảng toán học chuyên sâu:

* **Chỉ số mục tiêu (North Star):** **Tổng giá trị giao dịch (GMV)**
  $$GMV = \sum_{i=1}^{n} (Price_{current, i} \times Quantity_{sold, i})$$

* **Chỉ số thúc đẩy (Drivers):**
  * **Giá trị đơn hàng trung bình (AOV):** Đo lường mức chi tiêu trung bình trên mỗi sản phẩm.
  * **Tỷ lệ chiết khấu (Discount Rate):** $$\text{Discount Rate} = \frac{P_{original} - P_{current}}{P_{original}}$$
  * **Chỉ số uy tín:** Điểm trung bình `rating_average` và mật độ `review_count`.

### 4. Câu hỏi kinh doanh chiến lược (Key Questions)
1. **Brand Analysis:** 10 thương hiệu nào đang nắm giữ thị phần doanh thu lớn nhất?
2. **Pricing Strategy:** Có tồn tại "điểm ngọt" về giá (Price Sweet Spot) để tối ưu hóa `quantity_sold`?
3. **Correlation:** Hệ số tương quan Pearson ($r$) giữa mức giảm giá và số lượng bán ra là bao nhiêu?
4. **Sentiment Impact:** Sản phẩm có đánh giá dưới 4.0 sao bị sụt giảm bao nhiêu % doanh thu so với nhóm trên 4.5 sao?

### 5. Giả thuyết nghiên cứu (Hypotheses)
* **H1:** Sản phẩm có chiết khấu từ **15% - 25%** có tốc độ tiêu thụ (Velocity) cao gấp 1.8 lần nhóm không giảm giá.
* **H2:** Thương hiệu có trên 100 đánh giá có thể duy trì giá cao hơn 10% thị trường mà không giảm lượng đơn hàng.

### 6. Phương pháp tiếp cận kỹ thuật (Technical Vision)
* **Công cụ:** SQL truy vấn, **Python (Pandas)** xử lý dữ liệu từ tệp nén ZIP và **Power BI** trực quan hóa.
* **Tối ưu:** Xây dựng Data Cleaning Pipeline tự động hóa để thay thế quy trình xử lý thủ công.

---
*Dữ liệu được trích xuất từ bộ "Tiki E-Commerce Dataset" trên Kaggle phục vụ mục đích nghiên cứu và xây dựng Portfolio.*
