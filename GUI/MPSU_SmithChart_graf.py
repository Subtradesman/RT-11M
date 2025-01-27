import schematic as schm
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


    # добавление шкалы сопротивлений
    resistances = [0, 10, 25, 50, 100, 200, 500]
    for r in resistances:
        z = r + 0j  # только сопротивление
        gamma_r = (z - z0) / (z + z0)
        ax.text(gamma_r.real, gamma_r.imag, f"{r}", color='blue', fontsize=10, ha='right')

# добавление чисел вдоль окружности
    angles = np.linspace(0, 2 * np.pi, len(resistances), endpoint=False)
    for angle, r in zip(angles, resistances):
        x = 1.1 * np.cos(angle)  # чуть за пределами окружности
        y = 1.1 * np.sin(angle)
        ax.text(x, y, f"{r}", color='green', fontsize=10, ha='center', va='center')

    ax.legend()
    ax.set_title("Диаграмма Смита", fontsize=16)



# функция для построения графика S-параметров
def plotSParameters():
    # получение начального и конечного значения диапазона частот
    start_freq = float(textboxFreqStart.text)
    end_freq = float(textboxFreqEnd.text)

    # статичные данные
    frequencies = np.linspace(start_freq, end_freq, 100)  # частотный диапазон GHz
    s11_full_band = np.random.normal(0, 1, len(frequencies))  # генерация случайных данных для S11 по всему диапазону
    s11_band_of_interest = np.random.normal(0, 1,
                                            len(frequencies))  # генерация случайных данных для S11 в интересующем диапазоне

    # применяем логарифмическое преобразование для dB
    s11_full_band_db = 20 * np.log10(np.abs(s11_full_band))
    s11_band_of_interest_db = 20 * np.log10(np.abs(s11_band_of_interest))

    # построение графика
    plt.figure(figsize=(10, 6))
    plt.title('Ring Slot $S_{21}$')

    # визуализация полного диапазона S-параметра s11
    plt.plot(frequencies, s11_full_band_db, label='Full Band Response')

    # визуализация интересующего диапазона (например, 82-90 GHz)
    band_of_interest_mask = (frequencies >= 82) & (frequencies <= 90)
    plt.plot(frequencies[band_of_interest_mask], s11_band_of_interest_db[band_of_interest_mask], lw=3,
    label='Band of Interest')

    # настройка графика
    plt.xlabel('Frequency (GHz)')
    plt.ylabel('Magnitude (dB)')
    plt.legend()

    # показать график
    plt.show()
    
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
    
# обновление графика S-параметров
def updateSParameters(event):
    plotSParameters()

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

axButtonRedraw = plt.axes([0.02, 0.3, 0.2, 0.075])
buttonRedraw = Button(axButtonRedraw, "Перестроить диаграмму Смита")

axButtonSParams = plt.axes([0.02, 0.2, 0.2, 0.075])
buttonSParams = Button(axButtonSParams, "График S-параметров")

# элементы масштабирования диаграммы
button_frame = tk.Frame(master=root)
button_frame.pack(side=tk.BOTTOM)

zoom_in_button = tk.Button(master=button_frame, text="Увеличить", font=("Times New Roman", 12), command=zoom_in)
zoom_in_button.pack(side=tk.LEFT)

zoom_out_button = tk.Button(master=button_frame, text="Уменьшить", font=("Times New Roman", 12), command=zoom_out)
zoom_out_button.pack(side=tk.LEFT)

ser_res = schm.SerialResistor(1000)
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

buttonSParams.on_clicked(updateSParameters)

plt.show()

# холст Tkinter для отображения фигуры Matplotlib
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# цикл событий Tkinter
root.mainloop()


