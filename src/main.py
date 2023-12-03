# import cv2; 
# import pytesseract;

# image = cv2.imread('image.jpg');

# text = pytesseract.image_to_string(image);

# print(text);


# import io

from io import BytesIO

from typing import List
import cv2

import base64

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse

from fastapi.middleware.cors import CORSMiddleware  # Import the CORSMiddleware

from PIL import Image

import os

import time


app = FastAPI()

# Configure CORS
# Cho phép URL của angular sử dụng
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # Add your Angular app's origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Đặt đường dẫn đầy đủ đến thư mục chứa dữ liệu ngôn ngữ Tesseract
os.environ['TESSDATA_PREFIX'] = '../language'

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

def convert_bytes_to_human_readable(size_in_bytes):
    units = ['B', 'KB', 'MB', 'GB', 'TB']
    human_readable_sizes = []
    for unit in units:
        if size_in_bytes < 1024.0 or unit == units[-1]:
            human_readable_sizes.append(f"{size_in_bytes:.2f} {unit}")
        size_in_bytes /= 1024.0
    return human_readable_sizes

def process_base64_image(base64_str: str):
    try:

        print("bat dau xu ly")
        # Loại bỏ phần tiêu đề 'data:image/jpeg;base64,'
        base64_data = base64_str.split(',')[1]

        # Giải mã Base64 để nhận dữ liệu nhị phân
        binary_data = base64.b64decode(base64_data)

        # Chuyển dữ liệu nhị phân thành đối tượng hình ảnh
        image = Image.open(BytesIO(binary_data))

        # Thực hiện OCR để nhận văn bản từ hình ảnh
        text = pytesseract.image_to_string(image, lang='vie')

        print("ket thuc xu ly")

        return text
    except Exception as e:
        print(f"Error processing image: {str(e)}")
        return None

@app.get("/") # giống flask, khai báo phương thức get và url
async def root(): # do dùng ASGI nên ở đây thêm async, nếu bên thứ 3 không hỗ trợ thì bỏ async đi
    return {"message": "Hello World"}

@app.post("/process-images")
async def process_images(images: List[str]):
    try:
        processed_texts = []

        for base64_image in images:
            text = process_base64_image(base64_image)
            if text is not None:
                processed_texts.append(text)

        combined_text = "\n".join(processed_texts)

        return {"text": combined_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# @app.post("/image-to-text")
# async def image_to_text(files: List[UploadFile] = File(...)):
#     try:
#         result_texts = []

#         for file in files:
#             image = Image.open(BytesIO(await file.read()))
#             text = pytesseract.image_to_string(image, lang='vie')
#             result_texts.append(text)

#         # Combine or process the result_texts as needed
#         combined_text = "\n".join(result_texts)

#         # Save the combined text to a file
#         output_folder_path = '../output_folder'
#         os.makedirs(output_folder_path, exist_ok=True)
#         output_file_path = os.path.join(output_folder_path, 'output.txt')
#         with open(output_file_path, 'w', encoding='utf-8') as output_file:
#             output_file.write(combined_text)

#         # Get file size
#         file_size_bytes = os.path.getsize(output_file_path)
#         human_readable_sizes = convert_bytes_to_human_readable(file_size_bytes)

#         return {"text": combined_text, "file_size": human_readable_sizes[0]}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# Endpoint để tải xuống tệp tin .txt
@app.get("/download-text-file")
async def download_text_file():
    output_file_path = '../content/mushoku/2.txt'
    return FileResponse(output_file_path, filename='output.txt')




# # Tự động tạo thư mục nếu nó chưa tồn tại
# os.makedirs(OUTPUT_DIRECTORY, exist_ok=True)

# # pytesseract.pytesseract.tesseract_cmd = '/home/vscode/.local/lib/bib/tesseract'
# # pytesseract.pytesseract.tesseract_cmd = '/home/vscode/.local/lib/python3.9/site-packages/tesseract'
# # Preprocess the invoice image

# im = Image.open(PATH_FOLDER_IMG + "/mushoku/1" + DOT_FILE_PNG)

# # Bắt đầu đo thời gian
# start_time = time.time()


# text = pytesseract.image_to_string(im, lang='vie')

# # Kết thúc đo thời gian và tính toán thời gian đã trôi qua
# end_time = time.time()
# elapsed_time = end_time - start_time

# # Hiển thị nội dung và thời gian dịch
# print(f"Đã dịch thành công:\n{text}")
# print(f"Thời gian dịch: {elapsed_time} giây")

# # Ghi nội dung vào tệp tin .txt
# with open(OUTPUT_RESULT, 'w', encoding='utf-8') as file:
#     file.write(text)

# # Lấy kích thước của tệp tin
# file_size_bytes = os.path.getsize(OUTPUT_RESULT)

# # Chuyển đổi kích thước sang đơn vị thích hợp
# def convert_bytes_to_human_readable(size_in_bytes):
#     units = ['B', 'KB', 'MB', 'GB', 'TB']
#     human_readable_sizes = []
#     for unit in units:
#         if size_in_bytes < 1024.0 or unit == units[-1]:
#             human_readable_sizes.append(f"{size_in_bytes:.2f} {unit}")
#         size_in_bytes /= 1024.0
#     return human_readable_sizes

# # In ra thông báo thành công
# print(f"Dịch xong. Nội dung đã được lưu vào directory: {OUTPUT_RESULT}")
# # Chuyển đổi và hiển thị kích thước của tệp tin
# human_readable_sizes = convert_bytes_to_human_readable(file_size_bytes)
# print(f"Kích thước của tệp tin: \n{' || '.join(human_readable_sizes)}")

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




