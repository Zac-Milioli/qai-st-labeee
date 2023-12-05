from configurate import *

existe_janela = open(r'base\janela.txt', 'r').read()
if existe_janela == '1':
    existe_janela = True
else:
    existe_janela = False

create_top(big_text_title='Parece que temos um probleminha com o ambiente térmico...', img_url=r'static\Q1insat.png')
img_width = 200
st.subheader('Por favor indique quais dos itens a seguir estão presentes no seu ambiente de trabalho:')
st.title('')


nenhumcontroletermostato1, nenhumcontroletermostato2, nenhumcontrolejanela1, nenhumcontrolejanela2, nenhumcontrolejanela3, nenhumcontroleventilador1, nenhumcontroleventilador2, algumcontrolejanela, algumcontroletermostato1, algumcontroletermostato2, algumcontroletermostato3, algumcontroletermostato4 = False,False,False,False,False,False,False,False,False,False,False,False

vazio, esquerda, meio, direita, vazio2 = st.columns([0.5,0.6,1,1, 0.5])
esquerda.title('')
esquerda.title('')
esquerda.title('')
esquerda.title('')
esquerda.markdown('**sistema de climatização artificial**')
meio.image(r'static\arcondicionado.png', width=img_width)
arcondicionado = meio.checkbox(label='ar-condicionado')
direita.image(r'static\aquecedor.png', width=img_width)
aquecedor = direita.checkbox(label='aquecedores')
esquerda.title('')
esquerda.title('')
esquerda.title('')
esquerda.title('')
esquerda.title('')
esquerda.title('')
meio.title('')
direita.title('')
esquerda.markdown('**ventiladores**')
meio.image(r'static\ventiladorteto.png', width=img_width)
vent_teto = meio.checkbox(label='de teto e/ou parede')
direita.image(r'static\ventiladormesa.png', width=img_width) 
vent_mesa = direita.checkbox(label='portáteis, de mesa e/ou individuais')

st.title('')
st.title('')
st.title('')
st.title('')
st.subheader('Na sua estação de trabalho, como você descreve ou classifica...')
st.title('')

esquerda, meio, vazio, direita = st.columns([0.75, 1, 0.15, 1])
meio.markdown('**durante o verão e/ou meses quentes**')
direita.markdown('**durante o inverno e/ou meses frios**')

vazio, esquerda, meioesquerda, meiomeio, meiodireita,direitaesquerda, direitameio, direitadireita = st.columns([0.2,1,0.5,1,1,0.5,1,1])


esquerda.write('')
esquerda.write('')
esquerda.markdown('**o ambiente térmico?**')

meioesquerda.write('')
meioesquerda.write('')
meioesquerda.caption('quente')
ambientetermicoverao = meiomeio.radio(label='label', label_visibility='hidden', options=range(0,5), horizontal=True, format_func=(lambda x: ''), index=None, key='ambienteverao')
meiodireita.write('')
meiodireita.write('')
meiodireita.caption('frio')

direitaesquerda.write('')
direitaesquerda.write('')
direitaesquerda.caption('quente')
ambientetermicoinverno = direitameio.radio(label='label', label_visibility='hidden', options=range(0,5), horizontal=True, format_func=(lambda x: ''), index=None, key='ambienteinverno')
direitadireita.write('')
direitadireita.write('')
direitadireita.caption('frio')


esquerda.write('')
esquerda.write('')
esquerda.markdown('**o movimento do ar?**')

meioesquerda.write('')
meioesquerda.write('')
meioesquerda.caption('abafado')
arverao = meiomeio.radio(label='label', label_visibility='hidden', options=range(0,5), horizontal=True, format_func=(lambda x: ''), index=None, key='arverao')
meiodireita.write('')
meiodireita.write('')
meiodireita.caption('ventilado')

direitaesquerda.write('')
direitaesquerda.write('')
direitaesquerda.caption('abafado')
arinverno = direitameio.radio(label='label', label_visibility='hidden', options=range(0,5), horizontal=True, format_func=(lambda x: ''), index=None, key='arinverno')
direitadireita.write('')
direitadireita.write('')
direitadireita.caption('ventilado')


esquerda.write('')
esquerda.write('')
esquerda.markdown('**o ambiente térmico?**')

meioesquerda.write('')
meioesquerda.write('')
meioesquerda.caption('desconfortável')
confortoverao = meiomeio.radio(label='label', label_visibility='hidden', options=range(0,5), horizontal=True, format_func=(lambda x: ''), index=None, key='confortoverao')
meiodireita.write('')
meiodireita.write('')
meiodireita.caption('confortável')

direitaesquerda.write('')
direitaesquerda.write('')
direitaesquerda.caption('desconfortável')
confortoinverno = direitameio.radio(label='label', label_visibility='hidden', options=range(0,5), horizontal=True, format_func=(lambda x: ''), index=None, key='confortoinverno')
direitadireita.write('')
direitadireita.write('')
direitadireita.caption('confortável')

if existe_janela:
    st.title('')
    st.title('')
    st.title('')
    st.title('')
    st.subheader('como você classifica o nível de controle que você possui sobre a ventilação natural?')
    st.title('')
    classificacoes, esquerda, meioesquerda, meiodireita, direita = st.columns([0.5,1,1,1,1])
    classificacoes.title('')
    classificacoes.title('')
    classificacoes.title('')
    classificacoes.title('')
    classificacoes.title('')

    classificacoes.markdown('**nenhum controle:**')
    classificacoes.title('')
    classificacoes.title('')
    classificacoes.title('')
    classificacoes.title('')
    classificacoes.title('')
    classificacoes.write('')
    classificacoes.write('')
    classificacoes.write('')
    classificacoes.write('')
    esquerda.image(r'static\nenhumcontrolejanela1.png', width=img_width)
    nenhumcontrolejanela1 = esquerda.checkbox(label='as janelas não são operáveis e estão sempre fechadas', key='nenhumcontrolejanela1')
    meioesquerda.image(r'static\nenhumcontrolejanela2.png', width=img_width)
    nenhumcontrolejanela2 = meioesquerda.checkbox(label='as janelas são operáveis, porém é obrigatório que estejam sempre fechadas', key='nenhumcontrolejanela2')
    meiodireita.image(r'static\nenhumcontrolejanela3.png', width=img_width)
    nenhumcontrolejanela3 = meiodireita.checkbox(label='a decisão de abrir ou fechar as janelas não é minha', key='nenhumcontrolejanela3')
    meioesquerda.title('')
    esquerda.title('')

    classificacoes.markdown('**algum controle:**')
    classificacoes.title('')
    classificacoes.title('')
    classificacoes.title('')
    classificacoes.title('')
    classificacoes.title('')
    classificacoes.write('')
    classificacoes.write('')
    classificacoes.write('')
    esquerda.image(r'static\opiniaogeral.png', width=img_width)
    algumcontrolejanela = esquerda.checkbox(label='todos os colegas dão sua opinião e chegamos a um acordo', key='opiniaogeraljanela')

    esquerda.title('')

    classificacoes.markdown('**controle total:**')
    esquerda.image(r'static\controletotaljanela.png', width=img_width)
    controletotaljanela = esquerda.checkbox(label='abro/fecho a janela mais próxima à minha estação de trabalho sempre que me sinto desconfortável com a temperatura, o movimento e/ou a velocidade do ar', key='controletotaljanela')

if arcondicionado or aquecedor:
    st.title('')
    st.title('')
    st.title('')
    st.title('')
    st.subheader('como você classifica o nível de controle que você possui sobre o aquecimento e/ou resfriamento?')
    st.title('')
    classificacoes, esquerda, meioesquerda, meiodireita, direita = st.columns([0.5,1,1,1,1])
    classificacoes.title('')
    classificacoes.title('')
    classificacoes.title('')
    classificacoes.title('')
    classificacoes.title('')

    classificacoes.markdown('**nenhum controle:**')
    classificacoes.title('')
    classificacoes.title('')
    classificacoes.title('')
    classificacoes.title('')
    classificacoes.title('')
    classificacoes.title('')
    classificacoes.title('')
    esquerda.image(r'static\nenhumcontroletermostato1.png', width=img_width)
    nenhumcontroletermostato1 = esquerda.checkbox(label='o controle do termostato e da velocidade e direção do ar-condicionado não está disponível', key='nenhumcontroletermostato1')
    meioesquerda.image(r'static\nenhumcontroletermostato2.png', width=img_width)
    nenhumcontroletermostato2 = meioesquerda.checkbox(label='a decisão de ligar ou desligar o ar-condicionado não é minha', key='nenhumcontroletermostato2')
    meioesquerda.title('')
    esquerda.title('')
    direita.title('')
    meiodireita.title('')
    direita.title('')
    meiodireita.title('')
    direita.title('')
    meiodireita.title('')
    direita.title('')
    meiodireita.title('')
    direita.title('')
    meiodireita.title('')
    direita.write('')
    meiodireita.write('')
    direita.title('')
    meiodireita.title('')
    direita.title('')
    meiodireita.title('')

    classificacoes.markdown('**algum controle:**')
    classificacoes.title('')
    classificacoes.title('')
    classificacoes.title('')
    classificacoes.title('')
    classificacoes.title('')
    classificacoes.title('')
    classificacoes.title('')
    esquerda.image(r'static\algumcontroletermostato1.png', width=img_width)
    algumcontroletermostato1 = esquerda.checkbox(label='não posso controlar o termostato do ar-condicionado, apenas a velocidade e direção do ar', key='algumcontroletermostato1')
    meioesquerda.image(r'static\algumcontroletermostato2.png', width=img_width)
    algumcontroletermostato2 = meioesquerda.checkbox(label='não posso controlar a velocidade e direção do ar-condicionado, apenas o termostato', key='algumcontroletermostato2')
    meiodireita.image(r'static\algumcontroletermostato3.png', width=img_width)
    algumcontroletermostato3 = meiodireita.checkbox(label='é possível realizar alterações na temperatura conforme a minha preferência, porém é necessário abrir um chamado e/ou acionar o responsável pelo sistema', key='algumcontroletermostato3')
    direita.image(r'static\opiniaogeral.png', width=img_width)
    algumcontroletermostato4 = direita.checkbox(label='todos os colegas dão sua opinião e chegamos a um acordo', key='opiniaogeraltermostato')

    esquerda.title('')
    meioesquerda.title('')
    meiodireita.title('')
    direita.title('')

    classificacoes.markdown('**controle total:**')
    esquerda.image(r'static\controletotaltermostato.png', width=img_width)
    controletotaltermostato = esquerda.checkbox(label='altero o termostato e a velocidade e direção do ar-condicionado sempre que me sinto desconfortável com a temperatura interna', key='controletotaltermostato')

if vent_mesa or vent_teto:
    st.title('')
    st.title('')
    st.title('')
    st.title('')
    st.subheader('como você classifica o nível de controle que você possui sobre os ventiladores?') 
    st.title('')
    classificacoes, esquerda, meioesquerda, meiodireita, direita = st.columns([0.5,1,1,1,1])
    classificacoes.title('')
    classificacoes.title('')
    classificacoes.title('')
    classificacoes.title('')
    classificacoes.title('')

    classificacoes.markdown('**nenhum controle:**')
    classificacoes.title('')
    classificacoes.title('')
    classificacoes.title('')
    classificacoes.title('')
    classificacoes.write('')
    classificacoes.write('')
    classificacoes.write('')
    esquerda.image(r'static\nenhumcontroleventilador1.png', width=img_width)
    nenhumcontroleventilador1 = esquerda.checkbox(label='não posso controlar os ventiladores (ligar ou desligar, mudar a direção e intensidade do vento)', key='nenhumcontroleventilador1')
    meioesquerda.image(r'static\nenhumcontroleventilador2.png', width=img_width)
    nenhumcontroleventilador2 = meioesquerda.checkbox(label='a decisão de ligar ou desligar os ventiladores não é minha', key='nenhumcontroleventilador2')

    classificacoes.markdown('**algum controle:**')
    classificacoes.title('')
    classificacoes.title('')
    classificacoes.title('')
    classificacoes.title('')
    classificacoes.title('')
    classificacoes.write('')
    classificacoes.write('')
    classificacoes.write('')
    classificacoes.write('')
    esquerda.image(r'static\opiniaogeral.png', width=img_width)
    algumcontroleventilador = esquerda.checkbox(label='todos os colegas dão sua opinião e chegamos a um acordo', key='algumcontroleventilador')

    esquerda.title('')

    classificacoes.markdown('**controle total:**')
    esquerda.image(r'static\controletotalventilador.png')
    controletotalventilador = esquerda.checkbox(label='ligo e desligo o(s) ventilador(es) mais próximo à minha estação de trabalho sempre que me sinto desconfortável', key='controletotalventilador')

st.title('')
st.title('')
st.title('')
st.title('')
st.title('Considerando todos os aspectos,')
st.subheader('qual o seu nível de satisfação com o ambiente térmico da sua estação de trabalho?')
st.title('')
vazio, esquerda, vazio2, direita, vazio3 = st.columns([0.5,1,1.3,1,0.8])
esquerda.markdown('**durante o verão e/ou meses quentes**')
direita.markdown('**durante o inverno e/ou meses frios**')

vazio, caption_esquerda1, radioesquerda, caption_esquerda2, vazio2,caption_direita1, radiodireita, caption_direita2 = st.columns([0.1, 0.2,0.4,0.5, 0.1, 0.2,0.4,0.5])
caption_esquerda1.title('')
caption_esquerda1.caption('insatisfeito(a)')
caption_esquerda2.title('')
caption_esquerda2.caption('satisfeito(a)')
veraosatisfacao = radioesquerda.radio(label='no label', label_visibility='hidden', index=None, horizontal=True, options=range(0,5), format_func=(lambda x: ''), key='satisfacaoverao2')

caption_direita1.title('')
caption_direita1.caption('insatisfeito(a)')
caption_direita2.title('')
caption_direita2.caption('satisfeito(a)')
invernosatisfacao = radiodireita.radio(label='no label', label_visibility='hidden', index=None, horizontal=True, options=range(0,5), format_func=(lambda x: ''), key='satisfacaoinverno2')

st.title('')
st.title('')
st.title('')
st.title('')
st.title('Temo suma nota baixa para os meses quentes...')
st.subheader('Então, para termos certeza, por favor indique os motivos pelos quais você está insatisfeito(a) com o ambiente térmico durante esse período.')
st.title('')
baixaquentes6,baixaquentes12,baixaquentes7,baixaquentes8,baixaquentes11 = False,False,False,False,False
baixaquentes1 = st.checkbox(label='sinto desconforto por calor', key='baixasquentes1')
baixaquentes2 = st.checkbox(label='sinto desconforto por frio', key='baixasquentes2')
baixaquentes3 = st.checkbox(label='sinto desconforto porque há muito vento', key='baixasquentes3')
baixaquentes4 = st.checkbox(label='sinto desconforto porque há pouco vento', key='baixasquentes4')
baixaquentes5 = st.checkbox(label='o sol direto me atrapalha', key='baixasquentes5')
if nenhumcontroletermostato1 or nenhumcontroletermostato2 or algumcontroletermostato1 or algumcontroletermostato2 or algumcontroletermostato3 or algumcontroletermostato4:
    baixaquentes6 = st.checkbox(label='sinto desconforto devido à corrente de ar gerada pelo ar-condicionado', key='baixasquentes6')
    baixaquentes12 = st.checkbox(label='sinto desconforto por não poder controlar a temperatura do ar-condicionado de acordo com a minha preferência', key='baixasquentes12')
if vent_mesa or vent_teto:
    baixaquentes7 = st.checkbox(label='sinto desconforto devido à corrente de ar gerada pelo(s) ventilador(es)', key='baixasquentes7')
if nenhumcontrolejanela1 or nenhumcontrolejanela2 or nenhumcontrolejanela3 or algumcontrolejanela:
    baixaquentes8 = st.checkbox(label='sinto desconforto devido à corrente de ar proveniente da(s) janela(s)', key='baixasquentes8')
    baixaquentes11 = st.checkbox(label='sinto desconforto por não poder abrir ou fechar as janelas de acordo com a minha preferência', key='baixasquentes11')
baixaquentes9 = st.checkbox(label='há superfícies próximas (pisos, paredes, equipamentos etc) muito quentes ou muito frias', key='baixasquentes9')
baixaquentes10 = st.checkbox(label='sinto desconforto por frio ou calor em alguma parte específica do corpo (mãos, pés, pescoço, cabeça, etc)', key='baixasquentes10')

st.title('')
st.title('')
if next_page_button('Próximo'):
    siga = True
    message = 'Problemas no preenchimento de:  '
    if existe_janela:
        controlejanela = {'as janelas não são operáveis e estão sempre fechadas':nenhumcontrolejanela1, 'as janelas são operáveis, porém é obrigatório que estejam sempre fechadas':nenhumcontrolejanela2, 'a decisão de abrir ou fechar as janelas não é minha':nenhumcontrolejanela3, 'todos os colegas dão sua opinião e chegamos a um acordo':algumcontrolejanela, 'abro/fecho a janela mais próxima à minha estação de trabalho sempre que me sinto desconfortável com a temperatura, o movimento e/ou a velocidade do ar':controletotaljanela}
        verdadeiros_controlejanela = [chave for chave, valor in controlejanela.items() if valor]
        if len(verdadeiros_controlejanela) != 1:
            siga = False
            message += 'Controle de janela  '
    if arcondicionado or aquecedor:
        controletermostato = {'o controle do termostato e da velocidade e direção do ar-condicionado não está disponível':nenhumcontroletermostato1, 'a decisão de ligar ou desligar o ar-condicionado não é minha':nenhumcontroletermostato2, 'não posso controlar o termostato do ar-condicionado, apenas a velocidade e direção do ar':algumcontroletermostato1, 'não posso controlar a velocidade e direção do ar-condicionado, apenas o termostato':algumcontroletermostato2, 'é possível realizar alterações na temperatura conforme a minha preferência, porém é necessário abrir um chamado e/ou acionar o responsável pelo sistema':algumcontroletermostato3,  'todos os colegas dão sua opinião e chegamos a um acordo':algumcontroletermostato4, 'altero o termostato e a velocidade e direção do ar-condicionado sempre que me sinto desconfortável com a temperatura interna': controletotaltermostato}
        verdadeiros_termostato = [chave for chave, valor in controletermostato.items() if valor]
        if len(verdadeiros_termostato) != 1:
            siga = False
            message += 'Controle de ar-condicionados  '
    if vent_mesa or vent_teto:
        controleventilador = {'não posso controlar os ventiladores (ligar ou desligar, mudar a direção e intensidade do vento)':nenhumcontroleventilador1, 'a decisão de ligar ou desligar os ventiladores não é minha':nenhumcontroleventilador2, 'todos os colegas dão sua opinião e chegamos a um acordo':algumcontroleventilador,' ligo e desligo o(s) ventilador(es) mais próximo à minha estação de trabalho sempre que me sinto desconfortável':controletotalventilador}
        verdadeiros_vent = [chave for chave, valor in controlejanela.items() if valor]
        if len(verdadeiros_vent) != 1:
            siga = False
            message += 'Controle de ventiladores  '
    considerandoaspectos = [veraosatisfacao, invernosatisfacao]
    if None in considerandoaspectos:
        siga = False
        message += 'Nível de satisfação  '
    estacaodetrabalho = [ambientetermicoverao, ambientetermicoinverno, arverao, arinverno, confortoverao, confortoinverno]
    if None in estacaodetrabalho:
        siga = False
        message += 'Avaliação de ambiente térmico e movimento do ar  '
    motivos_insatisfacao = [baixaquentes1,baixaquentes2,baixaquentes3,baixaquentes4,baixaquentes5,baixaquentes6,baixaquentes7,baixaquentes8,baixaquentes9,baixaquentes10,baixaquentes11,baixaquentes12]
    itens_presentes = [arcondicionado, aquecedor, vent_teto, vent_mesa]
    if siga:
        PeR['id_pergunta'].append('q2a-controle de janela')
        PeR['resposta'].append(verdadeiros_controlejanela[0])
        PeR['id_pergunta'].append('q2a-controle de ar-condicionado')
        PeR['resposta'].append(verdadeiros_termostato[0])
        PeR['id_pergunta'].append('q2a-controle de ventiladores')
        PeR['resposta'].append(verdadeiros_vent[0])
        PeR['id_pergunta'].append('q2a-satisfacao em meses quentes')
        PeR['id_pergunta'].append('q2a-satisfacao em meses frios')
        PeR['resposta'] += considerandoaspectos
        PeR['id_pergunta'].append('q2a-ambiente térmico em meses quentes - temperatura')
        PeR['id_pergunta'].append('q2a-ambiente térmico em meses frios - temperatura')
        PeR['id_pergunta'].append('q2a-movimento do ar em meses quentes - ventilação')
        PeR['id_pergunta'].append('q2a-movimento do ar em meses frios - ventilação')
        PeR['id_pergunta'].append('q2a-ambiente térmico em meses quentes - conforto')
        PeR['id_pergunta'].append('q2a-ambiente  térmico em meses frios - conforto')
        PeR['resposta'] += estacaodetrabalho
        PeR['id_pergunta'] += ['q2a - sinto desconforto por calor', 'q2a - sinto desconforto por frio', 'q2a - sinto desconforto porque há muito vento', 'q2a - sinto desconforto porque há pouco vento', 'q2a - o sol direto me atrapalha', 'q2a - sinto desconforto devido à corrente de ar gerada pelo ar-condicionado', 'q2a - sinto desconforto devido à corrente de ar gerada pelo(s) ventialdor(es)', 'q2a - sinto desconforto devido à corrente de ar proveniente da(s) janela(s)',  'q2a - há superfícies próximas (pisos, paredes, equipamentos etc) muito quentes ou muito frias', 'q2a - sinto desconforto por frio ou calor em alguma parte específica do corpo (mãos, pés, pescoço, cabeça, etc)', 'q2a - sinto desconforto por não poder abrir ou fechar as janelas de acordo com a minha preferência', 'q2a - sinto desconforto por não poder controlar a temperatura do ar-condicionado de acordo com a minha preferência']
        PeR['resposta'] += motivos_insatisfacao
        PeR['id_pergunta'] += ['q2a - ar-condicionado', 'q2a - aquecedores', 'q2a - ventilador de teto e/ou parede', 'q2a - ventilador portátil, de mesa e/ou individual']
        PeR['resposta'] += itens_presentes
        switch_page('q3')
    else:
        st.error(message) 