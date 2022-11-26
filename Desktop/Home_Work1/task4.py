print("Введите немер четверти: ")
x=int(input())
if x == 1:
  print("X>0 и Y>0")
if x==2:
  print("X<0 и Y>0") 
if x== 3:
  print("X<0 и Y<0")
if x==4:
  print("X>0 и Y<0") 
if x > 4 or x<=0:
  print("такой четверти нет")
