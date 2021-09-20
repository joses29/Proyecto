from time import time
#from crudArchivos import Archivo
from datetime import date
from abc import ABC,abstractmethod
from help import Archivo
import os,time
class Empresa:
    def __init__(self,dir,tlf,rs,ruc):
        self.dir = dir # direccion
        self.tlf = tlf # telefono
        self.rs = rs # razon social
        self.ruc = ruc # ruc
        data = str(self.dir)+'|'+str(self.tlf)+'|'+str(self.rs)+'|'+str(self.ruc)
        emp = Archivo('./DATOS/empresa.txt','|')
        emp.escribir(data)
    def mostrarempresa(self):
        print(f''' {self.rs}
        -Ruc : {self.ruc}
        -Direccion : {self.dir}
        -Teléfono : {self.tlf}''')

class Departamento:
    def __init__(self,desp,id = 1):
        self.__id = id # id
        self.desp = desp # descripcion
        data = str(id)+'|'+str(self.desp)
        depar = Archivo('./DATOS/departamento.txt','|')
        depar.escribir(data)   
    @property
    def id(self):
        return self.__id
    def mostrardepartamento(self):
        print(f'{self.id} .Departamento de {self.desp}')

class Cargo:
    def __init__(self,desp,id=1):
        self.__id = id # id
        self.desp = desp # descripcion
        data = str(id)+'|'+str(self.desp)
        cargo = Archivo('./DATOS/cargo.txt','|')
        cargo.escribir(data)   
    @property
    def id(self):
        return self.__id
    def mostrarcargo(self):
        print(f'{self.id} .Cargo de {self.desp}')
    def getcargo(self):
        return [str(self.id),self.desp]

class Empleado:
    def __init__(self,id,nom,dep,cg,sl,fi,dir,tl,cedula):
        self.__id = id  # id
        self.nom = nom # nombre
        self.dep = dep
        self.cg = cg
        self.dir = dir
        self.ci = cedula # cedula
        self.tl = tl
        self.fi = fi # fecha de ingreso
        self.sl = sl # sueldo
    @property
    def id(self):
        return self.__id
    @abstractmethod
    def valorhora(self):
        return self.sl/240
    def MostrarEmpleado(self):
        print(f'''
        - Empleado: {self.nom}
        - Cedula: {self.ci}
        - Direccion: {self.dir}
        - Cargo: {self.cg}
        - Departamento: {self.dep}
        ''')
class Administrativo(Empleado):
    def __init__(self,id,nom,dep,cg,sl,fi,dir,tl,cedula,com = True):
        super().__init__(id,nom,dep,cg,sl,fi,dir,tl,cedula)
        self.com = com # comision
        id = self.id
        data = str(id)+'|'+str(self.nom)+'|'+str(self.dep)+'|'+str(self.cg)+'|'+\
        str(self.sl)+'|'+str(self.fi)+'|'+str(self.dir)+'|'+str(self.tl)+'|'+str(self.ci)+'|'+str(self.com)
        adm = Archivo('./DATOS/administrativo.txt','|')
        adm.escribir(data)
        
    def MostrarEmpleado(self):
        print(f'''
        - Administrativo: {self.nom}
        - Cedula: {self.ci}
        - Direccion: {self.dir}
        - Cargo: {self.cg.desp}
        - Departamento: {self.dep.desp}
        - Comision: {self.com}
        ''')
    def valorhora(self):
        return super().valorhora()
    def getempleado(self):
        return [self.id,self.nom,str(self.dep.id),str(self.cg.id),
        self.dir,self.ci,self.tl,str(self.fi),str(self.sl),str(self.com)]

class Obrero(Empleado):
    def __init__(self,id,nom,dep,cg,sl,fi,dir,tl,cedula,cc = True):
        super().__init__(id,nom,dep,cg,sl,fi,dir,tl,cedula)
        self.cc = cc # contrato colectivo
        id = self.id
        data = str(id)+'|'+str(self.nom)+'|'+str(self.dep)+'|'+str(self.cg)+'|'+\
        str(self.sl)+'|'+str(self.fi)+'|'+str(self.dir)+'|'+str(self.tl)+'|'+str(self.ci)+'|'+str(self.cc)
        ob = Archivo('./DATOS/obrero.txt','|')
        ob.escribir(data)   
    def MostrarEmpleado(self):
        print(f'''
        - Obrero: {self.nom}
        - Cedula: {self.ci}
        - Direccion: {self.dir}
        - Cargo: {self.cg.desp}
        - Departamento: {self.dep.desp}
        - Contrato colectivo: {self.cc}
        ''')
    def valorhora(self):
        return super().valorhora()
    def getempleado(self):
        return [self.id,self.nom,str(self.dep.id),str(self.cg.id),
        self.dir,self.ci,self.tl,str(self.fi),str(self.sl),str(self.cc)]

class Deduccion:
    def __init__(self,iess,com,ant):
        self.__iess = iess
        self.__com = com
        self.__ant = ant
    def get_Iess(self):
        return round(self.__iess/100,4)
    def get_comision(self):
        return round(self.__com/100,2)
    def get_antiguedad(self):
        return round(self.__ant/100,2)
    def mostrardeduccion(self):
        print(f'''
        - Valor iess {self.__iess}
        - Valor comision {self.__com}
        - Valor antiguedad {self.__ant}
        ''')
    def getdeduccion(self):
        return [str(self.__iess),str(self.__com),str(self.__ant)]

# class Nomina:
#     def __init__(self,fecha,aamm):
#         self.aamm = aamm
#         self.fecha = fecha
#         self.totIngresos = 0
#         self.totPagoNeto = 0
#         self.detalleNomina = []

#     @property
#     def id(self):
#         return self.__id

#     def calcularNominaDetalle(self,empleado,deduccion):
#         detalle = DetalleNomina(empleado)
#         rubrosIngresos = detalle.calculoRubrosIngresos(self.aamm,deduccion)
#         rubrosEgresos = detalle.calcularRubrosEgresos(self.aamm,deduccion)
#         self.totIngresos += detalle.totIng
#         self.totDescuentos += detalle.totDes
#         self.totPagoNeto += detalle.totLiq
#         self.detalleNomina.append([
#             empleado.id,empleado.cargo.departamento,
#             str(rubrosIngresos[0]),str(rubrosIngresos[1]),str(rubrosIngresos[2]),str(rubrosIngresos[3]),str(rubrosIngresos[4]),
#             str(rubrosEgresos[0]),str(rubrosEgresos[1]),str(rubrosEgresos[2]),str(rubrosEgresos[3])

#         ])
#     def getNomina(self):
#         return[self.aamm,str(self.fecha),str(self.totIngresos),str(self.totDescuentos),str(self.totPagoNeto)]

#     def getDetalle(self):
#         return self.detalleNomina

#     def mostrarCabeceraNomina(self, razonSocial, direccion, telefono, ruc, tipoROl):
#         os.system('cls')
#         print(' {}             Ruc :   {}             Teléfono:   {}         Dirección :  {}'.format(razonSocial, ruc,
#                                                                                                      telefono,
#                                                                                                      direccion))
#         print(
#             '************************************************************************************************************************************')
#         print('FECHA:  {}    N O M I N A     D E    P A G O     D E      E M P L E A D O S:  {} '.format(self.fecha,
#                                                                                                          #tipoRol))
#         print('Nomina correspondiente al Periodo: {}'.format(self.aamm))
#         print('--' * 59)
#         print("" * 5, "E M P L E A D O S", " " * 30, "I N G R E S O S ", "" * 22, "E G R E S O S")
#         print(
#             "Nombre     Cargo        Departamento     Sueldo    Sobretiempo    Antiguedad  Comision  TotIng   Iess    Prestamo   TotDes   Neto")

#     def mostrarDetalleNomina(self):
#         fila = 8
#         for det in self.detalleNomina:
#             archiCargo = Archivo("./archivos/cargo.txt", "|")
#             cargo = archiCargo.buscar(det[1])
#             if cargo:
#                 desCargo = cargo[1]
#             else:
#                 desCargo = "Sin Cargo"
#             archiDpto = Archivo("/archivos/departamento.txt", "|")
#             dpto = archiDpto.buscar(det[2])
#             if dpto:
#                 desDpto = dpto[1]
#             else:
#                 desDpto = "Sin Departamento"
#             print(det[0], end="")
#             print(desCargo, end="")
#             gotoxy(25, fila);print(desDpto, end="")
#             gotoxy(43, fila);print(det[3], end="")
#             gotoxy(53, fila);print(det[4], end="")
#             gotoxy(67, fila);print(det[5], end="")
#             gotoxy(78, fila);print(det[6], end="")
#             gotoxy(86, fila);print(det[7], end="")
#             gotoxy(95, fila);print(det[8], end="")
#             gotoxy(104, fila);print(det[9], end="")
#             gotoxy(114, fila);print(det[10], end="")
#             gotoxy(122, fila);print(det[11], end="")
#             fila += 1

# class DetalleNomina(CalculoRo1):
#     secuecia = 0
#     def __init__(self,empleado):
#         DetalleNomina.secuencia += 1
#         self.__id = DetalleNomina.secuencia
#         self.empleado = empleado
#         self.totIng=0
#         self.totDes=0
#         self.totLiq=9
#     def getSueldo(self):
#         return self.empleado.sueldo

#     def getSobretiempo(self,aamm):
#         calSob = 0
#         if self.empleado.id[0]=="0":
#             calSob = 20 #ir a sobre tiempo h50 y h100 y realizar calculo
#         return 0

#     def getAntiguedad(self,deduccion):
#         calAnt = 0
#         if self.empleado.id[0] == "0":
#             calAnt = 20 #Trae antiguedad de deducciones y realizar calculo
#             return calAnt

#     def getComision(self,deduccion):
#         calCom = 0
#         if self.empleado.id[0]=="A":
#             calCom = round(self.empleado.sueldo*deduccion.getComision(),2)
#         return

#     def getIess(self,deduccion):
#         return round(self.empleado.sueldo*deduccion.getIess(),2)

#     def getPrestamo(self,aamm):
#         archiPrestamo = Archivo("./archivos/prestamo.txt","|")
#         prestamo = archiPrestamo.buscar2(self.empleado.id,aamm)
#         if prestamo:
#             entPrestamo = Prestamo(prestamo[1],prestamo[2],float(prestamo[3]), int(prestamo[4]),float(prestamo[5]))
#             return round(entPrestamo.valor/entPrestamo.numPago,2)
#         else: return 0

#     def calculoRubrosIngresos(self, aamm,deduccion):
#         ingresos = []
#         ingresos.append(self.getSueldo())
#         ingresos.append(self.getSobretiempo(aamm))
#         ingresos.append(self.getAntiguedad(deduccion))
#         ingresos.append(self.getComision(deduccion))
#         for valor in ingresos:
#             self.totIng += valor
#         ingresos.append(self.totIng)
#         return ingresos

#     def calcularRubrosEgresos(self,aamm,deduccion):
#         descuentos = []
#         descuentos.append(self.getIess(deduccion))
#         descuentos.append(self.getPrestamo(aamm))
#         for valor in descuentos:
#             self.totDes += valor
#         self.totLiq = round(self.totIng - self.totDes,2)
#         descuentos.append(self.totDes)
#         descuentos.append(self.totLiq)
#         return descuentos

# class Prestamo:
#     def __init__(self,empleado, aamm, valor, numPagos , saldo, estado= True,id=1):
#         self.__id = id
#         self.empleado=empleado
#         self.aamm = aamm
#         self.valor = valor
#         self.numPagos = numPagos
#         self.cuota = valor/numPagos
#         self.saldo = saldo
#         self.estado = estado

#     @property
#     def id(self):
#         return self.__id

#     def mostrarSobretiempo(self):
#         return round(self.empleado.valorHora()+(self.h50*1.5+self.h100*2),2)

#     def mostrarSobretiempo(self):
#         print('''{}ª Sobretiempo realizado: {}
#           -Empleado= {}
#           -H50 = {}
#           -H100 = {}
#           -Valor = {:.2f}
#           -Estado = {}'''.format(self.id,self.aamm,self.empleado,self.nombre,self.h50,self.h100,self.valor,self.estado))

#     def getSobretiempo(self):
#         return [str(self.id),str(self.empleado.id),self.aamm,str(self.h50),str(self.h100),str(self.valor),str(self.estado)]


# class CalculoRol(ABC):
#     @abstractmethod
#     def getSueldo(self):
#         pass
#     @abstractmethod
#     def getSobretiempo(self,aamm):
#         pass
#     @abstractmethod
#     def getComision(self,deduccion):
#         pass
#     @abstractmethod
#     def getAntiguedad(self,deduccion):
#         pass
#     @abstractmethod
#     def getIess(self,deduccion):
#         pass
#     @abstractmethod
#     def getPrestamo(self,aamm):
#         pass

def sobretiempo():
    print("INGRESO DE LAS HORAS EXTRAS")


def sobretiempos():
    print("INGRESO DE LAS HORAS EXTRAS")
    empleado,entEmpleado = [],None
    aamm,h50,h100=0,0,0
    while not empleado:
        id = input("Empleado ID[    ]:").upper()
        archiEmpleado = Archivo("./DATOS/obrero.txt", "|")
        empleado = archiEmpleado.buscar(id)
        if empleado:
            entEmpleado = Obrero(empleado[1],empleado[2],empleado[3],empleado[4],empleado[5])
            print(entEmpleado.nom)
        else:
            print("No existe empleado con ese codigo [{}]".format(id))
            time.sleep(2);print(" "*40)
    print("Periodo[] ")
    h50 = input("Horas50")
    h100 = input("Horas100")
    print("Estas seguro de Grabar el registro(s/n)")
    grabar = input().lower()
    if grabar == "s":
        archiSobretiempo = Archivo("./DATOS/sobretiempo.txt","|")
        sobretiempos = archiSobretiempo.leer()
        if sobretiempo : idSig = int(sobretiempos[-1][0])+1
        else : idSig = 1
        datos = sobretiempo.getSobretiempo
        datos = '|'.join(datos)
        archiSobretiempo.escribir([datos],"a")
        input("Registro Grabado Sastifactoriamente/n Precione una tecla para continuar")
    else:
        input("Registro No fue grabado/n Precione una tecla para continuar")