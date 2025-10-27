def sao_anagramas(string1, string2):
    # TODO: Implementar a lógica
    pass

def cifra_de_cesar(texto, deslocamento):
    # TODO: Implementar a lógica
    pass

def encontrar_maior_palavra(frase):
    if isinstance(frase, str):
        res = ""
        maxLength = curStart = curLenght = 0

        for i in range(len(frase)):
            if(frase[i].isalnum()):
                curLenght += 1
            else:
                if(frase[i] == ' ' and curLenght > maxLength):
                    maxLength = curLenght
                    res = frase[curStart:curStart+maxLength]
                
                curStart = i+1
                curLenght = 0

        if(curLenght > maxLength):
            maxLength = curLenght
            res = frase[curStart:curStart+maxLength]
        
        return res

    return "ERRO: O parâmetro não é string"