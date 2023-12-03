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
![Alt text](image-1.png)



