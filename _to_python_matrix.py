matrix = []

while True:
    s = input()
    ss = s.split(" ")
    ss = list(map(lambda x: int(x), ss))
    matrix.append(ss)
    print(matrix)