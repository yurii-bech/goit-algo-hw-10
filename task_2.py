import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа
n = 100000  # Кількість випробувань

# Генерація випадкових точок
x_rand = np.random.uniform(a, b, n)
y_rand = np.random.uniform(0, f(b), n)

# Підрахунок точок, що потрапляють під криву
count = np.sum(y_rand <= f(x_rand))

# Обчислення площі під кривою
area = count / n * (b - a) * f(b)

# Використання функції quad для обчислення інтеграла
integral, _ = quad(f, a, b)

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

print("Значення інтеграла методом Монте-Карло:", area)
print("Значення інтеграла за допомогою quad:", integral)