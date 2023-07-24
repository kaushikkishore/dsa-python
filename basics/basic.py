# You can assign multiple variables

n, m = 3, 5

print(n, m)


# Increment in python

n = 1
m = 1

n = n+1
m = m+1

n += 1
m += 1

print(m, n)

# Null is known as None
var = None
print(var)


# Conditions
m = 10
n = 5

if m > 2:
    print("m is greater than 2")

m = -1

if m > 2:
    print("m is greater than 2")
elif n < 9:
    print("m is less than 10")
else:
    print("no condtion matching ")

# Here & is and and || is or

if m == -1 and n == 5:
    print("And condition is valid")


m = 1
n = 5

if m == 4 or n == 5:
    print("Or condition is validated")

# simple while loop
print("Simple while loop")
n = 0
while n < 10:
    print(n)
    n += 1

# for loop
print("for loop")
for i in range(5):  # 5 is not included
    print(i * 10)

# with the range
print("with the range")
for i in range(1, 6):  # 6 is not included
    print(i)

# with increment / decrement
print("with increment / decrement")
for i in range(5, 1, -1):
    print(i)

# reverse loop
print("reverse loop")
arr = [3, 5, 7, 9, 1]
for i in range(len(arr)-1, -1, -1):
    print(arr[i])


# division process
print("Division process")
