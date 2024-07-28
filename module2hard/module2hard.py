def decoder(x):
    result = ""
    for i in range(1, x):
        for j in range(i + 1, x):
            if x % (i + j) == 0:
                result += str(i) + str(j)
    return result


value = int(input())
print(decoder(value))
