def myList():
    tot = 0;
    lst = [];
    n= int(input("Enter number of elements : "));
    for i in range (0,n):
        ele = int(input());
        lst.append(ele);
    tot = sum(lst);
    print("The total is : ", tot);
myList();