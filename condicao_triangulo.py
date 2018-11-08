print("\nDigite abaixo os valores do triângulo...\n")

lado_a = float(input("Medida do lado 1 do triângulo: "))
lado_b = float(input("Medida do lado 2 do triângulo: "))
lado_c = float(input("Medida do lado 3 do triângulo: "))

if lado_a<=0 or lado_b<=0 or lado_c<=0 :
    print("\nLados nulos ou negativos não são aceitos.")

if lado_a>=lado_b+lado_c or lado_b>=lado_c+lado_a or lado_c>=lado_a+lado_b :
    print("\nNão é um Triângulo!")

elif lado_a==lado_b and lado_b==lado_c :
    print("\nÉ um Triângulo Equilátero!")

elif lado_a==lado_b or lado_b==lado_c or lado_c==lado_a :
    print("\nÉ um Triângulo Isósceles!")

else:
    print("\nÉ um Triângulo Escaleno!")