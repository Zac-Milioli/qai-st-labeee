from configurate import *

create_top(big_text_title='Sua resposta foi registrada com sucesso', subtitle='Agradecemos a sua participação na pesquisa', img_url=r'static/fim.png')

input_email = open(r'base/person_mail.txt', 'r').read()
mail_me(input_email, PeR)
