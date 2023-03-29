def inverte_string(s):
    nova_string = ""
    for i in range(len(s)-1, -1, -1):
        nova_string += s[i]
    return nova_string

# Exemplo de uso:
string_original = "Exemplo de string a ser invertida"
string_invertida = inverte_string(string_original)
print(string_invertida) # aditrevni res a gnirts ed olpmxE
