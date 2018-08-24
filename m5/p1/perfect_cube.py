"""# Write a python program to find if the given number is a perfect cube or not
# using guess and check algorithm

# testcase 1
# Input: 24389
# Output: 24389 is a perfect cube

# testcase 2
# Input: 21950
# Output: 21950 is not a perfect cube"""

def main():
    "Program to find the perfect cube"
    cube = int(input())
    for x_i in range(1, cube, 1):
        m_i = x_i * x_i * x_i
        if m_i == cube:
            break
    if m_i == cube:
        print(str(cube) + " " + "is a perfect cube")
    else:
        print(str(cube) + " " + "is not a perfect cube")
if __name__ == "__main__":
    main()
