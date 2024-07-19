from configurate import *

create_top(big_text_title='Sua resposta foi registrada com sucesso.', subtitle='Agradecemos a sua participação na pesquisa.', img_url=r'static/fim.png', use_line=False, use_progress=True, progress_percentage=100)

register_answer()
send_thanks_email(st.session_state['PeR']['email'])


footer()