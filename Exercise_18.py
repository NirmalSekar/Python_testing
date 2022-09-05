def print_two(*args):
    arg1, arg2 = args
    print(f"arg1 = {arg1},  arg2 = {arg2}")


def print_two_again(arg1, arg2):
    print(f"arg1 = {arg1},  arg2 = {arg2}")


print_two("nirmal", "kumar")
print_two_again("nirmalkumar", "sekar")