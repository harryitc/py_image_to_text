## Python V3.9.2
##### Tesseract and OpenCV
1. pip install pytesseract pip install opencv-python
`Run code: python root.py`

xy ra loi: 
`
Traceback (most recent call last):
  File "/workspaces/my_python/root.py", line 11, in <module>
    import cv2
  File "/home/vscode/.local/lib/python3.9/site-packages/cv2/__init__.py", line 181, in <module>
    bootstrap()
  File "/home/vscode/.local/lib/python3.9/site-packages/cv2/__init__.py", line 153, in bootstrap
    native_module = importlib.import_module("cv2")
  File "/usr/lib/python3.9/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
ImportError: libGL.so.1: cannot open shared object file: No such file or directory
`
```python
sudo apt-get update
sudo apt-get install ffmpeg libsm6 libxext6  -y
```

tesseract-ocr-dev se khong tim thay. Do do, phai bo no di.
sudo apt-get install libleptonica-dev tesseract-ocr tesseract-ocr-dev libtesseract-dev python3-pil tesseract-ocr-eng tesseract-ocr-script-latn


Loi: khong tim thay tessecract


cai ngon ngu
o day toi cau hinh la: /path/to/tessdata = language
wget https://github.com/tesseract-ocr/tessdata/raw/main/vie.traineddata -P /path/to/tessdata


#### Server
pip install fastapi uvicorn

run file
uvicorn main:app --reload

khi run se gap loi 
Error: loading ASGI app. Could not import module "main".

Nghĩa là không đúng cấu trúc thư mục.
[Tham khảo](https://stackoverflow.com/a/62934660)

sau khi run lại, cũng gặp lỗi.

chạy lệnh:
pip install python-multipart

ok chạy được rồi
```python
INFO:     Will watch for changes in these directories: ['/workspaces/my_python/src']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [3656] using StatReload
INFO:     Started server process [3662]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

Khi gọi api từ angular. Chúng ta sẽ gặp lỗi CQRS. Do đó, dùng middleware.






1. autoclick hinh anh save ve

2. di chuyen casc hinh anh vao 1 thu muc img/... nao do

3. chinh lai cac duong dan trong test.py

4. chinh lai {id value} o trong constant.ts tuong ung voi id: so chuong, value: ten chuong

5. LUU Y QUAN TRONG: kiem tra cac file html. Thường thì nó nằm ở dòng đầu tiên trong phần content của HTML. 
  5.1 Nếu là tên gì đó chả có trong nội dung chương thì BỎ. 
  5.2 Nếu tên chương xuất hiện trong nội dung thì BỎ. Vì đã có header rồi.

6. Chạy file doitenfile.py để đổi tên theo thứ tự

<!-- 6.1. TEST: Chayj file gen_output.py để đổi generate ra các folder -->

7. Chạy file html_to_text.py ~~~ DONE.