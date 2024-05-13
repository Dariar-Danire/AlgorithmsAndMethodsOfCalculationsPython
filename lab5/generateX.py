def generateX():
    print("Введите левую границу:")
    x_start = float(input())
    print("Введите правую границу:")
    x_end = float(input())
    print("Введите щаг:")
    step = float(input())

    listX = []
    x = x_start
    while x < x_end:
        listX.append(x)
        x += step

    return listX