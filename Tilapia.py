import numpy as np                                                              #Importa a biblioteca numpy.
import matplotlib.pyplot as plt                                                 #Importa o módulo pyplot da biblioteca matplotlib.
import matplotlib.patches as mp                                                 #Importa o módulo patches da biblioteca matplotlib.
meidan_age = np.array([0, 1,2, 3, 4, 5, 6, 7, 8])                               #Dados das idades.
meidan_size = np.array([11.0, 15, 17.4, 20.6, 22.7,25.3, 27.4, 28.2, 29.3])     #Dados dos tamanhos.
fit = np.polyfit(meidan_age,meidan_size,1)                                      #Ajuste um polinômio para pontos (x, y) e retorna um vetor de coeficientes.
poly = np.poly1d(fit)                                                           #Constrói um polinômio a partir de um vetor de coeficientes.
x_poly = np.linspace(meidan_age[0],meidan_age[-1],100)                          #Cria um vetor com uma partição do eixo do x.
y_poly = poly(x_poly)                                                           #Aplica o polinômio no vetor com a partição do eixo do x.
fig = plt.figure(figsize=(5, 5))                                                #Define o tamanho com gráfico em 5 polegadas.
plt.plot(x_poly, y_poly, color="blue")                                          #Imprime o polinômio resultante do ajuste.
plt.plot(meidan_age,meidan_size,color="red", marker="^", linewidth=0.0)         #Imprime os pontos que queremos ajustar.
red_patch = mp.Patch(color= "red", label="Dados")                               #Constrói legenda para os dados.
steel_blue_patch = mp.Patch(color= "steelblue",label= "Reta de Ajuste")         #Constrói legenda para a curva.
plt.legend(handles=[red_patch, steel_blue_patch])                               #Coloca as legendas no gráfico.
plt.title("Ajuste Tilápia com a Numpy")                                         #Adiciona o título no gráfico.
plt.xlabel("Idade")                                                             #Adiciona o texto do eixo do x.
plt.ylabel("Comprimento")                                                       #Adiciona o texto do eixo do y.
plt.show()                                                                      #Imprime o gráfico.
