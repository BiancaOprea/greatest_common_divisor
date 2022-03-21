#v1
def greateest_common_divisor_minus(a, b):
    while a != b:
        if a > b:
            a = a-b
        else:
            b = b-a
        print(f"a = {a}, b = {b}")
    return a


print(greateest_common_divisor_minus(18, 16))


#v2
def gcd_modulo(a, b):
    while a % b:
        rest = a % b
        a = b
        b = rest
        print(f"a = {a}, b = {b}")
    return b


print(gcd_modulo(18, 16))
print(gcd_modulo(30, 12))
print(gcd_modulo(7, 5))