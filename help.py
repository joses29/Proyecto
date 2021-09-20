class Archivo:
    def __init__(self,nombreArchivo,separador='-'):
        self.__archivo = nombreArchivo
        self.__separador = separador

    def leer(self):
        try:
            with open(self.__archivo, 'r', encoding="utf-8") as file:
                lista = []
                for line in file.readlines():
                    line = line[:-1].split(self.__separador)
                    lista.append(line)
                if len(lista) != 0:
                    return lista
                else:
                    print('No hay datos compadre')
                    return lista
        except IOError as io:
            print(f'Error: Operacion Incorrecta {io}  ')

    def buscar(self,buscado):
        resultado = []
        with open(self.__archivo, mode = 'r', encoding='utf-8') as file:
            for linea in file.readlines():
                if linea[:-1].split(self.__separador)[0].find(buscado) is not -1 :
                    resultado = linea[:-1].split(self.__separador)
        return resultado

   #  def buscarRol(self,buscado1,buscado2):
   #      resultado = []
   #      with open(self.__archivo,mode='r',encoding='utf-8') as file:
   #          for linea in file:
   #              registro = linea[:-1].split(self.__separador)
   #              if registro[1] == buscado1 and registro[2] == buscado2:
   #                  resultado = registro
   #      return resultado

    def escribir(self,datos):
        with open(self.__archivo, mode='a', encoding='UTF-8') as file:
            file.write(f'\n{datos}')

# class Archivo:
#    def __init__(self,ah,sg):
#       self.__ah = ah 
#       self.__ah = sg 
       
# with open(r'./DATOS/departamento.txt',mode='r',encoding='utf-8') as file:
#    print(file.readlines())
#f  = open(r'./DATOS/departamento.txt','r')
#print(f.readlines())
a = Archivo(r'./DATOS/administrativo.txt','|')
# #a.escribir('4|deparatamento de los pijudos')
b = a.buscar('1')
print(b)
