def sao_anagramas(string1, string2):
    # TODO: Implementar a lógica
    pass

def cifra_de_cesar(texto, deslocamento):
    deslocamento = deslocamento%26
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
