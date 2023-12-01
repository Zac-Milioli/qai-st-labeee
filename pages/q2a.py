from configurate import *

create_top(big_text_title='Parece que temos um probleminha com o ambiente térmico...', img_url=r'static\Q1insat.png')

st.subheader('Por favor indique quais dos itens a seguir estão presentes no seu ambiente de trabalho:')


if next_page_button('Próximo'):
    st.success('Clicou o botão')