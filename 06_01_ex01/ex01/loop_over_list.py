# loop_over_list.py
# Loop Over List -- Basic Programming Patterns
# 식물생산과학부 2022-14673 강준서

# Suppose you are given a list of numbers
xs = [62, 47, 86, 117, 48, 37, 73, 41, 27, 92,
      37, 47, 19,  25, 70, 46, 52, 51, 14, 4]


# 1. Summation
# Compute sum of xs. Do NOT use the built-in function sum()
result = 0
for x in xs:
    result += x
print(xs)


# 2. Counting
# How many even numbers in xs?
result = 0
for i in xs:
    if i % 2 == 0:
        result += 1
print('There Are {0} even numbers in xs'.format(result))



# 3. Searching
# Find the index of 73
result = 0
for i, x in enumerate(xs):
    if x == 73:
        result = i
print(result)



# 4. Sorting
# Find the maximum. Do NOT use the built-in function max()
result = xs[0]
for x in xs:
    if x > result:
        result = x
print(result)


# 5. Mapping
# Create a list of x*x for all x in xs
result = []
for x in xs:
    result.append(x*x)
print(result)


# 6. Filtering
# Filter even numbers in xs, i.e. select even numbers from xs
# and create a new list.

result = []
for x in xs:
    if x%2 == 0:
        result.append(x)
print(result)



