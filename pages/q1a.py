from configurate import *

create_top(big_text_title='O seu ambiente de trabalho', subtitle='Por favor selecione o tipo de layout do escritório que representa o seu ambiente de trabalho. (apenas um item)')
select_width = 120


esquerda, meioesquerda, meio, meiodireita = st.columns(4)
esquerda.title('')
esquerda.title('')
esquerda.title('')
esquerda.title('')
meioesquerda.title('')
meio.title('')
meiodireita.title('')
esquerda.markdown('**Sala privada:**')
meioesquerda.image(r'static/Q1a_indv.png', width=select_width)
meio.image(r'static/Q1a_compart.png', width=select_width)
individual = meioesquerda.checkbox('individual')
compartilhada = meio.checkbox('compartilhada com um ou mais colegas')

esquerda.title('')
esquerda.title('')
esquerda.title('')
esquerda.title('')
meioesquerda.title('')
meio.title('')
meiodireita.title('')
meiodireita.title('')
meiodireita.title('')
meiodireita.title('')
meiodireita.text('')
meiodireita.text('')
meiodireita.text('')
esquerda.markdown('**Planta aberta:**')
meioesquerda.image(r'static\Q1a_semdiv.png', width=select_width)
meio.image(r'static\Q1a_comdivbaixa.png', width=select_width)
meiodireita.image(r'static\Q1a_comdivalta.png', width=select_width)
semdivisorias = meioesquerda.checkbox('sem divisórias')
comdivisoriasbaixas = meio.checkbox('com divisórias baixas: consigo visualizar meus colegas e entorno mesmo estando sentado(a)')
comdivisoriasaltas = meiodireita.checkbox('com divisórias altas: preciso me levantar para visualizar meus colegas e entorno')



esquerda.title('')
esquerda.title('')
esquerda.title('')
esquerda.title('')
meioesquerda.title('')
esquerda.markdown('**Sem localização fixa:**')
meioesquerda.image(r'static\Q1a_semfixa.png', width=select_width)
semlocalizacaofixa = meioesquerda.checkbox('eu não tenho uma mesa designada para mim, posso escolher diariamente a minha estação de trabalho')

st.title('')
if next_page_button(name='Próximo'):
    options = {'individual': individual, 'fixa': compartilhada, 'sem divisórias': semdivisorias, 'com divisórias baixas': comdivisoriasbaixas, 'com divisórias altas': comdivisoriasaltas, 'sem localização fixa': semlocalizacaofixa}
    verdadeiros = [chave for chave, valor in options.items() if valor]
    if len(verdadeiros) != 1:
        st.error('Selecione **uma** opção para prosseguir')
    else:
        PeR['id_pergunta'].append('q1a')
        PeR['resposta'].append(verdadeiros[0])
        if verdadeiros[0] == 'sem localização fixa':
            switch_page('c0')
        else:
            switch_page('q1b')    
