n=int(input('Введите натуральное число  '))
if n%2==0:
    a=list(range(2,(n+1),2))
    print(a[0:((n+1)//2)])
    for i in a:
        print(i, end=', ')
if n%2==1:
    b=list(range(2,(n+1),2))
    print(b[0:((n+1)//2)])
    for d in b:
        print(d, end=', ')
