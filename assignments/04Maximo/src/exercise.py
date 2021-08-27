def main():
    #escribe tu código abajo de esta línea
    num1 = int(input("Ingresa el primer número: "))
    num2 = int(input("Ingresa el segundo número: "))
    num3 = int(input("Ingresa el tercer número: "))

    if num3 > num2:
        if num3 > num1:
            print(num3)
        else:
            print(num1)
    else:
        if num2 > num1:
            print(num2)
        else:
            print(num1)


if __name__=='__main__':
    main()
