def NULL_not_found(object: any) -> int:
    if isinstance(object, type(None)):
        print (f"Nothing : None {type(object)}")
    elif isinstance(object, float) and object != object:
        print(f"Cheese : nan {type(object)}")
    elif isinstance(object, bool) and object is False:
        print(f"Fake : {object} {type(object)}")
    elif isinstance(object, int) and object == 0:
        print(f"Zero : 0 {type(object)}")
    elif isinstance(object, str) and len(object) == 0:
        print(f"Empty : {type(object)}")
    else:
        print("Type not Found")
        return 1
    return 0