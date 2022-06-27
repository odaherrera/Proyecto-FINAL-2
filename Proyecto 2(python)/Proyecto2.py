import os
import json
print("=====================================================")
print("    Inventario para almanecer materiales secretos    ")
print("=====================================================")

with open('Proyecto 2(python)\clavesdeencriptado.json', 'r') as f:
    clave_de_encriptacion = json.load(f)

def codificador():
    dtext = open("Proyecto 2(python)\Listado de Materiales1.txt", 'r')
    dtext = dtext.readlines()

    encryptText(dtext)

def encryptText(dtext):
    etext = open("Proyecto 2(python)\Listado de Materiales1.txt", 'w')
    for line in dtext:
        for c in line:
            encrypted = (clave_de_encriptacion.get(c, c))
            etext.write(encrypted)
    etext.close()

def decodificador():
    dtext = open("Proyecto 2(python)\Listado de Materiales1.txt", 'r')
    dtext = dtext.readlines()

    desencriptador(dtext)

def desencriptador(dtext):
    etext = open("Proyecto 2(python)\Listado de Materiales1.txt", 'w')
    clave_inversa_de_encriptacion = {}
    for key, value in clave_de_encriptacion.items():
        clave_inversa_de_encriptacion[value] = key
    for line in dtext:
        for c in line:
            encrypted = (clave_inversa_de_encriptacion.get(c, c))
            etext.write(encrypted)
    etext.close()

def wordfill(word, size):
    if len(word) % 2 == 0:
        result = ' ' * int((size - len(word))/2) + word + ' ' * int((size - len(word))/2)
    else:
        result = ' ' * int((size - len(word))/2) + word + ' ' * int((size - len(word))/2) + ' '
    return result 

def Crear_archivo():
    print('CREACION DE LISTA DE MATERIALES ')
    print('')
    fh_w = open("Proyecto 2(python)\Listado de Materiales1.txt","w")
    nombre = input('Ingrese nombre del material: ')
    utilidad = input('Ingrese utilidad del material: ')
    letalidad = input('Ingrese x si es una material letal, ingrese "o"(la letra) si no lo es: ')
    prioridad = input('Es el material de alta o baja priodad: ')
    cantidad = (input('Ingrese la cantidad del material: '))
    print('')
    print('                     Se ha creado una lista                    ')
    print('')
    str_0 = wordfill(nombre, 30).lower()
    str_1 = wordfill(utilidad, 40).lower()
    str_2 = wordfill(letalidad, 11).lower()
    str_3 = wordfill(prioridad, 13).lower()
    str_4 = wordfill(cantidad, 12)
    enunciado_0 = wordfill('nombre', 30).lower()
    enunciado_1 = wordfill('utilidad', 40).lower()
    enunciado_2 = wordfill('letalidad', 11).lower()
    enunciado_3 = wordfill('prioridad', 11).lower()
    enunciado_4 = wordfill('cantidad', 12).lower()

    fh_w.write('='*126 + '\n') 
    fh_w.write('|{}|\t{}|\t{}|\t{}|\t{}\n'.format(enunciado_0, enunciado_1, enunciado_2, enunciado_3, enunciado_4))
    fh_w.write('='*126 + '\n')   
    fh_w.write('|{}|\t{}|\t{}|\t{}|\t{}\n'.format(str_0, str_1, str_2, str_3, str_4))
    fh_w.write('_'*126 + '\n')
    fh_w.close()

def transform_lista(input_list):
    output_list = []
    for algo in input_list:
        output_list.append(algo.strip())
    return output_list
   
def buscarmaterial():
    print('BUSQUEDA DE MATERIAL ')
    print('')
    fh_r = open("Proyecto 2(python)\Listado de Materiales1.txt","r")
    nombre = (input('Ingrese nombre del material: ')).lower()
    print('')

    s = ' '
    while(s):
        s = fh_r.readline()
        l = s.split("|")
        l = transform_lista(l)
        if nombre in l:
            print("nombre del material: ", l[1])
            print("utilidad: ", l[2])
            print("letalidad: ", l[3])
            print("Prioridad: ", l[4])
            print("Cantidad: ", l[5])

    print('')       
    print("Si el programa no realizo ninguna accion, ")
    print("se debe a que el material no existe en la lista")
    print("realice un registro de este material")
    print('')

def registrarmaterial():
    print('REGISTRO DE MATERIAL ')
    fh_w = open("Proyecto 2(python)\Listado de Materiales1.txt","a+")
    print('')
    nombre = input('Ingrese nombre del material: ')
    utilidad = input('Ingrese utilidad del material: ')
    letalidad = input('Ingrese x si es una material letal, ingrese o(la letra) si no lo es: ')
    prioridad = input('Es el material de alta o baja priodad: ')
    cantidad = (input('Ingrese la cantidad del material: '))
    str_0 = wordfill(nombre, 30).lower()
    str_1 = wordfill(utilidad, 40).lower()
    str_2 = wordfill(letalidad, 11).lower()
    str_3 = wordfill(prioridad, 13).lower()
    str_4 = wordfill(cantidad, 13)

    fh_w.write('|{}|\t{}|\t{}|\t{}|\t{}\n'.format(str_0, str_1, str_2, str_3, str_4))
    fh_w.write('_'*126 + '\n')

def actualizar_lista():
    print('Actualizar lista de materiales ')
    print('')
    buscarmaterial()
    print('')
    fh_r = open("Proyecto 2(python)\Listado de Materiales1.txt","r")
    fh_w = open("temp.txt","w")
    nombre = (input('Ingrese nombre del material que desea actualizar: ')).lower()
    print("\n")

    s = ' '
    while(s):
        s = fh_r.readline()
        l = s.split("|")
        l = transform_lista(l)
        if nombre in l:
            print('el nombre del material tiene que estar en plural(ejemplo: granadas)')
            nombre = input('Ingrese nombre corregido del material: ')
            utilidad = input('Ingrese utilidad del material: ')
            letalidad = input('Ingrese x si es una material letal, ingrese o(la letra) si no lo es: ')
            prioridad = input('Es el material de alta o baja priodad: ')
            cantidad = (input('Ingrese la cantidad total del material: '))
            print('')
            print('              Se ha actualizado la lista de materiales                   ')
            print('')
            str_0 = wordfill(nombre, 30).lower()
            str_1 = wordfill(utilidad, 40).lower()
            str_2 = wordfill(letalidad, 11).lower()
            str_3 = wordfill(prioridad, 13).lower()
            str_4 = wordfill(cantidad, 13)

            fh_w.write('|{}|\t{}|\t{}|\t{}|\t{}\n'.format(str_0, str_1, str_2, str_3, str_4))

        else:
            fh_w.write(s)

    print('')       
    print("Si el programa no realizo ninguna accion, ")
    print("se debe a que el material no existe en la lista")
    print("realice un registro de este material")


    fh_r.close()
    fh_w.close()
    os.remove("Proyecto 2(python)\Listado de Materiales1.txt")
    os.rename("temp.txt","Proyecto 2(python)\Listado de Materiales1.txt")

def retirar_cantidad_de_material_en_la_lista():
    print('RETIRO DE MATERIALES EN LISTA')
    print("")
    print('BUSQUEDA DE MATERIALES PARA RETIRAR')
    fh_r = open("Proyecto 2(python)\Listado de Materiales1.txt","r")
    nombre = (input('Ingrese nombre del material: ')).lower()
    print('')

    s = ' '
    while(s):
        s = fh_r.readline()
        l = s.split("|")
        l = transform_lista(l)
        if nombre in l:
            print("nombre del material: ", l[1])
            print("utilidad: ", l[2])
            print("letalidad: ", l[3])
            print("Prioridad: ", l[4])
            print("Cantidad: ", l[5])
            print('')
            print('')

    fh_r = open("Proyecto 2(python)\Listado de Materiales1.txt","r")
    fh_w = open("temp.txt","w")
    print('Porfavor vuelva a ingresar el nombre del material buscado')
    nombre = (input('Ingrese el nombre del material que va a retirar: ')).lower()
    print("\n")

    s = ' '
    while(s):
        s = fh_r.readline()
        l = s.split("|")
        l = transform_lista(l)
        if nombre in l:
            nombre = l[1]
            utilidad = l[2]
            letalidad = l[3]
            prioridad = l[4]
            cantidadvieja = l[5]
            cantidadviejanumero = int(cantidadvieja)
            print('                              Debe colocar un numero entero                         ')
            cantidadagregada = (input('Ingrese la cantidad que va a retirar del material al inventario: '))
            cantidadagregadanumero = int(cantidadagregada)
            cantidadtotalnumero = - cantidadagregadanumero + cantidadviejanumero
            if cantidadtotalnumero < 0:
                print('')
                print("la cantidad que desea retirar es mayor a la que existe en inventario")
                print('')
                cantidadtotalnumero = cantidadvieja
            else:
                cantidadtotalnumero = cantidadtotalnumero

            cantidad = str(cantidadtotalnumero)
            str_0 = wordfill(nombre, 30).lower()
            str_1 = wordfill(utilidad, 40).lower()
            str_2 = wordfill(letalidad, 11).lower()
            str_3 = wordfill(prioridad, 13).lower()
            str_4 = wordfill(cantidad, 13)

            fh_w.write('|{}|\t{}|\t{}|\t{}|\t{}\n'.format(str_0, str_1, str_2, str_3, str_4))

        else:
            fh_w.write(s)
   
    
    print('')       
    print("Si el programa no realizo ninguna accion, ")
    print("se debe a que el material no existe en la lista")
    print("realice un registro de este material")

    
    fh_r.close()
    fh_w.close()
    os.remove("Proyecto 2(python)\Listado de Materiales1.txt")
    os.rename("temp.txt","Proyecto 2(python)\Listado de Materiales1.txt")

def agregar_cantidad_lista():
    print('AGREGAR CANTIDAD DE MATERIAL EN LISTA ')
    print('')
    print('BUSQUEDA DE MATERIAL PARA AGREGAR')
    fh_r = open("Proyecto 2(python)\Listado de Materiales1.txt","r")
    nombre = (input('Ingrese nombre del material: ')).lower()
    print('')

    s = ' '
    while(s):
        s = fh_r.readline()
        l = s.split("|")
        l = transform_lista(l)
        if nombre in l:
            print("nombre del material: ", l[1])
            print("utilidad: ", l[2])
            print("letalidad: ", l[3])
            print("Prioridad: ", l[4])
            print("Cantidad: ", l[5])
            print('')
    print('')
    fh_r = open("Proyecto 2(python)\Listado de Materiales1.txt","r")
    fh_w = open("temp.txt","w")
    print('')
    print('Porfavor vuelva a ingresar el nombre del material buscado')
    nombre = (input('Ingrese el nombre del material que va a agregar: ')).lower()
    print("\n")

    s = ' '
    while(s):
        s = fh_r.readline()
        l = s.split("|")
        l = transform_lista(l)
        if nombre in l:
            nombre = l[1]
            utilidad = l[2]
            letalidad = l[3]
            prioridad = l[4]
            cantidadvieja = l[5]
            cantidadviejanumero = int(cantidadvieja)
            print('                   Debe colocar un numero entero             ')
            cantidadagregada = (input('Ingrese la cantidad que va a agregar del material al inventario: '))
            cantidadagregadanumero = int(cantidadagregada)
            cantidadtotalnumero = cantidadagregadanumero + cantidadviejanumero
            cantidad = str(cantidadtotalnumero)
            str_0 = wordfill(nombre, 30).lower()
            str_1 = wordfill(utilidad, 40).lower()
            str_2 = wordfill(letalidad, 11).lower()
            str_3 = wordfill(prioridad, 13).lower()
            str_4 = wordfill(cantidad, 13)

            fh_w.write('|{}|\t{}|\t{}|\t{}|\t{}\n'.format(str_0, str_1, str_2, str_3, str_4))

        else:
            fh_w.write(s)

    print('')       
    print("Si el programa no realizo ninguna accion, ")
    print("se debe a que el material no existe en la lista")
    print("realice un registro de este material")


    fh_r.close()
    fh_w.close()
    os.remove("Proyecto 2(python)\Listado de Materiales1.txt")
    os.rename("temp.txt","Proyecto 2(python)\Listado de Materiales1.txt")

def eliminarmaterial():
    print('ELIMINACION DE MATERIAL EN LA LISTA')
    print('')
    fh_r = open("Proyecto 2(python)\Listado de Materiales1.txt", "r")
    nombre = input('Ingrese nombre del material que desea eliminar: ').lower()
    cantidad = input('Ingrese la cantidad del material: ')
    print("\n")
    with open("Proyecto 2(python)\Listado de Materiales1.txt", "r") as fh_r, open("bb.txt", "w") as output:
        for line in fh_r:
            if nombre not in line or cantidad not in line:
                output.write(line)

    os.remove("Proyecto 2(python)\Listado de Materiales1.txt")
    os.replace('bb.txt', 'Proyecto 2(python)\Listado de Materiales1.txt')

def leer_lista():
    f = open("Proyecto 2(python)\Listado de Materiales1.txt", "r")
 
    while(True):
        line = f.readline()
        if not line*2:
            break
        print(line.strip())
    f.close

def salir():
    print('Se termino el ingreso de materiales')
    print('\n')

def menu():
    op = ''

    while op != "9":
        print("===============MENU================")
        print('1.-Crear lista de materiales')
        print('2.-Leer lista de materiales')
        print('3.-Buscar material')
        print('4.-Actualizar lista de materiales')
        print('5.-Agregar cantidad de material en inventario')
        print('6.-Retirar cantidad de material en inventario')
        print('7.-Registrar material')
        print('8.-Eliminar material de la lista')
        print('9.-Salir')
        print("===================================")
        op = str(input('Digite opcion: '))
        print("===================================")

        if op == '1':
            Crear_archivo()
            print('\n')
        elif op == '2':
            leer_lista()
            print('\n')
        elif op == '3':
            buscarmaterial()
            print('\n')
        elif op == '4':
            actualizar_lista()
            print('\n')
        elif op == '5':
            agregar_cantidad_lista()
            print('\n')    
        elif op == '6':
            retirar_cantidad_de_material_en_la_lista()
            print('\n')        
        elif op == '7':
            registrarmaterial()
            print('\n')
        elif op == '8':
            eliminarmaterial()
            print('\n')
        elif op =='9':
            salir()
        else:
            print("")
            print('Porfavor ingrese un numero del 1 al 7 dependiendo de los que desea')
            print("\n")

if os.path.exists("Proyecto 2(python)\Listado de Materiales1.txt"):
    decodificador()
    menu()  
    codificador()
else:
    menu()  
    codificador()