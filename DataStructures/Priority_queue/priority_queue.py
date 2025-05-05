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
