
def novo_ponto(x, y, direcao):
    # print("novoPonto   x: {} - y:{} - direcao: {}".format(x, y, direcao))

    if direcao == 'N':
        return x, y + 1
    if direcao == 'S':
        return x, y - 1
    if direcao == 'E':
        return x + 1, y
    if direcao == 'W':
        return x - 1, y


def calcula_movimento(inicio, percurso):
    # print("Inicio: {} - Percurso: {}".format(inicio, percurso))
    pos_x = inicio[0]
    pos_y = inicio[1]
    direcao = inicio[2]

    for p in percurso:
        if direcao == 'N' and p == 'L':
            direcao = "W"
        elif direcao == 'N' and p == 'R':
            direcao = "E"
        elif direcao == 'E' and p == 'L':
            direcao = "N"
        elif direcao == 'E' and p == 'R':
            direcao = "S"
        elif direcao == 'S' and p == 'L':
            direcao = "E"
        elif direcao == 'S' and p == 'R':
            direcao = "W"
        elif direcao == 'W' and p == 'L':
            direcao = "S"
        elif direcao == 'W' and p == 'R':
            direcao = "N"
        elif p == 'M':
            resp = novo_ponto(pos_x, pos_y, direcao)
            pos_x = resp[0]
            pos_y = resp[1]
            # print("resp: {}".format(resp))
        # print("calculaMovimento  x: {} - y:{} - direcao: {}".format(posX, posY, direcao))
    return [pos_x, pos_y, direcao]
    # print("Posicao Final  x:{} - y:{} - direcao:{}".format(posX, posY, direcao))


areaPlanalto = [5, 5]
sonda1PosInicial = [1, 2, "N"]
sonda1Movimentacao = ["L", "M", "L", "M", "L", "M", "L", "M", "M"]
sonda2PosInicial = [3, 3, "E"]
sonda2Movimentacao = ["M", "M", "R", "M", "M", "R", "M", "R", "R", "M"]

if __name__ == '__main__':
    print("sonda 1:")
    print(calcula_movimento(sonda1PosInicial, sonda1Movimentacao))
    print("sonda 2:")
    print(calcula_movimento(sonda2PosInicial, sonda2Movimentacao))
