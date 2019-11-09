def myFreq():
    lst = [];
    n= int(input("Number of elements : "));
    for i in range (0,n):
        ele = int(input());
        lst.append(ele);
    no1= int(input("Element to Search :"));
    count = lst.count(no1);
    print("Output :",count)
myFreq();