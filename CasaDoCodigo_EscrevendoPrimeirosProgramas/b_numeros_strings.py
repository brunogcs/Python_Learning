#Datatypes 

print(1) #int
print(1.0) #float
print(1.) #também float

num_complexo = 1 + 4j    #complex(real+imag.)
print(num_complexo.real) #complex(real)
print(num_complexo.imag) #complex+imag

#Func to set datatype

print(int(1.0))
print(float(1))
print(float('-inf')) #negative infinity
print(float('+inf')) #positive infinity
print(float('nan'))  #not a number
print(complex(1, 2)) #complex by func

#math with complex

print(complex(1, 2) + 2)    #add real
print(complex(2, 0) + 0+1j) #add imag
print(2 + 0+1j)             #add imag

#some arithmetic operators

print(10 // 3)  #floor division
print(10 % 3)   #remainder
print(2 ** 8)   #exponentiation

#bits operator
print('bits operator')

print(1 | 0)  #OR
print(1 ^ 5)  # EXCLUSIVE OR
print(4 & 1)  # AND
print(1 << 2) # x shifted left by y bits
print(4 >> 2) # x shifted right by y bits
print(~4)     # bitS inversion

#fun datatype

print(type(1 + 2.0))
print(type(1 + 2J))
print(type(1.0 + 2J))
print(type(1.0 + 1.0))