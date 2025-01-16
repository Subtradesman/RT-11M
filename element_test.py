import schematic as schm
import numpy as np
import csv

#serCap = SerialCapacitor(1e-12)
#gamma = serCap.getImpedanceCurve(50,1e9)




# gamma = serres.getImpedanceCurve(50)
# print(np.real(gamma))


ser_res = schm.SerialResistor(100)
ser_ind = schm.SerialInductor(10e-9)
#gamma = element.getImpedanceCurve(50,1e9)

schem = schm.schematic(50,50)

schem.addElement(ser_ind)
schem.addElement(ser_res)

gamma = schem.getImpedanceCurve(1e9)



print(np.imag(gamma))

with open('data.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(zip(np.real(gamma), np.imag(gamma)))


