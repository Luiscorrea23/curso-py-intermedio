def run():
    my_list = [1, "hello", True, 4.5]
    my_dict = {"FirstName": "Luis", "LastName": "Correa"}

    my_super_list = [
        {"FirstName": "Luis", "LastName": "Correa"},
        {"FirstName": "Luis", "LastName": "Correa"},
        {"FirstName": "Luis", "LastName": "Correa"},
        {"FirstName": "Luis", "LastName": "Correa"},
        {"FirstName": "Luis", "LastName": "Correa"}
    ]

    my_super_dict = {
        "Natural_Nums": [1,2,3,4,5,6,7],
        "Intergers_Nums": [1,2,0,-1,-2],
        "float_nums": [1.1, 4.5,6.43,5]
    }

    for key, value in my_super_dict.items():
        print(key, "-", value)

    for i in my_super_list:
        key = i.keys()
        value = i.values()
        complete = i.items()

        print(key, "-", value)
        print(complete)

if __name__ == "__main__":
    run()