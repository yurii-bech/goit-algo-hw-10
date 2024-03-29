**Порівняльний аналіз результатів, отриманих за допомогою методу Монте-Карло та функції quad, дозволяє зробити наступні висновки:**

1. Значення інтеграла:
   - За допомогою методу Монте-Карло: 2.6644
   - За допомогою функції quad: 2.666666666666667

2. Порівняння точності:
   - Зауважимо, що обидва методи надають близькі результати, але точніше значення було отримане за допомогою функції quad. Це через те, що метод Монте-Карло ґрунтується на випадкових вибірках, тому точність його результатів може залежати від кількості випробувань `n`. У цьому випадку використано значення `n = 100000`, що є достатньо великим, але не завжди забезпечує максимальну точність.

**Висновки:**
   - Функція quad використовує чисельні методи, які базуються на більш складних математичних алгоритмах, ніж метод Монте-Карло. Тому результат, отриманий за допомогою quad, може бути більш точним в більшості випадків.
   - Для задач, де точність є важливою, варто використовувати більш точні методи, такі як функція quad. Однак метод Монте-Карло може бути корисним у випадках, коли інші методи недоступні або непридатні для використання.

Тому, в залежності від вимог до точності та доступних ресурсів, можна вибирати між методом Монте-Карло та чисельними методами, такими як функція quad, для обчислення інтегралів.