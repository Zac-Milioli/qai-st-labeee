from configurate import *

create_top(big_text_title='Sua resposta foi registrada com sucesso', subtitle='Agradecemos a sua participação na pesquisa', img_url=r'static\fim.png')

open('results.txt', 'w', encoding='utf-8').write(f'{PeR}')
