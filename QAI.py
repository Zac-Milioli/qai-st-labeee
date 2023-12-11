from configurate import *

create_top(big_text_title='QAI em Escritórios', subtitle='Design e organização: Luiza de Castro', subtitle2='Desenvolvimento: Zac Milioli')

st.markdown('***Caso a barra lateral (sidebar) esteja aberta, feche-a. Ela serve apenas para configuração do questionário**')

st.title('')
if centered_button('Iniciar questionário'):
    switch_page('q0')
