import DataStructures.Map.map_functions as mp
import DataStructures.Map.map_entry as me
import random
import DataStructures.List.array_list as ar
import DataStructures.List.single_linked_list as sll
import DataStructures.List.list_node as ln

def new_map(num_elements,load_factor,prime= 109345121):
    map = {
        'prime': prime,
        'capacity': mp.next_prime(num_elements//load_factor),
        'scale':1, #random.randint(1, prime - 1)
        'shift': 0, #random.randint(0, prime - 1)
        'table': ar.new_list(),
        'current_factor': 0,
        'size':0,
        'limit_factor': load_factor
    }
    for _ in range(0, int(mp.next_prime(num_elements))):
        ar.add_last(map['table'], me.new_map_entry(None,sll.new_list()))
    return map

def default_compare(key, element):

   if (key == me.get_key(element)):
      return 0
   elif (key > me.get_key(element)):
      return 1
   return -1

def put(my_map, key, value):
    hash_v = mp.hash_value(my_map, key) 
    entry = ar.get_element(my_map['table'], hash_v)
    
    if entry is None:
        return my_map  
    
    bucket = entry['value']
    
    current = bucket['first']
    
    while current is not None:
        if default_compare(key, current['info']) == 0:
            current['info']['value'] = value
            return my_map  
    
        current = current['next']
    
    new_node = ln.new_single_node(me.new_map_entry(key, value))
    
    if bucket['first'] is None:
        bucket['first'] = new_node
        bucket['last'] = new_node
    else:
        bucket['last']['next'] = new_node
        bucket['last'] = new_node
    
    bucket['size'] += 1
    my_map['size'] += 1
    
    my_map['current_factor'] = my_map['size'] / my_map['capacity']
    
    if my_map['current_factor'] > my_map['limit_factor']:
        return rehash(my_map)
    
    return my_map
def contains(my_map, key):
    hash_v = mp.hash_value(my_map, key)
    entry = ar.get_element(my_map['table'], hash_v)
    
    if entry is None:
        return False
    
    bucket = entry['value']
    
    if bucket['first'] is None:
        return False 
    
    current = bucket['first']
    while current is not None:
        if default_compare(key, current['info']) == 0:
            return True
        current = current['next']
    
    return False
def rehash(my_map):
    
   
    mapa = new_map((my_map['capacity'] * 2), my_map['limit_factor'])
    
    
    for i in range((my_map['table']['size'])):  
        entry = ar.get_element(my_map['table'], i) 
        
        if entry is not None:  
            bucket = entry['value']
            current = bucket['first']
            
           
            while current is not None:
                put(mapa, 
                    current['info']['key'], 
                    current['info']['value'])
                current = current['next']
    mapa['capacity'] = my_map['capacity'] * 2
    
    return mapa  
def size(my_map):
    return my_map['size']
def is_empty(my_map):
    return my_map['size'] == 0 or my_map['table']['size'] == 0
def remove(my_map, key):
    hash_v = mp.hash_value(my_map, key)
    entry = ar.get_element(my_map['table'], hash_v)
    
    if entry is None:
        return my_map  
    
    bucket = entry['value']
    current = bucket['first']
    previous = None
    
    while current is not None:
        if default_compare(key, current['info']) == 0:
            if previous is None:
                bucket['first'] = current['next']
            else:
                previous['next'] = current['next']
            
            if current == bucket['last']:
                bucket['last'] = previous
            
            
            bucket['size'] -= 1
            my_map['size'] -= 1
            
            
            my_map['current_factor'] = my_map['size'] / my_map['capacity']
            return my_map  
        
        previous = current
        current = current['next']
    
    return my_map  
def get(my_map, key):
    hash_v = mp.hash_value(my_map, key) % my_map['capacity']
    entry = ar.get_element(my_map['table'], hash_v)
    
    if entry is None:
        return None  
    
    bucket = entry['value']
    current = bucket['first']
    
    while current is not None:
        if default_compare(key, current['info']) == 0:
            return current['info']['value']
        current = current['next']
    
    return None
def key_set(my_map):
    lista = ar.new_list()
    
    for i in range(my_map['table']['size']): 
        entry = ar.get_element(my_map['table'], i)
        
        if entry is not None:
            bucket = entry['value']
            current = bucket['first']
            
            while current is not None:
                ar.add_last(lista, current['info']['key'])
                current = current['next']
    
    return lista
def value_set(my_map):
    lista = ar.new_list()
    
    for i in range(my_map['table']['size']): 
        entry = ar.get_element(my_map['table'], i)
        
        if entry is not None:
            bucket = entry['value']
            current = bucket['first']
            
            while current is not None:
                ar.add_last(lista, current['info']['value'])
                current = current['next']
    
    return lista
