print("Введите координату x: ")
x=int(input())
print("Введите коор:динату y")
y=int(input())
if x > 0 and y>0:
  print("Первая четверть")
elif x<0 and y>0:
  print("Вторая четверть") 
elif x < 0 and y<0:
  print("Третья четверть")
elif x>0 and y<0:
  print("Четвертая четверть") 
