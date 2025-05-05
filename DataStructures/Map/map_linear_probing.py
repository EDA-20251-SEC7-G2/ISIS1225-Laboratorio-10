import random
from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mapf
from DataStructures.List import array_list as ar


def new_map(num_elements, load_factor, prime=109345121):
  capacity = mapf.next_prime(int(num_elements//load_factor))
  scale = random.randint(1,prime-1) 
  shift = random.randint(0,prime-1)
  table = ar.new_list()
  for entry in range(capacity):
    ar.add_last(table,me.new_map_entry(None, None))
  limit_factor = load_factor
  map = {
   'prime': prime,
   'capacity': capacity,
   'scale': scale, 
   'shift': shift, 
   'table': table,
   'current_factor': 0,
   'limit_factor': limit_factor,
   'size': 0}
  return map

def put(my_map, key, value):
  hash_value = mapf.hash_value(my_map,key)
  position = find_slot(my_map, key, hash_value)
  entry = ar.get_element(my_map["table"],position[1])
  if position[0] == True:
    me.set_value(entry, value)
  else:
    me.set_key(entry, key)
    me.set_value(entry, value)
    my_map["size"] += 1
    my_map["current_factor"] = my_map["size"] / my_map["capacity"]
    if my_map["current_factor"] > my_map["limit_factor"]:
      rehash(my_map)
  ar.change_info(my_map["table"], position[1], entry)
  return my_map

def find_slot(my_map, key, hash_value):
   first_avail = None
   found = False
   ocupied = False
   while not found:
      if is_available(my_map["table"], hash_value):
            if first_avail is None:
               first_avail = hash_value
            entry = ar.get_element(my_map["table"], hash_value)
            if me.get_key(entry) is None:
               found = True
      elif default_compare(key, ar.get_element(my_map["table"], hash_value)) == 0:
            first_avail = hash_value
            found = True
            ocupied = True
      hash_value = (hash_value + 1) % my_map["capacity"]
   return ocupied, first_avail

def is_available(table,pos):
   entry = ar.get_element(table, pos)
   if me.get_key(entry) is None or me.get_key(entry) == "__EMPTY__":
      return True
   return False    

def default_compare(key,entry):
   if key == me.get_key(entry):
      return 0
   elif key > me.get_key(entry):
      return 1
   return -1

def contains(my_map, key):
  hash_value = mapf.hash_value(my_map,key)
  position = find_slot(my_map, key, hash_value)
  if position[0] == True:
     return True
  else:
     return False

def remove(my_map, key):
  hash_value = mapf.hash_value(my_map,key)
  position = find_slot(my_map, key, hash_value)
  if position[0] == True:
    entry = ar.get_element(my_map["table"],position[1])
    me.set_key(entry, None)
    me.set_value(entry, None)
    my_map["size"] -= 1
  return my_map

def get(my_map, key):
  hash_value = mapf.hash_value(my_map,key)
  position = find_slot(my_map, key, hash_value)
  if position[0] == True:
    entry = ar.get_element(my_map["table"],position[1])
    return me.get_value(entry)
  return None

def size(my_map):
  return my_map["size"]

def is_empty(my_map):
  if size(my_map) == 0:
    return True
  else:
    return False

def key_set(my_map):
  key_set = ar.new_list()
  for entry in range(ar.size(my_map["table"])):
    key = me.get_key(ar.get_element(my_map["table"],entry))
    if key != None:
      ar.add_last(key_set, key)
  return key_set     

def value_set(my_map):
  value_set = ar.new_list()
  for entry in range(my_map["capacity"]):
    value = me.get_value(ar.get_element(my_map["table"],entry))
    if value != None:
      ar.add_last(value_set, value)
  return value_set   

def rehash(my_map):
    prev_capacity = my_map["capacity"]
    capacity = mapf.next_prime(my_map["capacity"]*2)
    my_map["capacity"] = capacity
    my_map["current_factor"] = my_map["size"] / my_map["capacity"]
    table_copy = my_map["table"]
    new_table = ar.new_list()
    for i in range(capacity):
        ar.add_last(new_table, me.new_map_entry(None, None))
    my_map["table"] = new_table
    my_map["size"] = 0
    for pos in range(prev_capacity):
        new_pos = ar.get_element(table_copy,pos) 
        if me.get_key(new_pos) != None:
          key = me.get_key(new_pos)
          value = me.get_value(new_pos)
          put(my_map,key,value)         
    return my_map

mmap = new_map(5,0.5)
put(mmap,1,1)
put(mmap,3,3)
put(mmap,4,5)
put(mmap,5,2)
put(mmap,6,9)
put(mmap,7,9)
print(get(mmap,4))
