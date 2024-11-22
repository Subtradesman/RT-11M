from tkinter import*
import tkinter as tk
from matplotlib.figure import Figure
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
from math import pi, tan
from matplotlib import pyplot as pp
#import plotly.graph_objects as go

# Создаем окно Tkinter
root = tk.Tk()
root.title("Калькулятор диаграммы Смита")
root.geometry('800x600')
root.option_add("*tearOff", FALSE)

def zoom_in():
    ax.set_xlim(ax.get_xlim()[0] * 0.9, ax.get_xlim()[1] * 0.9)
    ax.set_ylim(ax.get_ylim()[0] * 0.9, ax.get_ylim()[1] * 0.9)
    canvas.draw()

def zoom_out():
    ax.set_xlim(ax.get_xlim()[0] * 1.1, ax.get_xlim()[1] * 1.1)
    ax.set_ylim(ax.get_ylim()[0] * 1.1, ax.get_ylim()[1] * 1.1)
    canvas.draw()

def reset():
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    canvas.draw()



def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Текстовые файлы", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_area.get("1.0", tk.END))


def close_window():
    window.destroy()

def create_new_file():
    # Открываем диалоговое окно для выбора директории
    directory = filedialog.askdirectory()
    
    # Если директория выбрана, создаем новый файл
    if directory:
        # Запрашиваем имя файла у пользователя
        file_name = input("Введите имя файла: ")
        
        # Создаем новый файл
        with open(f"{directory}/{file_name}.py", "w") as file:
            file.write("")
        
        print(f"Файл {file_name}.py создан в директории {directory}")


def open_file():
    # Открываем диалоговое окно для выбора файла
    file_path = filedialog.askopenfilename()
    
    # Если файл выбран, открываем его
    if file_path:
        # Открываем файл в режиме чтения
        import os; 
        os.startfile(file_path)
           
main_menu = Menu()
 
file_menu = Menu()
file_menu.add_command(label="Создать файл",  command = create_new_file)
file_menu.add_command(label="Открыть файл", command = open_file)
file_menu.add_command(label="Сохранить как", command = save_file)
file_menu.add_separator()
file_menu.add_command(label="Выход", command = close_window)
 
main_menu.add_cascade(label="Файл", menu=file_menu)
main_menu.add_cascade(label="Настройки")
main_menu.add_cascade(label="Вид")
 
root.config(menu=main_menu)


button_frame = tk.Frame(master=root)
button_frame.pack(side=tk.BOTTOM)

zoom_in_button = tk.Button(master=button_frame, text="Увеличить", command=zoom_in)
zoom_in_button.pack(side=tk.LEFT)

zoom_out_button = tk.Button(master=button_frame, text="Уменьшить", command=zoom_out)
zoom_out_button.pack(side=tk.LEFT)

reset_button = tk.Button(master=button_frame, text="Сбросить", command=reset)
reset_button.pack(side=tk.LEFT)


frequencies = np.linspace(1, 100, 100)  # частоты
impedances = np.random.rand(len(frequencies)) + 1j * np.random.rand(len(frequencies))  # комплексные импедансы

# Расчет реальных и мнимых частей импедансов
real_parts = np.real(impedances)
imaginary_parts = np.imag(impedances)

# Создаем график Matplotlib
# Построение диаграммы Смита
figu = Figure(figsize=(8, 8))
ax = figu.add_subplot (111)
ax.plot(real_parts, imaginary_parts, 'o-')
ax.set_xlabel('Действительная часть')
ax.set_ylabel('Мнимая часть')
ax.set_title('Круговая Диаграмма Смита')
ax.grid(True)
ax.set_aspect('equal', adjustable='box')


 #Создаем canvas для отображения графика
canvas = FigureCanvasTkAgg(figu, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Запускаем главный цикл Tkinter
root.mainloop()