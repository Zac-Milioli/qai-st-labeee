from configurate import *

create_top(big_text_title='Conforto acústico')

st.subheader('Com relação ao conforto acústico na sua estação de trabalho, você costuma sentir algum dos itens a seguir?')

list_selection = ['sempre', 'muitas vezes', 'às vezes', 'poucas vezes', 'nunca']
choosen_width = [2,2]

st.title('')
conversacolegas = create_radio(large=True, show_values=True, use_list_selection=True, selection=list_selection, phrase='sinto desconforto com conversas dos colegas', key='conversacolegas', two_columns_width=choosen_width)
ruidoequipamentos = create_radio(large=True, show_values=True, use_list_selection=True, selection=list_selection, phrase='sinto desconforto com ruídos de equipamentos', key='ruidoequipamentos', two_columns_width=choosen_width)
barulhoexterno = create_radio(large=True, show_values=True, use_list_selection=True, selection=list_selection, phrase='sinto desconforto com o barulho externo, vindo da rua', key='barulhoexterno', two_columns_width=choosen_width)

st.title('')
if next_page_button('Próximo'):
    q5_quest = [conversacolegas, ruidoequipamentos, barulhoexterno]
    if None in q5_quest:
        st.error('Responda **todas** as questões pra prosseguir')
    else:
        PeR['id_pergunta'] += ['q5 - sinto desconforto com conversas dos colegas', 'q5 - sinto desconforto com ruídos de equipamentos', 'q5 - sinto desconforto com o barulho externo, vindo da rua']
        PeR['resposta'] += q5_quest
        if ('sempre' in q5_quest) or ('muitas vezes' in q5_quest) or ('às vezes' in q5_quest): 
            switch_page('q5a')
        else:
            if len(open(r'base/hierarquia.txt', 'r').read()) >= 2:
                switch_page('hi')
            else:
                switch_page('cg')