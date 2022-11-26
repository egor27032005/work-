print("Введите координаты x и y первой точки: ")
x1=int(input())
y1=int(input())
print("Введите координаты x и y второй точки: ")
x2=int(input())
y2=int(input())
length=((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))**0.5
print(round(length,2))