def sao_anagramas(string1, string2):
    # TODO: Implementar a lógica
    pass

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
