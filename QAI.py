from configurate import *

create_top(big_text_title='QAI em Escritórios', subtitle='Design e organização: Luiza de Castro', subtitle2='Desenvolvimento: Zac Milioli')

st.info('Para iniciar o questionário, é necessário inserir um email válido. Fazemos isso para garantir a autenticidade da pesquisa', icon='ℹ️')
st.title('')
caixa_email, botao_enviar = st.columns([1,0.1])
mail = caixa_email.text_input('no label', label_visibility='hidden', max_chars=100, key='emaildoparticipante', placeholder='Insira seu email')
botao_enviar.write('')
submit = botao_enviar.button('Enviar código de confirmação')

if submit:
    if not mail:
        st.error('Preencha seu email para receber o código de validação')
    elif mail:
        if '@' not in mail:
            st.error('Insira um email válido para receber o código de validação')
        else:
            st.session_state.authorization_code_random = mail_auth_code(mail_person=mail)


esquerda, meio, direita = st.columns([1.6,1,1.8])
confirmacao_texto = meio.text_input('nolabel', label_visibility='hidden', max_chars=10, key='codigoconfirmacao', placeholder='Código de confirmação')

st.title('')
if centered_button('Iniciar questionário'):
    if confirmacao_texto != st.session_state.authorization_code_random:
        st.error('Usuário não autorizado / Código incorreto')
    else:
        open(r'base/hierarquia.txt', 'w').write('')
        open(r'base/person_mail.txt', 'w').write(mail)
        switch_page('q0')
