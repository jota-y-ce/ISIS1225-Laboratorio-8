from DataStructures.Tree import bst_node as bst

def new_map():
    """Crea una tabla de simbolos ordenada basada en un árbol binario de búsqueda (BST) vacía

    Se crea una tabla de símbolos ordenada con los siguientes atributos:

    root: Raíz del árbol. Inicializado en None

    type: Tipo de árbol. Inicializado en “BST”

    Returns
    :
    La tabla de símbolos ordenada sin elementos

    Return type
    :
    binary_search_tree
    """
    mapa = {'root': None,
     'type': "BST"}
    return mapa

def get(my_bst, key):
    """Retorna el valor con llave igual a key

    Usa la función get_node() para buscar la llave en el arbol

    Parameters
    :
    my_bst (binary_search_tree) – El arbol de búsqueda

    key (any) – La llave asociada a la pareja

    Returns
    :
    La pareja el valor de la llave key. None en caso de no ser encontrada

    Return type
    :
    any
    """
    return bst.get_node(my_bst["root"], key)

def put(my_bst, key, value):
    """Ingresa una pareja llave,valor. Si la llave ya existe, se reemplaza el valor.

    Parameters
    :
    my_bst (binary_search_tree) – El BST

    key (any) – La llave asociada a la pareja

    value (any) – El valor asociado a la pareja

    Returns
    :
    El arbol con la nueva pareja

    Return type
    :
    binary_search_tree
    """
    my_bst["root"] = bst.insert_node(my_bst["root"], key, value)
    return my_bst

def contains(my_bst, key):
    """Informa si la llave key se encuentra en la tabla de hash.

    Usa la función get() para buscar la llave en el arbol

    Parameters
    :
    my_bst (binary_search_tree) – El arbol de búsqueda

    key (any) – La llave a buscar

    Returns
    :
    True si la llave está presente, False en caso contrario

    Return type
    :
    bool
    """
    return bst.contains_node(my_bst["root"], key)

def size(my_bst):
    """Retorna el número de entradas en la tabla de simbolos

    Usa la función size_tree() para contar el número de elementos

    Parameters
    :
    my_bst (binary_search_tree) – El arbol de búsqueda

    Returns
    :
    El número de elementos en la tabla

    Return type
    :
    int
    """
    if my_bst["root"] is None:
        my_bst["root"]["size"] = 0
    else:
        my_bst["root"]["size"]
        
    return my_bst["root"]["size"]

def is_empty(my_bst):
    """Informa si la tabla de simbolos se encuentra vacia.

    Parameters
    :
    my_bst (binary_search_tree) – El arbol de búsqueda

    Returns
    :
    True si la tabla es vacía, False en caso contrario

    Return type
    :
    bool
    """
    
    if my_bst["root"] is None:
        return True
    else:
        return False
    
