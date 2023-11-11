def fun1(n):
    if n == 0:
        return 5
    return fun1(n-1) + 3*n

def fun2(n):
    if n == 0:
        return 1
    return n**3 + fun2(n-1)

def fun3(n):
    if n == 0:
        return 1
    if n == 1:
        return 3
    return fun3(n-1)*fun3(n-2)

def fun4(n):
    if n == 0:
        return 1
    if n == 1:
        return 5
    return fun4(n-1) + fun4(n-2)**2

print([fun1(n) for n in range(10)]) # [5, 8, 14, 23, 35, 50, 68, 89, 113, 140]
print([fun2(n) for n in range(10)]) # [1, 2, 10, 37, 101, 226, 442, 785, 1297, 2026]
print([fun3(n) for n in range(10)]) # [1, 3, 3, 9, 27, 243, 6561, 1594323, 10460353203, 16677181699666569]
print([fun4(n) for n in range(10)]) # [1, 5, 6, 31, 67, 1028, 5517, 1062301, 31499590, 1128514914191]


seq1 = [i**3 for i in range(1, 54)]

seq2 = [2**i - 2 for i in range(4, 28)]

seq3 = [i**5 + 1 for i in range(-3, 19)]

seq4 = [2**i for i in range(-2, 8)]

print(sum(seq1)) # 2047761
print(sum(seq2)) # 268435392
print(sum(seq3)) # 6656947
print(sum(seq4)) # 255.75