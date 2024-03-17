from pulp import LpMaximize, LpProblem, LpVariable

# Створюємо проблему максимізації
problem = LpProblem("Maximize Production", LpMaximize)

# Створюємо змінні рішення - кількість одиниць лимонаду та фруктового соку
x1 = LpVariable("Lemonade", lowBound=0, cat='Integer')  # Кількість одиниць лимонаду
x2 = LpVariable("Fruit Juice", lowBound=0, cat='Integer')  # Кількість одиниць фруктового соку

# Функція мети - максимізація кількості вироблених продуктів
problem += x1 + x2, "Total Production"

# Обмеження на використання ресурсів
problem += 2 * x1 + x2 <= 100, "Water Constraint"
problem += x1 <= 50, "Sugar Constraint"
problem += x1 <= 30, "Lemon Juice Constraint"
problem += 2 * x2 <= 40, "Fruit Puree Constraint"

# Вирішуємо задачу оптимізації
problem.solve()

# Виводимо результати
print("Optimal Production Plan:")
print(f"Lemonade: {x1.varValue} units")
print(f"Fruit Juice: {x2.varValue} units")