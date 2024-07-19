from configurate import *

create_top(big_text_title=f'{project}')

st.info('Para garantir a autenticidade da pesquisa, será enviado um código de verificação para seu email. **Suas respostas são anônimas e confidenciais.**', icon='ℹ️')
st.title('')

form_email = st.container(border=True)
col1, col2 = form_email.columns([4,1])
email = col1.text_input(label="Email").strip()
col2.subheader('')
if col2.button(label="Enviar código de verificação", use_container_width=True):
    try:
        st.session_state['auth_code'] = mail_auth_code(email)
        st.session_state['email'] = email
    except:
        st.error('Um erro ocorreu ao tentar enviar o email de validação. Verifique se o email inserido está correto e tente novamente', icon="⚠️")
col1, col2 = form_email.columns(2)
codigo = col1.text_input(label="Código de validação", max_chars=6)
edificio = col2.text_input(label="Insira o ID do seu local de trabalho:", max_chars=8)
check_inputs = True if not (edificio and codigo) else False
col1, col2, col3 = form_email.columns(3)
if col2.button(label="Validar código e iniciar questionário", use_container_width=True, disabled=check_inputs):
    if not st.session_state.get('auth_code'):
        st.error('ERRO: O código de validação não foi gerado', icon="⚠️")
    elif st.session_state['auth_code'] == codigo:
        with st.spinner("Verificando código e ID de local de trabalho..."):
            returned, status = get_build_info_by_id(id_=int(edificio))
        if status == "OK":
            st.session_state['edificio'] = edificio
            st.session_state['hierarquia'] = 0
            st.session_state['janela'] = 0
            switch_page('q0')
        else:
            st.error("O ID do local de trabalho inserido não foi encontrado na base de dados", icon='⚠️')
    else:
        st.error('ERRO: O código inserido é diferente do código enviado', icon="⚠️")

footer()

# edificio = st.text_input(label='None', label_visibility="collapsed", max_chars=8, placeholder="Código do edifício")
# col1, col2, col3 = st.columns(3)
# caixa_email, botao_enviar = st.columns([1,0.1])
# mail = caixa_email.text_input('no label', label_visibility='hidden', max_chars=100, key='emaildoparticipante', placeholder='Insira seu email')
# botao_enviar.write('')

# if botao_enviar.button('Enviar código de verificação'):
#     if not mail:
#         st.error('Preencha seu email para receber o código de verificação')
#     elif mail:
#         if '@' not in mail:
#             st.error('Insira um email válido para receber o código de verificação')
#         if ' ' in mail:
#             st.error('Não utilize espaços no seu endereço de email')
#         else:
#             st.session_state['PeR']['email'] = mail
#             st.session_state['auth'] = mail_auth_code(mail_person=mail)


# esquerda, meio, direita = st.columns([1.6,1,1.8])
# confirmacao_texto = meio.text_input('nolabel', label_visibility='hidden', max_chars=10, key='codigoverificacao', placeholder='Código de verificação')

# st.title('')
# if centered_button('Iniciar questionário'):
#     if confirmacao_texto and edificio:
#         if st.session_state['auth']:
#             st.write(st.session_state['auth']) 
#             if confirmacao_texto != st.session_state['auth']:
#                 st.error('Usuário não autorizado / Código incorreto')
#             else:
#                 st.session_state['PeR']['edificio'] = edificio
#                 st.session_state['hierarquia'] = 0
#                 switch_page('q0')
#         else:
#             st.error('Código de verificação não gerado, insira seu email, clique no botão de envio e copie o código que receber por email')
#     else:
#         st.error('Insira todas as informações para prosseguir')
