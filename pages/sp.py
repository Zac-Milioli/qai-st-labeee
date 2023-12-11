from configurate import *

create_top('Ao solicitar algum ajuste e/ou alteração nos sistemas a seguir')

st.subheader('a fim de atender à sua preferência, qual o seu nível de satisfação com a velocidade e a eficiência da resposta à sua solicitação?')

my_width = [1.5,0.1,0.4,0.6,0.5]
st.title('')
esquerda, meio, direita = st.columns([0.2,1,0.2])
with esquerda:
    st.title('')
    st.write('')
    st.write('')
    st.markdown('**1.aquecimento e/ou resfriamento**')
    st.title('')
    st.markdown('**2.ventilação**')
    st.title('')
    st.markdown('**3.iluminação**')
with meio:
    st.title('')
    clima = create_radio(phrase='por exemplo, elevar ou reduzir a temperatura do sistema de climatização', extreme_left='insatisfeito(a)', extreme_right='satisfeito(a)', divide=True, key='clima', min=1, max=5, five_columns_width=my_width)
    ventilacao = create_radio(phrase='por exemplo, aumentar ou reduzir a velocidade e/ou direção do ar', extreme_left='insatisfeito(a)', extreme_right='satisfeito(a)', divide=True, key='ventilacao', min=1, max=5, five_columns_width=my_width)
    iluminacao = create_radio(phrase='por exemplo, trocar, acender ou apagar lâmpadas; abrir ou fechar elementos de sombreamento', extreme_left='insatisfeito(a)', extreme_right='satisfeito(a)', divide=True, key='iluminacao', min=1, max=5, five_columns_width=my_width)
with direita:
    st.markdown('**Nunca solicitei ajustes**')
    st.write('')
    st.write('')
    clima_checkbox = st.checkbox('no label', label_visibility='hidden', key='clima_checkbox')
    st.title('')
    ventilacao_checkbox = st.checkbox('no label', label_visibility='hidden', key='ventilacao_checkbox')
    st.title('')
    iluminacao_checkbox = st.checkbox('no label', label_visibility='hidden', key='iluminacao_checkbox')

st.title('')
st.title('')
esquerda, direita = st.columns(2, gap='large')
esquerda.subheader('Você gostaria de compartilhar alguma ocasião em que foi necessário algum ajuste dos sistemas do edifício com o objetivo de melhorar a sua satisfação com a sua estação de trabalho?')
entrada_solicitacao = direita.text_area(label='no label', label_visibility='hidden',value=None, key='entrybox_5', placeholder='Deixe sua mensagem aqui (não obrigatório)', max_chars=250)

st.title("")
if next_page_button('Próximo'):
    ok = True
    if not clima:
        if not clima_checkbox:
            ok = False
    if not ventilacao:
        if not ventilacao_checkbox:
            ok = False
    if not iluminacao:
        if not iluminacao_checkbox:
            ok = False
    if ok:
        PeR['id_pergunta'].append('sp - velocidade de resposta à solicitação de aquecimento e/ou resfriamento')
        if clima_checkbox:
            PeR['resposta'].append('Não possui')
        else:
            PeR['resposta'].append(clima)

        PeR['id_pergunta'].append('sp - velocidade de resposta à solicitação de controle de ventilação')
        if ventilacao_checkbox:
            PeR['resposta'].append('Não possui')
        else:
            PeR['resposta'].append(ventilacao)

        PeR['id_pergunta'].append('sp - velocidade de resposta à solicitação de alteração de iluminação')
        if iluminacao_checkbox:
            PeR['resposta'].append('Não possui')
        else:
            PeR['resposta'].append(iluminacao)
        
        PeR['id_pergunta'].append('sp - comentários')
        PeR['resposta'].append(entrada_solicitacao)
        switch_page('q6')
    else:
        st.error('Responda **todas** as perguntas para prosseguir')
