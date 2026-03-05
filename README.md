# 📌 PHÂN VÙNG ẢNH THEO MIỀN ĐỒNG NHẤT

Hệ thống phân vùng ảnh sử dụng **Split (Quadtree) và Merge** trong xử lý ảnh.

---

# 1️⃣ Giới thiệu

Dự án thực hiện phân vùng ảnh bằng phương pháp **Split and Merge**.

Chương trình gồm:

- **Main Program:** `BaiTapLon.py` (thực hiện đọc ảnh và phân vùng ảnh)
- **Input Image:** `anh_lena.jpg` (ảnh đầu vào)
- **Result Image:**  
  - `split.jpg` (kết quả sau khi phân vùng bằng Split)  
  - `merge.jpg` (kết quả sau khi Merge các vùng)

Quy trình hoạt động:


---

# 2️⃣ Yêu cầu hệ thống

Chương trình được phát triển và chạy trên môi trường:

- **Operating System:** Windows 10 / Windows 11  
- **Programming Language:** Python 3.8 trở lên  
- **IDE:** Visual Studio  

---

# 3️⃣ Thư viện sử dụng

Dự án sử dụng các thư viện Python sau:

### OpenCV (cv2)
- Dùng để đọc ảnh
- Hiển thị ảnh
- Lưu ảnh kết quả

### NumPy
- Xử lý ma trận ảnh
- Thực hiện các phép tính thống kê trên dữ liệu ảnh

---

# 4️⃣ Cài đặt thư viện

Cài đặt các thư viện cần thiết bằng lệnh:

```bash
pip install opencv-python
pip install numpy

project/
│
├── BaiTapLon.py        # Chương trình chính
├── anh_lena.jpg        # Ảnh đầu vào
├── split.jpg           # Kết quả sau Split
├── merge.jpg           # Kết quả sau Merge
└── README.md


