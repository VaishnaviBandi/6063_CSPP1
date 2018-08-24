"""#Exercise : Function and Objects Exercise-3
#Implement a function that converts the given
testList = [1, -4, 8, -9] into [1, 16, 64, 81]"""
def apply_to_each(L, f):
    new_list=[]
    for i in range(len(L)):
        new_list.append(square(L[i]))
    return new_list
def square(num):
    return num * num
    
def main():
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    print(apply_to_each(list1, square))

if __name__== "__main__":
    main()