# Datatypes

print(1)  # int
print(1.0)  # float
print(1.0)  # também float

num_complexo = 1 + 4j  # complex(real+imag.)
print(num_complexo.real)  # complex(real)
print(num_complexo.imag)  # complex+imag

# Func to set datatype

print(int(1.0))
print(float(1))
print(float("-inf"))  # negative infinity
print(float("+inf"))  # positive infinity
print(float("nan"))  # not a number
print(complex(1, 2))  # complex by func

# math with complex

print(complex(1, 2) + 2)  # add real
print(complex(2, 0) + 0 + 1j)  # add imag
print(2 + 0 + 1j)  # add imag

# some arithmetic operators

print(10 // 3)  # floor division
print(10 % 3)  # remainder
print(2**8)  # exponentiation

# bits operator
print("bits operator")

print(1 | 0)  # OR
print(1 ^ 5)  # EXCLUSIVE OR
print(4 & 1)  # AND
print(1 << 2)  # x shifted left by y bits
print(4 >> 2)  # x shifted right by y bits
print(~4)  # bitS inversion

# fun datatype

print(type(1 + 2.0))
print(type(1 + 2j))
print(type(1.0 + 2j))
print(type(1.0 + 1.0))

# how to declare quotes inside strings

print("copa 'padrão fifa'")
print('copa "padrão fifa"')

# coding: utf-8
print(
    """\
Uso: consulta_base [OPCOES]
-h Exibe saída de ajuda
-U url Url do dataset
"""
)

# acess string idex and len

st = "arena MRV"
print(st[0])
print(st[1:4])
print(st[2:])
print(st[:3])
print(len(st))

# check letters or words in string

print("m" in "arena")
print("x" not in "MRV")
print("a" + "rena")
print("mrv" * 3)

# ways to alter string value

minha_str = "livro python 3"
minha_str = minha_str[0:13] + "2"
print(minha_str)
minha_str = "livro python 3"
minha_str = minha_str.replace("3", "2")
print(minha_str)

# some string func

print("arena MRV".capitalize())
print("arena MRV".count("a"))
print("arena MRV".startswith("m"))
print("arena MRV".endswith("a"))
print("copa de 2014".split(" "))
print(" ".join(["Copa", "de", "2014"]))
print("copa de 2014".replace("2014", "2018"))

# Interpolate strings

print("%d dias para copa" % (100))
print("{} dias para copa".format(100))
print("{dias} dias para copa".format(dias=100))
print("{:<60}".format("alinhado à esquerda, ocupando 60 posições"))
print("{:>60}".format("alinhado à direita, ocupando 60 posições"))
print("{:^60}".format("centralizado, ocupando 60 posições"))
print("{:.^60}".format("centralizando ao alterar caractere"))
print("{:,^60}".format("centralizando ao alterar caractere"))
print("{:*^60}".format("centralizando ao alterar caractere"))
