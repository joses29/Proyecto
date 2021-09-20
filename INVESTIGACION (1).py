# def mostrarCabeceraNomina(self,razonSocial,direccion,telefono,ruc,tipoROl):
#     borrarPantalla()
#     print(' {}             Ruc :   {}             Teléfono:   {}         Dirección :  {}'.format(razonSocial,ruc,telefono,direccion))
#     print('************************************************************************************************************************************')
#     print('FECHA:  {}    N O M I N A     D E    P A G O     D E      E M P L E A D O S:  {} '.format(self.fecha,tipoRol))
#     print('Nomina correspondiente al Periodo: {}'.format(self.aamm))
#     print('--'*59)
#     print(""*5,"E M P L E A D O S"," "*30,"I N G R E S O S ",""*22,"E G R E S O S")
#     print("Nombre     Cargo        Departamento     Sueldo    Sobretiempo    Antiguedad  Comision  TotIng   Iess    Prestamo   TotDes   Neto")
#
#
# def mostrarDetalleNomina(self):
#     fila = 8
#     for det in sel.detalleNomina:
#         archiCargo = Archivo("./archivos/cargo.txt","|")
#         cargo = archiCargo.buscar(det[1])
#         if cargo: desCargo = cargo[1]
#         else : desCargo = "Sin Cargo"
#         archiDpto = Archivo("/archivos/departamento.txt","|")
#         dpto = archiDpto.buscar(det[2])
#         if dpto: desDpto = dpto[1]
#         else : desDpto = "Sin Departamento"
#         gotoxy(1,fila);print(det[0],end="")
#         gotoxy(10, fila);print(desCargo, end="")
#         gotoxy(25, fila);print(desDpto, end="")
#         gotoxy(43, fila);print(det[3], end="")
#         gotoxy(53, fila);print(det[4], end="")
#         gotoxy(67, fila);print(det[5], end="")
#         gotoxy(78, fila);print(det[6], end="")
#         gotoxy(86, fila);print(det[7], end="")
#         gotoxy(95, fila);print(det[8], end="")
#         gotoxy(104, fila);print(det[9], end="")
#         gotoxy(114, fila);print(det[10], end="")
#         gotoxy(122, fila);print(det[11], end="")
#         fila+=1

class Nomina:
    def __init__(self,fecha,aamm):
        self.aamm = aamm
        self.fecha = fecha
        self.totIngresos = 0
        self.totPagoNeto = 0
        self.detalleNomina = []

    @property
    def id(self):
        return self.__id

    def calcularNominaDetalle(self,empleado,deduccion):
        detalle = DetalleNomina(empleado)
        rubrosIngresos = detalle.calculoRubrosIngresos(self.aamm,deduccion)
        rubrosEgresos = detalle.calcularRubrosEgresos(self.aamm,deduccion)
        self.totIngresos += detalle.totIng
        self.totDescuentos += detalle.totDes
        self.totPagoNeto += detalle.totLiq
        self.detalleNomina.append([
            empleado.id,empleado.cargo.departamento,
            str(rubrosIngresos[0]),str(rubrosIngresos[1]),str(rubrosIngresos[2]),str(rubrosIngresos[3]),str(rubrosIngresos[4]),
            str(rubrosEgresos[0]),str(rubrosEgresos[1]),str(rubrosEgresos[2]),str(rubrosEgresos[3])

        ])
    def getNomina(self):
        return[self.aamm,str(self.fecha),str(self.totIngresos),str(self.totDescuentos),str(self.totPagoNeto)]

    def getDetalle(self):
        return self.detalleNomina

    def mostrarCabeceraNomina(self, razonSocial, direccion, telefono, ruc, tipoROl):
        borrarPantalla()
        print(' {}             Ruc :   {}             Teléfono:   {}         Dirección :  {}'.format(razonSocial, ruc,
                                                                                                     telefono,
                                                                                                     direccion))
        print(
            '************************************************************************************************************************************')
        print('FECHA:  {}    N O M I N A     D E    P A G O     D E      E M P L E A D O S:  {} '.format(self.fecha,
                                                                                                         tipoRol))
        print('Nomina correspondiente al Periodo: {}'.format(self.aamm))
        print('--' * 59)
        print("" * 5, "E M P L E A D O S", " " * 30, "I N G R E S O S ", "" * 22, "E G R E S O S")
        print(
            "Nombre     Cargo        Departamento     Sueldo    Sobretiempo    Antiguedad  Comision  TotIng   Iess    Prestamo   TotDes   Neto")

    def mostrarDetalleNomina(self):
        fila = 8
        for det in sel.detalleNomina:
            archiCargo = Archivo("./archivos/cargo.txt", "|")
            cargo = archiCargo.buscar(det[1])
            if cargo:
                desCargo = cargo[1]
            else:
                desCargo = "Sin Cargo"
            archiDpto = Archivo("/archivos/departamento.txt", "|")
            dpto = archiDpto.buscar(det[2])
            if dpto:
                desDpto = dpto[1]
            else:
                desDpto = "Sin Departamento"
            gotoxy(1, fila);print(det[0], end="")
            gotoxy(10, fila);print(desCargo, end="")
            gotoxy(25, fila);print(desDpto, end="")
            gotoxy(43, fila);print(det[3], end="")
            gotoxy(53, fila);print(det[4], end="")
            gotoxy(67, fila);print(det[5], end="")
            gotoxy(78, fila);print(det[6], end="")
            gotoxy(86, fila);print(det[7], end="")
            gotoxy(95, fila);print(det[8], end="")
            gotoxy(104, fila);print(det[9], end="")
            gotoxy(114, fila);print(det[10], end="")
            gotoxy(122, fila);print(det[11], end="")
            fila += 1

class DetalleNomina(CalculoRo1):
    secuecia = 0
    def __init__(self,empleado):
        DetalleNomina.secuencia += 1
        self.__id = DetalleNomina.secuencia
        self.empleado = empleado
        self.totIng=0
        self.totDes=0
        self.totLiq=9
    def getSueldo(self):
        return self.empleado.sueldo

    def getSobretiempo(self,aamm):
        calSob = 0
        if self.empleado.id[0]=="0":
            calSob = 20 #ir a sobre tiempo h50 y h100 y realizar calculo
        return 0

    def getAntiguedad(self,deduccion):
        calAnt = 0
        if self.empleado.id[0] == "0":
            calAnt = 20 #Trae antiguedad de deducciones y realizar calculo
            return calAnt

    def getComision(self,deduccion):
        calCom = 0
        if self.empleado.id[0]=="A":
            calCom = round(self.empleado.sueldo*deduccion.getComision(),2)
        return

    def getIess(self,deduccion):
        return round(self.empleado.sueldo*deduccion.getIess(),2)

    def getPrestamo(self,aamm):
        archiPrestamo = Archivo("./archivos/prestamo.txt","|")
        prestamo = archiPrestamo.buscar2(self.empleado.id,aamm)
        if prestamo:
            entPrestamo = Prestamo(prestamo[1],prestamo[2],float(prestamo[3]), int(prestamo[4]),float(prestamo[5]))
            return round(entPrestamo.valor/entPrestamo.numPago,2)
        else: return 0

    def calculoRubrosIngresos(self, aamm,deduccion):
        ingresos = []
        ingresos.append(self.getSueldo())
        ingresos.append(self.getSobretiempo(aamm))
        ingresos.append(self.getAntiguedad(deduccion))
        ingresos.append(self.getComision(deduccion))
        for valor in ingresos:
            self.totIng += valor
        ingresos.append(self.totIng)
        return ingresos

    def calcularRubrosEgresos(self,aamm,deduccion):
        descuentos = []
        descuentos.append(self.getIess(deduccion))
        descuentos.append(self.getPrestamo(aamm))
        for valor in descuentos:
            self.totDes += valor
        self.totLiq = round(self.totIng - self.totDes,2)
        descuentos.append(self.totDes)
        descuentos.append(self.totLiq)
        return descuentos

class Prestamo:
    def __init__(self,empleado, aamm, valor, numPagos , saldo, estado= True,id=1):
        self.__id = id
        self.empleado=empleado
        self.aamm = aamm
        self.valor = valor
        self.numPagos = numPagos
        self.cuota = valor/numPagos
        self.saldo = saldo
        self.estado = estado

    @property
    def id(self):
        return self.__id

    def mostrarSobretiempo(self):
        return round(self.empleado.valorHora()+(self.h50*1.5+self.h100*2),2)

    def mostrarSobretiempo(self):
        print('''{}ª Sobretiempo realizado: {}
          -Empleado= {}
          -H50 = {}
          -H100 = {}
          -Valor = {:.2f}
          -Estado = {}'''.format(self.id,self.aamm,self.empleado,self.nombre,self.h50,self.h100,self.valor,self.estado))

    def getSobretiempo(self):
        return [str(self.id),str(self.empleado.id),self.aamm,str(self.h50),str(self.h100),str(self.valor),str(self.estado)]


class CalculoRol(ABC):
    @abstractmethod
    def getSueldo(self):
        pass
    @abstractmethod
    def getSobretiempo(self,aamm):
        pass
    @abstractmethod
    def getComision(self,deduccion):
        pass
    @abstractmethod
    def getAntiguedad(self,deduccion):
        pass
    @abstractmethod
    def getIess(self,deduccion):
        pass
    @abstractmethod
    def getPrestamo(self,aamm):
        pass