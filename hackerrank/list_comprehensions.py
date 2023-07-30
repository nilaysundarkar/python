if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
inputs = []
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            inputs.append([i,j,k])
inputs_comprehension = list([i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n)
print(inputs)
print(inputs_comprehension)
