# Matchcalc library #

## What is this? ##
The module allows you calculate complex impedance and reflection coefficient for elements: 

1. Capacitance (serial and parallel connection)

2. Inductance (serial and parrallel connection)

3. Resistance (serial and parallel connection)

4. Open stub (only parallel connection)

5. Short stub (only parallel connection)

----------
## Functions ##

1.  ### cap_ser(z_source, frequency, capacitance) 
   
    Complex impedance and reflection coefficient for SERIAL connection of capasitor  

    #### input

    z_source: input complex impedance in Ohmn 

    frequency: frequency in Hz

    capacitance: capacitance in F

    ##### output

    z_c: complex impedance

    z_c_out: complex line impedance after element connection

    gamma_c: reflection coefficent
   
_________________________________________________________________________

2.  ### ind_ser(z_source, frequency, inductance)
   
    Complex impedance and reflection coefficient for SERIAL connection of inductor 
    
    ##### input

    z_source: input impedance in Ohmn 

    frequency: frequency in Hz

    inductance: inductance in H

    ##### output

    z_i: complex impedance

    z_i_out: complex line impedance after element connection

    gamma_i: reflection coefficent

_________________________________________________________________________

3.  ### res_ser(z_source, resistance)

    Complex impedance and reflection coefficient for SERIAL connection of resistor 
    
    ##### input

    z0: Input impedance in Ohmn 

    resistance: resistance in Ohm

    ##### output

    z_r: complex impedance

    z_r_out: complex line impedance after element connection

    gamma_r: reflection coefficent
    
_________________________________________________________________________

4.  ### cap_par(z_source, frequency, capacitance)
   
    Complex impedance and reflection coefficient for PARALLEL connection of capasitor  
    
    ##### input

    z_source: input complex impedance in Ohmn 

    frequency: frequency in Hz

    capacitance: capacitance in F
    
    ##### output

    z_c: complex impedance

    z_c_out: complex line impedance after element connection 

    gamma_c: reflection coefficent 

_________________________________________________________________________

5.  ### ind_par(z_source, frequency, inductance)
   
    Complex impedance and reflection coefficient for PARALLEL connection of inductor 
    
    ##### input

    z_source: input impedance in Ohmn 

    frequency: frequency in Hz

    inductance: inductance in H

    ##### output

    z_i: complex impedance

    z_i_out: complex line impedance after element connection
    
    gamma_i: reflection coefficent

_________________________________________________________________________

6.  ### res_par(z_source, resistance)

    Complex impedance and reflection coefficient for SERIAL connection of resistor 
    
    ##### input

    z0: input impedance in Ohmn 

    resistance: resistance in Ohm

    ##### output

    z_r: complex impedance

    z_r_out: complex line impedance after element connection

    gamma_r: reflection coefficent
    
_________________________________________________________________________

7.  ### os(z_source, frequency, length, velocity, z0):

    Complex impedance and reflection coefficient for open stub 
    
    ##### input
    
    z_source: input impedance in Ohmn
    
    frequency: frequency in Hz

    length: length of stub im m 

    velocity: signal propagation velocity in m/s

    z0: Characteristic complex impedance

    ##### output 
    
    z_os: complex impedance

    z_os_out: complex line impedance after element connection

    gamma_os: reflection coefficent

_________________________________________________________________________

8.  ### ss(z_source, frequency, length, z0):

    Complex impedance and reflection coefficient for short stub 
    
    ##### input

    z_source: input impedance in Ohmn 

    frequency: frequency in Hz

    length: length of stub im m 

    velocity: signal propagation velocity in m/s

    z0: Characteristic complex impedance
   
    ##### output

    z_ss: complex impedance

    z_ss_out: complex line impedance after element connection

    gamma_ss: reflection coefficent 



## Using ##


Using the library is so hard and danger for your life:

Let's import it first:
First, import everything from the library (use the ` from mathcalclib import calculate ` construct).

### Example of one function ###

_____________________________________________________________

from mathcalclib import calculate 

mc = calculate 

z_source = 50 

frequency = 1e9 

capacitance = 1e-12

zc, z_c_out, gamma_c = mc.cap_par(z_source, frequency, capacitance)

print(gamma_c)

____________________________________________________________________

## Developer ##
Grigoriy Nelyubov 

grisha.nelyubov@gmail.com
