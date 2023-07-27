import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10*np.pi, 1000)

x_t = np.sin(t)

tau = np.pi

x_tau = np.sin(t + tau)


plt.figure(figsize=(8, 8))
plt.plot(x_t, x_tau)
plt.xlabel('x(t)')
plt.ylabel('x(t+Tau)')
plt.title('x(t) = (x(t), x(t+Tau)')
plt.grid(True)
plt.savefig('tau.jpg')
