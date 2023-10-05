import numpy as np
import matplotlib.pyplot as plt

n = 3 # politropo
dxi = 0.001 # passo
xi_max = 1000 # valor superior da integral 

# Arrays
xi = np.arange(0.01, xi_max + dxi, dxi)
D = np.zeros_like(xi)
dD_dxi = np.zeros_like(xi)

# Condições Fronteira
dD_dxi[0] = 0
D[0] = 1

# Integração Numérica
for i in range(xi_max):
    dD_dxi[i+1] = -(xi[i]**2)*(D[i]**n) *dxi # Primeira integral * passo
    D[i+1] = dD_dxi[i+1]/(xi[i]**2) *dxi # Segunda integral * passo
    xi[i+1] = xi[i] + dxi # atualizar passo
    
# Plot
plt.plot(xi,D)
plt.xlabel(r"$\xi = r/\lambda_n$")
plt.ylabel(r"$D=\rho/\rho_c$")
plt.title("Politropo n=3")
plt.grid(True)
plt.show()


