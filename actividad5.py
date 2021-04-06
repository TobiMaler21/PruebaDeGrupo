frase = str (input('Ingrese una frase y un string '))
palabra = input()
lista = frase.lower().split()
cantidad = 0
for i in lista:
    if (i == palabra):
        cantidad = cantidad + 1                  #inc 1 ( cantidad ++ en java)
print(f'Frase: {frase} Palabra: {palabra} Resultado: {cantidad}')       
        



