#nested loops = The "inner loop" will finish all of its iterations before finishing
#   one iteration of the "Outer Loop"
rows = int(input("Enter number of rows?: "))
columns = int(input("Enter number of columns?: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()