import requests
import pandas as pd

### Access the API ###
def acessa_api():
    url = 'https://api.cartolafc.globo.com/atletas/mercado'
    request_api = requests.get(url)
    return request_api.text

### Finding each scout, if it exists ##
def busca_scout(x):
    if scout.find(x) == -1:
        return 0
    else:
        busca = scout[scout.find(x)+len(x)+1:]
        if busca[:busca.find(",")] == -1:
            return busca[:busca.find("}")]
        else:
            return busca[:busca.find(",")]

r = acessa_api()

atletas = r[r.find("\"scout"):]
num_atletas = atletas.count("atleta_id")

### Creates the DataFrame ###
df = pd.DataFrame({'atleta_id':['NA'],
                    'clube_id':['NA'],
                    'posicao_id':['NA'],
                    'status_id':['NA'],
                    'pontos_num':[0],
                    'preco_num':[0],
                    'variacao_num':[0],
                    'media_num':[0],
                    'jogos_num':[0],
                    'slug':['NA'],
                    'apelido':['NA'],
                    'apelido_abreviado':['NA'],
                    'nome':['NA'],
                    'A':[0],
                    'CA':[0],
                    'CV':[0],
                    'DE':[0],
                    'DP':[0],
                    'DS':[0],
                    'FC':[0],
                    'FD':[0],
                    'FF':[0],
                    'FS':[0],
                    'FT':[0],
                    'G':[0],
                    'GC':[0],
                    'GS':[0],
                    'I':[0],
                    'PC':[0],
                    'PI':[0],
                    'PS':[0],
                    'PP':[0],
                    'SG':[0],
                    })

cont = 1
while cont <= num_atletas:
    x = atletas.find("{")
    y = atletas.find(",{")
    bloco = atletas[x:y]

    atleta_id = bloco[bloco.find("\"atleta_id\"")+12:bloco.find("\"rodada_id\"")-1]
    clube_id = bloco[bloco.find("\"clube_id\"")+11:bloco.find("\"posicao_id\"")-1]
    posicao_id = bloco[bloco.find("\"posicao_id\"")+13:bloco.find("\"status_id\"")-1]
    status_id = bloco[bloco.find("\"status_id\"")+12:bloco.find("\"pontos_num\"")-1]
    pontos_num = bloco[bloco.find("\"pontos_num\"")+13:bloco.find("\"preco_num\"")-1]
    preco_num = bloco[bloco.find("\"preco_num\"")+12:bloco.find("\"variacao_num\"")-1]
    variacao_num = bloco[bloco.find("\"variacao_num\"")+15:bloco.find("\"media_num\"")-1]
    media_num = bloco[bloco.find("\"media_num\"") + 12:bloco.find("\"jogos_num\"") - 1]
    jogos_num = bloco[bloco.find("\"jogos_num\"")+12:bloco.find("\"slug\"")-1]
    slug = bloco[bloco.find("\"slug\"")+8:bloco.find("\"apelido\"")-2]
    apelido = bloco[bloco.find("\"apelido\"")+11:bloco.find("\"apelido_abreviado\"")-2]
    apelido_abreviado = bloco[bloco.find("\"apelido_abreviado\"") + 21:bloco.find("\"nome\"") - 2]
    nome = bloco[bloco.find("\"nome\"")+8:bloco.find("\"foto\"")-2]

    scout = atletas[atletas.find("\"scout\"")+8:atletas.find("},")+1]

    A = busca_scout("\"A\"")
    CA = busca_scout("\"CA\"")
    CV = busca_scout("\"CV\"")
    DE = busca_scout("\"DD\"")
    DP = busca_scout("\"DP\"")
    DS = busca_scout("\"DS\"")
    FC = busca_scout("\"FC\"")
    FD = busca_scout("\"FD\"")
    FF = busca_scout("\"FF\"")
    FS = busca_scout("\"FS\"")
    FT = busca_scout("\"FT\"")
    G = busca_scout("\"G\"")
    GC = busca_scout("\"GC\"")
    GS = busca_scout("\"GS\"")
    I = busca_scout("\"I\"")
    PC = busca_scout("\"PC\"")
    PI = busca_scout("\"PI\"")
    PS = busca_scout("\"PS\"")
    PP = busca_scout("\"PP\"")
    SG = busca_scout("\"SG\"")

    df2 = pd.DataFrame({'nome': [nome],
                        'slug': [slug],
                        'apelido': [apelido],
                        'apelido_abreviado': [apelido_abreviado],
                        'atleta_id': [atleta_id],
                        'clube_id': [clube_id],
                        'posicao_id': [posicao_id],
                        'status_id': [status_id],
                        'pontos_num': [pontos_num],
                        'preco_num': [preco_num],
                        'variacao_num': [variacao_num],
                        'media_num': [media_num],
                        'jogos_num': [jogos_num],
                        'A': [A],
                        'CA': [CA],
                        'CV': [CV],
                        'DE': [DE],
                        'DP': [DP],
                        'DS': [DS],
                        'FC': [FC],
                        'FD': [FD],
                        'FF': [FF],
                        'FS': [FS],
                        'FT': [FT],
                        'G': [G],
                        'GC': [GC],
                        'GS': [GS],
                        'I': [I],
                        'PC': [PC],
                        'PI': [PI],
                        'PS': [PS],
                        'PP': [PP],
                        'SG': [SG],
                        })

    df = df.append(df2)

    atletas = atletas[y+1:]
    cont = cont + 1
#print(df)

### Saving DataFrame as .csv file ###
df.to_csv('cartola.csv')