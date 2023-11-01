from sys import argv

script, n, m = argv

n = int(n)
m = int(m)

path = [1]

circle_arr = []

end_value = path[0]
interval = []
counter = 0

while 1:

    for i in range(m):
        interval.append(counter + 1)
        if counter != m:
            counter += 1
        else:
            counter = 0

    print(interval)
    if counter != 0:
        path.append(counter)
    else:
        path.append(n)
    print(path)
    interval.clear()
    counter -= abs(n-m)

    if (path[-1] == end_value) & (len(path) > 1):
        path.pop()
        print(*path, sep=" ")
        break