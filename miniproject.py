import string
import random

# Character sets
s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

# Get user input
length = int(input("How many characters do you want in your password?: "))

if length >= 8:
    random.shuffle(s1)
    random.shuffle(s2)
    random.shuffle(s3)
    random.shuffle(s4)

    part1 = round(length * (30 / 100))  # lowercase + uppercase
    part2 = round(length * (20 / 100))  # digits + punctuation

    result = []

    for x in range(part1):
        result.append(s1[x])
        result.append(s2[x])

    for x in range(part2):
        result.append(s3[x])
        result.append(s4[x])

    while len(result) < length:
        result.append(random.choice(s1 + s2 + s3 + s4))

    random.shuffle(result)
    password = "".join(result)

    print("Strong Password:", password)

else:
    print("The length should be greater than 8")
