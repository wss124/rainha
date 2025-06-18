# 🔢 Definições para o problema das N Rainhas

def eh_seguro(tabuleiro, linha, coluna, N):
    # Verificar linha à esquerda
    for i in range(coluna):
        if tabuleiro[linha][i] == 'R':
            return False

    # Verificar diagonal superior à esquerda
    for i, j in zip(range(linha, -1, -1), range(coluna, -1, -1)):
        if tabuleiro[i][j] == 'R':
            return False

    # Verificar diagonal inferior à esquerda
    for i, j in zip(range(linha, N), range(coluna, -1, -1)):
        if tabuleiro[i][j] == 'R':
            return False

    return True


def resolver_rainhas(tabuleiro, coluna, N):
    if coluna >= N:
        return True

    for i in range(N):
        if eh_seguro(tabuleiro, i, coluna, N):
            tabuleiro[i][coluna] = 'R'
            if resolver_rainhas(tabuleiro, coluna + 1, N):
                return True
            tabuleiro[i][coluna] = '.'  # backtrack

    return False


# ♞ Definições para o Passeio do Cavalo

movimentos_cavalo = [
    (2, 1), (1, 2), (-1, 2), (-2, 1),
    (-2, -1), (-1, -2), (1, -2), (2, -1)
]


def passeio_cavalo(tabuleiro, linha, coluna, visitados, N):
    if len(visitados) == sum(row.count('.') for row in tabuleiro):
        return True

    for dx, dy in movimentos_cavalo:
        nova_linha = linha + dx
        nova_coluna = coluna + dy

        if (0 <= nova_linha < N) and (0 <= nova_coluna < N):
            if tabuleiro[nova_linha][nova_coluna] == '.' and (nova_linha, nova_coluna) not in visitados:
                visitados.add((nova_linha, nova_coluna))
                if passeio_cavalo(tabuleiro, nova_linha, nova_coluna, visitados, N):
                    return True
                visitados.remove((nova_linha, nova_coluna))

    return False


# 📦 Funções auxiliares

def criar_tabuleiro(N):
    return [['.' for _ in range(N)] for _ in range(N)]


def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(' '.join(linha))
    print()


# 🚀 Função principal

def main():
    print("\n--- Problema das N Rainhas + Passeio do Cavalo ---\n")
    N = int(input("Digite o valor de N para o tabuleiro NxN: "))
    tabuleiro = criar_tabuleiro(N)

    # Resolver o problema das N Rainhas
    if not resolver_rainhas(tabuleiro, 0, N):
        print(f"Não foi possível posicionar as rainhas para N = {N}")
        return
    else:
        print("\n✅ Posicionamento das Rainhas:")
        imprimir_tabuleiro(tabuleiro)

    # Definir posição inicial do cavalo
    linha = int(input(f"Digite a linha inicial do cavalo (0 a {N-1}): "))
    coluna = int(input(f"Digite a coluna inicial do cavalo (0 a {N-1}): "))

    if tabuleiro[linha][coluna] == 'R':
        print("❌ Posição inválida! Está ocupada por uma rainha.")
        return

    visitados = set()
    visitados.add((linha, coluna))

    if passeio_cavalo(tabuleiro, linha, coluna, visitados, N):
        print("\n✅ O cavalo CONSEGUIU visitar todas as posições livres!")
    else:
        print("\n❌ O cavalo NÃO conseguiu visitar todas as posições livres.")


if __name__ == "__main__":
    main()
