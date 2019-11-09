def myMax():
    lst = [];
    n= int(input("Enter number of elements : "));
    for i in range (0,n):
        ele = int(input());
        lst.append(ele);
    print("The maximum number from list is : ", max(lst));
myMax();