from DataStructures.List import array_list as al

"""
  Estructura que contiene la información a guardar en una ``nodo`` de un árbol binario
"""


def new_node(key, value):
    """Estructura que contiene la información a guardar en un nodo de un árbol binario

    Se crea un nodo con los siguientes atributos:
    - **key**: Llave del nodo
    - **value**: Valor del nodo
    - **size**: Tamaño del nodo. Inicializado en 1
    - **left**: Hijo izquierdo del nodo. Inicializado en ``None``
    - **right**: Hijo derecho del nodo. Inicializado en ``None``
    - **type**: Tipo de árbol. Inicializado en "BST"

    :param key: Llave del nodo
    :type key: any
    :param value: Valor del nodo
    :type value: any

    :returns: Nodo creado
    :rtype: bst_node
    """
    node = {
        "key": key,
        "value": value,
        "size": 1,
        "left": None,
        "right": None,
        "type": "BST",
    }
    return node


def get_value(my_node):
    """Retorna el valor asociado a un nodo

    :param my_node: El nodo con la iformación
    :type my_node: bst_node

    :returns: El valor almacenado en el nodo
    :rtype: any
    """
    value = None
    if my_node is not None:
        value = my_node["value"]
    return value


def get_key(my_node):
    """Retorna la llave asociada a un nodo

    :param my_node: El nodo con la información
    :type my_node: bst_node

    :returns: La llave almacenada en el nodo
    :rtype: any
    """
    key = None
    if my_node is not None:
        key = my_node["key"]
    return key

def get_node(root,key):
    """Retorna el valor de la llave igual a key

    Parameters
    :
    root (bst_node) – La raiz del arbol

    key (any) – La llave asociada a la pareja a buscar

    Returns
    :
    El valor de la llave key. None en caso de no ser encontrada
    """

    if root is None:
        return None
    
    else:
    
        if get_key(root) == key:
            return get_value(root)
        
        elif key < get_key(root):
            nodo = get_node(root["left"], key)
            return get_value(nodo)
            
        elif key > get_key(root):
            nodo = get_node(root["right"], key)
            return get_value(nodo)
        
def insert_node(root, key, value):
    """Ingresa una pareja llave,valor. Si la llave ya existe, se reemplaza el valor.

    Es usada en la función put()

    Parameters
    :
    root (bst_node) – La raiz del arbol

    key (any) – La llave asociada a la pareja

    value (any) – El valor asociado a la pareja

    Returns
    :
    El arbol con la nueva pareja

    Return type
    :
    bst_node
    """
    
    if get_key(root) is None:
        root = new_node(key, value)
        
    elif get_key(root) == key:
        root["value"] = value
    
    elif key < get_key(root):
        root = insert_node(root["left"], key, value)
        
    elif key > get_key(root):
        root = insert_node(root["right"], key, value)
    
    
    
    if root["left"] is not None and root["right"] is not None:
        root["size"] = 1 + root["left"]["size"] + root["right"]["size"]
    if root["left"] is None and root["right"] is not None:
        root["size"] = 1 + root["right"]["size"]
    if root["right"] is None and root["left"] is not None:
        root["size"] = 1 + root["left"]["size"]
        
    return root

def contains_node(root, key):
    
    if root != None:
        
        if get_key(root) == key:
            return True
        elif key < get_key(root):
            return contains_node(root["left"], key)
        elif key > get_key(root):
            return contains_node(root["right"], key)
        else:
            return False
    else:
        return False

def left_key_node (root):
    
    """Retorna la llave mas a la izquierda de la tabla de simbolos

    Importante: Dependiendo de la definición de la función de comparación, 
                la llave más a la izquierda puede ser la menor o la mayor.

    Es usada en la función left_key() Usa la función left_key_node() 
    para encontrar la llave más a la izquierda

    Parameters
    :
    root (bst_node) – La raiz del arbol a examinar

    Returns
    :
    La llave más a la izquierda

    Return type
    :
    any
    """
    
    if root is None:
        return None
    
    if root["left"] is None:
        return get_key(root)
    
    else:
        return left_key_node(root["left"])
    
def right_key_node (root):
    
    """Retorna la llave mas a la derecha de la tabla de simbolos

    Importante: Dependiendo de la definición de la función de comparación, 
    la llave más a la derecha puede ser la menor o la mayor.

    Es usada en la función right_key() Usa la función right_key_node() 
    para encontrar la llave más a la derecha

    Parameters
    :
    root (bst_node) – La raiz del arbol a examinar

    Returns
    :
    La llave más a la derecha

    Return type
    :
    any
    """
    
    if root is None:
        return None
    
    elif root["right"] is None:
        return get_key(root)
    
    else:
        return right_key_node(root["right"])
    
def delete_left_tree (root):
    
    """Encuentra y remueve la llave mas a la izquierda de la 
    tabla de simbolos y su valor asociado

    Importante: Dependiendo de la definición de la función de comparación, 
    la llave más a la izquierda puede ser la menor o la mayor.

    Es usada en la función delete_left() Usa la función delete_left_tree() 
    para eliminar la llave más a la izquierda

    Parameters
    :
    root (bst_node) – La raiz del arbol a examinar

    Returns
    :
    Retorna la raiz del arbol sin la llave más a la izquierda

    Return type
    :
    bst_node
    """
    
    if root == None:
        return None
    
    else:
    
        if root["left"] is None:
            root = root["right"]
        
        elif root["left"] is not None:
            root = delete_left_tree(root["left"])
            root["size"] -= 1
        
        
        return root

def delete_right_tree (root):
    """Encuentra y remueve la llave mas a la derecha de la 
       tabla de simbolos y su valor asociado.

    Importante: Dependiendo de la definición de la función de comparación, 
    la llave más a la derecha puede ser la menor o la mayor.

    Es usada en la función delete_right() Usa la función 
    delete_right_tree() para eliminar la llave más a la derecha

    Parameters
    :
    root (bst_node) – La raiz del arbol a examinar

    Returns
    :
    Retorna la raiz del arbol sin la llave más a la derecha

    Return type
    :
    bst_node
    """
    
    if root == None:
        return None
    
    else:
    
        if root["right"] is None:
            root = root["left"]
        
        elif root["right"] is not None:
            root = delete_right_tree(root["right"])
            root["size"] -= 1
        
        return root
    
def inorder_tree (root, lst):
    """Recorrer el subárbol en Inorden desde el nodo root.
    Solución:
    1. Verificar que el nodo root sea válido.
    2. Aplicar recursión sobre el hijo izquierdo 
    3. Incluir el nodo raíz a la lista 
    4. Aplicar recursión sobre el hijo derecho 
    5. Retornar la lista resultante.
    """
    
    #node_list = al.new_list()
    
    if root != None:
        
        lst = inorder_tree(root["left"], lst)
            
        al.add_last(key_list, root)
        
        lst = inorder_tree(root["right"], lst)
        
    return lst
        