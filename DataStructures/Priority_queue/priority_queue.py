from DataStructures.List import array_list as lt
from DataStructures.Priority_queue import index_pq_entry as pqe

def new_heap(is_min_pq= True):
    heap = {
        'elements': lt.new_list(),
        'size': 0,
        'cmp_function':None
    }
    if is_min_pq:
        heap['cmp_function'] = default_compare_lower_value
    else:
        heap['cmp_function'] = default_compare_higher_value
    return heap

def default_compare_higher_value(father_node, child_node):
    if pqe.get_key(father_node) >= pqe.get_key(child_node):
        return True
    return False

def default_compare_lower_value(father_node, child_node):
    if pqe.get_key(father_node) <= pqe.get_key(child_node):
        return True
    return False

def size(priority_queue):
    return priority_queue['size']

def is_empty(priority_queue):
    return size(priority_queue) == 0

def get_first_priority(my_heap):
    if my_heap['size'] > 0:
        return lt.get_element(my_heap['elements'], 0)['value']
    return None

def insert(my_heap, element, key):
    my_heap["size"] += 1
    lt.add_last(my_heap['elements'], {
                      'key': key, 'value': element})
    swim(my_heap, my_heap['size']-1)
    return my_heap


def remove(my_heap):
    if my_heap['size'] > 0:
        min = lt.get_element(my_heap['elements'], 0)
        last = lt.get_element(my_heap['elements'], my_heap["size"]-1)
        lt.change_info(my_heap['elements'], 0, last)
        lt.remove_last(my_heap['elements'])
        my_heap["size"] -= 1
        sink(my_heap, 1)
        return min["value"]
    return None

def swim(my_heap, pos):
    found = False
    while pos > 1 and not found:
        parent = lt.get_element(my_heap['elements'], int((pos // 2)))
        element = lt.get_element(my_heap['elements'], int(pos))
        if not priority(my_heap, parent, element):
            exchange(my_heap, pos, int(pos / 2))
        else:
            found = True
        pos = pos // 2

def sink(my_heap, pos):
    size = my_heap["size"]
    while 2 * pos <= size:
        j = 2 * pos
        if j < size:
            if not priority(
                my_heap,
                lt.get_element(my_heap['elements'], j),
                lt.get_element(my_heap['elements'], (j + 1)),
            ):
                j += 1
        if priority(
            my_heap,
            lt.get_element(my_heap['elements'], pos),
            lt.get_element(my_heap['elements'], j),
        ):
            break
        exchange(my_heap, pos, j)
        pos = j

def priority(my_heap, parent, child):
    cmp = my_heap["cmp_function"](parent, child)
    if cmp > 0:
        return True
    return False

def exchange(my_heap, pos_i, pos_j):
    lt.exchange(my_heap['elements'], pos_i, pos_j)