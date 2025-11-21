# _ _ _ 1
# _ _ 2 1
# _ 3 2 1
# 4 3 2 1

for row in range(4):
    spaces = 4 - row - 1
    for col in range(4):
        if col < spaces:
            print(" ",end="")
        else:
            print(4 - col,end="")
    print()