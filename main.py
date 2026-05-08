import customtkinter as ctk
from tkinter import ttk
app=ctk.CTk()
app.geometry("800x500")
app.title("Quản lý sinh viên")
label=ctk.CTkLabel(app,text="Hệ thống quản lý sinh viên",font=("Arial",20,"bold"))
label.pack(pady=20)
msv=ctk.CTkEntry(app,placeholder_text="mã sinh viên",width=200)
msv.pack(pady=10)
ten=ctk.CTkEntry(app,placeholder_text="tên sinh viên",width=200)
ten.pack(pady=10)
lop=ctk.CTkEntry(app,placeholder_text="lớp",width=200)
lop.pack(pady=10)
diem=ctk.CTkEntry(app,placeholder_text="điểm",width=200)
diem.pack(pady=10)
result=ctk.CTkLabel(app,text="")
result.pack(pady=10)
students = []
def add_student():

    student = {
        "id": msv.get(),
        "name": ten.get(),
        "class": lop.get(),
        "score": diem.get()
    }

    students.append(student)
    tree.insert(
    "",
    "end",
    values=(
        student["id"],
        student["name"],
        student["class"],
        student["score"]
    )
)

    result.configure(
        text=f"\nĐã thêm:\n{student['id']} - {student['name']}"
    )
    
    print(students)
    msv.delete(0, "end")
    ten.delete(0, "end")
    lop.delete(0, "end")
    diem.delete(0, "end")
add_button=ctk.CTkButton(app,text="Thêm sinh viên",command=add_student)
add_button.pack(pady=20)
# tạo bảng
tree = ttk.Treeview(
    app,
    columns=("MSSV", "Tên", "Lớp", "Điểm"),
    show="headings",
    height=8
)

# tạo tiêu đề cột
tree.heading("MSSV", text="MSSV")
tree.heading("Tên", text="Họ tên")
tree.heading("Lớp", text="Lớp")
tree.heading("Điểm", text="Điểm")

# chỉnh độ rộng cột
tree.column("MSSV", width=100)
tree.column("Tên", width=200)
tree.column("Lớp", width=100)
tree.column("Điểm", width=100)

tree.pack(pady=20)
app.mainloop()