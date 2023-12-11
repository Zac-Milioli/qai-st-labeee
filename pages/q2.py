from configurate import *

create_top(big_text_title='Conforto Térmico', subtitle='Com relação ao ambiente térmico da sua estação de trabalho, você costuma sentir algum dos itens a seguir?')

opcoes = ['sempre', 'muitas vezes', 'às vezes', 'poucas vezes', 'nunca']
choose_width = [2,2]

calor = create_radio(phrase='sinto desconforto pelo calor', selection=opcoes, use_list_selection=True, large=True, key='calor', show_values=True, two_columns_width=choose_width)
st.markdown('---')
frio = create_radio(phrase='sinto desconforto pelo frio', selection=opcoes, use_list_selection=True, large=True, key='frio', show_values=True, two_columns_width=choose_width)
st.markdown('---') 
mvento = create_radio(phrase='sinto desconforto porque há muito vento', selection=opcoes, use_list_selection=True, large=True, key='mvento', show_values=True, two_columns_width=choose_width)
st.markdown('---')
pvento = create_radio(phrase='sinto desconforto porque há pouco vento', selection=opcoes, use_list_selection=True, large=True, key='pvento', show_values=True, two_columns_width=choose_width)
st.markdown('---')
sol = create_radio(phrase='o sol direto me atrapalha', selection=opcoes, use_list_selection=True, large=True, key='sol', show_values=True, two_columns_width=choose_width)
st.markdown('---')
superficie = create_radio(phrase='há superfícies próximas (pisos, paredes, etc) muito quentes ou muito frias', selection=opcoes, use_list_selection=True, large=True, key='super', show_values=True, two_columns_width=choose_width)
st.markdown('---')
corpo = create_radio(phrase='sinto desconforto por frio ou calor em alguma parte específica do corpo (mãos, pés, pescoço, cabeça, etc)', selection=opcoes, use_list_selection=True, large=True, key='corpo', show_values=True, two_columns_width=choose_width)

st.title('')
if next_page_button('Próximo'):
    options = [calor, frio, mvento, pvento, sol, superficie, corpo]
    if None in options:
        st.error('Responda **todas** as questões para continuar')
    else:
        PeR['id_pergunta'] += ['q2 - desconforto pelo calor', 'q2 - desconforto pelo frio', 'q2 - desconforto por excesso de vento', 'q2 - desconforto por falta de vento', 'q2 - desconforto por sol direto', 'q2 - desconforto com temperatura de superfícies próximas', 'q2 - desconforto por frio ou calor em partes específicas do corpo']
        PeR['resposta'] += options
        if ('sempre' in options) or ('muitas vezes' in options) or ('às vezes' in options): 
            switch_page('q2a')
        else:
            switch_page('q3')
