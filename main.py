def novo_ponto(x, y, direcao):
    if direcao == 'N':
        return x, y + 1
    if direcao == 'S':
        return x, y - 1
    if direcao == 'E':
        return x + 1, y
    if direcao == 'W':
        return x - 1, y


def calcula_movimento(inicio, percurso):
    pos_x = int(inicio[0])
    pos_y = int(inicio[1])
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
    return [str(pos_x), str(pos_y), direcao]


def menu():
    continua = True
    pos_inicial = input('entre com a posicao inicial das sondas: ')
    i = 0
    sondas = []
    while continua:
        sonda_pos_inicial = input('sonda {} posicao inicial: '.format(i + 1))
        sonda_movimentacao = input('sonda {} movimentacao: '.format(i + 1))
        resp = input('adicionar dados de mais uma sonda [S/N] ?')
        sondas.append((sonda_pos_inicial, sonda_movimentacao))
        i += 1
        if resp.upper() == 'N':
            break

    return pos_inicial, sondas

def processa_movimentos(movimentos):
    pos_inicial = movimentos[0].split(' ')
    sondas = movimentos[1]
    for s in sondas:
        movs = list(s[1].strip())
        resp = calcula_movimento(s[0].split(' '), movs)
        print(' '.join(resp))


if __name__ == '__main__':
    movimentos = menu()
    processa_movimentos(movimentos)

