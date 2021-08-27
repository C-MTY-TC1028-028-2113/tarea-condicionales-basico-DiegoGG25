
def main():
    edad = int(input("Ingresa tu edad: "))
    #Aquí empieza tu programa...
    if 0 < edad < 18:
        print('No cumples requisitos')
    elif edad <= 0:
        print('Respuesta incorrecta')
    else:
        id = str(input('¿Tienes identificación oficial? (s/n): '))
        if id == 's':
            print('Trámite de licencia concedido')
        elif id == 'n':
            print('No cumples requisitos')
        else:
            print('Respuesta incorrecta')

if __name__ == '__main__':
    main()
