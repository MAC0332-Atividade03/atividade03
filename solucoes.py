def sao_anagramas(string1, string2):
    # TODO: Implementar a lógica
    pass

def cifra_de_cesar(texto, deslocamento):
    # TODO: Implementar a lógica
    pass

def encontrar_maior_palavra(frase):
    if isinstance(frase, str):
        res = ""
        curString = []
        maxLength = curLenght = 0

        for i in range(len(frase)):
            if frase[i].isalnum() or frase[i] == '-':
                curString.append(frase[i]) 
                curLenght += 1
            else:
                if frase[i] == ' ':
                    if curLenght > maxLength:
                        maxLength = curLenght
                        res = ''.join(curString)
                    
                    curString = []
                    curLenght = 0
                
        if curLenght > maxLength:
            maxLength = curLenght
            res = ''.join(curString)
        
        return res

    return "ERRO: O parâmetro não é string"