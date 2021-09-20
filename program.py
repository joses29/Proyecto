import os
import time
from help import Archivo
from entidades import Administrativo, Departamento, Empresa, Obrero,Cargo,sobretiempos
listop = ['1','2','3','4']
# === objetos
cg = Archivo('./DATOS/cargo.txt','|') 
dadm = Archivo('./DATOS/administrativo.txt','|')
dp = Archivo('./DATOS/departamento.txt','|')
dob = Archivo('./DATOS/obrero.txt','|')
emp = Archivo('./DATOS/empresa.txt','|')
# ===
print('\t\t Menu Principal')
print('1) Mantenimiento\n2) Novedades\n3) Rol de pago\n4) Salir')
op = input('Opcion: ')
while op != '4':
    if op in listop:
        if op == '1':
            os.system('cls')
            listop.extend(['5','6','7'])
            print('\t\t Mantenimiento')
            print('''
            1) Empleados administrativos
            2) Empleados obreros
            3) Cargos
            4) Departamentos
            5) Empresa
            6) Parametros
            7) Salir
            ''')
            op1 = input('Opcion: ')
            if op1 in listop:
                if op1 == '1':
                    print('Empleados administrativos')
                    print('Listado')
                    for _ in dadm.leer() :
                        print(f'{_}')
                    id = input('Id: ')
                    nom = input('Nombres: ')
                    # === list departamento
                    print('Departamentos disponibles: ')
                    for _ in dp.leer() :
                        print(f'{_}')
                    if len(dp.leer()) != 0:dep = input('Id departamento: ')
                    else: dep = ''
                    # === list cargo
                    print('Cargos disponibles: ')
                    for _ in cg.leer() :
                        print(f'{_}')
                    if len(cg.leer()) != 0:crg = input('Id cargo: ')
                    else: crg = ''
                    sl = int(input('Sueldo: '))
                    fi = input('Fecha de ingreso: ')
                    dir = input('Direccion: ')
                    tl = input('Teléfono: ')
                    ci = input('Cedula: ')
                    Administrativo(id,nom,dep,crg,sl,fi,dir,tl,ci)
                if op1 == '2':
                    print('Empleados obreros')
                    print('Listado')
                    for _ in dob.leer() :
                        print(f'{_}')
                    id = input('Id: ')
                    nom = input('Nombres: ')
                    # === list departamento
                    print('Departamentos disponibles: ')
                    for _ in dp.leer() :
                        print(f'{_}')
                    if len(dp.leer()) != 0:dep = input('Id departamento: ')
                    else: dep = ''
                    # === list cargo
                    print('Cargos disponibles: ')
                    for _ in cg.leer() :
                        print(f'{_}')
                    if len(cg.leer()) != 0:crg = input('Id cargo: ')
                    else: crg = ''
                    sl = int(input('Sueldo: '))
                    fi = input('Fecha de ingreso: ')
                    dir = input('Direccion: ')
                    tl = input('Teléfono: ')
                    ci = input('Cedula: ')
                    Obrero(id,nom,dep,crg,sl,fi,dir,tl,ci)
                if op1 == '3':
                    print('Cargos')
                    for _ in cg.leer() :
                        print(f'{_}')
                    id = input('Id: ')
                    deps = input('Descripcion: ')
                    Cargo(deps,id)
                if op1 == '4':
                    print('Departamentos')
                    for _ in dp.leer() :
                        print(f'{_}')
                    id = input('Id: ')
                    deps = input('Descripcion: ')
                    Departamento(deps,id)
                if op1 == '5':
                    print('Empresa')
                    for _ in emp.leer() :
                        print(f'{_}')
                    dir = input('Direccion: ')
                    tlf = input('Teléfono: ')
                    rs = input('Razon social: ')
                    ruc = input('RUC: ')
                    Empresa(dir,tlf,rs,ruc)
                if op1 == '6':
                    print('Parametros')
            else:
                print('La opcion que ingreso no se encuentra disponible')
            input('Presione una tecla para continuar... ')
            os.system('cls')
        if op == '2':
            os.system('cls')
            listop = listop[:3]
            print('\t\t Novedades')
            print('''
            1) Sobretiempo
            2) Prestamos
            3) Salir
            ''')
            op1 = input('Opcion: ')
            if op1 in listop:
                if op1 == '1':
                    print('Sobretiempo')
                    #sobretiempos()
                if op1 == '2':
                    print('Prestamos')
            else:
                print('La opcion que ingreso no se encuentra disponible')
            input('Presione una tecla para continuar... ')
            os.system('cls')
        if op == '3':
            listop = listop[:3]
            os.system('cls')
            print('\t\t Rol de pago')
            print('''
            1) Rol administrativos
            2) Rol obreros
            3) Salir
            ''')
            op1 = input('Opcion: ')
            if op1 in listop:
                if op1 == '1':
                    print('Rol administrativos')
                if op1 == '2':
                    print('Rol obreros')
            else:
                print('La opcion que ingreso no se encuentra disponible')
            input('Presione una tecla para continuar... ')
            os.system('cls')
    else:
        print('La opcion que ingreso no se encuentra disponible')
        time.sleep(2)
        os.system('cls')
    print('\t\t Menu Principal')
    print('1) Mantenimiento\n2) Novedades\n3) Rol de pago\n4) Salir')
    op = input('Opcion: ')
