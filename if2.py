a = "hfwfvbfif"
b = "wddwvvd"
def lines(a,b):
    if type(a) == str or type(b) == str:
        if len(a) == len(b):
            return 1
        if len(a) > len(b):
            return 2
        if len(a) != len(b) and "learn" in b:
            return 3
    else:
        return 0
result = lines(a,b)
print(result)