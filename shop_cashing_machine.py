i = 1
coffee = 2500
water = 1000
orange_juice = 2000
tea = 1500
lst = []
total = 0

while i>0:
  order = input()
  if order == "coffee":
    cof_amount = int(input())
    total_cof = coffee * cof_amount
    lst.append(total_cof)
  elif order == 'water':
    wat_amount = int(input())
    total_wat = water * wat_amount
    lst.append(total_wat)
  elif order == 'orange juice':
    or_amount = int(input())
    total_or = orange_juice * or_amount
    lst.append(total_or)
  elif order == 'tea':
    tea_amount = int(input())
    total_tea = tea * tea_amount
    lst.append(total_tea)
  elif order == 'end':
    break

for i in lst:
  total += i

print(total)