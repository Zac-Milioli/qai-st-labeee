from configurate import *

create_top(big_text_title='Proximidade a janelas', subtitle='Existem janelas e/ou outras áreas envidraçadas no seu ambiente de trabalho?')
select_width = 200

esquerda, meio, direita = st.columns(3)

esquerda.image(r'static/Q1b_janela.png', width=select_width)
meio.image(r'static/Q1b_janelalonge.png', width=select_width)
direita.image(r'static/Q1b_semjanela.png', width=select_width)

simconsigo = esquerda.checkbox('sim, consigo ver o exterior mesmo quando estou sentado(a) em minha estação de trabalho')
simporem = meio.checkbox('sim, porém estão muito afastadas da minha estação de trabalho')
nao = direita.checkbox('não existem janelas ou outras áreas envidraçadas no meu ambiente de trabalho')

st.title('')
if next_page_button('Próximo'):
    options = {'Sim consigo': simconsigo, 'Sim porém estão muito afastadas': simporem, 'Não': nao}
    verdadeiros = [chave for chave,valor in options.items() if valor]
    if len(verdadeiros) != 1:
        st.error('Selecione **uma** opção para continuar')
    else:
        PeR['id_pergunta'].append('q1b')
        PeR['resposta'].append(verdadeiros[0])
        if 'Sim' in verdadeiros[0]:
            open(r'base\janela.txt', 'w').write('1')
        else:
            open(r'base\janela.txt', 'w').write('0')
        switch_page('q1c')
