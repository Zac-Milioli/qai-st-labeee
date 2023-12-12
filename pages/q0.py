from configurate import *

create_top(big_text_title='Pesquisa de clima organizacional', img_url=r'static\Q0.png')

place_left_subtitle('Como você classifica a sua satisfação com as condições físicas (temperatura, qualidade do ar interno, iluminação e acústica) do seu ambiente de trabalho para a realização das suas atividades?')

valor = create_radio(phrase='Em uma escala de 0 a 10', show_values=True, large=True, min=0, max=10)

st.title('')
if next_page_button('Próxima página'):
    if valor == None:
        st.error('Responda para prosseguir')
    else:
        PeR['id_pergunta'].append('q0')
        PeR['resposta'].append(valor)
        st.session_state['q0'] = valor
        if valor <= 6:
            switch_page('introq1_insat')
        else:
            switch_page('introq1_sat')
