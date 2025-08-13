name = str(input("enter your name: "))
age = int(input("enter your age: "))
print(f"hello {name},you are {age} years old")

if (age<18):
  print("you are not old enough to give the bill")
else:
  print("you can give the bill thanks")

print("\nhere's your bill")

item1 = int(input("enter price of item1: "))
item2 = int(input("enter price of item2: "))
item3 = int(input("enter price of item3: "))

total = item1 +item2+ item3
print("\nthe total price is",total)

average = total/3
print("\nthe average price is",average)

tax = total*0.15
print("\nthe tax is",tax)

print("\nthe grand total is",total+tax)

print("\nthanks for the shopping anyway")



