from enum import Enum
from typing import List
from abc import ABC, abstractmethod
import numpy as np

#Абстрактный класс, все классы такие как последовательный конденсатор, замкнутая индуктивность и т.д. будут наследоваться от этого класса
class element:
    #Функция getImpedanceCurve вычисляет кривую импедансов, на выходе должен быть массив np.Complex64, InputImpedance - представляет собой complex значение.
    #например complex(1,2) равен: 1 + i2. 

    @abstractmethod 
    def getImpedanceCurve(self,InputImpedance)->np.complex64:
        pass

#-----------------------------------
#-----Последовательные элементы-----
#-----------------------------------

#Последовательный конденсатор
class SerialCapacitor(element):

    elem_capacitance:float

    def __init__(self,capacitence):
        elem_capacitance = capacitence

    #TODO
    #Функция возвращает массив точек кривой импедансов, для последовательного конденсатора.
    def getImpedanceCurve(self,InputImpedance)->np.complex64:
        pass

#Последовательная индуктивность
class SerialInductor(element):
    elem_inductance:float
    def __init__(self,inductance):
        elem_inductance = inductance
    
    #TODO
    #Функция возвращает массив точек кривой импедансов, для последовательной индуктивности.
    def getImpedanceCurve(self,InputImpedance):
        pass
    
#Последовательный резистор
class SerialResistor(element):
    elem_resistance:float
    def __init__(self,resistance):
        elem_resistance = resistance
    
    #TODO
    #Функция возвращает массив точек кривой импедансов, для последовательного резистра
    def getImpedanceCurve(self,InputImpedance):
        pass

#-----------------------------------
#------Параллельные элементы--------
#-----------------------------------

class ParallelCapacitor(element):

    elem_capacitance:float

    def __init__(self,capacitence):
        elem_capacitance = capacitence

    #TODO
    def getImpedanceCurve(self,InputImpedance)->np.complex64:
        pass

class ParallelInductor(element):
    elem_inductance:float
    def __init__(self,inductance):
        elem_inductance = inductance

    #TODO
    def getImpedanceCurve(self,InputImpedance):
        pass

class ParallelResistor(element):
    elem_resistance:float
    def __init__(self,resistance):
        elem_resistance = resistance
    
    #TODO
    def getImpedanceCurve(self,InputImpedance):
        pass

#-------------------------------
#----Топологические элементы----
#-------------------------------

class OpenStub(element):
    elem_resistance:float
    def __init__(self,resistance):
        elem_resistance = resistance
    
    #TODO
    #Функция возвращает массив точек кривой импедансов, для последовательного резистра
    def getImpedanceCurve(self,InputImpedance):
        pass

class ShortStyb(element):
    elem_resistance:float
    def __init__(self,resistance):
        elem_resistance = resistance
    
    #TODO
    #Функция возвращает массив точек кривой импедансов, для последовательного резистра
    def getImpedanceCurve(self,InputImpedance):
        pass



class Port(element):
    Impedance:float
    def __init__(self,Impedance):
        self.Impedance = Impedance
    
    #TODO
    #Функция возвращает массив точек кривой импедансов, для последовательного резистра
    def getImpedanceCurve(self,InputImpedance):
        return self.Impedance


#|-------------------|
#|----Класс схемы----|
#|-------------------|


#Опрделяет схему представляет собой список элементов.
class schematic:
    def __init__(self,InputImpedance):
        x = Port(complex(50,0))
        self.elem_list:List[element] = [x]
        pass

    #TODO Функция выдает массив точек импедансов всей схемы.
    def getImpedanceCurve(self,frequency):
        pass 