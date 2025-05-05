from datetime import datetime

def new_list():
    newlist = {'elements': [],
                'size': 0
            }
    return newlist

def get_element(my_list,index):
    if 0 <= index < len(my_list['elements']):
        return my_list['elements'][index]
    else:
        return None

def is_present(my_list,element,cmp_function):
    size = my_list['size']
    if size > 0:
        keyexist = False
        for keypos in range(0,size):
            info = my_list['elements'][keypos]
            if cmp_function(element,info) == 0:
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1

def add_first(my_list, element):
    if my_list['size'] == 0:
        my_list['elements'] = [element]
    else:
        my_list['elements'].insert(0,element)
    my_list['size'] +=1
    return my_list

def add_last(my_list, element):
    my_list['elements'].insert(-1,element)
    my_list['size']+=1
    return my_list

def size(my_list):
    return my_list['size']

def first_element(my_list):
    return my_list['elements'][0]

def is_empty(my_list):
    return my_list["size"] == 0

def remove_first(my_list):
    if not is_empty(my_list):
        elemento = my_list['elements'].pop(0)
        my_list["size"] -= 1
        return elemento
    else:
        raise Exception


def remove_last(my_list):
    if not is_empty(my_list):
        elemento = my_list['elements'].pop(-1)
        my_list["size"] -= 1
        return elemento
    else:
        raise Exception

def delete_element(my_list,pos):
    my_list['elements'].pop(pos)
    return my_list

def insert_element(my_list,pos, element):
    my_list['elements'].insert(pos,element)
    return my_list

def change_info(my_list, pos, element):
    my_list['elements'][pos]= element
    return my_list

def exchange(my_list,pos_1,pos_2):
    el_1 = my_list['elements'][pos_1]
    el_2 = my_list['elements'][pos_2]
    my_list['elements'][pos_1] = el_2
    my_list['elements'][pos_2] = el_1
    return my_list

def sub_list(my_list,pos_i,num_elements):
    list = my_list['elements'][pos_i:pos_i+num_elements]
    return {'size': len(list),'elements': list}

def default_sort_criteria(elemento1, elemento2):
    return elemento1 < elemento2

def selection_sort(my_list, default_sort_criteria):
    n = my_list['size']
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if type(my_list['elements'][j]) == dict:
                if default_sort_criteria(my_list['elements'][j]['average_rating'], my_list['elements'][min_index]['average_rating']):
                    min_index = j
                if min_index != i:
                    exchange(my_list,i,min_index)
            else:
                if default_sort_criteria(my_list['elements'][j], my_list['elements'][min_index]):
                    min_index = j
                if min_index != i:
                    exchange(my_list,i,min_index)
    return my_list

def dict_selection_sort(my_list, default_sort_criteria):
    n = my_list['size']
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if type(my_list['elements'][j]) == dict:
                if default_sort_criteria(my_list['elements'][j]['load_time'], my_list['elements'][min_index]['load_time']):
                    min_index = j
                if min_index != i:
                    exchange(my_list,i,min_index)
            else:
                if default_sort_criteria(my_list['elements'][j]['load_time'], my_list['elements'][min_index]['load_time']):
                    min_index = j
                if min_index != i:
                    exchange(my_list,i,min_index)
    return my_list
    

def merge(left,right):
    sorted_array = new_list()
    i = k = 0
    while (i <left['size']) and ( k < right['size']):
        if default_sort_criteria(left['elements'][i],right['elements'][k]) or (left['elements'][i]==right['elements'][k]):
            add_last(sorted_array, left['elements'][i])
            i += 1
        else:
            add_last(sorted_array, right['elements'][k])
            k +=1 
            
    sorted_array['elements'].extend(left['elements'][i:])
    sorted_array['elements'].extend(right['elements'][k:])
    sorted_array['size'] = len(sorted_array['elements'])
    return sorted_array
                
def merge_sort(my_list, default_sort_criteria):
    
    if my_list['size'] <= 1:
        return my_list
    mid = my_list['size']//2
    left = new_list()
    left['elements']= my_list['elements'][:mid]
    left['size'] = len(left['elements'])
    right =new_list()
    right['elements'] = my_list['elements'][mid:]
    right['size'] = len(right['elements'])
    left_half = merge_sort(left, default_sort_criteria)
    right_half = merge_sort(right,default_sort_criteria)
    
    return merge(left_half,right_half)
    
    
        
#ORDENAMIENTOS

def insertion_sort(my_list, default_sort_criteria):
    n = my_list['size']
    elements = my_list['elements']  
    
    for i in range(1, n):
        
        key = elements[i]
        j = i - 1
        if type(key) == dict:
            while j >= 0 and default_sort_criteria(elements[j]['average_rating'], key['average_rating']):
                elements[j + 1] = elements[j]
                j -= 1
        else:
            while j >= 0 and default_sort_criteria(elements[j], key):
                elements[j + 1] = elements[j]
                j -= 1
        
        elements[j + 1] = key  
    
    return my_list

def dict_insertion_sort(my_list, default_sort_criteria):
    n = my_list['size']
    elements = my_list['elements']  
    
    for i in range(1, n):
        
        key = elements[i]
        j = i - 1
        if type(key) == dict:
            while j >= 0 and default_sort_criteria(date_to_days(elements[j]['load_time']) ,date_to_days( key['load_time'])):
                elements[j + 1] = elements[j]
                j -= 1

        elements[j + 1] = key  
    
    return my_list



def shell_sort(my_list, default_sort_criteria):
    n = my_list["size"]
    h = 1
    while h < n // 3:  
        h = 3 * h + 1
    
    while h > 0:
        for i in range(h, n):
            key = my_list["elements"][i]
            j = i
            if type(key) == dict:
                while j >= h and my_list["elements"][j - h]['average_rating'] > key['average_rating']:
                    my_list["elements"][j] = my_list["elements"][j - h]
                    j -= h
                my_list["elements"][j] = key
            else:
                while j >= h and my_list["elements"][j - h] > key:
                    my_list["elements"][j] = my_list["elements"][j - h]
                    j -= h
                my_list["elements"][j] = key
                
        h //= 3  
    return my_list

def date_sort_criteria(elemento1, elemento2):
    fecha1 = date_to_days(elemento1['load_time'])
    fecha2 = date_to_days(elemento2['load_time'])
    dev = False
    if fecha1 < fecha2:
        dev = True
    elif (fecha1 == fecha2) and (elemento1['state_name']> elemento2['state_name']):
        dev = True
    return dev

    
def dict_shell_sort(my_list, date_sort_criteria):
    n = my_list["size"]
    h = 1
    while h < n // 3:  
        h = 3 * h + 1
    
    while h > 0:
        for i in range(h, n):
            key = my_list["elements"][i]
            j = i
            if type(key) == dict:
                while j >= h and date_sort_criteria((my_list["elements"][j - h]),key) : #and default_sort_criteria(my_list["elements"][j - h]['state_name'],key['state_name'])
                    my_list["elements"][j] = my_list["elements"][j - h]
                    j -= h
                my_list["elements"][j] = key
                
        h //= 3  
    return my_list


def dict_shell_sort_bono(my_list, default_sort_criteria):
    n = my_list["size"]
    h = 1
    while h < n // 3:  
        h = 3 * h + 1
    
    while h > 0:
        for i in range(h, n):
            key = my_list["elements"][i]
            j = i
            if type(key) == dict:
                while j >= h and default_sort_criteria((my_list["elements"][j - h]['promedio']),key['promedio']) : 
                    my_list["elements"][j] = my_list["elements"][j - h]
                    j -= h
                my_list["elements"][j] = key
                
        h //= 3  
    return my_list

def dict_quick_sort_asc(my_list, default_sort_criteria, low=0, high=None):
    """
    Ordena un diccionario con estructura específica utilizando Quick Sort in-place en orden ascendente.
    
    :param my_list: Diccionario con las claves 'elements' y 'size'
    :type my_list: dict
    :param default_sort_criteria: Función de comparación para elementos
    :type default_sort_criteria: function
    :param low: Índice inferior de la partición actual
    :type low: int
    :param high: Índice superior de la partición actual
    :type high: int
    """
    if high is None:
        high = my_list["size"] - 1
        
    def partition(lst, low, high):
        pivot = lst["elements"][high]  # Pivote como último elemento
        i = low  # Índice del menor elemento
        
        for j in range(low, high):
            # Usamos default_sort_criteria para la comparación
            if date_sort_criteria(lst["elements"][j], pivot):
                # Intercambio
                lst["elements"][i], lst["elements"][j] = lst["elements"][j], lst["elements"][i]
                i += 1
                
        # Colocar el pivote en su lugar
        lst["elements"][i], lst["elements"][high] = lst["elements"][high], lst["elements"][i]
        return i
        
    if low < high:
        pivot_index = partition(my_list, low, high)
        dict_quick_sort_asc(my_list, default_sort_criteria, low, pivot_index - 1)
        dict_quick_sort_asc(my_list, default_sort_criteria, pivot_index + 1, high)
        
    return my_list

def dict_quick_sort_desc(my_list, default_sort_criteria, low=0, high=None):
    """
    Ordena un diccionario con estructura específica utilizando Quick Sort in-place en orden descendente.
    
    :param my_list: Diccionario con las claves 'elements' y 'size'
    :type my_list: dict
    :param default_sort_criteria: Función de comparación para elementos
    :type default_sort_criteria: function
    :param low: Índice inferior de la partición actual
    :type low: int
    :param high: Índice superior de la partición actual
    :type high: int
    """
    if high is None:
        high = my_list["size"] - 1
        
    def partition(lst, low, high):
        pivot = lst["elements"][high]  # Pivote como último elemento
        i = low  # Índice del menor elemento
        
        for j in range(low, high):
            # Usamos default_sort_criteria para la comparación
            if not date_sort_criteria(lst["elements"][j], pivot):  # Invertimos la comparación
                # Intercambio
                lst["elements"][i], lst["elements"][j] = lst["elements"][j], lst["elements"][i]
                i += 1
                
        # Colocar el pivote en su lugar
        lst["elements"][i], lst["elements"][high] = lst["elements"][high], lst["elements"][i]
        return i
        
    if low < high:
        pivot_index = partition(my_list, low, high)
        dict_quick_sort_desc(my_list, default_sort_criteria, low, pivot_index - 1)
        dict_quick_sort_desc(my_list, default_sort_criteria, pivot_index + 1, high)
        
    return my_list
def dict_shell_sort_asc(my_list,ingresos_sort_criteria):
    n = my_list["size"]
    h = 1
    while h < n // 3:  
        h = 3 * h + 1
    
    while h > 0:
        for i in range(h, n):
            key = my_list["elements"][i]
            j = i
            if type(key) == dict:
                while j >= h and not ingresos_sort_criteria((my_list["elements"][j - h]),key) : #and default_sort_criteria(my_list["elements"][j - h]['state_name'],key['state_name'])
                    my_list["elements"][j] = my_list["elements"][j - h]
                    j -= h
                my_list["elements"][j] = key
                
        h //= 3  
    return my_list
def dict_shell_sort_desc(my_list,ingresos_sort_criteria):
    n = my_list["size"]
    h = 1
    while h < n // 3:  
        h = 3 * h + 1
    
    while h > 0:
        for i in range(h, n):
            key = my_list["elements"][i]
            j = i
            if type(key) == dict:
                while j >= h and ingresos_sort_criteria((my_list["elements"][j - h]),key) : #and default_sort_criteria(my_list["elements"][j - h]['state_name'],key['state_name'])
                    my_list["elements"][j] = my_list["elements"][j - h]
                    j -= h
                my_list["elements"][j] = key
                
        h //= 3  
    return my_list
def load_time_sort_criteria(element1, element2):
    return date_to_days(element1['load_time']) < date_to_days(element2['load_time'])
def ingresos_sort_criteria(element1, element2):
    if element1['ingresos_totales'] != element2['ingresos_totales']:
        return element1['ingresos_totales'] < element2['ingresos_totales']  # Ascendente
    else:
        return element1['num_registros'] > element2['num_registros']  # Descendente

def date_to_seconds(date_str):
    date_part, _, time_part = str(date_str).partition(" ")  #splitea el str por el espacio que separa fecha y hora
    dev = datetime.strptime(date_part, "%Y-%m-%d")  # Convierte fecha a datetime
    days = dev.toordinal()  # fecha en numero de dias

    if time_part:  # Si hay parte horaria
        time_obj = datetime.strptime(time_part, "%H:%M:%S")  # Convierte hora a datetime
        seconds = time_obj.hour * 3600 + time_obj.minute * 60 + time_obj.second  # Convierte a segundos
    else:
        seconds = 0  # Si no hay hora, solo usamos días

    return days * 86400 + seconds  # opera días a segundos y se suma la hora

def date_to_days(date_str): #funcion de apoyo para transformar str de fechas a numero de dias
    days = str(date_str).partition(" ")[0] #splitea el str por el espacio que separa fecha y hora
    dev = datetime.strptime(days, "%Y-%m-%d") #transforma el str a fecha
    
    return dev 
