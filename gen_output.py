import os
from bs4 import BeautifulSoup  # Cần cài đặt thư viện beautifulsoup4
import glob

# Đường dẫn đến thư mục chứa file HTML
input_folder = "truyen_copy_2"
DUOI_FILE = ".txt"

# Số lượng file mỗi thư mục
batch_size = 10


# Tạo thư mục đầu ra nếu chưa tồn tại
output_folder = "truyen_output"
os.makedirs(output_folder, exist_ok=True)

def read_html_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        # Trích xuất nội dung từ file HTML mà không có thẻ
        # print(file_path)
        text_content = soup.get_text(separator=' ', strip=False)
        return text_content

# Lấy danh sách các file trong thư mục
html_files = [f for f in os.listdir(input_folder) if f.endswith('.html')]
html_files = sorted(html_files, key=lambda x: int(os.path.basename(x).split('.')[0]))


current_batch = 1
current_batch_size = 0

for file_name in html_files:
    file_path = os.path.join(input_folder, file_name)
    text_content = read_html_content(file_path)

    # Tạo tên file output dựa trên tên file HTML
    output_file_name = os.path.splitext(file_name)[0] + ".txt"

    # Nếu đã đạt đến số lượng file cho mỗi thư mục, tạo thư mục mới
    if current_batch_size == batch_size:
        current_batch += 1
        current_batch_size = 0

    # Tạo tên thư mục dựa trên khoảng file
    folder_name = f"{current_batch * batch_size - batch_size + 1}_{current_batch * batch_size}"
    folder_path = os.path.join(output_folder, folder_name)
    os.makedirs(folder_path, exist_ok=True)

    output_file_path = os.path.join(folder_path, output_file_name)

    # Ghi nội dung đã được xử lý vào file
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(text_content)

    current_batch_size += 1
