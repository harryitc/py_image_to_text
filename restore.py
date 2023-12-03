# import cv2; 
# import pytesseract;

# image = cv2.imread('image.jpg');

# text = pytesseract.image_to_string(image);

# print(text);


import cv2

from PIL import Image

import os

import time


# Đặt đường dẫn đầy đủ đến thư mục chứa dữ liệu ngôn ngữ Tesseract
os.environ['TESSDATA_PREFIX'] = 'language'

import pytesseract

DOT_FILE_JPG = ".jpg"
DOT_FILE_PNG = ".png"

PATH_FOLDER_IMG = "img" 
PATH_FOLDER_CONTENT = "content" 


OPEN_IMAGE = PATH_FOLDER_IMG + "/mushoku/1" + DOT_FILE_PNG

# Đặt đường dẫn đến tệp tin .txt
OUTPUT_DIRECTORY = PATH_FOLDER_CONTENT + "/mushoku"
OUTPUT_FILE_IN_DIRECTORY = "2.txt"
OUTPUT_RESULT = os.path.join(OUTPUT_DIRECTORY, OUTPUT_FILE_IN_DIRECTORY)


# Tự động tạo thư mục nếu nó chưa tồn tại
os.makedirs(OUTPUT_DIRECTORY, exist_ok=True)

# pytesseract.pytesseract.tesseract_cmd = '/home/vscode/.local/lib/bib/tesseract'
# pytesseract.pytesseract.tesseract_cmd = '/home/vscode/.local/lib/python3.9/site-packages/tesseract'
# Preprocess the invoice image

im = Image.open(PATH_FOLDER_IMG + "/mushoku/1" + DOT_FILE_PNG)

# Bắt đầu đo thời gian
start_time = time.time()


text = pytesseract.image_to_string(im, lang='vie')

# Kết thúc đo thời gian và tính toán thời gian đã trôi qua
end_time = time.time()
elapsed_time = end_time - start_time

# Hiển thị nội dung và thời gian dịch
print(f"Đã dịch thành công:\n{text}")
print(f"Thời gian dịch: {elapsed_time} giây")

# Ghi nội dung vào tệp tin .txt
with open(OUTPUT_RESULT, 'w', encoding='utf-8') as file:
    file.write(text)

# Lấy kích thước của tệp tin
file_size_bytes = os.path.getsize(OUTPUT_RESULT)

# Chuyển đổi kích thước sang đơn vị thích hợp
def convert_bytes_to_human_readable(size_in_bytes):
    units = ['B', 'KB', 'MB', 'GB', 'TB']
    human_readable_sizes = []
    for unit in units:
        if size_in_bytes < 1024.0 or unit == units[-1]:
            human_readable_sizes.append(f"{size_in_bytes:.2f} {unit}")
        size_in_bytes /= 1024.0
    return human_readable_sizes

# In ra thông báo thành công
print(f"Dịch xong. Nội dung đã được lưu vào directory: {OUTPUT_RESULT}")
# Chuyển đổi và hiển thị kích thước của tệp tin
human_readable_sizes = convert_bytes_to_human_readable(file_size_bytes)
print(f"Kích thước của tệp tin: \n{' || '.join(human_readable_sizes)}")

# image = cv2.imread(PATH_FOLDER + "/mushoku/1" + DOT_FILE_PNG)

# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

# median = cv2.medianBlur(thresh, 3)

# # Extract the text from the invoice image

# text = pytesseract.image_to_string(median, lang='vie')

# print(text)

# Parse the text to extract the invoice data

# vendor_name = extract_vendor_name(text)

# invoice_number = extract_invoice_number(text)

# date = extract_date(text)

# amount_due = extract_amount_due(text)

# Store the extracted data in a database or other storage system

# store_invoice_data(vendor_name, invoice_number, date, amount_due)




