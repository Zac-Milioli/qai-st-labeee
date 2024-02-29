from configurate import *

create_top(big_text_title='Conforto visual', use_progress=True, progress_percentage=50)

st.subheader('Com relação ao conforto visual na sua estação de trabalho, você costuma sentir algum dos itens a seguir?')

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

opt = ['sempre', 'muitas vezes', 'às vezes', 'poucas vezes', 'nunca']
choosen_width = [1.7,2]

claro = create_radio(large=True, phrase='sinto desconforto com o ambiente muito claro (muito iluminado)', selection=opt, use_list_selection=True, key='claro', two_columns_width=choosen_width)
escuro = create_radio(large=True, phrase='sinto desconforto com o ambiente muito escuro (pouco iluminado)', selection=opt, use_list_selection=True, key='escuro', two_columns_width=choosen_width)
ofuscamento = create_radio(large=True, phrase='sinto desconforto com o ofuscamento', selection=opt, use_list_selection=True, key='ofuscamento', two_columns_width=choosen_width)
reflexos = create_radio(large=True, phrase='sinto desconforto com os reflexos na tela do meu computador', selection=opt, use_list_selection=True, key='reflexos', two_columns_width=choosen_width)
luzes = create_radio(large=True, phrase='sinto desconforto com luzes piscando', selection=opt, use_list_selection=True, key='luzes', two_columns_width=choosen_width)
objetos = create_radio(large=True, phrase='sinto desconforto pois não consigo diferenciar objetos (alto e/ou baixo contraste)', selection=opt, use_list_selection=True, key='objetos', two_columns_width=choosen_width)

st.title('')
if next_page_button('Próximo'):
    respostas = [claro, escuro, ofuscamento, reflexos, luzes, objetos]
    if None in respostas:
        st.error('Responda **todas** as questões para prosseguir')
    else:
        PeR['q4 - sinto desconforto com o ambiente muito claro (muito iluminado)'] = claro
        PeR['q4 - sinto desconforto com o ambiente muito escuro (pouco iluminado)'] = escuro
        PeR['q4 - sinto desconforto com o ofuscamento'] = ofuscamento
        PeR['q4 - sinto desconforto com os reflexos na tela do meu computador'] = reflexos
        PeR['q4 - sinto desconforto com luzes piscando'] = luzes
        PeR['q4 - sinto desconforto pois não consigo diferenciar objetos (alto e/ou baixo contraste)'] = objetos
        if ('sempre' in respostas) or ('muitas vezes' in respostas) or ('às vezes' in respostas): 
            switch_page('q4a')
        else:
            switch_page('q5')
