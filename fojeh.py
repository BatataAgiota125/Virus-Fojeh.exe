import os
import subprocess
import ctypes
import time
import cv2
import tkinter as tk
from tkinter import messagebox

usuario = os.getlogin()

root = tk.Tk()
root.withdraw()
root.iconbitmap("icone.ico")
root.attributes("-topmost", True)

# Saudação inicial
messagebox.showinfo("VIRUS", f"OLA {usuario} TUDO BEM???")

# Permissão de acesso à câmera
pode_ver = messagebox.askyesno("VIRUS", "EU POSSO TE VER???")

if pode_ver:
    video = cv2.VideoCapture(0)
    if not video.isOpened():
        messagebox.showinfo("VIRUS", "NÃO ENCONTREI SUA CÂMERA")
    else:
        messagebox.showinfo("VIRUS", "OBRIGADO PELA IMAGEM")
        while True:
            ok, frame = video.read()
            if not ok:
                break
            cv2.imshow("Camera", frame)
            if cv2.getWindowProperty("Camera", cv2.WND_PROP_VISIBLE) < 1:
                break
        video.release()
        cv2.destroyAllWindows()
else:
    messagebox.showinfo("VIRUS", "VOCÊ ME IRRITOU >:(")
    time.sleep(1)
    messagebox.showinfo("VIRUS", "ACESSANDO ARQUIVOS DO SISTEMA...")
    time.sleep(2)
    messagebox.showinfo("VIRUS", "INICIANDO FORMATAÇÃO EM 3...")
    time.sleep(1)
    messagebox.showinfo("VIRUS", "2...")
    time.sleep(1)
    messagebox.showinfo("VIRUS", "1...")
    time.sleep(1)
    root.iconbitmap("Windows-11-Icon.ico")
    messagebox.showerror(
        "Windows", "fojeh.exe Não tem permissão de administrador")
root.iconbitmap("icone.ico")
messagebox.showinfo("VIRUS", "MAS AGORA A DIVERSÃO COMEÇA HAHAHA")
messagebox.askyesno("VIRUS", "ESTA PREPARADO???")
messagebox.showinfo("¨V!&RO$§", "*P)OR@U# NÁ¨ ¹MPORTA OQUE VOCÊ E§$SC'LHEU")
subprocess.Popen(["python", "virus.py"])
messagebox.showinfo("DIGA ADEUS", "DIGA ADEUS AO SEU COMPUTADOR HAHAHA")
