import customtkinter as ctk
from tkinter import ttk
app=ctk.CTk()
app.geometry("600x400")
app.title("Quan ly sinh vien")
label=ctk.CTkLabel(app,text="He thong quan ly sinh vien",font=ctk.CTkFont(size=20,weight="bold"))
label.pack(pady=20)
msv=ctk.CTkEntry(app,placeholder_text="Nhap ma sinh vien")
msv.pack(pady=10)
ten=ctk.CTkEntry(app,placeholder_text="Nhap ten sinh vien")
ten.pack(pady=10)
lop=ctk.CTkEntry(app,placeholder_text="Nhap lop sinh vien")
lop.pack(pady=10)
diem=ctk.CTkEntry(app,placeholder_text="Nhap diem sinh vien")
diem.pack(pady=10)
result=ctk.CTkLabel(app,text="",font=ctk.CTkFont(size=16))
result.pack(pady=10)
students=[]
app2=ctk.CTkToplevel(app)
app2.geometry("600x400")
app2.title("Danh sach sinh vien")
tree =ttk.Treeview(
    app2,columns=("msv","ten","lop","diem"),
    show="headings",
    height=10
)
tree.heading("msv",text="msv")
tree.heading("ten",text="ten")
tree.heading("lop",text="lop")
tree.heading("diem",text="diem")
tree.pack(pady=20, fill="both", expand=True)
def add_sv():
    student={
        "msv":msv.get(),
        "ten":ten.get(),
        "lop":lop.get(),
        "diem":diem.get()
    }
    students.append(student)
    tree.insert(
        "",
        "end",
        values=(
            student["msv"],
            student["ten"],
            student["lop"],
            student["diem"]
        )
    )
    result.configure(text=f"Da them sinh vien: {student['ten']}")
    print(students)
    msv.delete(0,ctk.END)
    ten.delete(0,ctk.END)
    lop.delete(0,ctk.END)
    diem.delete(0,ctk.END)
button=ctk.CTkButton(app,text="Them sinh vien",command=add_sv)
button.pack(pady=10)

app.mainloop()