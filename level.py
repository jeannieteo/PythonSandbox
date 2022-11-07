'''Your task is to write a program which reads the number of blocks the 
builders have, and outputs the height of the pyramid that can be built 
using these blocks.


Test Data
Sample input: 6
Expected output: The height of the pyramid: 3
Sample input: 20
Expected output: The height of the pyramid: 5
Sample input: 1000
Expected output: The height of the pyramid: 44
Sample input: 2
Expected output: The height of the pyramid: 1
'''
blocks = int(input("Enter the number of blocks: "))

total = 1
height = 1
while total < blocks:
    print(height, blocks - total)
    total = height + total
    if (blocks - total) >= height:
        height += 1
print("The height of the pyramid:", height)
print("total:", total)

v=1
while v < 10:
    print("#")
    v = v<<1
    print(v)