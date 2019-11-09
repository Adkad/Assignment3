def myMin():
    lst = [];
    n= int(input("Enter number of elements : "));
    for i in range (0,n):
        ele = int(input());
        lst.append(ele);
    print("The minimum number from the list is : ", min(lst));
myMin();