print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
# usuario y contrasena predefinidos
user = "51604"
password = "40615"
name = input("Introduzca su usuario:") # se pide usuario predefinido
if name != user:
    print("Error")
else:
    clave = input("Introduzca su password:") # se pide clave predefinida
    if clave != password:
        print("Error")
    else:
        print("CAPTCHA")
        first_num = 604
        second_num = (((6*5)-(5*4))-(4+6))
        add = first_num+second_num
        response_captcha = int(input(f"{first_num} + {second_num} = ")) # solucionar operación matemática
        if response_captcha != add:
            print("Error")
        else:
            print("Sesión iniciada")