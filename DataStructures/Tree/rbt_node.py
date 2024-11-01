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
    
    if root["left"] != None and root["right"] != None:
    
        if root["left"]["color"] == "BLACK" and root["right"]["color"] == "RED":
            root = rotate_left(root)
        
        if root["left"]["left"] != None:
            if root["left"]["color"] == "RED" and root["left"]["left"]["color"] == "RED":
                root = rotate_right(root)
            
        if root["left"]["color"] == "RED" and root["right"]["color"] == "RED":
            root = flip_colors(root)
        
    return root