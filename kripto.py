# main.py

import tkinter as tk
from tkinter import messagebox
from vigenere import vigenere_encrypt, vigenere_decrypt
from affine import affine_encrypt, affine_decrypt
from aes_custom import aes_encrypt, aes_decrypt

def process_text():
    text = input_text.get("1.0", tk.END).strip()
    key = key_entry.get().strip()
    algo = algo_var.get()
    mode = mode_var.get()

    if not text or not key:
        messagebox.showerror("Error", "Teks dan kunci harus diisi.")
        return

    try:
        if algo == "Vigenère":
            result = vigenere_encrypt(text, key) if mode == "Encrypt" else vigenere_decrypt(text, key)
        elif algo == "Affine":
            a, b = map(int, key.split(","))
            result = affine_encrypt(text, a, b) if mode == "Encrypt" else affine_decrypt(text, a, b)
        elif algo == "AES":
            result = aes_encrypt(text, key) if mode == "Encrypt" else aes_decrypt(text, key)
        else:
            result = "Algoritma tidak dikenali."
    except Exception as e:
        result = f"Terjadi kesalahan: {e}"

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)

# GUI setup
root = tk.Tk()
root.title("Aplikasi Kriptografi")
root.geometry("500x500")
root.configure(bg='#696969')

algo_var = tk.StringVar(value="Vigenère")
mode_var = tk.StringVar(value="Encrypt")

# Input Text
tk.Label(root, bg='#A9A9A9',borderwidth=2, relief="groove",text="Masukkan Teks:").pack()
input_text = tk.Text(root, bg='#D3D3D3',height=4, width=50, borderwidth=2, relief="raised")
input_text.pack()

# Key Input
tk.Label(root, bg='#A9A9A9', borderwidth=2, relief="groove",text="Masukkan Kunci:").pack()
key_entry = tk.Entry(root, bg='#D3D3D3',width=50, borderwidth=2, relief="raised")
key_entry.pack()

# Algorithm Selection
tk.Label(root, bg='#A9A9A9', borderwidth=2, relief="groove", text="Pilih Algoritma:").pack()
tk.OptionMenu(root, algo_var, "Vigenère", "Affine", "AES").pack()

# Mode Selection
tk.Label(root, bg='#A9A9A9',borderwidth=2, relief="groove",text="Mode:").pack()
tk.Radiobutton(root, bg='#A9A9A9',borderwidth=2, relief="raised",text="Enkripsi", variable=mode_var, value="Encrypt").pack()
tk.Radiobutton(root, bg='#A9A9A9',borderwidth=2, relief="raised",text="Dekripsi", variable=mode_var, value="Decrypt").pack()

# Process Button
tk.Button(root, bg='#A9A9A9',borderwidth=2, relief="raised",text="Proses", command=process_text).pack(pady=10)

# Output Text
tk.Label(root, bg='#A9A9A9',borderwidth=2, relief="groove",text="Hasil:").pack()
output_text = tk.Text(root, bg='#D3D3D3',height=4, width=50,borderwidth=2, relief="raised")
output_text.pack()

# Run GUI
root.mainloop()
