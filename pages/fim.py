from configurate import *

create_top(big_text_title='Sua resposta foi registrada com sucesso.', subtitle='Agradecemos a sua participação na pesquisa.', img_url=r'static/fim.png', use_line=False, use_progress=True, progress_percentage=100)

input_email = open(r'base/person_mail.txt', 'r').read()
mail_me(input_email, PeR)
send_thanks_email(input_email)
