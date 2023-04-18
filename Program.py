import pandas as pd

# Funçao menor valor faturado por dia
def menor_valor_faturado(lista_valores):
    return lista_valores.min()

# Funcao maior valor faturado por dia
def maior_valor_faturado(lista_valores):
    return lista_valores.max()

# Funcao para achar a media de valores mensal
def media_mensal(lista_valores):
    return lista_valores.mean()

# DataFrame de todos os dados fornecidos
dados_df = pd.read_json("dados.json")

# DataFrame com extraçao dos dias sem faturamento
faturamento_df = dados_df.loc[dados_df['valor'] > 0.0]

# Lista com os valores da coluna 'Valor'
valores_series = faturamento_df['valor']

# Imprimir menor valor faturado encontrado na lista
print(f'Menor valor faturado: $ {menor_valor_faturado(valores_series):,.2f}')

# Imprimir maior valor faturado encontrado na lista
print(f'Maior valor faturado: $ {maior_valor_faturado(valores_series):,.2f}')

# Busca o valor da media na funçao media_mensal()
valor_media = media_mensal(valores_series)
# Imprime a media mensal dos dias faturados
print(f'Media valor faturado: $ {valor_media:,.2f}')

# Gera tabela com registros maiores e igual a media mensal
maior_que_a_media = faturamento_df.loc[faturamento_df['valor'] > valor_media]
print(f'\nFaturamento superior a media mensal:\n{maior_que_a_media}')

# Pega coluna 'dia' e passa para uma lista
qtd_dias = maior_que_a_media['dia']
# Imprime a quantia de itens da lista 'dia'
print(f'Quantidade de dias com faturamento superior a media mensal: {qtd_dias.count()} dias')