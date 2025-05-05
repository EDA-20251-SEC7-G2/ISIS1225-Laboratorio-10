def new_list ():
    newlist = {
        "first": None,
        "last": None,
        "size": 0,
    }
    
    return newlist

def is_empty(my_list):
    return my_list["size"] == 0

        
def new_single_node(element):
    
    return {"info": element, "next": None}

def get_element(my_list, pos):
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos:
        node = node["next"]
        searchpos += 1
    return node["info"]

def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp = my_list["first"]
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"]) == 0:
            is_in_array = True
        else:
            temp = temp["next"]
            count += 1
            
    if not is_in_array:
        count = -1
    return count

    
def add_first(my_list, element):
    nodo = new_single_node(element)
    
    nodo["next"] = my_list["first"]
    my_list["first"] = nodo
    
    if my_list["size"] == 0:
        my_list["last"] = my_list["first"]
        
    my_list["size"] += 1
 
    return my_list

def add_last(my_list, element):
    new_node=new_single_node(element)
    
    if my_list["size"] == 0:
        my_list["first"] = new_node
    else:
        my_list["last"]["next"] = new_node

    my_list["last"] = new_node

    
    my_list["size"] += 1  
    
    return my_list

def size(my_list):
    size = my_list["size"]
    return size

def first_element(my_list):
    if is_empty(my_list):
        raise Exception
    element=None
    if my_list["first"] is not None:
        element=my_list["first"]
    return element

def last_element(my_list):
    result = None
    
    if my_list["last"] is not None:
        current_node = my_list["last"]
        result = current_node["info"]
        
    return result

def remove_first(my_list):
    removed_info = None
    
    if my_list["size"] > 0:
        node = my_list["first"]
        removed_info = node["info"]
        my_list['first']= node['next']
    my_list['size']-=1
        
    return removed_info

def remove_last(my_list):
    removed_info = None
    
    if my_list["size"] > 0:
        if my_list["first"] == my_list ["last"]:
            removed_info = remove_first(my_list)
            my_list['first']=None
            my_list['last']=None
            
        else:
            current_node = my_list["first"]
                                   
            while current_node["next"] != my_list["last"]:
                current_node = current_node["next"]
            removed_info = my_list['last']['info']
            current_node['next']=None
            my_list['last']=current_node
    my_list['size']-=1
    return removed_info

def insert_element(my_list, element, pos):
    searchpos = 0
    node = my_list["first"]
    current_node = node
    while searchpos < pos:
        node = node["next"]
        searchpos += 1
        current_node = node["info"]
    
    nuevo_nodo = new_single_node(element)
    
    current_node["next"] = nuevo_nodo["info"]
        
    my_list["size"] += 1
 
    return my_list

def delete_element(my_list, pos):
    searchpos = 0
    node = my_list["first"]
    current_node = node
    while searchpos < pos:
        node = node["next"]
        searchpos += 1
        current_node = node["info"]
    current_node = current_node["next"]
        
    my_list["size"] -= 1
 
    return my_list

def change_info(my_list, pos, new_info):
    searchpos = 0
    node = my_list["first"]
    current_node = node
    while searchpos < pos:
        node = node["next"]
        searchpos += 1
        current_node = node["info"]
    current_node["info"] = new_info
 
    return my_list


def exchange(my_list, pos_1, pos_2):
    searchpos1 = 0
    node = my_list["first"]
    current_node1 = None
    current_node2 = None

    while searchpos1 < pos_1:
        node = node["next"]
        searchpos1 += 1
    current_node1 = node  

    searchpos2 = 0
    node = my_list["first"]

    while searchpos2 < pos_2:
        node = node["next"]
        searchpos2 += 1
    current_node2 = node 

    current_node1["info"], current_node2["info"] = current_node2["info"], current_node1["info"]

    return my_list

def sub_list(my_list, pos, num_elements):
    sublist = new_list()  
    if pos < 0 or pos >= my_list["size"]:
        sublist=None
    current = my_list["first"]  
    for _ in range(pos):
        current = current["next"]
    count = 0  
    while current is not None and count < num_elements:
        if sublist["size"] == 0:
            sublist = add_first(sublist, current["info"])  
        else:
            sublist = add_last(sublist, current["info"])  
        current = current["next"]  
        count += 1  
    return sublist

def default_sort_criteria(elemento1, elemento2):
    return elemento1 < elemento2

def selection_sort(my_list, default_sort_criteria):
    n = my_list['size']
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if type(get_element(my_list,j)) == dict:
                if default_sort_criteria(get_element(my_list,j)['average_rating'],get_element(my_list,min_index)['average_rating']):
                    min_index = j
                if min_index != i:
                    exchange(my_list,i,min_index)
            else:
                if default_sort_criteria(get_element(my_list,j),get_element(my_list,min_index)):
                    min_index = j
                if min_index != i:
                    exchange(my_list,i,min_index)
                
    return my_list
            
def merge( left, right):
    sorted_sll = new_list()
    i = k = 0
    while (i<left['size']) and (k< right['size']):
        if default_sort_criteria(get_element(left,i),get_element(right,k)) or (get_element(left,i)==get_element(right,k)):
            add_last(sorted_sll,get_element(left,i))
            i+=1
        else:
            add_last(sorted_sll,get_element(right,k))
            k+=1
            
    if i != left['size']:
        for index in range(i, left['size']-1):
            add_last(sorted_sll(get_element(left,index)))
    if k !=right['size']:
            for index in range(k, right['size']-1):
                add_last(sorted_sll(get_element(right,index)))
    return sorted_sll

def merge_sort(my_list, default_sort_criteria):
    if my_list['size'] <= 1:
        return my_list
    mid = my_list['size']//2
    
    left = new_list()
    for index in range(mid):
        add_last(left, get_element(my_list,index))
        
    right = new_list()
    for index in range(mid,my_list['size']-1):
        add_last(right, get_element(my_list,index))
        
    left_half = merge_sort(left, default_sort_criteria)
    right_half = merge_sort(right,default_sort_criteria)
    return merge(left_half,right_half)
    
            

def insertion_sort(my_list, default_sort_criteria):
    if my_list is None or my_list['first'] is None or my_list['first']['next'] is None:
        return my_list

    
    sorted_head = my_list['first']
    current_node = sorted_head['next']
    sorted_head['next'] = None  

    while current_node is not None:
        next_node = current_node['next']  
        
        if type(current_node['info']) == dict:
            if default_sort_criteria(current_node['info']['average_rating'], sorted_head['info']['average_rating']):
                current_node['next'] = sorted_head
                sorted_head = current_node
            else:
                temp = sorted_head
                while temp['next'] is not None and not default_sort_criteria(current_node['info']['average_rating'], temp['next']['info']['average_rating']):
                    temp = temp['next']
                current_node['next'] = temp['next']
                temp['next'] = current_node
        else:
            if default_sort_criteria(current_node['info'], sorted_head['info']):
                current_node['next'] = sorted_head
                sorted_head = current_node
            else:
                temp = sorted_head
                while temp['next'] is not None and not default_sort_criteria(current_node['info'], temp['next']['info']):
                    temp = temp['next']
                current_node['next'] = temp['next']
                temp['next'] = current_node
        
        current_node = next_node  

    my_list['first'] = sorted_head  
    return my_list

def quick_sort(my_list, default_sort_criteria):
    def nodo(index):
        nodo_actual = my_list["first"]
        for nodos in range(index):
            nodo_actual = nodo_actual["next"]
        return nodo_actual
    
    def quick_sorting(my_list, low = 0, high = None):
        if high is None:
            high = my_list["size"] - 1
    
            def partition(low, high):
                pivot = nodo(high)
                i = low
                for j in range(low, high):
                    nodo_j = nodo(j)
                    nodo_i = nodo(i)
                    if nodo_j['average_rating'] < pivot['average_rating']:
                        nodo_i, nodo_j["info"] = nodo_j["info"], nodo_i["info"]
                        i += 1
                nodo_i["info"], pivot["info"] = pivot["info"], nodo_i["info"]
                return i
    
            if low < high:
                pivot_index = partition(low, high)
                quick_sorting(my_list, default_sort_criteria(low, pivot_index - 1))
                quick_sorting(my_list, default_sort_criteria(high, pivot_index + 1))
            
    return my_list


def shell_sort(my_list, default_sort_criteria):
    def nodo(index):
        nodo_actual = my_list["first"]
        for nodos in range(index):
            nodo_actual = nodo_actual["next"]
        return nodo_actual
    
    n = my_list["size"]
    h = 1
    while h < n // 3:  
        h = 3 * h + 1
    
    while h > 0:
        for i in range(h, n):
            nodo_actual = nodo(i)
            info = nodo_actual['info']
            j = i
            continuar = True
            while j >= h and continuar:
                nodo_ant = nodo(j - h)
                if type(info) == dict:
                    if default_sort_criteria(nodo_ant['info']['average_rating'], info['average_rating']):
                        nodo(j)["info"] = nodo_ant["info"]
                        j -= h
                    else:
                        continuar = False
                else:
                    if default_sort_criteria(nodo_ant['info'], info):
                        nodo(j)["info"] = nodo_ant["info"]
                        j -= h
                    else:
                        continuar = False
            nodo(j)["info"] = info
        h //= 3
    return my_list
