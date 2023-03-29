import json

with open('faturamento.json', 'r') as f:
    dados = json.load(f)

faturamento = dados['faturamento']
media = sum(faturamento) / len(faturamento)
dias_acima_media = 0
maior = float('-inf')
menor = float('inf')

for valor in faturamento:
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor
    if valor > media:
        dias_acima_media += 1

print(f"Menor faturamento diário: R${menor:.2f}")
print(f"Maior faturamento diário: R${maior:.2f}")
print(f"{dias_acima_media} dias tiveram faturamento acima da média mensal")
