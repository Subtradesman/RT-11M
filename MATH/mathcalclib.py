"""
Mathematics calculating library (MathCalcLib) v.0.0.1

Nelyubov Grigoriy © 2024 

All rights not reserved

Appropriation of labor is punishable by curse 

""" 
import numpy as np

class calculate:

    def cap_ser(z_source, frequency, capacitance): 
   
       """
       Complex impedance and reflection coefficient for SERIAL connection of capasitor  
       
       z_source: input complex impedance in Ohmn 
       frequency: frequency in Hz
       capacitance: capacitance in F
       
       """
       # Complex impedance
       z_c = 1 / (1j * 2 * np.pi * frequency)
       z_c = z_c/capacitance
       
       # Complex line impedance after element connection 
       z_c_out = z_source + z_c

       # Reflection coefficent 
       gamma_c = (z_c_out - z_source) / (z_c_out + z_source)
       
       return z_c_out

    def ind_ser(z_source, frequency, inductance):
   
       """
       Complex impedance and reflection coefficient for SERIAL connection of inductor 
       
       z_source: input impedance in Ohmn 
       frequency: frequency in Hz
       inductance: inductance in H

       """
       # Complex impedance
       z_i = 1j * 2 * np.pi * frequency * inductance

       # Complex line impedance after element connection
       z_i_out = z_i + z_source 

       # Reflection coefficent 
       gamma_i = (z_i_out - z_source) / (z_i_out + z_source)
       
       return z_i_out

    def res_ser(z_source, resistance):
       """
       Complex impedance and reflection coefficient for SERIAL connection of resistor 
       
       z0: Input impedance in Ohmn 
       resistance: resistance in Ohm

       """
       # Complex impedance
       z_r = resistance

       # Complex line impedance after element connection
       z_r_out = z_r + z_source

       # Reflection coefficent 
       gamma_r = (z_r_out - z_source) / (z_r_out + z_source)
       
       return z_r_out

    def cap_par(z_source, frequency, capacitance): 
   
       """
       Complex impedance and reflection coefficient for PARALLEL connection of capasitor  
       
       z_source: input complex impedance in Ohmn 
       frequency: frequency in Hz
       capacitance: capacitance in F
       
       """
       # Complex impedance
       z_c = 1 / (1j * 2 * np.pi * frequency * capacitance)
       
       # Complex line impedance after element connection 
       z_c_out = (z_source * z_c)/(z_source + z_c)

       # Reflection coefficent 
       gamma_c = (z_c_out - z_source) / (z_c_out + z_source)
       
       return z_c, z_c_out, gamma_c

    def ind_par(z_source, frequency, inductance):
   
       """
       Complex impedance and reflection coefficient for PARALLEL connection of inductor 
       
       z_source: input impedance in Ohmn 
       frequency: frequency in Hz
       inductance: inductance in H

       """
       # Complex impedance
       z_i = 1j * 2 * np.pi * frequency * inductance

       # Complex line impedance after element connection
       z_i_out = (z_i * z_source)/(z_i + z_source) 

       # Reflection coefficent 
       gamma_i = (z_i_out - z_source) / (z_i_out + z_source)
       
       return z_i, z_i_out, gamma_i

    def res_par(z_source, resistance):
       
       """
       Complex impedance and reflection coefficient for SERIAL connection of resistor 
       
       z0: input impedance in Ohmn 
       resistance: resistance in Ohm

       """
       # Complex impedance
       z_r = resistance

       # Complex line impedance after element connection
       z_r_out = (z_r * z_source)/(z_r + z_source)

       # Reflection coefficent 
       gamma_r = (z_r_out - z_source) / (z_r_out + z_source)
       
       return z_r, z_r_out, gamma_r

    def os(z_source, frequency, length, velocity, z0):
       
       """
       Complex impedance and reflection coefficient for open stub 
       
       z_source: input impedance in Ohmn 
       frequency: frequency in Hz
       length: length of stub im m 
       velocity: signal propagation velocity in m/s
       z0: Characteristic complex impedance

       """
       velocity = 3e8

       # Wavenumber
       beta_os = 2 * np.pi * frequency / velocity
       
       # Complex impedance
       z_os = -1j * z0 / np.tan(beta_os * length)
       
       # Complex line impedance after element connection
       z_os_out = (z_source * z_os)/(z_source + z_os)

       # Reflection coefficent
       gamma_os = (z_os_out - z_source) / (z_os_out + z_source)
       
       return z_os, z_os_out, gamma_os

    def ss(z_source, frequency, length, z0):
       """
       Complex impedance and reflection coefficient for short stub 
       
       z_source: input impedance in Ohmn 
       frequency: frequency in Hz
       length: length of stub im m 
       velocity: signal propagation velocity in m/s
       z0: Characteristic complex impedance
       """
       velocity = 3e8

       # Wavenumber
       beta = 2 * np.pi * frequency / velocity

       # Complex impedance
       z_ss = 1j * z0 * np.tan(beta * length)

       # Complex line impedance after element connection
       z_ss_out = (z_source * z_ss)/(z_source + z_ss)

       # Reflection coefficent
       gamma_ss = (z_ss_out - z_source) / (z_ss_out +z_source)
       
       return z_ss, z_ss_out, gamma_ss