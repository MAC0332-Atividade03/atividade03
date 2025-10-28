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
	# --------- tratamento de tipo errado no deslocamento
    if isinstance(deslocamento, str):
    	# se for uma string, tenta ver se é possível convertê-la num float
        try:
            deslocamento_float = float(deslocamento)
        except ValueError:
            raise TypeError(f"Deslocamento inválido: {deslocamento}")
            
    elif isinstance(deslocamento, (int, float)):
    	# se recebeu número, converte pra float
        deslocamento_float = float(deslocamento)
        
    else:
        raise TypeError(f"Deslocamento deve ser int, float ou str numérica, recebeu {type(deslocamento).__name__}")
    
    if not deslocamento_float.is_integer():
    	# dado o float, tenta converter pra int
        raise TypeError(f"Deslocamento deve ser um inteiro, recebeu {deslocamento_float}")
        
    # --------- tratamento de tipo errado no texto
    texto = str(texto)

	# --------- começo da lógica da cifra
    deslocamento = int(deslocamento_float)%26
    caractere_temp = ''
    
    resposta = [] 
    # vou dar um join no final porque é mais rápido que concatenar string
    
    for caractere in texto:
        caractere_temp = ord(caractere)
    
        if ('a' <= caractere) and (caractere <= 'z'):
            caractere_temp = (caractere_temp+deslocamento-97)%26 + 97
        elif ('A' <= caractere) and (caractere <= 'Z'):
            caractere_temp = (caractere_temp+deslocamento-65)%26 + 65

        resposta.append(chr(caractere_temp))
        
    return ''.join(resposta)

def valida_cpf(cpf_string):
    # TODO: Implementar a lógica
    pass
