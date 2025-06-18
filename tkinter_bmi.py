import tkinter as tk

# ฟังก์ชันคำนวณ BMI
def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100  # แปลงจาก cm เป็น m
        bmi = weight / (height ** 2)
        result_label.config(text=f"BMI ของคุณคือ: {bmi:.2f}")
    except ValueError:
        result_label.config(text="กรุณากรอกตัวเลขให้ถูกต้อง")

# สร้างหน้าต่าง
window = tk.Tk()
window.title("เครื่องคำนวณ BMI")
window.geometry("300x200")

# สร้าง Label และ Entry สำหรับน้ำหนัก
tk.Label(window, text="น้ำหนัก (kg):").pack()
weight_entry = tk.Entry(window)
weight_entry.pack()

# สร้าง Label และ Entry สำหรับส่วนสูง
tk.Label(window, text="ส่วนสูง (cm):").pack()
height_entry = tk.Entry(window)
height_entry.pack()

# ปุ่มคำนวณ
calculate_button = tk.Button(window, text="คำนวณ BMI", command=calculate_bmi)
calculate_button.pack(pady=20)

# แสดงผลลัพธ์
result_label = tk.Label(window, text="")
result_label.pack()

# เริ่มโปรแกรม
window.mainloop()
