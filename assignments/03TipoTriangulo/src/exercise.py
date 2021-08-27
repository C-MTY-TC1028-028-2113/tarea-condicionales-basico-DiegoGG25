def main():
    lado1 = int(input("Ingresa la medida del lado 1: "))
    lado2 = int(input("Ingresa la medida del lado 2: "))
    lado3 = int(input("Ingresa la medida del lado 3: "))
    #Escribe aquí tu código...

    r1 = lado1 + lado2
    r2 = lado2 + lado3
    r3 = lado3 + lado1

    if r1 <= lado3:
        #cosa
        print('NO ES TRIANGULO')
    elif r2 <= lado1:
        #cosa
        print('NO ES TRIANGULO')
    elif r3 <= lado2:
        #cosa
        print('NO ES TRIANGULO')
    else:
        if lado1 == lado2 == lado3:
            print('ES UN TRIANGULO EQUILATERO')
        elif lado1 != lado2 and lado2 != lado3 and lado3 != lado1:
            print('ES UN TRIANGULO ESCALENO')
        else:
            print('ES UN TRIANGULO ISOSCELES')


if __name__=='__main__':
    main()
