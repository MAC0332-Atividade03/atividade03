def limpa_string(string : str) -> str:
    # Transforma todos os caractere em minúsculos
    # Splita a string
    lista_de_termos = string.lower().split()

    # Reune as peças, retirando os espaços entre os termos
    return "".join(map(str.strip, lista_de_termos))

def sao_anagramas(string1 : str, string2 : str) -> bool:
    if not isinstance(string1, str) or not isinstance(string2, str):
        raise Exception("Insert two strings as arguments")
    
    # Passar todos os maiúsculos para minúsculos
    nova_string1 = limpa_string(string1)
    nova_string2 = limpa_string(string2)

    # Definir variáveis auxiliares
    size1 = len(nova_string1)
    size2 = len(nova_string2)
    mapeador = {}

    # Contabilizar cada caractere da string limpa
    for i in range(size1):
        char_ascii = nova_string1[i]
        if char_ascii not in mapeador:
            mapeador[char_ascii] = 1
        else:
            mapeador[char_ascii] += 1
    
    # Para todo caractere lido, reduz um da contagem
    for i in range(size2):
        char_ascii = nova_string2[i]
        if char_ascii not in mapeador:
            mapeador[char_ascii] = -1
        else:
            mapeador[char_ascii] -= 1
    
    # Dos caracteres válidos, verifica se o mapeamento é nulo
    for value in mapeador.values():
        if value != 0:
            return False
    
    return True

def cifra_de_cesar(texto, deslocamento):
    # TODO: Implementar a lógica
    pass

def valida_cpf(cpf_string):
    # TODO: Implementar a lógica
    pass
