def add_one(num):
    if (num >=9):
        return num + 1
    total = num + 1
    print(f"num = {num}")
    print(f"total = {total}")

    return add_one(total)

mynewtotal = add_one(0)

print(mynewtotal)
