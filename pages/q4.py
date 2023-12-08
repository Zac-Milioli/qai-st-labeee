from configurate import *

create_top(big_text_title='Conforto visual')

st.subheader('Com relação ao conforto visual na sua estação de trabalho, você costuma sentir algum dos itens a seguir?')

opt = ['sempre', 'muitas vezes', 'às vezes', 'poucas vezes', 'nunca']
choosen_width = [2,2]

st.title('')
claro = create_radio(large=True, phrase='sinto desconforto com o ambiente muito claro (muito iluminado)', selection=opt, show_values=True, use_list_selection=True, key='claro', two_columns_width=choosen_width)
st.markdown('---')
escuro = create_radio(large=True, phrase='sinto desconforto com o ambiente muito escuro (pouco iluminado)', selection=opt, show_values=True, use_list_selection=True, key='escuro', two_columns_width=choosen_width)
st.markdown('---')
ofuscamento = create_radio(large=True, phrase='sinto desconforto com o ofuscamento', selection=opt, show_values=True, use_list_selection=True, key='ofuscamento', two_columns_width=choosen_width)
st.markdown('---')
reflexos = create_radio(large=True, phrase='sinto desconforto com os reflexos na tela do meu computador', selection=opt, show_values=True, use_list_selection=True, key='reflexos', two_columns_width=choosen_width)
st.markdown('---')
luzes = create_radio(large=True, phrase='sinto desconforto com luzes piscando', selection=opt, show_values=True, use_list_selection=True, key='luzes', two_columns_width=choosen_width)
st.markdown('---')
objetos = create_radio(large=True, phrase='sinto desconforto pois não consigo diferenciar objetos (alto e/ou baixo contraste)', selection=opt, show_values=True, use_list_selection=True, key='objetos', two_columns_width=choosen_width)

st.title('')
st.title('')
st.title('')
if next_page_button('Próximo'):
    respostas = [claro, escuro, ofuscamento, reflexos, luzes, objetos]
    if None in respostas:
        st.error('Responda **todas** as questões para prosseguir')
    else:
        PeR['id_pergunta'] += ['q4 - sinto desconforto com o ambiente muito claro (muito iluminado)', 'q4 - sinto desconforto com o ambiente muito escuro (pouco iluminado)', 'q4 - sinto desconforto com o ofuscamento', 'q4 - sinto desconforto com os reflexos na tela do meu computador', 'q4 - sinto desconforto com luzes piscando', 'q4 - sinto desconforto pois não consigo diferenciar objetos (alto e/ou baixo contraste)']
        PeR['resposta'] += respostas
        switch_page('q4a')
