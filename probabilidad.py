import numpy as np
import matplotlib.pyplot as plt
#arreglo con los x dados en donde caen las particulas
x = np.array([1.2, 2.5, 2.8, 5.0])
#probabilidad de pl asignada arbitrariamente
pl = 1
#medida del vidrio en donde caen las particulas
x0 = 1
x1 = 20
#funcion que me retorna la constante de normalizacion dado un lambda, la probabilidad asignada, y la medida en donde caen las particulas
def nnorm(pl, x0, x1, lam):
	return (pl*(np.exp(-1/lam)-np.exp(-20/lam)))
#funcion que retorna un valor de probabilidad dado un lambda y una posicion en x
def fun(pl, lam, n, x):
	return pl/(n*lam)*(np.exp(-x/lam))
#lambdas distintos a evaluar y a graficar
lam = np.linspace(1, 10, 10)
#generacion de grafica para distintos lambdas
for i in range(len(lam)):
	n = nnorm(pl, x0, x1, lam[i])
	plt.plot(x, fun(pl, lam[i], n, x), label = "lambda = " + str(lam[i]) )
	plt.xlabel("posicion en x")
	plt.ylabel("probabilidad de lambda")
	plt.legend(loc = 0)
plt.savefig("grafica")

