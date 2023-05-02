# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

cadena = 'An!t@ 1@va La  T!na'  # input('Ingrese cadena a evaluar: ')#

print("12".isdigit())


def es_vocal(letra):
    vocales = "aeiou"
    vocales = vocales + vocales.upper()
    return letra in vocales


def es_consonante(letra):
    return letra.isalpha() and not es_vocal(letra)


def es_numero(letra):
    return letra.isdigit()


cantidad_consonantes = 0
cantidad_consonantes_mayusculas = 0
cantidad_consonantes_minusculas = 0
cantidad_vocales = 0
cantidad_vocales_mayuscula = 0
cantidad_vocales_minuscula = 0
cantidad_numeros = 0
cantidad_especiales = 0
cantidad_espacios = 0
for key, letra in enumerate(cadena):
    if es_consonante(letra):
        cantidad_consonantes += 1

    if es_consonante(letra) and letra == letra.upper():
        cantidad_consonantes_mayusculas += 1

    if es_consonante(letra) and letra == letra.lower():
        cantidad_consonantes_minusculas += 1

    if es_vocal(letra):
        cantidad_vocales += 1

    if es_vocal(letra) and letra == letra.upper():
        cantidad_vocales_mayuscula += 1

    if es_vocal(letra) and letra == letra.lower():
        cantidad_vocales_minuscula += 1

    if es_numero(letra):
        cantidad_numeros += 1

    if not es_consonante(letra) and not es_numero(letra) and es_vocal(letra):
        cantidad_especiales += 1

    if letra == ' ' and cadena[key + 1] != ' ':
        cantidad_espacios += 1

print('Contabilizar la logitud total de la cadena de caracteres que ha sido ingresadas: ', len(cadena))
print('Contabilizar las constantes que han sido ingresadas: ', cantidad_consonantes)
print('Contabilizar las constantes en mayusculas que han sido ingresadas: ', cantidad_consonantes_mayusculas)
print('Contabilizar las constantes en minusculas que han sido ingresadas: ', cantidad_consonantes_minusculas)
print('Contabilizar las vocales que han sido ingresadas: ', cantidad_vocales)
print('Contabilizar las vocales en mayuscula que han sido ingresadas: ', cantidad_vocales_mayuscula)
print('Contabilizar las vocales en minuscula que han sido ingresadas: ', cantidad_vocales_minuscula)
print('Contabilizar los números que han sido ingresados: ', cantidad_numeros)
print('Contabilizar los caracteres especiales que han sido ingresados: ', cantidad_especiales)
print('Contabilizar los espacios que han sido ingresados: ', cantidad_espacios)

print('Contabilizar las palabras que han sido ingresadas en la frase: ', len(cadena.replace('  ', ' ').split(' ')))

print('\n\nPresentación en cantidad\n')
dict_caracteres = {}
for key, letra in enumerate(cadena):
    d_c = dict_caracteres.get(letra)
    if d_c is None:
        dict_caracteres[letra] = cadena.count(letra)

for key, value in dict_caracteres.items():
    esp = "(espacios en blanco)" if key == ' ' else ""
    print(f'Carácter encontrado: {key} = {value} {esp} ')

suma_p = 0
print('\n\nPresentación en porcentaje\n')
for key, value in dict_caracteres.items():
    esp = "(espacios en blanco)" if key == ' ' else ""
    porcentaje = round((value / len(cadena)) * 100, 0)
    suma_p += porcentaje
    print(f'Carácter encontrado: {key} = {porcentaje}% {esp} ')

print(f'Total procentaje: {suma_p}%')
