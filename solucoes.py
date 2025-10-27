def sao_anagramas(string1 : str, string2 : str) -> bool:
    # Passar todos os maiúsculos para minúsculos
    string1 = string1.lower().strip()
    string2 = string2.lower().strip()

    string1 = string1.split()
    string2 = string2.split()

    string1 = "".join(s.strip() for s in string1)
    string2 = "".join(s.strip() for s in string2)

    # Definir variáveis auxiliares
    size1 = len(string1)
    size2 = len(string2)
    mapeador = {}

    # Observar na tabela ASCII que os caracteres válidos estão entre 33 e 126, inclusos
    for i in range(size1):
        char_ascii = string1[i]
        if char_ascii not in mapeador:
            mapeador[char_ascii] = 1
        else:
            mapeador[char_ascii] += 1
    
    # Para todo caractere lido, reduz um da contagem
    for i in range(size2):
        char_ascii = string2[i]
        if char_ascii not in mapeador:
            mapeador[char_ascii] = -1
        else:
            mapeador[char_ascii] -= 1
    
    # Dos caracteres válidos, verifica se o mapeamento é nulo
    for value in mapeador.values():
        if(value != 0):
            return False
    
    return True

def cifra_de_cesar(texto, deslocamento):
    # TODO: Implementar a lógica
    pass

def valida_cpf(cpf_string):
    # TODO: Implementar a lógica
    pass
