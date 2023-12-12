from configurate import *

create_top(big_text_title='Sua resposta foi registrada com sucesso', subtitle='Agradecemos a sua participação na pesquisa', img_url=r'static/fim.png')

mail_me(participante['Email'], PeR)
