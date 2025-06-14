import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import qrcode

def generate_qr():
    data = entry.get()
    if not data:
        messagebox.showwarning("Warning", "Please enter a link or text.")
        return

    global qr_image


    qr = qrcode.QRCode(
        version=1,
        box_size=5,   
        border=2
    )
    qr.add_data(data)
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color="black", back_color="white").convert("RGB")


    qr_resized = qr_image.resize((200, 200)) 
    qr_tk = ImageTk.PhotoImage(qr_resized)
    qr_label.config(image=qr_tk)
    qr_label.image = qr_tk

def save_qr():
    if qr_image is None:
        messagebox.showinfo("Info", "First generate a QR Code.")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
    if file_path:
        qr_image.save(file_path)
        messagebox.showinfo("Saved", "QR Code saved successfully.")
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x450")
root.resizable(False, False)

title = tk.Label(root, text="Enter link or text below", font=("Arial", 14))
title.pack(pady=10)

entry = tk.Entry(root, width=40, font=("Arial", 12))
entry.pack(pady=10)

gen_button = tk.Button(root, text="Generate QR Code", font=("Arial", 12), command=generate_qr)
gen_button.pack(pady=10)

qr_label = tk.Label(root)
qr_label.pack(pady=10)

save_button = tk.Button(root, text="Save QR Code", font=("Arial", 12), command=save_qr)
save_button.pack(pady=10)

qr_image = None

root.mainloop()
