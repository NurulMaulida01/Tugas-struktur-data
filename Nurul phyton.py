def binary_tree(x):
    return[x,[],[]]
def insert_left(root, new_branch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(2, [new_branch, [], []])
    return root
def insert_right(root, new_branch):
    t=root.pop(2)
    if len(t) > 1:
        root.insert(2, [new_branch, [], t])
    else:
        root.insert(2, [new_branch, [], []])
    return root
def get_root_val(root):
    return root[0]
def set_root_val(root, new_val):
    root[0] = new_val
def get_left_child(root):
    return root[1]
def get_right_child(root):
    return root[2]


x =  binary_tree(input(str("input akar : ")))
insert_left (x,input(str("input simpul kiri : ")))
insert_left (x,input(str("input simpul kanan : ")))
insert_right(x,input(str("input ranting kanan : ")))      
insert_right(x,input(str("input ranting kiri ")))
l=get_left_child(x)
print (1)

print(x)


