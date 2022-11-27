# Напишите программу для проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. 
# ¬ - Отрицание 
# ⋁ - логическое "Или" 
# ⋀ - логическое "И"

xe = [True, False]
ye = [True, False]
ze = [True, False]

for x in xe:
    for y in ye:
        for z in ze:
            print(x, y, z)
            print(not (x or y or z) == ((not x) and (not y) and (not z)))

