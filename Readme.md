Aprendizagem Supervisionada
---

Leonardo Azzi Martins, 00323721, Turma A

Alisson Claudino de Jesus, 00246796, Turma A

Vitor Pedrollo dos Santos, 00312948, Turma A

# **Regressão Linear**

| Parâmetro    | Valor |
| -------- | ------- |
| Bias | 0.803184 |
| Weight  | 0.724285    |
| Alpha | 0.01     |
| Número de iterações    | 1000    |
| EQM | 8.530213277569304 |

# **Redes Neurais**

## CIFAR-10
O CIFAR-10 é um dataset que contém 60000 imagens RGB 32x32 pixels, divididas entre 10 classes (6000 imagens cada). O dataset já disponibilizado como um conjunto de treino com 50.000 imagens e um conjunto de teste com 10.000 imagens.

As 10 classes são divididas entre veículos humanos como aviões, navios e carros, e animais, como pássaros, cachorros e gatos.

https://www.cs.toronto.edu/~kriz/cifar.html


| Número de classes    | Número de amostras | Tamanho das imagens |
| -------- | ------- | ------- |
| 10 | 60.000, 6.000 por classe | (32, 32, 3)

### Configuração 0

Vamos começar com uma rede convolucional simples, sugerida pelo professor no kit do trabalho:
- 1x camada convolucional com 32 filtros 3x3
- Max Pooling 2x2
- Camada flatten
- MLP com 64 neuronios
- MLP com 10 neurônios - softmax (saída)

Apenas uma camada convolucional não é suficiente para a tarefa deste dataset.

$$
\begin{array}{|c|c|} \hline
Setup & test acc & test loss & trainingTime \\ \hline
0 & 0.3320 & 1.6574 & 84.766\\ \hline
\end{array}
$$

### Configuração 1
Adicionamos mais camadas convolucionais, para tentar aprender mais filtros e, consequentemente, características mais complexas das imagens.
- 3x camadas convolucionais com 32 filtros 3x3
- Max Pooling 2x2
- Camada flatten
- MLP com 64 neuronios
- MLP com 10 neurônios - softmax (saída)

A acurácia do conjunto de teste apresentou ganhos. Porém, o erro no conjunto de teste e validação ficaram altos e tendiam a aumentar, o que não é desejável. Ainda estamos em underfit.

$$
\begin{array}{|c|c|} \hline
Setup & test acc & test loss & trainingTime \\ \hline
0 & 0.3320 & 1.6574 & 84.766\\ \hline
1 & 0.5866 & 1.9993 & 85.073 \\\hline
\end{array}
$$

### Configuração 2
Mesmo com mais camadas convolucionais, ainda não tivemos ganho suficiente. Triplicamos as camadas, com o mesmo número de filtros, mas aumentando o tamanho ao longo das camadas, para tentar aprender características mais gerais e abstratas.

- 1x camada convolucional com 32 filtros 3x3
- 1x camada convolucional com 32 filtros 7x7
- 1x camada convolucional com 32 filtros 11x11
- Max Pooling 2x2
- Camada flatten
- MLP com 64 neuronios
- MLP com 10 neurônios - softmax (saída)

Apesar de retomarmos o padrão de descida do erro no dataset de validação, ele estabiliza a partir da epoch 3, não indicando que acompanharia o erro do dataset de treino. O mesmo se observa na acurácia, a partir da mesma epoch.

$$
\begin{array}{|c|c|} \hline
Setup & test acc & test loss & trainingTime \\ \hline
0 & 0.3320 & 1.6574 & 84.766\\ \hline
1 & 0.5866 & 1.9993 & 85.073 \\\hline
2 & 0.5155 & 1.4969 & 84.731 \\ \hline
\end{array}
$$

### Configuração 3
Tivemos alguns sinais trabalhando o tamanho de filtros profundos. Podemos também progredir com o número de filtros de forma profunda, para aumentar sua capacidade de identificar características diferentes em cada camada.
- 1x camada convolucional com 32 filtros 3x3
- 1x camada convolucional com 64 filtros 7x7
- 1x camada convolucional com 128 filtros 11x11
- Max Pooling 2x2
- Camada flatten
- MLP com 64 neuronios
- MLP com 10 neurônios - softmax (saída)

Diminuimos a acurácia e aumentamos um pouco o erro, além de que podemos observar um padrão estranho nos plots. Talvez a rede ainda esteja relativamente simples para a complexidade oferecida pelo dataset. Curiosamente, este foi o treinamento mais demorado dos 5 setups.

$$
\begin{array}{|c|c|} \hline
Setup & test acc & test loss & trainingTime \\ \hline
0 & 0.3320 & 1.6574 & 84.766\\ \hline
1 & 0.5866 & 1.9993 & 85.073 \\\hline
2 & 0.5155 & 1.4969 & 84.731 \\ \hline
3 & 0.4437 & 1.5709 & 144.646 \\ \hline
\end{array}
$$

### Configuração 4
A estratégia foi adicionar mais camadas convolucionais, para tentar aumentar a complexidade do modelo. Além disto, nos inspiramos em arquiteturas clássicas, como VGG, AlexNet, etc, trazendo padrões como a combinação Conv-Pool-Conv-Pool ou Conv-Conv-Pool. Outros padrões muito utilizados são a sequência de tamanho de filtros 32-64-128 ou 32-32-64-64.

Para esta configuração, trouxe alguns aspectos da VGG-16, com um padrão reduzido de 2 conv + pool e 3 conv + pool, pelo tamanho reduzido das imagens do dataset.

- 2x camadas convolucionais com 32 filtros 3x3
- Max Pooling 2x2, stride 2x2
- 3x camadas convolucionais com 64 filtros 3x3
- Max Pooling 2x2, stride 2x2
- Camada flatten
- MLP com 120 neuronios
- MLP com 84 neuronios
- MLP com 10 neurônios - softmax (saída)

Esta foi a configuração mais promissora até o momento. Poderíamos criar mais camadas ainda, mas um dos problemas é que a imagem acaba se reduzindo ao longo dos strides, perdendo algumas características das bordas ao longo das camadas convolucionais.

$$
\begin{array}{|c|c|} \hline
Setup & test acc & test loss & trainingTime \\ \hline
0 & 0.3320 & 1.6574 & 84.766\\ \hline
1 & 0.5866 & 1.9993 & 85.073 \\\hline
2 & 0.5155 & 1.4969 & 84.731 \\ \hline
3 & 0.4437 & 1.5709 & 144.646 \\ \hline
4 & 0.6885 & 0.9940 & 76.213 \\ \hline
\end{array}
$$

### Configuração 5
Podemos experimentar usar padding em algumas camadas, para considerar características mais próximas das bordas das imagens. Além disto, ajuda a preservar as dimensões de entrada da imagem, permitindo uma arquitetura mais profunda e tendendo a uma melhor performance.

- 2x camadas convolucionais com 32 filtros 3x3
- Max Pooling 2x2, stride 2x2
- 3x camadas convolucionais com 64 filtros 3x3
- Max Pooling 2x2, stride 2x2
- 3x camadas convolucionais com 128 filtros 3x3
- Max Pooling 2x2, stride 2x2
- Camada flatten
- MLP com 120 neuronios
- MLP com 84 neuronios
- MLP com 10 neurônios - softmax (saída)


### Resultados CIFAR-10

$$
\begin{array}{|c|c|} \hline
Setup & test acc & test loss & trainingTime \\ \hline
0 & 0.3320 & 1.6574 & 84.766\\ \hline
1 & 0.5866 & 1.9993 & 85.073 \\\hline
2 & 0.5155 & 1.4969 & 84.731 \\ \hline
3 & 0.4437 & 1.5709 & 144.646 \\ \hline
4 & 0.6885 & 0.9940 & 76.213 \\ \hline
5 & 0.7187 & 0.8870 & 145.902 \\ \hline
\end{array}
$$

## CIFAR-100

O CIFAR-100 é uma extensão do CIFAR-10, pois também contém 60000 imagens, mas divididas entre 100 classes (600 imagens cada). Também conta com imagens RGB, de tamanho 32x32 pixels.

O dataset já disponibiliza um conjunto de treino com 50.000 imagens e um conjunto de teste com 10.000 imagens.

As 100 classes são divididas em 20 super-classes bastante diversas, como fauna (aquáticos, peixes, insetos, répteis, mamíferos), flora (flores, árvores), e elementos humanos (pessoas, veículos, objetos manufaturados, etc).

A alta similaridade entre as classes dentro das superclasses faz deste um problema difícil de ser treinado (https://arxiv.org/pdf/2210.16914v1.pdf).

https://www.cs.toronto.edu/~kriz/cifar.html

| Número de classes    | Número de amostras | Tamanho das imagens |
| -------- | ------- | ------- |
| 100 | 60.000, 600 por classe | (32, 32, 3)

### Configuração 1
Para iniciar, a primeira intuição foi testar a arquitetura criada para o CIFAR-10 no dataset CIFAR-100. A única modificação foi na MLP de saída, com mais neurônios por camada e uma camada final com 100 neurônios para as 100 classes.

- 2x camadas convolucionais com 32 filtros 3x3
- Max Pooling 2x2, stride 2x2
- 3x camadas convolucionais com 64 filtros 3x3
- Max Pooling 2x2, stride 2x2
- 3x camadas convolucionais com 128 filtros 3x3
- Max Pooling 2x2, stride 2x2
- Camada flatten
- MLP com 256 neuronios
- MLP com 128 neuronios
- MLP com 100 neurônios - softmax (saída)

Inicialmente, me pareceu uma  tendência de descida das curvas de erro, e subida das curvas de acurácia, tanto em treino quanto em validação. Porém, testando com algumas epochs a mais, foi possível observar uma estabilização, tendendo a um plateau por volta de 23% e 25% de acurácia.

Sendo um dataset com diferenças entre classes cada vez mais sutis e que contém 10 vezes mais classes, o modelo precisa encontrar mais filtros e extrair mais features dos dados. Porém, se torna difícil realizar esta tarefa com apenas 600 imagens por classe, ao contrário das 6.000 do CIFAR-10.

- CIFAR-10
$$
\begin{array}{|c|c|} \hline
Setup & test acc & test loss & trainingTime \\ \hline
5 & 0.7187 & 0.8870 & 145.902 \\ \hline
\end{array}
$$

- CIFAR-100
$$
\begin{array}{|c|c|} \hline
Setup & test acc & test loss & trainingTime \\ \hline
1 & 0.2593 & 3.0888 & 146.951 \\ \hline
\end{array}
$$

### Configuração 2
Tentar com um outro padrão de arquitetura.

- 1x camada convolucional com 32 filtros 3x3
- Max Pooling 2x2, stride 2x2
- 1x camada convolucional com 128 filtros 3x3
- Max Pooling 2x2, stride 2x2
- 1x camada convolucional com 128 filtros 3x3
- Max Pooling 2x2, stride 2x2
- Camada flatten
- MLP com 512 neuronios
- MLP com 100 neurônios - softmax (saída)

Obtivemos um modelo pior, ainda em underfitting.

$$
\begin{array}{|c|c|} \hline
Setup & test acc & test loss & trainingTime \\ \hline
1 & 0.2593 & 3.0888 & 146.951 \\ \hline
2 & 0.2785 & 3.3499 & 85.152 \\ \hline
\end{array}
$$

### Configuração 3
Ajusta o hiperparâmetro de learning rate do otimizador Adam para 1e-4. Modifica as camadas, adicionando padding, trocando stride para 1x1.

- 1x camada convolucional com 32 filtros 3x3
- 1x camada convolucional com 64 filtros 3x3
- Max Pooling 2x2, stride 1x1
- 2x camada convolucionais com 128 filtros 3x3
- Max Pooling 2x2, stride 1x1
- 1x camada convolucional com 128 filtros 3x3
- Max Pooling 2x2, stride 1x1
- Camada flatten
- MLP com 512 neuronios
- MLP com 100 neurônios - softmax (saída)

O ajuste do learning rate trouxe um pequeno ganho, mas o modelo apresenta overfitting, com o erro crescendo.

$$
\begin{array}{|c|c|} \hline
Setup & test acc & test loss & trainingTime \\ \hline
1 & 0.2593 & 3.0888 & 146.951 \\ \hline
2 & 0.2785 & 3.3499 & 85.152 \\ \hline
3 & 0.3329 & 4.5566 & 85.638 \\ \hline
\end{array}
$$

### Resultados CIFAR-100

$$
\begin{array}{|c|c|} \hline
Setup & test acc & test loss & trainingTime \\ \hline
1 & 0.2593 & 3.0888 & 146.951 \\ \hline
2 & 0.2785 & 3.3499 & 85.152 \\ \hline
3 & 0.3329 & 4.5566 & 85.638 \\ \hline
\end{array}
$$

Este dataset é particularmente difícil de treinar sem técnicas um pouco mais sofisticadas. O CIFAR-100 contém apenas 600 amostras de cada classe, diferente das 6.000 do CIFAR-10. Além disto, as classes dentro de cada superclasse apresentam uma alta similaridade, o que torna a tarefa de classificação mais difícil.

Com isto, nossa hipótese é que os dados de treinamento são insuficientes para um treinamento satisfatório. Uma das possibilidades imediatas seria utilizar data augmentation para criar mais amostras das imagens por classe e facilitar a tarefa de treinamento. Além disto, existem outras técnicas, como batch normalization, que ainda poderiam ser exploradas para melhoria da acurácia. Outra possibilidade é o uso de transfer learning.

## MNIST

O MNIST é um dataset de dígitos escritos à mão, que contém 70.000 amostras, 60.000 no conjunto de treino e 10.000 no conjunto de teste. É composto por imagens monocromáticas 28x28 divididas em 10 classes, que representam os dígitos de 0 a 9.

| Número de classes    | Número de amostras | Tamanho das imagens |
| -------- | ------- | ------- |
| 10 | 70.000, 7.000 por classe | (28, 28, 1)

### Configuração 1
Usando uma rede neural simples.
- Flatten 28x28
- Camada densamente conectada, 128 neurônios, ativação ReLU
- Camada densamente conectada, 10 neurônios, ativação softmax (saída)

Com uma simples rede neural MLP, já atingimos uma acurácia de quase 95%, com um tempo de treinamento de menos de um minuto. Isto reforça a importância da exploração dos dados para definir as arquiteturas, pois muitas vezes menos é mais.

$$
\begin{array}{|c|c|} \hline
Setup & test acc & test loss & trainingTime \\ \hline
1 & 0.9478 & 0.2561 & 50.002 \\ \hline
\end{array}
$$

### Configuração 2
Usando uma rede neural convolucional simples.
- Camada convolucional com 32 filtros 3x3, ativação ReLU
- Max Pooling 2x2, stride 1x1
- Camada flatten
- MLP densamente conectada com 50 neurônios, ativação ReLU
- MLP densamente conectada com 10 neurônios, ativação softmax (saída)

Uma rede neural convolucional simples conseguiu melhorar em todos os aspectos.

$$
\begin{array}{|c|c|} \hline
Setup & test acc & test loss & trainingTime \\ \hline
1 & 0.9478 & 0.2561 & 50.002 \\ \hline
2 & 0.9778 & 0.1297 & 61.650 \\ \hline
\end{array}
$$

### Configuração 3
Aumentando a profundidade da rede neural convolucional.
- Camada convolucional com 32 filtros 3x3, ativação ReLU
- Max Pooling 2x2, stride 1x1
- Camada convolucional com 64 filtros 3x3, ativação ReLU
- Max Pooling 2x2, stride 1x1
- Camada flatten
- MLP densamente conectada com 50 neurônios, ativação ReLU
- MLP densamente conectada com 10 neurônios, ativação softmax (saída)

Conseguimos uma pequena melhoria na acurácia, mas uma diminuição interessante no erro. Todavia, observando o perfil do teste-validação, talvez esteja se aproximando de um overfitting.

$$
\begin{array}{|c|c|} \hline
Setup & test acc & test loss & trainingTime \\ \hline
1 & 0.9478 & 0.2561 & 50.002 \\ \hline
2 & 0.9778 & 0.1297 & 61.650 \\ \hline
3 & 0.9862 & 0.0705 & 83.641 \\ \hline
\end{array}
$$

### Configuração 4
Aumentando um pouco mais a profundidade da rede, tentando se aproximar de um overfitting.
- Camada convolucional com 32 filtros 3x3, ativação ReLU
- Max Pooling 2x2, stride 1x1
- Camada convolucional com 64 filtros 3x3, ativação ReLU
- Max Pooling 2x2, stride 1x1
- Camada convolucional com 128 filtros 3x3, ativação ReLU
- Max Pooling 2x2, stride 1x1
- Camada flatten
- MLP densamente conectada com 50 neurônios, ativação ReLU
- MLP densamente conectada com 10 neurônios, ativação softmax (saída)

Esta arquitetura mostrou pouco ganho em acurácia e diminuição de erro, além de apresentar um perfil mais irregular durante a validação.

$$
\begin{array}{|c|c|} \hline
Setup & test acc & test loss & trainingTime \\ \hline
1 & 0.9478 & 0.2561 & 50.002 \\ \hline
2 & 0.9778 & 0.1297 & 61.650 \\ \hline
3 & 0.9862 & 0.0705 & 83.641 \\ \hline
4 & 0.9822 & 0.0862 & 86.034 \\ \hline
\end{array}
$$

### Configuração 5
Aumentando um pouco mais a complexidade do modelo, tentando se aproximar de um overfitting.
- 2x Camada convolucional com 32 filtros 3x3, ativação ReLU
- Max Pooling 2x2, stride 1x1
- 2x Camada convolucional com 64 filtros 3x3, ativação ReLU
- Max Pooling 2x2, stride 1x1
- Camada convolucional com 128 filtros 3x3, ativação ReLU
- Max Pooling 2x2, stride 1x1
- Camada flatten
- MLP densamente conectada com 50 neurônios, ativação ReLU
- MLP densamente conectada com 10 neurônios, ativação softmax (saída)

Com um tempo significantemente maior de treinamento, esta arquitetura teve pequenos ganhos de acurácia, mas um ganho relativamente significativo de diminuição de erro. Ainda observamos um perfil irregular na validação, porém neste caso mais comportado.

$$
\begin{array}{|c|c|} \hline
Setup & test acc & test loss & trainingTime \\ \hline
1 & 0.9478 & 0.2561 & 50.002 \\ \hline
2 & 0.9778 & 0.1297 & 61.650 \\ \hline
3 & 0.9862 & 0.0705 & 83.641 \\ \hline
4 & 0.9822 & 0.0862 & 86.034 \\ \hline
5 & 0.9899 & 0.0407 & 146.842 \\ \hline
\end{array}
$$

## Resultados MNIST

Tanto com o uso de uma rede neural simples e enxuta, quanto com redes convolucionais grandes, o MNIST é um dataset fácil de ser trabalhado, a devido a sua baixa complexidade espacial, pequeno número de classes e baixa similaridade interclasses.

$$
\begin{array}{|c|c|} \hline
Setup & test acc & test loss & trainingTime \\ \hline
1 & 0.9478 & 0.2561 & 50.002 \\ \hline
2 & 0.9778 & 0.1297 & 61.650 \\ \hline
3 & 0.9862 & 0.0705 & 83.641 \\ \hline
4 & 0.9822 & 0.0862 & 86.034 \\ \hline
5 & 0.9899 & 0.0407 & 146.842 \\ \hline
\end{array}
$$

## Fashion MNIST

O Fashion MNIST é um dataset de imagens de produtos de moda, que contém 70.000 amostras, 60.000 no conjunto de treino e 10.000 no conjunto de teste. É composto por imagens monocromáticas 28x28 divididas em 10 classes de produtos diferentes, de forma similar ao dataset MNIST.

| Número de classes    | Número de amostras | Tamanho das imagens |
| -------- | ------- | ------- |
| 10 | 70.000, 7.000 por classe | (28, 28, 1)

### Configuração 1
Usando uma rede neural simples.
- Flatten 28x28
- Camada densamente conectada, 128 neurônios, ativação ReLU
- Camada densamente conectada, 10 neurônios, ativação softmax (saída)

$$
\begin{array}{|c|c|} \hline
    Setup & test acc & test loss & trainingTime \\ \hline
    1 & 0.8151 & 0.5496 & 84.925 \\ \hline
\end{array}
$$

### Configuração 2
Usando uma rede neural convolucional simples.
- Camada convolucional com 32 filtros 3x3, ativação ReLU
- Max Pooling 2x2, stride 1x1
- Camada flatten
- MLP densamente conectada com 50 neurônios, ativação ReLU
- MLP densamente conectada com 10 neurônios, ativação softmax (saída)

$$
\begin{array}{|c|c|} \hline
    Setup & test acc & test loss & trainingTime \\ \hline
    1 & 0.8151 & 0.5496 & 84.925 \\ \hline
    2 & 0.8854 & 0.3871 & 84.201 \\ \hline
\end{array}
$$

### Configuração 3
Aumentando a profundidade da rede neural convolucional.
- Camada convolucional com 32 filtros 3x3, ativação ReLU
- Max Pooling 2x2, stride 1x1
- Camada convolucional com 64 filtros 3x3, ativação ReLU
- Max Pooling 2x2, stride 1x1
- Camada flatten
- MLP densamente conectada com 50 neurônios, ativação ReLU
- MLP densamente conectada com 10 neurônios, ativação softmax (saída)

$$
\begin{array}{|c|c|} \hline
    Setup & test acc & test loss & trainingTime \\ \hline
    1 & 0.8151 & 0.5496 & 84.925 \\ \hline
    2 & 0.8854 & 0.3871 & 84.201 \\ \hline
    3 & 0.8882 & 0.3394 & 84.249 \\ \hline
\end{array}
$$

### Configuração 4
Aumentando um pouco mais a profundidade da rede, tentando se aproximar de um overfitting.
- Camada convolucional com 32 filtros 3x3, ativação ReLU
- Max Pooling 2x2, stride 1x1
- Camada convolucional com 64 filtros 3x3, ativação ReLU
- Max Pooling 2x2, stride 1x1
- Camada convolucional com 128 filtros 3x3, ativação ReLU
- Max Pooling 2x2, stride 1x1
- Camada flatten
- MLP densamente conectada com 50 neurônios, ativação ReLU
- MLP densamente conectada com 10 neurônios, ativação softmax (saída)

Esta configuração apresentou uma diminuição da acurácia e aumento do erro em relação a sua execução no MNIST.

O Fashion MNIST é um dataset mais desafiador que o MNIST, pois contém imagens com maior complexidade espacial, exigindo um modelo que extraia mais features para diferenciar melhor as classes.

$$
\begin{array}{|c|c|} \hline
Setup & test acc & test loss & trainingTime \\ \hline
1 & 0.8151 & 0.5496 & 84.925 \\ \hline
2 & 0.8854 & 0.3871 & 84.201 \\ \hline
3 & 0.8882 & 0.3394 & 84.249 \\ \hline
4 & 0.8787 & 0.3857 & 85.038 \\ \hline
\end{array}
$$

### Configuração 5
Aumentando um pouco mais a complexidade do modelo, tentando se aproximar de um overfitting.
- 2x Camada convolucional com 32 filtros 3x3, ativação ReLU
- Max Pooling 2x2, stride 1x1
- 2x Camada convolucional com 64 filtros 3x3, ativação ReLU
- Max Pooling 2x2, stride 1x1
- Camada convolucional com 128 filtros 3x3, ativação ReLU
- Max Pooling 2x2, stride 1x1
- Camada flatten
- MLP densamente conectada com 50 neurônios, ativação ReLU
- MLP densamente conectada com 10 neurônios, ativação softmax (saída)

$$
\begin{array}{|c|c|} \hline
    Setup & test acc & test loss & trainingTime \\ \hline
    1 & 0.8151 & 0.5496 & 84.925 \\ \hline
    2 & 0.8854 & 0.3871 & 84.201 \\ \hline
    3 & 0.8882 & 0.3394 & 84.249 \\ \hline
    4 & 0.8787 & 0.3857 & 85.038 \\ \hline
    5 & 0.9003 & 0.2858 & 145.299 \\ \hline
\end{array}
$$

### Resultados Fashion MNIST

O Fashion MNIST é um dataset mais desafiador que o MNIST, pois contém imagens com maior complexidade espacial, exigindo um modelo que extraia mais features para diferenciar melhor as classes.

- MNIST
$$
\begin{array}{|c|c|} \hline
Setup & test acc & test loss & trainingTime \\ \hline
1 & 0.9478 & 0.2561 & 50.002 \\ \hline
2 & 0.9778 & 0.1297 & 61.650 \\ \hline
3 & 0.9862 & 0.0705 & 83.641 \\ \hline
4 & 0.9822 & 0.0862 & 86.034 \\ \hline
5 & 0.9899 & 0.0407 & 146.842 \\ \hline
\end{array}
$$

- Fashion MNIST
$$
\begin{array}{|c|c|} \hline
Setup & test acc & test loss & trainingTime \\ \hline
1 & 0.8151 & 0.5496 & 84.925 \\ \hline
2 & 0.8854 & 0.3871 & 84.201 \\ \hline
3 & 0.8882 & 0.3394 & 84.249 \\ \hline
4 & 0.8787 & 0.3857 & 85.038 \\ \hline
5 & 0.9003 & 0.2858 & 145.299 \\ \hline
\end{array}

$$

---
Universidade Federal do Rio Grande do Sul

Instituto de Informática - Departamento de Informática Aplicada

Inteligência Artificial - Prof. Joel Luís Carbonera (2023/2)
