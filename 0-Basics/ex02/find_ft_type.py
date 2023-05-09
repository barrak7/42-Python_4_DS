def all_thing_is_obj(object: any) -> int:
    print(type(object))
    return 42


'''test'''
object = 'test'

all_thing_is_obj(object)