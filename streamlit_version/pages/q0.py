import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from configurate import *

create_top(big_text_title='Pesquisa de clima organizacional', img_url='https://github.com/Zac-Milioli/Quest_Luiza/blob/master/static/Q0.png?raw=true')

place_left_subtitle('Como você classifica a sua satisfação com as condições físicas (temperatura, qualidade do ar interno, iluminação e acústica) do seu ambiente de trabalho para a realização das suas atividades?')

valor = create_radio_0_10('Em uma escala de 0 a 10:')

if next_page_button('Próxima página'):
    PeR['id_pergunta'].append('q0')
    PeR['resposta'].append(valor)
    st.session_state['q0'] = valor
    if valor <= 6:
        switch_page('introq1_insat')
    else:
        switch_page('introq1_sat')
