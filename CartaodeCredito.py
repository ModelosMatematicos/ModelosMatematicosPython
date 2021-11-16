import numpy as np                                                              #Importa a biblioteca numpy.
import matplotlib.pyplot as plt                                                 #Importa o módulo pyplot da biblioteca matplotlib.
import matplotlib.patches as mp                                                 #Importa o módulo patches da biblioteca matplotlib.
import sympy as sp                                                              #Importa a biblioteca sympy.
x = sp.Symbol("x")                                                              #Define o símbolo para a biblioteca sympy.
a11 = float(sp.integrate((1), [x,0,1]))                                         #Calcula a integral de f(x)=1 no intervalo [0,1] na variável x e define como a entrada a11 da matriz A.
a12 = float(sp.integrate(x, [x,0,1]))                                           #Calcula a integral de f(x)=x no intervalo [0,1] na variável x e define como a entrada a12 da matriz A.
a21 = a12                                                                       #Define como a entrada a21 igual a entrada a12 da matriz A.
a22 = float(sp.integrate(x**2, [x,0,1]))                                        #Calcula a integral de f(x)=x² no intervalo [0,1] na variável x e define como a entrada a22 da matriz A.
A = np.array([[a11,a12],[a21,a22]])                                             #Define a matriz A.
b11 = float(4*sp.integrate(x**3, [x,0,1]))                                      #Calcula a integral de f(x)=4x³ no intervalo [0,1] na variável x e define como a entrada b11 da matriz B.
b21 = float(4*sp.integrate(x**4, [x,0,1]))                                      #Calcula a integral de f(x)=4x⁴ no intervalo [0,1] na variável x e define como a entrada b21 da matriz B.
B = np.array([b11,b21])                                                         #Define a matriz B.
S = np.linalg.solve(A, B)                                                       #Calcula a solução do sistema A.X=B.
poly = np.poly1d(np.flip(S))                                                    #Constrói um polinômio a partir de um vetor de coeficientes.
fig = plt.figure(figsize=( 5, 5))                                               #Define o tamanho com gráfico em 5 polegadas.
t = np.linspace(0,1,5000)                                                       #Cria um vetor com uma partição do intervalo [0,1] com 5000 pedaços.
plt.plot(t,4*t**3,color= "red")                                                 #Imprime a curva que descreve os dados.
plt.plot(t,poly(t),color= "blue")                                               #Imprime o polinômio resultante do ajuste.
greenpatch = mp.Patch(color= "red", label= "Dados")                             #Constrói legenda para os dados.
orangepatch = mp.Patch(color= "blue", label= "Reta de Ajuste")                  #Constrói legenda para a reta de ajuste.
plt.legend(handles=[greenpatch, orangepatch])                                   #Coloca as legendas no gráfico.
plt.title("Ajuste dados Contínuos")                                             #Adiciona o título no gráfico.
plt.xlabel("Tempo")                                                             #Adiciona o texto do eixo do x.
plt.ylabel("Juros")                                                             #Adiciona o texto do eixo do y.
plt.show()                                                                      #Imprime o gráfico.
