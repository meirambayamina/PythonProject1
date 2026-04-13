#Basic Level
#Task 1
name = input("Name: ")
age = input("Age: ")
print(f"Hi {name}! You are {age}\n")

#Task 2
n1 = float(input("Num1: "))
n2 = float(input("Num2: "))
print("Sum:", n1+n2)
print("Diff:", n1-n2)
print("Prod:", n1*n2, "\n")

#Task 3
c = float(input("Celsius: "))
f = c*9/5+32
print("F:", f, "\n")

#Task 4
a = 5
b = 10
a, b = b, a
print("a =", a, "b =", b, "\n")

#Intermediate
#Task 5
num = int(input("Number: "))
print("Even\n" if num%2==0 else "Odd\n")

#Task 6
age = int(input("Age: "))
if age <=12: print("Child\n")
elif age <=17: print("Teen\n")
else: print("Adult\n")

#Task 7
x = float(input("Num1: "))
y = float(input("Num2: "))
z = float(input("Num3: "))
print("Max:", max(x,y,z), "\n")

#Task 8
x = float(input("Num1: "))
y = float(input("Num2: "))
op = input("Op (+,-,*,/): ")
if op=="+": print("Result:", x+y)
elif op=="-": print("Result:", x-y)
elif op=="*": print("Result:", x*y)
elif op=="/": print("Result:", x/y if y!=0 else "Error")
else: print("Bad op\n")

#Advanced

#Task 9
year = int(input("Year: "))
print("Leap\n" if (year%4==0 and year%100!=0) or year%400==0 else "No leap\n")

#Task 10
score = float(input("Score: "))
if score>=90: g="A"
elif score>=75: g="B"
elif score>=50: g="C"
else: g="F"
print("Grade:", g, "\n")

#Task 11
bal = 1000
w = float(input("Withdraw: "))
if w<=bal: bal-=w; print("New bal:", bal, "\n")
else: print("Not enough\n")

#Task 12
login = "admin"
pw = "1234"
l = input("Login: ")
p = input("Password: ")
print("Ok\n" if l==login and p==pw else "Fail\n")

#Challenge
#Task 13
buy = float(input("Buy: "))
disc = 0.1 if buy>=10000 else 0.05 if buy>=5000 else 0
print("Final:", buy*(1-disc), "\n")

#Task 14
s1 = float(input("Side1: "))
s2 = float(input("Side2: "))
s3 = float(input("Side3: "))
if s1+s2>s3 and s1+s3>s2 and s2+s3>s1:
    t = "Equi" if s1==s2==s3 else "Iso" if s1==s2 or s2==s3 or s1==s3 else "Scal"
    print("Triangle ok:", t, "\n")
else: print("No triangle\n")

#Task 15
color = input("Color: ").lower()
if color=="red": print("Stop\n")
elif color=="yellow": print("Wait\n")
elif color=="green": print("Go\n")
else: print("Bad color\n")

#Expert

#Task 16
num = float(input("Number: "))
print("Pos" if num>0 else "Neg" if num<0 else "Zero", "Even" if num%2==0 else "Odd", "In 1-100" if 1<=num<=100 else "Out", "\n")

#Task 17
x = float(input("Num1: "))
y = float(input("Num2: "))
op = input("Op (+,-,*,/,**, %): ")
res = "Bad op"
if op=="+": res = x+y
elif op=="-": res = x-y
elif op=="*": res = x*y
elif op=="/": res = x/y if y!=0 else "Err"
elif op=="**": res = x**y
elif op=="%": res = x%y
print("Result:", res, "\n")

#Task 18
pw = input("Password: ")
strength = "Weak"
if len(pw)>=8:
    if any(c.isdigit() for c in pw) and any(c.isupper() for c in pw): strength="Strong"
    else: strength="Medium"
print("Strength:", strength, "\n")

#Task 19
bal = 5000
ch = input("Check/Dep/W: ").lower()
if ch=="check": print("Bal:", bal)
elif ch=="dep": amt=float(input("Amount: ")); bal+=amt; print("Bal:",bal)
elif ch=="w": amt=float(input("Amount: ")); bal-=amt if amt<=bal else 0; print("Bal:", bal if amt<=bal else "Not enough")

#Task 20
secret = 7
guess = int(input("Guess: "))
print("Low\n" if guess<secret else "High\n" if guess>secret else "Correct\n")

#Task 21
scr = int(input("Score: "))
att = int(input("Attendance %: "))
grade = "Fail"
if scr>=50 and att>=60:
    grade = "A" if scr>=90 else "B" if scr>=75 else "C"
print("Grade:", grade, "\n")

#Task 22
ord_amt = float(input("Order: "))
dist = float(input("Dist km: "))
deliv = 0 if ord_amt>15000 else 1000+(dist-5)*200 if dist>5 else 1000
print("Delivery:", deliv, "\n")

#Task 23
sal = float(input("Salary: "))
hist = input("Credit history (good/bad): ").lower()
print("Ok\n" if sal>200000 and hist=="good" else "No\n")

#Task 24
login = "admin"
pw = "1234"
l1 = input("L1: "); p1 = input("P1: ")
l2 = input("L2: "); p2 = input("P2: ")
print("Ok\n" if (l1==login and p1==pw) or (l2==login and p2==pw) else "Blocked\n")

#Task 25
print("Menu: + - * Exit")
ch = input("Choice: ").lower()
x = float(input("Num1: "))
y = float(input("Num2: "))
if ch=="+": print("Result:", x+y)
elif ch=="-": print("Result:", x-y)
elif ch=="*": print("Result:", x*y)
elif ch=="exit": print("Bye")
else: print("Bad")
