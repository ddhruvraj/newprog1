'''
    a=inp
    b=inp
1
    ans=a+b/2
    f(ans)
    f(ans)<0 than ans=a
    else ans=b
    than again repeat

'''

def f(x):
    return x * x  - 4 * x - 9


i = 0
while (True):
    print(f"f({i})={f(i)}")
    i += 1
    if f(i) < 0 and f(i + 1) >= 0:
        print(f"your a and b is {i} and {i + 1} because f({i})={f(i)} and f({i+1})={f(i+1)} ")
        break
def bisection(a,b,n):
    i=1
    condition=True
    while condition:
        x=(a+b)/2
        print(f"iteration={i} ,   a={a}   ,   b={b}  ,   x={round(x,2)}   ,  f(x)={f(x)}")
        if f(x)<0:
            a=x
        else:
            b=x
        if i==n:
            condition=False
        else:
            condition=True
            i+=1

a=float(i)
b=float(i+1)
n=int(input("how many iteration you want:"))

if f(a) * f(b) > 0:
    print("please enter another interval,because root doesn't exise between your given interval")
else:
    bisection(a, b, n)


print("from above iterations if root value(x) is same at any iteration than you got your approx root of given equation")
