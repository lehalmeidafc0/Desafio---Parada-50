import unicodedata

def remove_acento(text):
    return ''.join(c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn')

def contar_vogais(texto):
    vogais = 'aeiou'
    contador = {vogal: 0 for vogal in vogais}
    
    for char in texto.lower():
        char_sem_acento = remove_acento(char)
        if char_sem_acento in vogais:
            contador[char_sem_acento] += 1
            
    return contador

def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as file:
        return file.read()

# Substitua 'texto.txt' pelo caminho do arquivo de texto
nome_arquivo = 'texto.txt'
texto = ler_arquivo(nome_arquivo)
resultado = contar_vogais(texto)

print("Contagem de vogais:")
for vogal, quantidade in resultado.items():
    print(f"{vogal}: {quantidade}")
