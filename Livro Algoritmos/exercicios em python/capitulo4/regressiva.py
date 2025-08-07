def regressiva(i):
    if i <= 0:
        return
    else:
        print(i)
        regressiva(i-1)


print(regressiva(10))

def progressiva(i):
    if i >= 10:
        return
    else:
        print(i)
        progressiva(i + 1)

print(progressiva(1))