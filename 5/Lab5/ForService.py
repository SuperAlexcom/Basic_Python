def input_int():
    isInputted = False
    num = 0
    while (not isInputted):
        num = input()
        try:
            num = int(num)
            isInputted = True
        except ValueError:
            print("Wrong input. Enter again: ", end='')
    return num