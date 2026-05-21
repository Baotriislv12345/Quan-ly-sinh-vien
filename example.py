import customtkinter as ctk
from tkinter import ttk

# Cấu hình theme cho đồng bộ
ctk.set_appearance_mode("System")  # Hoặc "Dark", "Light"
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("900 x 450")  # Nới rộng chiều ngang để chứa cả form và bảng
app.title("Quản lý sinh viên")

# --- STYLE CHO TREEVIEW (Fix lỗi lệch tông màu) ---
style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview", 
                background="#2a2d2e", 
                foreground="white", 
                fieldbackground="#2a2d2e", 
                rowheight=25)
style.map("Treeview", background=[("selected", "#1f538d")])
style.configure("Treeview.Heading", background="#1f6aa5", foreground="white", relief="flat")

students = []

def add_sv():
    # Validate cơ bản
    if not msv.get() or not ten.get():
        result.configure(text="Lỗi: Mã SV và Tên không được để trống!", text_color="red")
        return
    
    student = {
        "msv": msv.get(),
        "ten": ten.get(),
        "lop": lop.get(),
        "diem": diem.get()
    }
    students.append(student)
    
    # Thêm vào bảng
    tree.insert("", "end", values=(student["msv"], student["ten"], student["lop"], student["diem"]))
    
    # Thông báo thành công
    result.configure(text=f"Đã thêm: {student['ten']}", text_color="green")
    
    # Xóa dữ liệu cũ ở ô nhập
    msv.delete(0, ctk.END)
    ten.delete(0, ctk.END)
    lop.delete(0, ctk.END)
    diem.delete(0, ctk.END)

# --- BỐ CỤC GIAO DIỆN (Layout) ---
# Chia làm 2 khu vực chính: Left Frame (Nhập liệu) và Right Frame (Hiển thị)
left_frame = ctk.CTkFrame(app, width=250, corner_radius=10)
left_frame.pack(side="left", fill="y", padx=15, pady=15)

right_frame = ctk.CTkFrame(app, corner_radius=10)
right_frame.pack(side="right", fill="both", expand=True, padx=15, pady=15)

# --- KHU VỰC NHẬP LIỆU (Left) ---
label = ctk.CTkLabel(left_frame, text="HỆ THỐNG QUẢN LÝ", font=ctk.CTkFont(size=16, weight="bold"))
label.pack(pady=15)

msv = ctk.CTkEntry(left_frame, placeholder_text="Nhập mã sinh viên", width=200)
msv.pack(pady=8)

ten = ctk.CTkEntry(left_frame, placeholder_text="Nhập tên sinh viên", width=200)
ten.pack(pady=8)

lop = ctk.CTkEntry(left_frame, placeholder_text="Nhập lớp sinh viên", width=200)
lop.pack(pady=8)

diem = ctk.CTkEntry(left_frame, placeholder_text="Nhập điểm sinh viên", width=200)
diem.pack(pady=8)

button = ctk.CTkButton(left_frame, text="Thêm sinh viên", command=add_sv, font=ctk.CTkFont(weight="bold"))
button.pack(pady=15)

result = ctk.CTkLabel(left_frame, text="", font=ctk.CTkFont(size=13))
result.pack(pady=5)

# --- KHU VỰC BẢNG (Right) ---
table_title = ctk.CTkLabel(right_frame, text="Danh Sách Sinh Viên", font=ctk.CTkFont(size=16, weight="bold"))
table_title.pack(pady=10)

tree = ttk.Treeview(right_frame, columns=("msv", "ten", "lop", "diem"), show="headings")
tree.heading("msv", text="Mã SV")
tree.heading("ten", text="Họ Tên")
tree.heading("lop", text="Lớp")
tree.heading("diem", text="Điểm")

# Chỉnh độ rộng các cột cho đẹp
tree.column("msv", width=80, anchor="center")
tree.column("ten", width=150, anchor="w")
tree.column("lop", width=80, anchor="center")
tree.column("diem", width=60, anchor="center")

tree.pack(pady=10, padx=10, fill="both", expand=True)

app.mainloop()