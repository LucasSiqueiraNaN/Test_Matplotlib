from random import randrange
import matplotlib.pyplot as plt

notas_matematica = []
for notas in range(8):
    notas_matematica.append(randrange(1, 10))

x = list(range(1, 9))
y = notas_matematica

plt.plot(x, y, marker='o')
plt.xlabel('Provas')
plt.ylabel('Notas')
plt.title('Notas Matematica')
plt.show()
