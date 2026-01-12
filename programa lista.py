"""
Escribir un programa que gestione datos almacenados en una lista, de forma que muestre
un menú con las siguientes opciones:
"""
"""
El programa deberá pedir la información necesaria para cada opción elegida por el
usuario
"""

OPCIONES: str = """
1. Añadir un elemento a la lista.
2. Cambiar el valor de un elemento de la lista.
3. Eliminar un elemento de la lista.
4. Eliminar todos los elementos de la lista.
5. Mostrar los elementos de la lista.
0. Salir del programa.
"""


def imprimir_menú(opciones: str) -> None:
    """
    muestra un menú de opciones.

    Args:
        opciones (str): las opciones del menú
                        (una cadena multilinea).
    
    Returns:
        None.
    """
    print(opciones)
    
    
def pedir_entero(mensaje) -> int:
    """
    Pide un numero entero al usuario y lo devuelve.
    
    Args:
        Mensaje (str): El mensaje que se muestra al usuario.
        
    Returns:
        El entero que el usuario ha introducido.
    """
    while True:
        try:
            opc: int = int(input(mensaje))
            return opc
        except ValueError:
            print("El valor introducido no es válido")
            

def pedir_opcion() -> int:
    """
    Pide una opción del menú y la devuelve.
    
    Returns:
        El entero que es la opción elegida.
        """
    return pedir_entero("Introduzca un valor: ")
    

def anyadir(lst: list[str]) -> None:
    """
    Añade un elemento a la lista.
    El elemento a añadir se pide al usuario.
    
    Args:
        lst(list[str]: la lista en la que se va añadir el entero.
        
        Returns: None
        """
    valor = input("Introduzca un valor: ")
    lst.append(valor)


def pedir_posición(lst: list) -> int:
    """
    Pide al usuario un índice válido de entrada y lo devuelve.
    el índice devuelto debe estar comprendido entre 0 <= indice < len(lst)
    
    Args:
        lst(list[str]: la lista en la que se va añadir el entero.
    
    Returns:
        El entero que representa el índice introducido por el ususario.
    """
    while True:
        i = pedir_entero("Introduzca la posicion a cambiar: ")
        if i >= 0 and i < len(lst):
            return i
    print("la posición debe ser valida")
    

def cambiar(lst: list[str]) -> None:
    """
    Cambia un elemento de la lista, indicado por el usuario.
    
    tanto la posición del elemtno a cambiar como el nuevo valor serán
    introducidos por el usuario
    
    Args:
        lst(list[str]: la lista en la que se va a cambiar un elmento.
        
    Returns:
        None
    """
    
    
    if len(lst) == 0:
        print("no se puede cambiar una lista vacia")
        return
    i = pedir_posición(lst)
    nuevo = input("Introduzca el valor nuevo: ")
    lst[i] = nuevo


def mostrar(lst: list[str]) -> None:
    """Muestra una lista por la salida."""
    print(lst)
    
    
def es_vacia(lst: list) -> bool:
    """
    Comprueba si una lista es vacía, si esta vacía
    lo advierte al usuario por la salida.
    
    Args:
        lst(list): la lista.
        
    Returns:
        True si esta vacía, false si no lo está
        """
    if len(lst) == 0:
        print("No se puede cambiar o eliminar una lista vacia.")
        return True
    return False


def eliminar(lst: list[str]) -> None:
    """
    Elimina un elemento de la lista.
    
    La posicion a eliminar será la que concrete el usuario.
    
    Args:
        lst(list):la lista en la cual se quiere eliminar un elemento.
        
    Returns:
        None
    """
    if es_vacia(lst):
        return
    i = pedir_posición(lst)
    del lst[i]
    

def eliminar_todos(lst: list) -> None:
    """Elimina todos los elementos de la lista"""
    lst.clear()

# Programa príncipal:



def main():
    lista: list[str] = []

    while True:
        imprimir_menú(OPCIONES)
        opc: int = pedir_opcion() 


        if opc == 1:
            anyadir(lista)
        elif opc == 2:
            cambiar(lista)
        elif opc == 3:
            eliminar(lista)
        elif opc == 4:
            eliminar_todos(lista)
        elif opc == 5:
            mostrar(lista)
        else:
             break

main()