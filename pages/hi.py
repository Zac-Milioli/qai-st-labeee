from configurate import *

create_top(big_text_title='Considerando a atual configuração física do seu escritório,')

st.subheader('você poderia indicar a importância dos fatores a seguir na realização das suas atividades de trabalho diárias?')
left = 'pouco importante'
right = 'muito importante'

st.title('')
fat1 = create_radio(phrase='conforto térmico', divide=True, extreme_left=left, extreme_right=right, min=1, max=5, key='fat1')
fat2 = create_radio(phrase='qualidade do ar', divide=True, extreme_left=left, extreme_right=right, min=1, max=5, key='fat2')
fat3 = create_radio(phrase='conforto visual', divide=True, extreme_left=left, extreme_right=right, min=1, max=5, key='fat3')
fat4 = create_radio(phrase='conforto acústico', divide=True, extreme_left=left, extreme_right=right, min=1, max=5, key='fat4')
fat5 = create_radio(phrase='ambientes específicos para atividades diferenciadas', divide=True, extreme_left=left, extreme_right=right, min=1, max=5, key='fat5')
fat6 = create_radio(phrase='proximidade e/ou acesso a vistas externas', divide=True, extreme_left=left, extreme_right=right, min=1, max=5, key='fat6')
fat7 = create_radio(phrase='privacidade visual', divide=True, extreme_left=left, extreme_right=right, min=1, max=5, key='fat7')
fat8 = create_radio(phrase='privacidade acústica', divide=True, extreme_left=left, extreme_right=right, min=1, max=5, key='fat8')
fat9 = create_radio(phrase='estar próximo à colegas e equipe de trabalho mesmo que não esteja totalmente confortável', divide=True, extreme_left=left, extreme_right=right, min=1, max=5, key='fat9')

st.title('')
if next_page_button('Próximo'):
    questoes = [fat1, fat2, fat3, fat4, fat5, fat6, fat7, fat8, fat9]
    if None in questoes:
        st.error('Responda **todas** as questões para prosseguir')
    else:
        PeR['id_pergunta'] += ['hi - conforto térmico', 'hi - qualidade do ar', 'hi - conforto visual', 'hi - conforto acústico', 'hi - ambientes específicos para atividades diferenciadas', 'hi - proximidade e/ou acesso a vistas externas', 'hi - privacidade visual', 'hi - privacidade acústica', 'hi - estar próximo à colegas e equipe de trabalho mesmo que não esteja totalmente confortável']
        PeR['resposta'] += questoes
        switch_page('cg')
