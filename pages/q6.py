from configurate import *

create_top(big_text_title='Dados pessoais')

st.subheader('Para caracterizar a amostra da nossa pesquisa, precisamos de algumas informações pessoais')
st.title('')

esquerda, meio, direita = st.columns(3)

with esquerda:
    faixa_etaria_opt = ['até 20 anos', '21 a 30 anos', '31 a 40 anos', '41 a 50 anos', '51 a 60 anos', 'acima de 60 anos']
    st.markdown('**Qual é a sua faixa etária?**')
    faixa_etaria_radio = st.radio(label='no label', label_visibility='hidden', options=faixa_etaria_opt, key='faixaetaria', index=None)
with meio:
    escolaridade_opt = ['ensino fundamental', 'ensino médio', 'ensino técnico', 'ensino superior', 'pós-graduação']
    st.markdown('**Qual é o seu grau de escolaridade?**')
    escolaridade_radio = st.radio(label='no label', label_visibility='hidden', options=escolaridade_opt, key='escolaridade', index=None)
with direita:
    genero_opt = ['feminino', 'masculino', 'outro', 'prefiro não responder']
    st.markdown('**Com qual gênero você se identifica?**')
    genero_radio = st.radio(label='no label', label_visibility='hidden', options=genero_opt, key='genero', index=None)

st.title('')
if next_page_button('Submeter', aviso='Suas respostas serão gravadas quando você encerrar a pesquisa, clicando em Submeter.'):
    ok = True
    options = [faixa_etaria_radio, escolaridade_radio, genero_radio]
    if None in options:
        ok = False
    if ok:
        PeR['id_pergunta'] += ['q6 - faixa etária', 'q6 - escolaridade', 'q6 - gênero']
        PeR['resposta'] += options
        switch_page('fim')
    else:
        st.error('Responda **todas** as perguntas para submeter')