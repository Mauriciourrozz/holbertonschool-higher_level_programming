def new_in_list(my_list, idx, element):
    nueva_lista = list(my_list)
    if idx < 0 and idx >= len(my_list):
        return my_list
    nueva_lista[idx] = element
    return nueva_lista
