p,r,t=input().split()
P=float(p)
R=float(r)
T=float(t)
x=1+(R/100)
amount=P*(x**T)
ci=amount
print("%.2f"%ci)