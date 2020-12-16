"""Arquivo principal que será interpretado pelo interpretador."""


def main():
    """Função principal que será rodada quando o script for passado para o interpretador."""
    # COLOQUE SEU CÓDIGO AQUI
    n_ligacoes = int(input("Digite o número de ligações que você fez: "))
    y = 0.6
    z = 0.5
    w = 0.4

    if n_ligacoes <= 100:
     valor = 200
     print(f"O valor devido é R$ {valor:.2f}.")
    elif n_ligacoes > 100 and n_ligacoes <= 150:
     valor = (n_ligacoes - 100) * y + 200
     print(f"O valor devido é R$ {valor:.2f}.")
    elif n_ligacoes > 150 and n_ligacoes <= 200:
     valor = (n_ligacoes - 150) * z + 230
     print(f"O valor devido é R$ {valor:.2f}.")
    else: 
     valor = (n_ligacoes - 200) * w + 255
     print(f"O valor devido é R$ {valor:.2f}.") 


if __name__ == '__main__':
    main()
