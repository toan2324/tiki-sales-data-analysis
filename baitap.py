import os

# Danh sách cấu trúc thư mục chuyên nghiệp
folders = [
    'data/raw',          # Dữ liệu gốc từ Kaggle (ZIP/CSV thô)
    'data/processed',    # Dữ liệu sau khi gộp và dọn dẹp (Excel/CSV sạch)
    'sql',               # Các file .sql truy vấn KPI
    'notebooks',         # File Python (.ipynb) xử lý dữ liệu
    'dashboards',        # File Power BI (.pbix)
    'reports/images',    # Ảnh chụp Dashboard để chèn vào README
    'docs'               # Project Charter, tài liệu hướng dẫn
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)
    # Tạo file .gitkeep để GitHub nhận diện thư mục
    with open(os.path.join(folder, '.gitkeep'), 'w') as f:
        pass

print("Cấu trúc thư mục đã sẵn sàng!")