def number_compare(a, b):
    if a == b:
        return("Numbers are equal")
    elif a < b:
        return("First is greater")
    else:
        return("Second is greater")

print(number_compare(4,3))