# Treasure Map.  Your code will mark a spot with an X.
# 11 21 31
# 12 22 32
# 13 23 33

row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")
horizontal = int(position[0])
vertical = int(position[1])

map[vertical - 1][horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")

