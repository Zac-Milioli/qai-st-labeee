import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from configurate import *

create_top(big_text_title='QAI em Escritórios', subtitle='Design e organização: Luiza de Castro', subtitle2='Desenvolvimento: Zac Milioli')

st.markdown('***Caso a barra de menu esteja abertam feche-a. Ela serve apenas para configuração do questionário**')

if centered_button('Iniciar questionário'):
    switch_page('q0')
