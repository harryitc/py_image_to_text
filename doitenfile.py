import glob
import os

folder_path = "truyen_copy_2"

file_list = glob.glob(os.path.join(folder_path, '*.html'))

# Sắp xếp theo thứ tự số trong tên file
def get_number_from_filename(file_name):
    # Trích xuất số từ tên file, ví dụ: 'file1.txt' -> 1
    return int(''.join(filter(str.isdigit, os.path.basename(file_name))))

file_list_sorted = sorted(file_list, key=get_number_from_filename)

# Duyệt qua file_list_sorted và đổi tên các file
for index, old_file_path in enumerate(file_list_sorted, start=1):
    _, file_extension = os.path.splitext(old_file_path)
    new_file_name = f"{index}{file_extension}"
    new_file_path = os.path.join(folder_path, new_file_name)
    os.rename(old_file_path, new_file_path)

print("Đã đổi tên các file thành công.")
