import numpy as np 
import matplolib.pyplot as plt 

plt.style.use('seaborn')

def fourier(x,n):
    m = 2*n-1 # numero  impar
    f = (4/np.pi)*(1/m)*np.sin(m*np.pi*x/l) # serie de fourier

l = np.pi #comprimento do ciclo
ciclos = 2 #quantidade de ciclos
x = np.linspace(0, 2*l*ciclos,1000)

f = 0 # primeiro valor da serie
n = 1 # primeiro valor da iteração
n_total = 5 # quantidade de iteraçoes

while n<n_total:
    f += fourier(x,n)
    plt.plot(x, f, label="n = {}".format(2*n-1))
    n += 1