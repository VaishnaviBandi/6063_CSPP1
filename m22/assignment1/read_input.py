'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
	string = ''
	no_of_lines = int(input())
	for each_line in range(no_of_lines):
		string = string + (input()) + "\n"
		each_line += 1
	print(string)

if __name__ == '__main__':
    main()
