row_1 = ["O", "O", "O"]
row_2 = ["O", "O", "O"]
row_3 = ["O", "O", "O"]

map = [row_1, row_2, row_3]

print (f"{row_1}\n{row_2}\n{row_3}")

position = input("Where do you want to put the treasure?")
col = int(position[0])
row = int(position[1])

selected_row = map[col -1]
selected_row[row - 1] = "X"


print (f"{row_1}\n{row_2}\n{row_3}")
