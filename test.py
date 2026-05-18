def func(n,d):
    a = []
    for i in range(len(n)):
        if n[i] == d:
            t = n[:i]+n[(i+1):]
            a.append(int(t))
    print(str(max(a)))

func("1361","6")





