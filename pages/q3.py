from configurate import *

create_top(big_text_title='Qualidade do ar interno')

st.subheader('Com relação à qualidade do ar interno próximo à sua estação de trabalho, você costuma sentir algum dos itens a seguir?')
opt = ['sempre', 'muitas vezes', 'às vezes', 'poucas vezes', 'nunca']
choosen_width = [2,2]

cheiros = create_radio(large=True, phrase='sinto desconforto devido a cheiros e odores', selection=opt, show_values=True, use_list_selection=True, key='cheiros', two_columns_width=choosen_width)
st.markdown('---')
abafado = create_radio(large=True, phrase='sinto desconforto com o ambiente abafado', selection=opt, show_values=True, use_list_selection=True, key='abafado', two_columns_width=choosen_width)
st.markdown('---')
arseco = create_radio(large=True, phrase='sinto desconforto com o ar interno muito seco ou muito úmido', selection=opt, show_values=True, use_list_selection=True, key='arseco', two_columns_width=choosen_width)
st.markdown('---')
poeira = create_radio(large=True, phrase='sinto desconforto devido à poeira', selection=opt, show_values=True, use_list_selection=True, key='poeira', two_columns_width=choosen_width)

if next_page_button('Próximo'):
    valores = [cheiros, abafado, arseco, poeira]
    if None in valores:
        st.error('Responda **todas** as questões para prosseguir')
    else:
        PeR['id_pergunta'] += ['q3 - desconforto por cheiros e odores', 'q3 - desconforto por ambiente abafado', 'q3 - desconforto com ar interno seco ou úmido demais', 'q3 - desconforto devido à poeira']
        PeR['resposta'] += valores
        if ('sempre' in valores) or ('muitas vezes' in valores) or ('às vezes' in valores): 
            switch_page('q3a')
        else:
            switch_page('q4')
