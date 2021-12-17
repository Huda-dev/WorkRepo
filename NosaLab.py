x= 5
y= 9

py_operators= {
    "add": "+",
    "substract": "-",
    "multiply": "*",
    "division": "/"
    }

def add(i, j):
    return i + j
    
def substract(i, j):
    return i - j
    
def multiply(i, j):
    return i * j

def division(i, j):
    return i / j

user_input= input("Please, type your operation to perform: ").lower()
result= 0
flag = 0

for op in py_operators:
    if op == user_input:
        result= add(x,y)
        print(f"The result of {x} {py_operators[op]} {y} = {result}")
        flag = 1
        break
    elif op == user_input:
        result= substract(x,y)
        print(f"The result of {x} {py_operators[op]} {y} = {result}")
        flag = 1
        break
    elif op == user_input:
        result= multiply(x,y)
        print(f"The result of {x} {py_operators[op]} {y} = {result}")
        flag = 1
        break
    elif op == user_input:
        result= division(x,y)
        print(f"The result of {x} {py_operators[op]} {y} = {result}")
        flag = 1
        break
if flag == 0:
    print(f"In this part of the universal, we do not accept such operation {user_input}")

#result= add(x,y)
#print(f"The result of {x} {py_operators} {y} = {result}")
