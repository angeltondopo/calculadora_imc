def masa_corporal():
    nombre = input('Escribe tu nombre \U0001f642: ').capitalize()
    peso = float(input('Cúal es tu peso  en Kilogramos(kg) \U0001faa8? '))
    altura = float(input('Cúal es tu altura en Metros(m) \U0001f4cf? '))
    indice_masa = peso / (altura * altura)
    indice_masa = round(indice_masa, 2)
    print('Hola \U0001f44b ' + str(nombre) + ' tu imc \U0001f4aa \U0001f9b4 es de ' + str(indice_masa))


def run():
    print('''Descubre si tu estado de salud es favorable.
El imc es un indicador \u2695\uFE0F muy fiable para saber si estas obeso o desnutrido \u2696\uFE0F''')
    masa_corporal()


if __name__ == '__main__':
    run()