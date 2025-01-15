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
def updateSmithChart(ax, inductance, capacitance):
    ax.clear()    # очистить ось
    smith(ax=ax)  # нарисовать диаграмму Смита

    # вычисление импедансов
    impedances = calculateImpedance(inductance, capacitance, frequencies)
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
updateSmithChart(ax, inductance, capacitance)

# создание кнопок
axButtonInductance1 = plt.axes([0.02, 0.1, 0.2, 0.1])  # позиция и размер кнопки
buttonInductance1 = Button(axButtonInductance1, "L+")
buttonInductance1.on_clicked(increaseInductancePLS)

axButtonInductance = plt.axes([0.25, 0.1, 0.2, 0.1])  # позиция и размер кнопки
buttonInductance = Button(axButtonInductance, "L-")
buttonInductance.on_clicked(increaseInductanceMIN)

axButtonCapacitance = plt.axes([0.55, 0.1, 0.2, 0.1])  # позиция и размер кнопки
buttonCapacitance = Button(axButtonCapacitance, "С+")
buttonCapacitance.on_clicked(increaseCapacitancePLS)

axButtonCapacitance1 = plt.axes([0.78, 0.1, 0.2, 0.1])  # позиция и размер кнопки
buttonCapacitance1 = Button(axButtonCapacitance1, "С-")
buttonCapacitance1.on_clicked(increaseCapacitanceMIN)

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

zoom_in_button = tk.Button(master=button_frame, text="Увеличить", font=("Times New Roman", 12), command=zoom_in)
zoom_in_button.pack(side=tk.LEFT)

zoom_out_button = tk.Button(master=button_frame, text="Уменьшить", font=("Times New Roman", 12), command=zoom_out)
zoom_out_button.pack(side=tk.LEFT)

reset_button = tk.Button(master=button_frame, text="Сбросить", font=("Times New Roman", 12), command=reset)
reset_button.pack(side=tk.LEFT)

label = ttk.Label(root, text="F =", font=("Times New Roman", 14))  
label.place(x=1, y=1) 
entry = ttk.Entry()
entry.pack(anchor=NW, padx=35, pady=2)
label1 = ttk.Label(root, text="Hz", font=("Times New Roman", 14))  
label1.place(x=165, y=1) 
btn = ttk.Button(root, text="Задать", command=show_message)
btn.pack(anchor=NW, padx=6, pady=6)

label2 = ttk.Label(root, text="Z =", font=("Times New Roman", 14))  
label2.place(x=1, y=75) 
entry1 = ttk.Entry()
entry1.pack(anchor=NW, padx=35, pady=15)
label3 = ttk.Label(root, text="Ohm", font=("Times New Roman", 14))  
label3.place(x=165, y=75) 
btn1 = ttk.Button(root, text="Задать", command=show_message)
btn1.pack(anchor=NW, padx=6, pady=6)

# холст Tkinter для отображения фигуры Matplotlib
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# цикл событий Tkinter
root.mainloop()
