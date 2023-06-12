def draw_pyramid(rows, columns, symbol):
  for i in range(rows):
    for j in range(columns):
      if i + j >= rows - 1:
        print(symbol, end="")
      else:
        print(" ", end="")
    print()


# Get user input
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter the symbol: ")

# Draw the pyramid
draw_pyramid(rows, columns, symbol)
