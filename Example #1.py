# initialize variables to hold the first two numbers in the sequence
a, b = 0, 1

# loop 10 times to generate and print the first 10 numbers in the sequence
for i in range(10):
    print(a)
    a, b = b, a + b
