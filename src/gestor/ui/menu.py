def mostrarMenu(n1):

    #ESTOY INTENTANDO HACER QUE SE MUESTRE EL MENSAJE POR LO MENOS 1 VEZ Y LUEGO INTENTAR
    #QUE EN CASO DE QUE Opcion1 Sea Distinto de 0 vuelva a enviar todos los print
    #Y en CASO DE QUE Opcion1 Sea Igual a 0 Termine el Programa.
    #Estoy usando While y Ok como variable bool.
    #Pero sigue sin funcionar y nose porque
    Ok = True
    Opcion1 = n1
    if(Opcion1 != 0):
        while Ok:
            
            print("========================================","\nMI SISTEMA — MENÚ PRINCIPAL", "\n========================================")
            print(1,". Buscar elemento")
            print(2,". Explorar por categorías")
            print(3,". Listar todo ordenado")
            print(4,". Agregar elemento")
            print(5,". Eliminar elemento")
            print(6,". Deshacer última operación")
            print(7,". Ver estadísticas")
            print(0,". Salir")
            print("----------------------------------------")
            Opcion2 = int(input("Opción:"))
            Opcion1 = Opcion2
            if(Opcion1 == 0):
                Ok = False
                print("Saliendo del programa")
    return Opcion1

#MAIN    
m1 = 9
m1 = mostrarMenu(m1)
print(m1)







""" ========================================
1. Buscar elemento
2. Explorar por categorías
3. Listar todo ordenado
4. Agregar elemento
5. Eliminar elemento
6. Deshacer última operación
7. Ver estadísticas
0. Salir
----------------------------------------
Opción:") """