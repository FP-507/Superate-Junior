import csv 
from ConsultaBD import ConsultaBD
from Cuenta_yappy import Usuario


def main():
    print("===Bienvenido a Yappy===") 

    

    while True:
        print("1. Iniciar Sesión")
        print("2. Registrarse")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            usuario = input("Ingrese su usuario: ")
            contrasena = input("Ingrese su contraseña: ")
            consulta= ConsultaBD(usuario, contrasena)
            if consulta.autenticar():
                print("Inicio de sesión exitoso.")
                with open('Clases Superate\yappy_count\cuentas_yappy.csv', 'r') as archivo:
                    lector = csv.DictReader(archivo)
                    for fila in lector:
                        if fila['usuario'] == usuario:
                            saldo = float(fila['saldo'])
                            user_count = Usuario(nombre=usuario, saldo=saldo)
                break
        elif opcion == '2':
            usuario = input("Ingrese su usuario: ")
            contrasena = input("Ingrese su contraseña: ")
            consulta= ConsultaBD(usuario, contrasena)
            consulta.registrar()
        elif opcion == '3':
            print("Saliendo...")
            return
        else:
            print("Opción no válida. Intente nuevamente.")


    
    while True:
        
        
        print("=== Y A P P Y ===")
        print("1. Depositar")
        print("2. Enviar")
        print("3. Consultar saldo")
        print("4. Salir")
        opcion_menu = int(input("Seleccione una opción: "))

        if opcion_menu == 1:
            cantidad = float(input("Ingrese la cantidad a depositar: "))

            if user_count:
                user_count.depositar(cantidad= cantidad) 
                consulta.actualizar_saldo(user_count.get_saldo(cantidad= cantidad))

            print(f"Se han depositado {cantidad} exitosamente.")

        elif opcion_menu == 2:
            cantidad = float(input("Ingrese la cantidad a enviar: "))
            user_count.enviar(cantidad= cantidad)

            if user_count:
                consulta.actualizar_saldo(user_count.get_saldo(cantidad= cantidad))

            print(f"Se han enviado {cantidad} exitosamente.")

        elif opcion_menu == 3:
            user_count.estado()
            print("Consulta de saldo exitosa.")

        elif opcion_menu == 4:  
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


main()
