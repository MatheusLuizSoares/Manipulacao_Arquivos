def calcular_soma(notas):
    try:
        with open(notas, 'r') as arquivo:
            numeros_str = arquivo.read()
            numeros = [int(num) for num in numeros_str.split(',')]
            soma = sum(numeros)
            return soma
    except FileNotFoundError:
        print(f"Arquivo '{notas}' não encontrado.")
        return None
    except ValueError:
        print("Erro ao ler os números. Certifique-se de que o arquivo contém apenas números inteiros separados por vírgulas.")
        return None

nome_do_arquivo = 'exercicios/numeros.txt'
soma_numeros = calcular_soma(nome_do_arquivo)

if soma_numeros is not None:
    print(f"A soma dos números no arquivo '{nome_do_arquivo}' é: {soma_numeros}")
