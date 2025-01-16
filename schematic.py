from enum import Enum
from typing import List
from abc import ABC, abstractmethod
import numpy as np
import MATH.mathcalclib as ml



def genInverseParamArr(final_parameter,N,step):
    params = np.zeros(param_arr_size)
    a = final_parameter*param_step*param_arr_size
    params[0] = np.inf
    for i in range(1,param_arr_size):
        params[i] = a/(i*param_step)
    return params


def genLinearParamArr(final_parameter,N):
    params = np.linspace(0,final_parameter,N)
    return params



#Абстрактный класс, все классы такие как последовательный конденсатор, замкнутая индуктивность и т.д. будут наследоваться от этого класса

param_step = 0.01
param_arr_size = 1000

class element:
    #Функция getImpedanceCurve вычисляет кривую импедансов, на выходе должен быть массив np.Complex64, InputImpedance - представляет собой complex значение.
    #например complex(1,2) равен: 1 + i2. 
    @abstractmethod 
    def getImpedanceCurve(self,InputImpedance, frequency):
        pass

#-----------------------------------
#-----Последовательные элементы-----
#-----------------------------------

#Последовательный конденсатор
class SerialCapacitor(element):

    elem_capacitance:float

    def __init__(self,capacitence):
        self.elem_capacitance = capacitence

    #Функция возвращает массив точек кривой импедансов, для последовательного конденсатора.
    def getImpedanceCurve(self,InputImpedance,frequency)->np.complex64:
            params = genInverseParamArr(self.elem_capacitance,param_arr_size,param_step)
            omega = ml.calculate.cap_ser(InputImpedance,frequency,params)
            return omega

#Последовательная индуктивность
class SerialInductor(element):
    elem_inductance:float

    def __init__(self,inductance):
        self.elem_inductance = inductance
    
    #Функция возвращает массив точек кривой импедансов, для последовательной индуктивности.
    def getImpedanceCurve(self,InputImpedance, frequency):
        params = genLinearParamArr(self.elem_inductance,param_arr_size)
        omega = ml.calculate.ind_ser(InputImpedance,frequency,params)
        return omega


    
#Последовательный резистор
class SerialResistor(element):
    elem_resistance:float
    def __init__(self,resistance):
        self.elem_resistance = resistance
    
    #Функция возвращает массив точек кривой импедансов, для последовательного резистра
    def getImpedanceCurve(self,InputImpedance, frequency):
        params = genLinearParamArr(self.elem_resistance,param_arr_size)
        omega = ml.calculate.res_ser(InputImpedance,params)
        return omega

#-----------------------------------
#------Параллельные элементы--------
#-----------------------------------

class ParallelCapacitor(element):

    elem_capacitance:float

    def __init__(self,capacitence):
        elem_capacitance = capacitence

    #TODO
    def getImpedanceCurve(self,InputImpedance, frequency):
        pass

class ParallelInductor(element):
    elem_inductance:float
    def __init__(self,inductance):
        elem_inductance = inductance

    #TODO
    def getImpedanceCurve(self,InputImpedance, frequency):
        pass

class ParallelResistor(element):
    elem_resistance:float
    def __init__(self,resistance):
        elem_resistance = resistance
    
    #TODO
    def getImpedanceCurve(self,InputImpedance, frequency):
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
    def getImpedanceCurve(self,InputImpedance, frequency):
        pass

class ShortStub(element):
    elem_resistance:float
    def __init__(self,resistance):
        elem_resistance = resistance
    
    #TODO
    #Функция возвращает массив точек кривой импедансов, для последовательного резистра
    def getImpedanceCurve(self,InputImpedance, frequency):
        pass



class Port(element):
    Impedance:float
    def __init__(self,Impedance):
        self.Impedance = Impedance
    
    #TODO
    #Функция возвращает массив точек кривой импедансов, для последовательного резистра
    def getImpedanceCurve(self,InputImpedance, frequency):
        return self.Impedance


#|-------------------|
#|----Класс схемы----|
#|-------------------|


#Опрделяет схему представляет собой список элементов.
class schematic:
    elem_list: List[element]
    is_init = False
    elem_InputImpedance:float
    elem_OutputImpedance:float

    def __init__(self,InputImpedance,OutpuImpedance):
        self.elem_InputImpedance = InputImpedance
        self.elem_OutputImpedance = OutpuImpedance
        self.elem_list = []

    def addElement(self,elem:element):
        self.elem_list.append(elem)

    #TODO Функция выдает массив точек импедансов всей схемы.
    def getImpedanceCurve(self,frequency):
        Imp = self.elem_InputImpedance
        sigma = np.ndarray(0)
        for x in self.elem_list:
            omega = x.getImpedanceCurve(Imp,frequency)
            Imp = omega[-1]
            sigma = np.append(sigma,omega)
        return sigma
