#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    lt = []
    index = 0
    if list_length < index:
        print("out of range")
    while index < list_length:
        try:
            lt.append(my_list_1[index] / my_list_2[index])
        except ZeroDivisionError:
            print("division by 0")
            lt.append(0)
        except TypeError:
            print("wrong type")
            lt.append(0)
        except IndexError:
            print("out of range")
            lt.append(0)
        finally:
            index += 1
    return lt
