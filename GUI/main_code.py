from tkinter import*
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import filedialog
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, TextBox
from skrf.plotting import smith
from PIL import Image

# окно Tkinter
root = tk.Tk()
root.title("Калькулятор диаграммы Смита")
root.geometry('1200x720')
root.option_add("*tearOff", FALSE)

# параметры
frequencies = np.linspace(1e6, 1e9, 500)  # частоты от 1 МГц до 1 ГГц
z0 = 50  # номинальный импеданс
inductance = 0e-9  # начальная индуктивность (гн)
capacitance = 0e-12  # начальная ёмкость (ф)

# функция для вычисления импедансов
def calculateImpedance(inductance, capacitance, frequencies):
    omega = 2 * np.pi * frequencies
    zL = 1j * omega * inductance  # индуктивное сопротивление
    zC = 1 / (1j * omega * capacitance)  # ёмкостное сопротивление
    return zL + zC

# обновление диаграммы Смита
def updateSmithChart(ax, inductance, capacitance, frequencies, z0):
    ax.clear()  # очистить ось
    smith(ax=ax)  # нарисовать диаграмму Смита
    impedances = calculateImpedance(inductance, capacitance, frequencies)
    gamma = (impedances - z0) / (impedances + z0)  # коэффициенты отражения
    ax.plot(gamma.real, gamma.imag, color='red',
            label=f"L = {inductance * 1e9:.2f} nH, C = {capacitance * 1e12:.2f} pF")
    ax.legend()
    ax.set_title("Диаграмма Смита", fontsize=16)

# добавление шкалы сопротивлений
    resistances = [0, 10, 25, 50, 100, 200, 500]
    for r in resistances:
        normalized_r = (r - z0) / (r + z0)
        ax.plot([normalized_r, normalized_r], [-1, 1], '--', color='black')
        ax.text(normalized_r, 0.05, f"{r}", color='blue', fontsize=10)

# добавление чисел вдоль окружности
    angles = np.linspace(0, 2 * np.pi, len(resistances), endpoint=False)
    for angle, r in zip(angles, resistances):
        x = 1.1 * np.cos(angle)  # чуть за пределами окружности
        y = 1.1 * np.sin(angle)
        ax.text(x, y, f"{r}", color='green', fontsize=10, ha='center', va='center')

# обработчики кнопок
def redrawSmithChart(event):
    global frequencies, z0, inductance, capacitance
    try:
        start_freq = float(textboxFreqStart.text) * 1e6
        end_freq = float(textboxFreqEnd.text) * 1e6
        frequencies = np.linspace(start_freq, end_freq, 500)
        z0 = float(textboxZ0.text)
        inductance = float(textboxInduct.text) * 1e-9
        capacitance = float(textboxCapacit.text) * 1e-12
        updateSmithChart(axSmith, inductance, capacitance, frequencies, z0)
        plt.draw()
    except ValueError:
        print("Некорректный ввод. Убедитесь, что введены числовые значения.")

def zoom_in():
    axSmith.set_xlim(axSmith.get_xlim()[0] * 0.9, axSmith.get_xlim()[1] * 0.9)
    axSmith.set_ylim(axSmith.get_ylim()[0] * 0.9, axSmith.get_ylim()[1] * 0.9)
    canvas.draw()

def zoom_out():
    axSmith.set_xlim(axSmith.get_xlim()[0] * 1.1, axSmith.get_xlim()[1] * 1.1)
    axSmith.set_ylim(axSmith.get_ylim()[0] * 1.1, axSmith.get_ylim()[1] * 1.1)
    canvas.draw()

def save_figure():
    fig.canvas.draw()
    buf = fig.canvas.tostring_argb()
    width, height = fig.canvas.get_width_height()
    pil_image = Image.frombytes("RGB", (width, height), buf)
    pil_image.save('smith_chart.png')

def save_file():
    root.destroy()

def close_window():
    root.destroy()

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

# создание окна
fig = plt.figure(figsize=(14, 8))  # сделать окно шире
axSmith = fig.add_axes([0.4, 0.1, 0.55, 0.8])  # диаграмма справа
updateSmithChart(axSmith, inductance, capacitance, frequencies, z0)

# элементы управления слева
axTextboxFreqStart = plt.axes([0.12, 0.8, 0.1, 0.05])
textboxFreqStart = TextBox(axTextboxFreqStart, "Fmin(MHz) = ", initial="0")

axTextboxFreqEnd = plt.axes([0.12, 0.7, 0.1, 0.05])
textboxFreqEnd = TextBox(axTextboxFreqEnd, "Fmax(MHz) = ", initial="0")

axTextboxZ0 = plt.axes([0.12, 0.6, 0.1, 0.05])
textboxZ0 = TextBox(axTextboxZ0, "Zo(Ohm) = ", initial="50")

axTextboxCapacit = plt.axes([0.12, 0.5, 0.1, 0.05])
textboxCapacit = TextBox(axTextboxCapacit, "С(pF) = ", initial="0")

axTextboxInduct = plt.axes([0.12, 0.4, 0.1, 0.05])
textboxInduct = TextBox(axTextboxInduct, "L(nH) = ", initial="0")

axButtonRedraw = plt.axes([0.02, 0.2, 0.2, 0.075])
buttonRedraw = Button(axButtonRedraw, "Перестроить диаграмму Смита")

# элементы масштабирования диаграммы
button_frame = tk.Frame(master=root)
button_frame.pack(side=tk.BOTTOM)

zoom_in_button = tk.Button(master=button_frame, text="Увеличить", font=("Times New Roman", 12), command=zoom_in)
zoom_in_button.pack(side=tk.LEFT)

zoom_out_button = tk.Button(master=button_frame, text="Уменьшить", font=("Times New Roman", 12), command=zoom_out)
zoom_out_button.pack(side=tk.LEFT)

main_menu = Menu()
 
file_menu = Menu()
file_menu.add_command(label="Создать файл",  command = create_new_file)
file_menu.add_command(label="Открыть файл", command = open_file)
file_menu.add_command(label="Сохранить график", command = save_figure)
file_menu.add_command(label="Сохранить как", command = save_file)
file_menu.add_separator()
file_menu.add_command(label="Выход", command = close_window)
 
main_menu.add_cascade(label="Файл", menu=file_menu)
main_menu.add_cascade(label="Настройки")
main_menu.add_cascade(label="Вид")
 
root.config(menu=main_menu)

# привязка функций к кнопкам
buttonRedraw.on_clicked(redrawSmithChart)

# холст Tkinter для отображения фигуры Matplotlib
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# цикл событий Tkinter
root.mainloop()
