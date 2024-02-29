from configurate import *

create_top(big_text_title='Qualidade do ar interno', use_progress=True, progress_percentage=40)

st.markdown("""
    <style>
    [role=radiogroup]{
        gap: 5rem;
    }
    </style>
    """,unsafe_allow_html=True)


st.subheader('Com relação à qualidade do ar interno próximo à sua estação de trabalho, você costuma sentir algum dos itens a seguir?')
st.title('')
opt = ['sempre', 'muitas vezes', 'às vezes', 'poucas vezes', 'nunca']
choosen_width = [1.7,2]

esquerda, meio, direita = st.columns([1.1,1.1,0.3], gap='large')
with meio:
    sempre, muitas_vezes, as_vezes, poucas_vezes, nunca, nao_possui = st.columns(6, gap='large')
    sempre.write('sempre')
    muitas_vezes.write('muitas vezes')
    as_vezes.write('às vezes')
    poucas_vezes.write('poucas vezes')
    nunca.write('nunca')

cheiros = create_radio(large=True, phrase='sinto desconforto devido a cheiros e odores', selection=opt, use_list_selection=True, key='cheiros', two_columns_width=choosen_width)
abafado = create_radio(large=True, phrase='sinto desconforto com o ambiente abafado', selection=opt, use_list_selection=True, key='abafado', two_columns_width=choosen_width)
arseco = create_radio(large=True, phrase='sinto desconforto com o ar interno muito seco ou muito úmido', selection=opt, use_list_selection=True, key='arseco', two_columns_width=choosen_width)
poeira = create_radio(large=True, phrase='sinto desconforto devido à poeira', selection=opt, use_list_selection=True, key='poeira', two_columns_width=choosen_width)

st.title('')
if next_page_button('Próximo'):
    valores = [cheiros, abafado, arseco, poeira]
    if None in valores:
        st.error('Responda **todas** as questões para prosseguir')
    else:
        PeR['q3 - desconforto por cheiros e odores'] = cheiros 
        PeR['q3 - desconforto por ambiente abafado'] = abafado
        PeR['q3 - desconforto com ar interno seco ou úmido demais'] = arseco 
        PeR['q3 - desconforto devido à poeira'] = poeira
        if ('sempre' in valores) or ('muitas vezes' in valores) or ('às vezes' in valores): 
            switch_page('q3a')
        else:
            switch_page('q4')
