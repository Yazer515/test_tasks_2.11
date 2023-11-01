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
        if counter != n:
            interval.append(counter + 1)
            counter += 1
        else:
            if counter == m:
                interval.append(counter + 1)
                counter += 1
            else:
                counter = 0
                interval.append(counter + 1)
                counter += 1


    if counter != 0:
        path.append(counter)
    else:
        path.append(1)
    interval.clear()
    if counter != 0:
        counter -= 1
    else:
        counter = n - 1


    if (path[-1] == end_value) & (len(path) > 1):
        path.pop()
        print(*path, sep=" ")
        break