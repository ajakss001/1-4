arr = []
for i in range(5):
    arr.append(int(input()))
    arr.append(sum(arr))
for x in arr:
    print(x)