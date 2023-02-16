 # programa para convertir una cantidad a grados centigrados a su equivalencia en farenheit y kelvin 

print("-------------------------------------")
print("------- valor de grados centigrados --")
print("---------------------------------------")

# input 
C= int (input("digiteel valor de c:"))

# proccesig 
F = ( C*1.8 +32)
K= (C + 273.15)

# untput
print("---------------------------------------")
print("------------RESULTADOS-----------------")
print("---------------------------------------")
print("la conversion en farenheit en" +str (F) )
print( " la conversion de kelvin es " + str (K))
