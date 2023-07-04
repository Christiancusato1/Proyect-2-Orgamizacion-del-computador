import re
from itertools import islice
from pathlib import Path

class Node:
    '''Nodo de un árbol binario, contiene un valor 'key' para el ordenamiento y una 'data'''
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key, data):
        '''Inserta un nodo en el árbol binario, según el valor 'key'''
        self.root = self.insertNode(self.root, key, data)

    def insertNode(self, node, key, data):
        '''De manera recursiva con el valor 'key' busca donde isnertar el nodo '''
        if node is None:
            return Node(key, data)

        if key < node.key:
            node.left = self.insertNode(node.left, key, data)
        elif key > node.key:
            node.right = self.insertNode(node.right, key, data)

        return node

    def search(self, key):
        '''Busca un nodo en el árbol binario, con el valor 'key'''
        return self.searchNode(self.root, key)

    def searchNode(self, node, key):
        '''De manera recursiva busca el nodo con el valor 'key' '''
        if node is None or node.key == key:
            return node

        if key < node.key:
            return self.searchNode(node.left, key)
        return self.searchNode(node.right, key)

    def delete(self, key):
        '''Elimina un nodo del árbol binario, con el valor 'key'''
        self.root = self.deleteNode(self.root, key)

    def deleteNode(self, node, key):
        '''De manera recursiva busca el nodo con el valor 'key' para eliminarlo '''
        if node is None:
            return node

        if key < node.key:
            node.left = self.deleteNode(node.left, key)
        elif key > node.key:
            node.right = self.deleteNode(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            successor = self.min(node.right)
            node.key = successor.key
            node.right = self.deleteNode(node.right, successor.key)

        return node
    
    def min(self, node):
        ''' Recorre el árbol por la izquierda para conseguir el nodo con el valor 'key' más pequeño '''
        current = node
        while current.left is not None:
            current = current.left
        return current

class AdminPinturas:
    def __init__(self):
        self.pinturas = []
        self.indexNombre = BinarySearchTree()
        self.indexCota = BinarySearchTree()
    
    def cargar_datos(self):
        ''' Lee el archivo pinturas.txt y construye las estructuras de datos correspondientes '''
        file_loc = Path("./pinturas.txt")
        with open(file_loc) as f:
            try:
                while True:
                    data =  islice(f, 0, 6)
                    cota = next(data).split(":")[1].strip()
                    nombre = next(data).split(":")[1].strip()
                    precio = next(data).split(":")[1].strip()
                    anio = next(data).split(":")[1].strip()
                    status = next(data).split(":")[1].strip()
                    next(data)
                
                    self.insertar(cota, nombre, precio, anio, status)
            except StopIteration:
                pass
    
    def guardar_datos(self):
        ''' Escribe en el archivo pinturas.txt '''
        file_loc = Path("./pinturas.txt")
        f = open(file_loc, "w")
        for pintura in self.pinturas:
            f.write("Cota: " + pintura.cota + "\n")
            f.write("Nombre: " + pintura.nombre + "\n")
            f.write("Precio: " + pintura.precio + "\n")
            f.write("Anio: " + pintura.anio + "\n")
            f.write("Status: " + pintura.status + "\n")
            f.write("\n")      
        
    def insertar(self, cota, nombre, precio, anio, status): 
        ''' Toma todos los datos de una pintura y crea una nueva y las añade a las estructuras de datos '''    
        nuevaPintura = Pintura(cota, nombre, precio, anio, status)
        self.pinturas.append(nuevaPintura)
        index = self.pinturas.index(nuevaPintura)
        
        self.indexCota.insert(cota, index)
        self.indexNombre.insert(nombre, index)
    
    def buscar_por_cota(self, cota):
        ''' Busca un nodo en el árbol binario con los índices según la cota '''   
        try:
            nodo = self.indexCota.search(cota)
            indice = nodo.data
            pintura = self.pinturas[indice]
            pintura.mostrar_datos()
        except:
            print('ERROR: Esta pintura no se encuentra registrada.')
        
    def buscar_por_nombre(self, nombre):
        ''' Busca un nodo en el árbol binario con los índices según el nombre '''   
        try:
            nodo = self.indexNombre.search(nombre)
            indice = nodo.data
            pintura = self.pinturas[indice]
            pintura.mostrar_datos()
        except:
            print('ERROR: Esta pintura no se encuentra registrada.')
    
    def mantenimiento_por_cota(self, cota):
        ''' Busca un nodo en el árbol binario con los índices según la cota y lo pone EN MANTENIMIETO '''   
        try:
            nodo = self.indexCota.search(cota)
            indice = nodo.data
            pintura = self.pinturas[indice]
            pintura.poner_en_mantenimiento()
        except:
            print('ERROR: Esta pintura no se encuentra registrada.')
            
    def mantenimiento_por_nombre(self, nombre):
        ''' Busca un nodo en el árbol binario con los índices según el nombre y lo pone EN MANTENIMIETO '''   
        try:
            nodo = self.indexNombre.search(nombre)
            indice = nodo.data
            pintura = self.pinturas[indice]
            pintura.poner_en_mantenimiento()
        except:
            print('ERROR: Esta pintura no se encuentra registrada.')
            
    def exhibicion_por_cota(self, cota):
        ''' Busca un nodo en el árbol binario con los índices según la cota y lo pone EN EXHIBICION'''   
        try:
            nodo = self.indexCota.search(cota)
            indice = nodo.data
            pintura = self.pinturas[indice]
            pintura.poner_en_exhibicion()
        except:
            print('ERROR: Esta pintura no se encuentra registrada.')
            
    def exhibicion_por_nombre(self, nombre):
        ''' Busca un nodo en el árbol binario con los índices según el nombre y lo pone EN EXHIBICION'''   
        try:
            nodo = self.indexNombre.search(nombre)
            indice = nodo.data
            pintura = self.pinturas[indice]
            pintura.poner_en_exhibicion()
        except:
            print('ERROR: Esta pintura no se encuentra registrada.')
    
    def eliminar_por_cota(self, cota):
        ''' Busca un nodo en el árbol binario con los índices según la cota y lo marca como eliminado'''   
        try:
            nodo = self.indexCota.search(cota)
            indice = nodo.data
            pintura = self.pinturas[indice]
            pintura.eliminar()
        except:
            print('ERROR: Esta pintura no se encuentra registrada.')
            
    def eliminar_por_nombre(self, nombre):
        ''' Busca un nodo en el árbol binario con los índices según el nombre y lo marca como eliminado'''   
        try:
            nodo = self.indexNombre.search(nombre)
            indice = nodo.data
            pintura = self.pinturas[indice]
            pintura.eliminar()
        except:
            print('ERROR: Esta pintura no se encuentra registrada.')
    
    def eliminar_definitivamente(self):
        ''' Busca en el arreglo de pinturas las que fueron marcadas como eliminadas y las borra de todas las estrcutras de datos'''   
        for pintura in self.pinturas:
            if pintura.eliminada == True:
                self.indexCota.delete(pintura.cota)
                self.indexNombre.delete(pintura.nombre)
                self.pinturas.remove(pintura)               
                
        print('Las pinturas eliminadas fueron borradas definitivamente.')
    
    def validar_cota(self, cota):
        ''' Valida la estructura de la cota y que sea única '''   
        regex = "^\w{4}[0-9]{4}$"
        if not re.match(regex, cota):
            print("ERROR: El código debe contener 4 letras y 4 dígitos.")
            return False
        elif self.indexCota.search(cota) is not None:
            print("ERROR: Ya existe una obra registrada con este código.")
            return False
        return True
    
    def validar_nombre(self, nombre):
        ''' Valida la longitud del nombre y que sea único '''   
        if len(nombre) > 10:
            print("ERROR: El nombre no puede exceder de 10 carácteres.")
            return False
        elif self.indexNombre.search(nombre) is not None:
            print("ERROR: Ya existe una obra registrada con este nombre.")
            return False
        return True
    
    def validar_precio(self, precio):
        ''' Valida que el precio sea un flotante y que sea mayor a 0 '''   
        precio = precio.replace(",", ".")
        try:
            precio = float(precio)
            if(precio <= 0.0):
                print("ERROR: El precio debe ser un valor positivo.")
                return False
            
            return True
        except:
            print("ERROR: El precio debe ser un número real.")
            return False
    
    def validar_status(self, status):
        ''' Valida que el status sea 1 o 2 '''   
        if(status in {"1", "2"}):
            return True
        print("ERROR: Opción inválida, marque '1' o '2.")
        return False
    
    def ejecutar(self):
        ''' Ciclo de ejecución principal del programa, imprime el menú en cada iteración'''   
        self.cargar_datos()
        print("Gestión de Pinturas para la Galeria de Arte Nacional")
        while(True):
            opcion = input(
                "\n1. Insertar una pintura\n"
                "2. Consultar pintura\n"
                "3. Poner en mantenimiento\n"
                "4. Poner en exhibición\n"
                "5. Eliminar pintura\n"
                "6. Compactar\n"
                "7. Salir\n\n"
                
                "Por favor ingrese su opcion: "
            )
            
            if(opcion == "1"):
                print("\nIngrese los siguientes datos de la pintura: ")
                
                cota_valida = False
                while(cota_valida is False):
                    cota = input("Cota: ").strip().upper()
                    cota_valida = self.validar_cota(cota)
                
                nombre_valido = False
                while(nombre_valido is False):
                    nombre = input("Nombre: ").strip().upper() 
                    nombre_valido = self.validar_nombre(nombre)  
                
                precio_valido = False
                while(precio_valido is False):
                    precio = input("Precio: ")
                    precio_valido = self.validar_precio(precio)   
                    
                anio = input("Año: ")
                
                status_valido = False
                while(status_valido is False):
                    status = input("Status (Escriba '1' para poner el status 'EN MANTENIMIENTO' o '2' para poner 'EN EXHIBICION'): ")
                    status_valido = self.validar_status(status)
                    
                if(status == "1"):
                    status = "EN MANTENIMIENTO"
                else: 
                    status = "EN EXHIBICION"
                          
                self.insertar(cota, nombre, precio, anio, status)
                print("La pintura fue registrada exitosamente!")
                
            elif(opcion == "2"):
                busqueda = input("\nSeleccione una opción para buscar la pintura: \n1. Por cota \n2. Por nombre \n\nOpción: ")
                if(busqueda == "1"):
                    cota = input("Ingrese la cota: ").upper()
                    self.buscar_por_cota(cota)
                elif(busqueda == "2"):
                    nombre = input("Ingrese el nombre: ").upper()
                    self.buscar_por_nombre(nombre)
                else:
                    print("Opción inválida")

            elif(opcion == "3"):
                busqueda = input("\nSeleccione una opción para poner la pintura en mantenimiento: \n1. Por cota \n2. Por nombre \n\nOpción: ")
                if(busqueda == "1"):
                    cota = input("Ingrese la cota: ").upper()
                    self.mantenimiento_por_cota(cota)
                elif(busqueda == "2"):
                    nombre = input("Ingrese el nombre: ").upper()
                    self.mantenimiento_por_nombre(nombre)
                else:
                    print("Opción inválida")
            
            elif(opcion == "4"):
                busqueda = input("\nSeleccione una opción para poner la pintura en exhibición: \n1. Por cota \n2. Por nombre \n\nOpción: ")
                if(busqueda == "1"):
                    cota = input("Ingrese la cota: ").upper()
                    self.exhibicion_por_cota(cota)
                elif(busqueda == "2"):
                    nombre = input("Ingrese el nombre: ").upper()
                    self.exhibicion_por_nombre(nombre)
                else:
                    print("Opción inválida")
                    
            elif(opcion == "5"):
                busqueda = input("\nSeleccione una opción para eliminar lógicamente la pintura: \n1. Por cota \n2. Por nombre \n\nOpción: ")
                if(busqueda == "1"):
                    cota = input("Ingrese la cota: ").upper()
                    self.eliminar_por_cota(cota)
                elif(busqueda == "2"):
                    nombre = input("Ingrese el nombre: ").upper()
                    self.eliminar_por_nombre(nombre)
                else:
                    print("Opción inválida")
            elif(opcion == "6"):
                self.eliminar_definitivamente()
                
            elif(opcion == "7"):
                self.guardar_datos()
                print("Los datos de las pinturas han sido actualizados en disco")
                break
            
            else:
                print("Opción inválida")

class Pintura:
    def __init__(self, cota, nombre, precio, anio, status):
        self.cota = cota
        self.nombre = nombre
        self.precio = precio
        self.anio = anio
        self.status = status
        self.eliminada = False
    
    def mostrar_datos(self):
        ''' Imprime los datos de una pintura si no esta marcada como eliminada '''   
        if(self.eliminada == False):
            print("\nLos datos de la pintura registrada son: \nCota: {cota}\nNombre: {nombre}\nPrecio: {precio}\nAño: {anio}\nStatus: {status}".format(
                        cota=self.cota, nombre=self.nombre, precio=self.precio, anio=self.anio, status=self.status
            ))
        else: 
            print('ERROR: Esta pintura no se encuentra registrada.')
            
    def poner_en_mantenimiento(self):
        ''' Marca a una pintura EN MANTENIMIENTO si no esta marcada como eliminada'''   
        if(self.eliminada == False):
            if(self.status == "EN EXHIBICION"):
                self.status = "EN MANTENIMIENTO"
                print("La pintura fue puesta en mantemiento.")
            else:
                print("La pintura ya se encuentra en mantenimiento.")
        else:
            print('ERROR: Esta pintura no se encuentra registrada.')
    
    def poner_en_exhibicion(self):
        ''' Marca a una pintura EN EXHIBICION si no esta marcada como eliminada'''  
        if(self.eliminada == False):
            if(self.status == "EN MANTENIMIENTO"):
                self.status = "EN EXHIBICION"
                print("La pintura fue puesta en exhibición.")
            else:
                print("La pintura ya se encuentra en exhibición.")
        else:
            print('ERROR: Esta pintura no se encuentra registrada.')
            
    def eliminar(self):
        ''' Marca a una pintura como eliminada'''  
        if(self.eliminada == False):
            self.eliminada = True
            print("La pintura fue eliminada.")
        else:
            print('ERROR: Esta pintura no se encuentra registrada.')
        
def main():
    admin = AdminPinturas()
    admin.ejecutar()

if __name__ == "__main__":
    main()