#!/usr/bin/python3
# Author: Michael Ifeoluwalose Adesina
def list_division(my_list_1, my_list_2, list_length):
    """list_division: divides element by element 2 lists.

    Args:
        my_list_1:
        my_list_2:
        list_length:

    Returns:
        a new list (length = list_length) with all divisions
    """
    output_list = []
    for i in range(list_length):
        try:
            quotient = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            quotient = 0
        except IndexError:
            print("out of range")
            quotient = 0
        except ZeroDivisionError:
            print("division by 0")
            quotient = 0
        finally:
            output_list.append(quotient)
    return output_list
