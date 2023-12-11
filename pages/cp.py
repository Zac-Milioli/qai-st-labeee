from configurate import *

create_top(big_text_title='Qual é o seu nível de satisfação com a disponibilidade de controle')

st.subheader('dos itens a seguir para adaptação da sua estação de trabalho de forma a atender às suas preferências?')
my_width = [1.5,0.5,0.4,0.6,0.5]
st.title('')
esquerda, direita = st.columns([1,0.2])
with esquerda:
    st.title('')
    arcondicionado = create_radio(phrase='ar-condicionado e/ou aquecedores', extreme_left='insatisfeito(a)', extreme_right='satisfeito(a)', divide=True, key='controlearcondicionado', min=1, max=5, five_columns_width=my_width)
    ventiladores = create_radio(phrase='ventiladores', extreme_left='insatisfeito(a)', extreme_right='satisfeito(a)', divide=True, key='controleventiladores', min=1, max=5, five_columns_width=my_width)
    janelas = create_radio(phrase='abrir ou fechar janelas', extreme_left='insatisfeito(a)', extreme_right='satisfeito(a)', divide=True, key='controlejanelas', min=1, max=5, five_columns_width=my_width)
    cortinas = create_radio(phrase='abrir ou fechar cortinas', extreme_left='insatisfeito(a)', extreme_right='satisfeito(a)', divide=True, key='controlecortinas', min=1, max=5, five_columns_width=my_width)
    luzes = create_radio(phrase='acender ou apagar as luzes', extreme_left='insatisfeito(a)', extreme_right='satisfeito(a)', divide=True, key='controleluzes', min=1, max=5, five_columns_width=my_width)
with direita:
    st.markdown('**Não possui**')
    st.write('')
    st.write('')
    arcondicionado_checkbox = st.checkbox('no label', label_visibility='hidden', key='arcondicionado_checkbox')
    st.title('')
    ventiladores_checkbox = st.checkbox('no label', label_visibility='hidden', key='ventiladores_checkbox')
    st.title('')
    janelas_checkbox = st.checkbox('no label', label_visibility='hidden', key='janelas_checkbox')
    st.title('')
    cortinas_checkbox = st.checkbox('no label', label_visibility='hidden', key='cortinas_checkbox')
    st.title('')
    luzes_checkbox = st.checkbox('no label', label_visibility='hidden', key='luzes_checkbox')


if next_page_button('Próximo'):
    ok = True
    if not arcondicionado:
        if not arcondicionado_checkbox:
            ok = False
    if not ventiladores:
        if not ventiladores_checkbox:
            ok = False
    if not janelas:
        if not janelas_checkbox:
            ok = False
    if not cortinas:
        if not cortinas_checkbox:
            ok = False
    if not luzes:
        if not luzes_checkbox:
            ok = False
    if ok:
        PeR['id_pergunta'].append('cp - controle de ar-condicionado e aquecedores')
        if arcondicionado_checkbox:
            PeR['resposta'].append('Não possui')
        else:
            PeR['resposta'].append(arcondicionado)

        PeR['id_pergunta'].append('cp - controle de ventiladores')
        if ventiladores_checkbox:
            PeR['resposta'].append('Não possui')
        else:
            PeR['resposta'].append(ventiladores)

        PeR['id_pergunta'].append('cp - controle de janelas')
        if janelas_checkbox:
            PeR['resposta'].append('Não possui')
        else:
            PeR['resposta'].append(janelas)

        PeR['id_pergunta'].append('cp - controle de cortinas')
        if cortinas_checkbox:
            PeR['resposta'].append('Não possui')
        else:
            PeR['resposta'].append(cortinas)

        PeR['id_pergunta'].append('cp - controle de luzes')
        if luzes_checkbox:
            PeR['resposta'].append('Não possui')
        else:
            PeR['resposta'].append(luzes)

        switch_page('sp')
    else:
        st.error('Responda **todas** as perguntas')
