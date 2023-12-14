from configurate import *

create_top(big_text_title='Conforto Térmico', subtitle='Com relação ao ambiente térmico da sua estação de trabalho, você costuma sentir algum dos itens a seguir?')

st.markdown("""
    <style>
    [role=radiogroup]{
        gap: 5rem;
    }
    </style>
    """,unsafe_allow_html=True)


esquerda, meio, direita = st.columns([1.1,1.1,0.3], gap='large')
with meio:
    sempre, muitas_vezes, as_vezes, poucas_vezes, nunca, nao_possui = st.columns(6, gap='large')
    sempre.write('sempre')
    muitas_vezes.write('muitas vezes')
    as_vezes.write('às vezes')
    poucas_vezes.write('poucas vezes')
    nunca.write('nunca')

opcoes = ['sempre', 'muitas vezes', 'às vezes', 'poucas vezes', 'nunca']
choose_width = [1.7,2]

calor = create_radio(phrase='sinto desconforto pelo calor', selection=opcoes, use_list_selection=True, large=True, key='calor', two_columns_width=choose_width)
frio = create_radio(phrase='sinto desconforto pelo frio', selection=opcoes, use_list_selection=True, large=True, key='frio', two_columns_width=choose_width)
mvento = create_radio(phrase='sinto desconforto porque há muito vento', selection=opcoes, use_list_selection=True, large=True, key='mvento', two_columns_width=choose_width)
pvento = create_radio(phrase='sinto desconforto porque há pouco vento', selection=opcoes, use_list_selection=True, large=True, key='pvento', two_columns_width=choose_width)
sol = create_radio(phrase='o sol direto me atrapalha', selection=opcoes, use_list_selection=True, large=True, key='sol', two_columns_width=choose_width)
superficie = create_radio(phrase='há superfícies próximas (pisos, paredes, etc) muito quentes ou muito frias', selection=opcoes, use_list_selection=True, large=True, key='super', two_columns_width=choose_width)
corpo = create_radio(phrase='sinto desconforto por frio ou calor em alguma parte específica do corpo (mãos, pés, pescoço, cabeça, etc)', selection=opcoes, use_list_selection=True, large=True, key='corpo', two_columns_width=choose_width)

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
