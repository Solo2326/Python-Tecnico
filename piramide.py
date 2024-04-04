pyramid_size = 8
building_block = "*"

for level in range(pyramid_size):
    spaces = " " * (pyramid_size - level - 1)
    blocks = building_block * (2 * level + 2)
    print(spaces + "./" + blocks + "\\")
print("/" + "_" * (2 * pyramid_size) + "\\") 
