from configurate import *

create_top(big_text_title='QAI em Escritórios')

st.info('Para garantir a autenticidade da pesquisa, será enviado um código de verificação para seu email. **Suas respostas são anônimas e confidenciais.**', icon='ℹ️')
st.title('')

col1, col2, col3 = st.columns(3)
edificio = col2.text_input(label='None', label_visibility="collapsed", max_chars=8, placeholder="Código do edifício")
caixa_email, botao_enviar = st.columns([1,0.1])
mail = caixa_email.text_input('no label', label_visibility='hidden', max_chars=100, key='emaildoparticipante', placeholder='Insira seu email')
botao_enviar.write('')
submit = botao_enviar.button('Enviar código de verificação')

if submit:
    if not mail:
        st.error('Preencha seu email para receber o código de verificação')
    elif mail:
        if '@' not in mail:
            st.error('Insira um email válido para receber o código de verificação')
        if ' ' in mail:
            st.error('Não utilize espaços no seu endereço de email')
        else:
            st.session_state['auth'] = mail_auth_code(mail_person=mail)


esquerda, meio, direita = st.columns([1.6,1,1.8])
confirmacao_texto = meio.text_input('nolabel', label_visibility='hidden', max_chars=10, key='codigoverificacao', placeholder='Código de verificação')

st.title('')
if centered_button('Iniciar questionário'):
    if confirmacao_texto and edificio:
        if st.session_state['auth']:
            st.write(st.session_state['auth']) 
            if confirmacao_texto != st.session_state['auth']:
                st.error('Usuário não autorizado / Código incorreto')
            else:
                PeR['edificio'] = edificio
                open(r'base/hierarquia.txt', 'w').write('')
                open(r'base/person_mail.txt', 'w').write('')
                open(r'base/person_mail.txt', 'w').write(mail)
                switch_page('q0')
        else:
            st.error('Código de verificação não gerado, insira seu email, clique no botão de envio e copie o código que receber por email')
    else:
        st.error('Insira todas as informações para prosseguir')
