from configurate import *

create_top(big_text_title='Onde você passa mais tempo?', subtitle='Em um dia típico de trabalho, com que frequência você estima que utilize...')

opcoes = ['sempre', 'muitas vezes', 'às vezes', 'poucas vezes', 'nunca', 'não possui']

estacaodetrabalho = create_radio(large=True, phrase='sua estação de trabalho?', use_list_selection=True, selection=opcoes, show_values=True, two_columns_width=[1.5,2], key='estacaotrab')
st.markdown('---')
estacaodetrabalhorotativa = create_radio(large=True, phrase='estações de trabalho rotativas e/ou não-fixas?', use_list_selection=True, selection=opcoes, show_values=True, two_columns_width=[1.5,2], key='estacaorotativa')
st.markdown('---')
areagrupo = create_radio(large=True, phrase='áreas específicas para desenvolver atividades em grupo e/ou dinâmicas?', use_list_selection=True, selection=opcoes, show_values=True, two_columns_width=[1.5,2], key='areagrupo')
st.markdown('---')
individual = create_radio(large=True, phrase='áreas específicas para desenvolver atividades individuais e/ou focadas?', use_list_selection=True, selection=opcoes, show_values=True, two_columns_width=[1.5,2], key='individual') 
st.markdown('---')
conferencia = create_radio(large=True, phrase='salas de conferência e/ou reunião?', use_list_selection=True, selection=opcoes, show_values=True, two_columns_width=[1.5,2], key='conf')
st.markdown('---')
fora = create_radio(large=True, phrase='fica fora do escritório, em atividades externas?', use_list_selection=True, selection=opcoes, show_values=True, two_columns_width=[1.5,2], key='fora')

st.title('')
if next_page_button('Próximo'):
    options = [estacaodetrabalho, estacaodetrabalhorotativa, areagrupo, individual, conferencia, fora]
    if None in options:
        st.error('Responda **todas** as questões para prosseguir') 
    else:
        PeR['id_pergunta'] += ['q1c - estação de trabalho', 'q1c - estações de trabalho rotativas', 'q1c - áreas para atividades em grupo', 'q1c - áreas para atividades focadas ou individuais', 'q1c - salas comerciais ou de reunião', 'q1c - atividades externas ou fica fora do escritório']
        PeR['resposta'] += options
        switch_page('q2')
