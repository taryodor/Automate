def boxPrint(symbol, width, height):
    #Makes box with given instructions
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)

boxPrint('*', 10, 7)
