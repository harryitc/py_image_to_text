# from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
import os
import re

# Đường dẫn tới file const.ts
file_const_path = "const.ts"

# Mở file và đọc nội dung
with open(file_const_path, 'r', encoding='utf-8') as file:
    ts_content = file.read()

# Thay thế dấu nháy đơn bằng dấu nháy kép trong chuỗi JSON
# ts_content_fixed = re.sub(r"'", '"', ts_content)

# Sử dụng biểu thức chính quy để trích xuất mảng JSON từ nội dung TypeScript
match = re.search(r'\[.*?\]', ts_content, re.DOTALL)


if match:
    # Lấy chuỗi JSON từ biểu thức chính quy
    json_array_str = match.group(0)

    # Chuyển chuỗi JSON thành mảng Python
    import json
    ts_array = json.loads(json_array_str)

    # In mảng Python
    # print(ts_array)
else:
    print("Không tìm thấy mảng JSON trong file.")


# --------------------------------- ID ANCHOR HTML --------------------------
HEADER_ID = "reader-title"
CONTENT_ID = "readability-page-1"

# boi so 
MAX_FILE_IN_FOLDER = 5

# Đường dẫn thư mục chứa các file HTML
FOLDER_PATH_INPUT = "truyen"

# FOLDER_PATH_OUTPUT_MERGE = "truyen_format/merge/" + str(ts_array[0]["id"]) + '_' + str(ts_array[-1]["id"])
result_content_merge = ""

# FOLDER_PATH_OUTPUT_SEPRATE = "truyen_format/seprate/" + str(ts_array[0]["id"]) + '_' + str(ts_array[-1]["id"])

FOLDER_PATH_OUTPUT_RESULT = "output_html_to_text"

SUBFOLDER_PATH_OUTPUT_REULST_MERGE = FOLDER_PATH_OUTPUT_RESULT + "/merge"

FILE_NAME_PATH_OUTPUT = ".txt"


# Tự động tạo thư mục nếu nó chưa tồn tại
# os.makedirs(FOLDER_PATH_OUTPUT_MERGE, exist_ok=True)
# os.makedirs(FOLDER_PATH_OUTPUT_SEPRATE, exist_ok=True)
os.makedirs(FOLDER_PATH_OUTPUT_RESULT, exist_ok=True)
os.makedirs(SUBFOLDER_PATH_OUTPUT_REULST_MERGE, exist_ok=True)

def extract_content_from_html(file_path, element_id):
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    # Tìm đối tượng có ID tương ứng
    target_element = soup.find(id=element_id)
    
    # Kiểm tra xem đối tượng có tồn tại không
    if target_element:

        # Lấy nội dung văn bản từ đối tượng
        # Param: separator sẽ thêm một khoảng trắng giữa các phần văn bản khác nhau
        # Param: skip = true sẽ loại bỏ các khoảng trắng không cần thiết từ đầu và cuối chuỗi.
        text_content = target_element.get_text(separator=' ', strip=False)

        # if(element_id != HEADER_ID):
        #     text_content = te
        return text_content
    else:
        return f"No element with ID '{element_id}' found."

    # Lấy nội dung từ mỗi thẻ p, div, br, vv.
    # extracted_content = []
    # for tag in soup.find_all(['p', 'div', 'br', 'span']):
    #     tag_content = ''.join(str(child) for child in tag.contents if child.name is None)
    #     extracted_content.append(tag_content)

    # # Kết hợp nội dung lại với định dạng cấu trúc gốc
    # formatted_content = ' '.join(extracted_content)

    # return formatted_content


# Lấy danh sách các file trong thư mục
# file_list = [f for f in os.listdir(FOLDER_PATH_INPUT) if f.endswith('.html')]
file_list = [f for f in os.listdir(FOLDER_PATH_INPUT) if f.endswith('.html')]
file_list = sorted(file_list, key=lambda x: int(os.path.basename(x).split('.')[0]))

#Bug: Sort danh sách file. Vì lấy ra tự nhiên nó bị đảo

current_batch = 1
current_batch_size = 0

# Lặp qua từng file và lấy nội dung
for file_name in file_list:
    file_input_path = os.path.join(FOLDER_PATH_INPUT, file_name)
    
    header = extract_content_from_html(file_input_path, HEADER_ID)
    
    content = extract_content_from_html(file_input_path, CONTENT_ID)
    # Sử dụng replace để thay thế chuỗi cần xóa bằng chuỗi rỗng
    content = content.replace("Chương: Kingofbattle.", "")
    # Sử dụng biểu thức chính quy để tìm kiếm chữ "Chương" và số
    match = re.search(r'Chương (\d+)', header)

    if match:
        # Lấy kết quả từ nhóm bắt (capturing group) trong biểu thức chính quy
        chuong_text = match.group(0)
        chuong_number = match.group(1)

        # print(chuong_text)
        # print("Số:", chuong_number)
    else:
        print("Không tìm thấy chương và số trong chuỗi.")


    result = "Chương: " + chuong_number + "\n"

    # Lặp qua danh sách để kiểm tra từng phần tử
    for item in ts_array:
        # Kiểm tra nếu id và value của phần tử bằng nhau
        if (int(item["id"]) == int(chuong_number)):
            result = result + item["value"]
            break
        # else:
        #     print(f"Đã có lỗi xảy ra khi so sánh CHƯƠNG và danh sách ID tại item = {item} này!")

    # in ra 3 dòng chấm
    result += '\n.' * 3
    
    # đề phòng
    result += "\n"

    # cuoi cung la add content vao
    # result = content
    result = result + content + "\n" 

    # Tạo tên file output dựa trên tên file HTML
    # output_file_name = os.path.splitext(file_name)[0] + FILE_NAME_PATH_OUTPUT
    # output_file_name = chuong_number + FILE_NAME_PATH_OUTPUT
    # output_file_name = os.path.splitext(file_name)[0] + "_output.txt"

    # output_file_path_seprate = os.path.join(FOLDER_PATH_OUTPUT_SEPRATE, output_file_name)

    # Ghi nội dung đã được xử lý vào file được tổng hợp
    result_content_merge = result_content_merge + result + "\n"

    # Ghi nội dung đã được trích xuất vào file
    # with open(output_file_path_seprate, 'w', encoding='utf-8') as output_file:
    #     output_file.write(result)

    # file_path = os.path.join(input_folder, file_name)
    # text_content = read_html_content(file_path)

    # Tạo tên file output dựa trên tên file HTML
    output_file_name = os.path.splitext(file_name)[0] + ".txt"

    # Nếu đã đạt đến số lượng file cho mỗi thư mục, tạo thư mục mới
    if current_batch_size == MAX_FILE_IN_FOLDER:
        current_batch += 1
        current_batch_size = 0

    # Tạo tên thư mục dựa trên khoảng file
    folder_name = f"{current_batch * MAX_FILE_IN_FOLDER - MAX_FILE_IN_FOLDER + 1}_{current_batch * MAX_FILE_IN_FOLDER}"
    folder_path = os.path.join(FOLDER_PATH_OUTPUT_RESULT, folder_name)
    os.makedirs(folder_path, exist_ok=True)

    output_file_path = os.path.join(folder_path, output_file_name)

    # Ghi nội dung đã được xử lý vào file
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(result)

    current_batch_size += 1




print("---------------------- START FILE MERGE ----------------")
# Ghi nội dung đã được trích xuất vào file
output_file_path_merge = os.path.join(
    SUBFOLDER_PATH_OUTPUT_REULST_MERGE,
    str(ts_array[0]["id"]) 
    + '_' + 
    str(ts_array[-1]["id"]) + 
    FILE_NAME_PATH_OUTPUT
    )
with open(output_file_path_merge , 'w', encoding='utf-8') as output_file:
        output_file.write(result_content_merge)
# print(f"Content from {file_name} has been saved to {output_file_path_merge}")