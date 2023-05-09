import math

def NULL_not_found(object : any) -> int:
    if not object or math.isnan(object):
        print(type(object))
        return 0
    
    print("Type not Found!")
    return 1

test = None
print(NULL_not_found(test))