# Sistema antiprocessos jurídicos para tweets
# Escreva qualquer atrocidade sem peso na consciência
# Versao 0.1

def converter_em_asteriscos(texto):
    texto_convertido = ''
    for caractere in texto:
        if caractere == ' ':
            texto_convertido += ' '  # Mantém o espaço
        else:
            texto_convertido += '*'  # Substitui por asterisco
        
    return texto_convertido


# Obtém o texto do usuário
texto_usuario = input("Digite um texto: ")

# Converte o texto em asteriscos
texto_convertido = converter_em_asteriscos(texto_usuario)

# Imprime o resultado
print("Texto convertido:", texto_convertido)
