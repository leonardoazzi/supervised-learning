import numpy as np

def compute_mse(b, w, data):
    """
    Calcula o erro quadratico medio
    :param b: float - bias (intercepto da reta) (θ_0)
    :param w: float - peso (inclinacao da reta) (θ_1)
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :return: float - o erro quadratico medio
    """
    m = len(data) # número de amostras

    sqd_error = 0
    for x in data:
        h_theta = b + w * x[0]
        error = h_theta - x[1]
        sqd_error = sqd_error + error ** 2

    mse = sqd_error / m

    return mse

def step_gradient(b, w, data, alpha):
    """
    Executa uma atualização por descida do gradiente  e retorna os valores atualizados de b e w.
    :param b: float - bias (intercepto da reta)
    :param w: float - peso (inclinacao da reta)
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :return: float,float - os novos valores de b e w, respectivamente
    """
    m = len(data) # número de amostras

    ## derivada parcial da função de custo em relação ao bias
    pd_bias = 0
    for x in data:
        h_theta = b + w * x[0]
        error_bias = h_theta - x[1]
        next_error_bias = 2 * error_bias
        pd_bias = pd_bias + next_error_bias

    new_b = pd_bias / m
      
    updated_b = b - alpha * new_b

    ## derivada parcial da função de custo em relação ao peso
    pd_weight = 0
    for x in data:
        h_theta = b + w * x[0]
        error_weight = h_theta - x[1]
        next_error_weight = 2 * x[0] * error_weight
        pd_weight = pd_weight + next_error_weight
    new_w = pd_weight / m

    updated_w = w - alpha * new_w

    return updated_b, updated_w

def fit(data, b, w, alpha, num_iterations):
    """
    Para cada época/iteração, executa uma atualização por descida de
    gradiente e registra os valores atualizados de b e w.
    Ao final, retorna duas listas, uma com os b e outra com os w
    obtidos ao longo da execução (o último valor das listas deve
    corresponder à última época/iteração).

    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param b: float - bias (intercepto da reta)
    :param w: float - peso (inclinacao da reta)
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :param num_iterations: int - numero de épocas/iterações para executar a descida de gradiente
    :return: list,list - uma lista com os b e outra com os w obtidos ao longo da execução
    """
    trained_bias = []
    trained_weights = []

    for n in range(0, num_iterations):
        b, w = step_gradient(b, w, data, alpha)
        trained_bias.append(b)
        trained_weights.append(w)

    print(trained_bias, trained_weights)

    return trained_bias, trained_weights