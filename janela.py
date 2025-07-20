import tkinter as tk
import random
import threading
import keyboard

root = tk.Tk()
root.withdraw()  # Oculta a janela principal

janelas = []

def criar_janela():
    win = tk.Toplevel()
    win.title("IDIOTA IDIOTA IDIOTA")
    win.geometry("300x100")

    # Tamanho da tela
    largura_tela = root.winfo_screenwidth()
    altura_tela = root.winfo_screenheight()

    # Posição aleatória
    x = random.randint(0, largura_tela - 300)
    y = random.randint(0, altura_tela - 100)

    win.geometry(f"300x100+{x}+{y}")

    # Texto com fonte maior
    tk.Label(win, text="IDIOTA IDIOTA IDIOTA", font=("Arial", 16, "bold")).pack(expand=True)

    janelas.append(win)

def fechar_todas():
    for janela in janelas:
        janela.destroy()

# Cria 50 janelas com intervalo
for i in range(50):
    root.after(i * 300, criar_janela)

# Fecha todas após 4000ms
root.after(4000, fechar_todas)
root.after(8000, fechar_todas)

def esc_global():
    keyboard.wait('esc')
    root.destroy()        # fecha a janela principal


threading.Thread(target=esc_global, daemon=True).start()

root.mainloop()