centavos = int(input("Informe a quantia de centavos: "))

moedas_de_um_pila = centavos // 100
sobra = centavos - moedas_de_um_pila * 100
print ("Moedas de 1 real: ", moedas_de_um_pila, "Sobrou: ", sobra)

moedas_de_cinquenta = sobra // 50
sobra = sobra % 50
print ("Moedas de 50 centavos: ", moedas_de_cinquenta, "Sobrou: ", sobra)

moedas_de_25 = sobra // 25
sobra = sobra % 25
print ("Moedas de 25 centavos: ", moedas_de_25, "Sobrou: ", sobra)

moedas_de_10 = sobra // 10
sobra = sobra % 10
print ("Moedas de 10 centavos: ", moedas_de_10, "Sobrou: ", sobra)

moedas_de_5 = sobra // 5
sobra = sobra % 5
print ("Moedas de 5 centavos: ", moedas_de_5, "Sobrou: ", sobra)

moedas_de_1 = sobra // 1
sobra = sobra % 1
print ("Moedas de 1 centavos: ", moedas_de_1, "Sobrou: ", sobra)

centavos = int(input("Informe a quantia de centavos: "))

moedas_de_um_pila = centavos // 100
sobra = centavos - moedas_de_um_pila * 100


moedas_de_cinquenta = sobra // 50
sobra = sobra % 50


moedas_de_25 = sobra // 25
sobra = sobra % 25
print ("Moedas de 25 centavos: ", moedas_de_25, "Sobrou: ", sobra)

moedas_de_10 = sobra // 10
sobra = sobra % 10
print ("Moedas de 10 centavos: ", moedas_de_10, "Sobrou: ", sobra)

moedas_de_5 = sobra // 5
sobra = sobra % 5
print ("Moedas de 5 centavos: ", moedas_de_5, "Sobrou: ", sobra)

moedas_de_1 = sobra // 1
sobra = sobra % 1
print ("Moedas de 1 centavos: ", moedas_de_1, "Sobrou: ", sobra)

print ("Moedas de 1 real: ", moedas_de_um_pila, "Sobrou: ", sobra)