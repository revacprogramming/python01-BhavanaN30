# Conditional Execution

hrs=input("Enter hours:")
h=float(hrs)
rt=input("Enter the rate:")
r=float(rt)
if h<=40:
  print(h*r)
elif h>40:
    print(40*r+(h-40)*1.5*r)