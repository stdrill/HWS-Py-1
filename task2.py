# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

flag = True
for x in [0,1]:
    for y in [0,1]:
        for z in [0,1]:
            f1 = not(x or y or z)
            f2 = not(x) and not(y) and not(z)
            print(x, y, z)
            if f1 != f2:
                flag = False
if flag:
    print('True')
else:
    print('False')