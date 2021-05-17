#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    if not x or not my_list:
        return count
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
            count = count + 1
        except (ValueError, TypeError):
            continue
        except IndexError:
            print()
            return count
    print()
    return count
