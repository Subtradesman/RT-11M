import schematic as schm
from tkinter import*
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import filedialog
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from skrf.plotting import smith

#Это основной файл. Он инициализирует Графический интерфейс и его взаимодействие с schematic. 

# окно Tkinter
root = tk.Tk()
root.title("Калькулятор диаграммы Смита")
root.geometry('800x600')
root.option_add("*tearOff", FALSE)

# параметры
frequencies = np.linspace(1e6, 1e9, 500)  # частоты от 1 мГц до 1 ГГц
z0 = 50  # номинальный импеданс
inductance = 1e-9   # начальная индуктивность (гн)
capacitance = 1e-12  # начальная ёмкость (ф)

# функция для вычисления импедансов
def calculateImpedance(inductance, capacitance, frequencies):
    omega = 2 * np.pi * frequencies
    zL = 1j * omega * inductance  # индуктивное сопротивление
    zC = 1 / (1j * omega * capacitance)  # ёмкостное сопротивление
    return zL + zC

# обновление диаграммы Смита
def updateSmithChart(ax, schema:schm.schematic,frequency):
    ax.clear()    # очистить ось
    smith(ax=ax)  # нарисовать диаграмму Смита

    # вычисление импедансов
    impedances = schema.getImpedanceCurve(frequency)
    gamma = (impedances - z0) / (impedances + z0)  # коэффициенты отражения

    # построение линии на диаграмме
    ax.plot(gamma.real, gamma.imag, color='red', label=f"L = {inductance * 1e9:.2f} nH, C = {capacitance * 1e12:.2f} pF")
    ax.legend()
    ax.set_title("Диаграмма Смита", fontsize=16)

def show_message():
    label["text"] = entry.get()     # получаем введенный текст

# обработчик для кнопки "Индуктивность +"
def increaseInductancePLS(event):
    global inductance
    inductance += 1e-9  # увеличить индуктивность на 1 нГн
    updateSmithChart(ax, inductance, capacitance)
    plt.draw()

# обработчик для кнопки "Индуктивность -"
def increaseInductanceMIN(event):
    global inductance
    inductance -= 1e-9  # уменьшить Индуктивность на 1 нГн

    if inductance > 0:
        updateSmithChart(ax, inductance, capacitance)
        plt.draw()
    if inductance <= 0:
        inductance = 5e-12

# обработчик для кнопки "Емкость +"
def increaseCapacitancePLS(event):
    global capacitance
    capacitance += 0.5e-12  # увеличить ёмкость на 0.5 пФ
    updateSmithChart(ax, inductance, capacitance)
    plt.draw()

# обработчик для кнопки "Ёмкость -"
def increaseCapacitanceMIN(event):
    global capacitance
    capacitance -= 0.5e-12  # уменьшить ёмкость на 0.5 пФ

    if capacitance > 0:
        updateSmithChart(ax, inductance, capacitance)
        plt.draw()
    if capacitance <= 0:
        capacitance = 5e-12

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
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("Изображение", "*.png")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_area.get("1.0", tk.END))


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

# создание окна и диаграммы
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)  # добавить место для кнопок

ser_res = schm.SerialResistor(100)
ser_ind = schm.SerialInductor(10e-9)
schem = schm.schematic(50,50)

schem.addElement(ser_ind)
schem.addElement(ser_res)

updateSmithChart(ax, schem,1e9)




schem.addElement(ser_ind)
schem.addElement(ser_res)

gamma = schem.getImpedanceCurve(1e9)




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

# холст Tkinter для отображения фигуры Matplotlib
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

elem_viewer = Canvas(bg="white")
elem_viewer.pack(anchor=S,fill=X ,expand=1)

elem_viewer.create_line(10, 10, 200, 50,width=3)


# цикл событий Tkinter
root.mainloop()



