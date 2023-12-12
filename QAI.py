from configurate import *

create_top(big_text_title='QAI em Escritórios', subtitle='Design e organização: Luiza de Castro', subtitle2='Desenvolvimento: Zac Milioli')

st.markdown('***Caso a barra lateral (sidebar) esteja aberta, feche-a. Ela serve apenas para configuração do questionário**')

st.title('')
mail = st.text_input('no label', label_visibility='hidden', max_chars=100, key='emaildoparticipante', placeholder='Insira seu email')

st.title('')
if centered_button('Iniciar questionário'):
    if not mail:
        st.error('Preencha seu email para prosseguir')
    elif mail:
        if '@' not in mail:
            st.error('Insira um email válido para prosseguir')
        else:
            open(r'base/hierarquia.txt', 'w').write('')
            open(r'base/person_mail.txt', 'w').write(mail)
            switch_page('q0')
