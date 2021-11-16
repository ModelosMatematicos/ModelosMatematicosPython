import numpy as np                                                              #Importa a biblioteca numpy.
import matplotlib.pyplot as plt                                                 #Importa o módulo pyplot da biblioteca matplotlib.
import matplotlib.patches as mp                                                 #Importa o módulo patches da biblioteca matplotlib.
import scipy.integrate as scp                                                   #Importa o módulo integrate da biblioteca scipy.
k1 = 0.25                                                                       #Taxa de crescimento do modelo MCPE.
Time = np.linspace(0, 50, 5000)                                                 #intervalo do modelo.
def equations(t, y):                                                            #Define a função cresc_exponencial(y, t) no qual t é o tempo e y é uma lista com os valores da população.
  dydt = k1*t                                                                   #Equação correspondente a derivada de y com relação ao tempo.
  return np.array([dydt], float)                                                #Retorna um vetor com a derivada de y no tempo t.
r0 = [50]                                                                       #condição inicial para o modelo MCPE.
solution = scp.solve_ivp(equations, [0, Time[-1]], r0, t_eval=Time)             #Calcula a solução numérica de cresc_exponencial(y, t) com y(0)=y0 no intervalo [0, 50].
fig = plt.figure(figsize=( 5, 5))                                               #Define o tamanho com gráfico em 5 polegadas.
plt.plot(Time,solution.y[0],"b")                                                #Imprime y(t) no intervalo [0,50].
blue_patch = mp.Patch(color="blue", label="População")                          #Constrói legenda para y(t).
plt.legend(handles=[blue_patch])                                                #Coloca as legendas no gráfico.
plt.title("Modelo Populacional Exponencial")                                    #Adiciona o título no gráfico.
plt.xlabel("Tempo")                                                             #Adiciona o texto do eixo do x.
plt.ylabel("Populacão")                                                         #Adiciona o texto do eixo do y.
plt.show()                                                                      #Imprime o gráfico.
