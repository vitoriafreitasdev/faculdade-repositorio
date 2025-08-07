# import time
def fat(x):
    if x == 1:
        return 1
    else:
        print(f"{x} * {x - 1}")
        return x * fat(x-1)
        
    
print(fat(3))

# def Fibonacci(idx):
#     if idx <= 1:
#         return idx
#     else:
#         return Fibonacci(idx-1)+Fibonacci(idx-2)



# def fibonacci(idx):
#     seq = [0, 1]
#     for i in range(idx):
#         seq.append(seq[-1] + seq[-2])
#     return seq[-2]


# print(Fibonacci(8))
# print("**** recursiva ****")
# rec = time.time()
# print(Fibonacci(8))
# print("speed : " + str(time.time()-rec))

# print("**** for ****")
# it = time.time()
# print(fibonacci(8))
# print("speed : " + str(time.time()-it))



def my_sum(n):
    if n == 0:
        return n #caso base 
    else:
        return n + my_sum(n-1)
#print(my_sum(3))