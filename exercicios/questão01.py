def calcular_media(notas):
    try:
        with open(notas, 'r') as arquivo:
            notas = [int(line.strip()) for line in arquivo]
            if not notas:
                print("O arquivo está vazio.")
                return None
            media = sum(notas) / len(notas)
            return media
    except FileNotFoundError:
        print(f"Arquivo '{notas}' não encontrado.")
        return None
    except ValueError:
        print("Erro ao ler as notas. Certifique-se de que o arquivo contém apenas números inteiros.")
        return None

# Exemplo de uso:
notas = "exercicios/notas.txt"
media_notas = calcular_media(notas)

if media_notas is not None:
    print(f"A média das notas no arquivo '{notas}' é: {media_notas}")
