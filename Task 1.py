def task(array):
    start = 0
    end = len(array)
    if end < 2:
        return -1
    while True:
        point = (end - start) // 2 + start
        # print(f'{start}, {point}, {end}')
        if point == start or point == end:
            return -1
        a = array[point]
        if a == '0':
            if array[point - 1] == '1':
                return point
            else:
                end = point
        else:
            start = point


print(task("111111111111111111111111100000000"))
