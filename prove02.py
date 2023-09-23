def is_even(x):
    return x % 2 == 0

def is_natural(x):
    return x > 0

def is_palindrome(x):
    return x == x[::-1]

def in_unit_circle(point):
    return (point[0]**2 + point[1]**2) <= 1

def forall(predicate, domain):
    print(f"\u2200x ({predicate.__name__}) domain={domain}")
    # Add your code here to return True or False
    boolVar = True
    for item in domain:
        if predicate(item) == True:
            boolVar = True
        else:
            boolVar =  False
            break
    return boolVar


def exists(predicate, domain):
    print(f"\u2203x ({predicate.__name__}) domain={domain}")
    # Add your code here to return True or False
    boolVar = False
    for item in domain:
        if predicate(item) == False:
            boolVar = False
        else:
            boolVar = True
            break
    return boolVar

numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(forall(is_even,numbers1)) # False
print(exists(is_even,numbers1)) # True
print("================================")
print(forall(is_natural,numbers1)) # True
print(exists(is_natural,numbers1)) # True
print("================================")

numbers2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(forall(is_natural,numbers2)) # False
print(exists(is_natural,numbers2)) # True

print("================================")
words1 = ['civic', 'rotor', 'apple']
print(forall(is_palindrome,words1)) # False
print(exists(is_palindrome,words1)) # True
print("================================")

words2 = ['racecar', 'madam', '123454321']
print(forall(is_palindrome,words2)) # True
print(exists(is_palindrome,words2)) # True
print("================================")

words3 = ['no', 'palindromes', 'here']
print(forall(is_palindrome,words3)) # False
print(exists(is_palindrome,words3)) # False
print("================================")

points1 = [(0.5,0.5), (-1,0), (-0.75,-0.3)]
print(forall(in_unit_circle,points1)) # True
print(exists(in_unit_circle,points1)) # True
print("================================")

points2 = [(0.25,-1), (0.9,1.1), (0.1,-0.1)]
print(forall(in_unit_circle,points2)) # False
print(exists(in_unit_circle,points2)) # True