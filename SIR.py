import numpy as np                                                              #Importa a biblioteca numpy.
import matplotlib.pyplot as plt                                                 #Importa o módulo pyplot da biblioteca matplotlib.
import matplotlib.patches as mp                                                 #Importa o módulo patches da biblioteca matplotlib.
import scipy.integrate as scp                                                   #Importa o módulo integrate da biblioteca scipy.
alpha = 0.005                                                                   #Parâmetro alpha das equações que descrevem o modelo SIR
beta = 0.2                                                                      #Parâmetro beta das equações que descrevem o modelo SIR
time = np.linspace(0,80,1000)                                                   #intervalo de tempo do modelo SIR.
def equations(t, y):                                                            #Define a função F(t,y) no qual t é o tempo e y é uma lista com os valores de S,I e R.
 S,I,R = y                                                                      #Escreve nas variáveis S,I e R o valores atuais de y.
 dSdt = -alpha*S*I                                                              #Equação correspondente a derivada de S com relação ao tempo.
 dIdt = alpha*S*I - beta*I                                                      #Equação correspondente a derivada de I com relação ao tempo.
 dRdt = beta*I                                                                  #Equação correspondente a derivada de R com relação ao tempo.
 return np.array([dSdt,dIdt,dRdt], float)                                       #Retorna um vetor com as derivadas de S,I e R no tempo t.
y0 = np.array([99,1,0], float)                                                  #condição inicial para o modelo SIR.
solution = scp.solve_ivp(equations, [0,time[-1]], y0, t_eval = time)            #Calcula a solução numérica de F(t,y) com para y(0)=y0 no intervalo [0, 80].
fig = plt.figure(figsize=( 5, 5))                                               #Define o tamanho com gráfico em 5 polegadas.
black_patch = mp.Patch(color='black', label='Suscetíveis')                      #Constrói legenda para S(t).
red_patch = mp.Patch(color='red', label='Infectados')                           #Constrói legenda para I(t).
blue_patch = mp.Patch(color='blue', label='Recuperados')                        #Constrói legenda para R(t).
plt.legend(handles=[black_patch,red_patch,blue_patch])                          #Coloca as legendas no gráfico.
plt.title("Modelo SIR")                                                         #Adiciona o título no gráfico.
plt.xlabel("Tempo")                                                             #Adiciona o texto do eixo do x.
plt.ylabel("População")                                                         #Adiciona o texto do eixo do y.
plt.plot(time,solution.y[0], color="black")                                     #Imprime S(t) no intervalo [0,80].
plt.plot(time,solution.y[1], color="red")                                       #Imprime I(t) no intervalo [0,80].
plt.plot(time,solution.y[2],color="blue")                                       #Imprime R(t) no intervalo [0,80].
plt.show()                                                                      #Imprime o gráfico.
