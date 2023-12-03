import numpy as np
import matplotlib.pyplot as plt

# Пример 1: Движение и Скорость
t = np.linspace(0, 5, 100)
s = 2 * t**2  # Пример функции положения

plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(t, s, label='Положение $s(t)$')
plt.title('График Положения')
plt.xlabel('Время $t$')
plt.ylabel('Положение $s$')
plt.legend()

# Рассчитываем производную (скорость)
v = np.gradient(s, t)

plt.subplot(1, 2, 2)
plt.plot(t, v, label='Скорость $v(t)$', color='orange')
plt.title('График Скорости (производной)')
plt.xlabel('Время $t$')
plt.ylabel('Скорость $v$')
plt.legend()

plt.tight_layout()
plt.show()

# Пример 2: Температурные Изменения и Тепловой Поток
x = np.linspace(0, 10, 100)
T = -0.5 * (x - 5)**2 + 25  # Пример функции температуры

plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(x, T, label='Температура $T(x)$')
plt.title('График Температуры')
plt.xlabel('Координата $x$')
plt.ylabel('Температура $T$')
plt.legend()

# Рассчитываем производную (тепловой поток)
dT_dx = np.gradient(T, x)

plt.subplot(1, 2, 2)
plt.plot(x, dT_dx, label='Тепловой Поток $\dfrac{dT}{dx}$', color='orange')
plt.title('График Теплового Потока (производной)')
plt.xlabel('Координата $x$')
plt.ylabel('Тепловой Поток $\dfrac{dT}{dx}$')
plt.legend()

plt.tight_layout()
plt.show()