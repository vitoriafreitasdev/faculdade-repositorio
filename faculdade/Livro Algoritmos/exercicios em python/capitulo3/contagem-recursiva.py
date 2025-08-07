max = 10
def cont(x):
    if x == max:
        return x
    else:
        print(x)
        return cont(x + 1)

print(cont(1))

def fat(x):
    if x == 1:
        return 1
    else:
        print(f"{x} * {x - 1}")
        return x * fat(x-1)
    
print(fat(10))