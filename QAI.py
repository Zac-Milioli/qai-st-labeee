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
            st.session_state['init_time'] = datetime.now()
            switch_page('q0')
        else:
            st.error("O ID do local de trabalho inserido não foi encontrado na base de dados", icon='⚠️')
    else:
        st.error('ERRO: O código inserido é diferente do código enviado', icon="⚠️")

footer()
