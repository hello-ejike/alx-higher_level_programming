#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    n_list = []
    for i in range(list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("Error: Wrong type encountered.")
            div = 0
        except ZeroDivisionError:
            print("Error: Division by zero.")
            div = 0
        except IndexError:
            print("Error: Index out of range.")
            div = 0
        n_list.append(div)
    return n_list
