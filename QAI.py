from configurate import *

create_top(big_text_title='QAI em Escritórios', subtitle='Design e organização: Luiza de Castro', subtitle2='Desenvolvimento: Zac Milioli')

st.info('Para iniciar o questionário, é necessário inserir um email válido, copiar o código que receber em sua caixa de entrada e colar no local designado. Fazemos isso para garantir a autenticidade da pesquisa. **Seus email não será visto por ninguém além da equipe de pesquisadores**.', icon='ℹ️')
st.title('')
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
        else:
            st.session_state.authorization_code_random = mail_auth_code(mail_person=mail)


esquerda, meio, direita = st.columns([1.6,1,1.8])
confirmacao_texto = meio.text_input('nolabel', label_visibility='hidden', max_chars=10, key='codigoverificacao', placeholder='Código de verificação')

st.title('')
if centered_button('Iniciar questionário'):
    if confirmacao_texto:
        try: 
            if confirmacao_texto != st.session_state.authorization_code_random:
                st.error('Usuário não autorizado / Código incorreto')
            else:
                open(r'base/hierarquia.txt', 'w').write('')
                open(r'base/person_mail.txt', 'w').write(mail)
                switch_page('q0')
        except:
            st.error('Código de verificação não gerado, insira seu email, clique no botão de envio e copie o código que receber por email')
    else:
        st.error('Código de verificação não inserido')
