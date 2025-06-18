import tkinter as tk

def submit():
    name = entry.get()
    label_result.config(text=f"Hello, {name}!")

# สร้างหน้าต่าง
window = tk.Tk()
window.title("แบบฟอร์มรับชื่อ")
window.geometry("300x200")

# เพิ่ม Label และ Entry
label = tk.Label(window, text="กรอกชื่อของคุณ:")
label.pack(pady=10)

entry = tk.Entry(window)
entry.pack()

# ปุ่ม Submit
button = tk.Button(window, text="ส่ง", command=submit)
button.pack(pady=5)

# แสดงผลลัพธ์
label_result = tk.Label(window, text="")
label_result.pack(pady=10)

window.mainloop()
