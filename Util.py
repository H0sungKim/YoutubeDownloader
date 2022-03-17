def printProgressBar(a, b) :
    # Loading #################################################  | 98.7%  9872/10000
    percentage = a / b * 100
    bar = "#" * int(percentage // 2) + " " * int(50 - percentage // 2)
    print(f'\033[34mLoading... {bar} | {round(percentage, 2)}%\t{str(a).zfill(len(str(b)))}/{b}', end='\r')