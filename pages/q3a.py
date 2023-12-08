from configurate import *

create_top(big_text_title='Puxa, encontramos um problema com a qualidade do ar interno...', img_url=r'static\Q3a.png')

st.subheader('Com relação ao ar interno próximo à sua estação de trabalho, com qual frequência você costuma identificar algum dos itens ou sintomas a seguir?')
opt = ['diariamente, na maior parte do tempo', 'diariamente, durante algumas horas', 'eventualmente, durante algumas horas', 'raramente, durante algumas horas', 'nunca sinto']
width_choosen = [0.3,1.3]

st.title('')
cheiro = create_radio(phrase='sinto cheiros e/ou odores no ambiente', large=True, two_columns_width=width_choosen, selection=opt, use_list_selection=True, show_values=True, key='cheirosfortes')
st.markdown('---')
fadiga = create_radio(phrase='sensação de fadiga e/ou sonolência', large=True, two_columns_width=width_choosen, selection=opt, use_list_selection=True, show_values=True, key='fadiga')
st.markdown('---')
ressecamento = create_radio(phrase='sensação de ressecamento nos olhos, nariz e/ou mãos', large=True, two_columns_width=width_choosen, selection=opt, use_list_selection=True, show_values=True, key='ressecamento')
st.markdown('---')
alergia = create_radio(phrase='irritações na pele e/ou alergias', large=True, two_columns_width=width_choosen, selection=opt, use_list_selection=True, show_values=True, key='alergias')

st.title('')
st.title('')
st.title('')
st.title('')
st.title('Considerando todos os aspectos,')
st.subheader('qual o seu nível de satisfação com a qualidade do ar interno na sua estação de trabalho?')
st.title('')

new_width = [0.8,0.2,0.25,0.4,0.4]

qualidadedoar = create_radio(divide=True, five_columns_width=new_width, min=1, max=5, extreme_left='insatisfeito(a)', extreme_right='satisfeito(a)')


st.title('')
st.title('')
st.title('')
st.title('')
st.title("Temos uma nota baixa para a qualidade do ar...")
st.subheader('Então, para termos certeza, por favor indique os motivos pelos quais você está insatisfeito(a).')

cheiroscheckbox = st.checkbox('cheiros e odores', key='cheiroscheckbox')
abafadocheckbox = st.checkbox('ambiente abafado', key='abafadocheckbox')
arsecocheckbox = st.checkbox('ar interno muito seco', key='arsecocheckbox')
arumidocheckbox = st.checkbox('ar interno muito úmido', key='arumidocheckbox')
poeiracheckbox = st.checkbox('há poeira que causa irritação ou alergias', key='poeiracheckbox')
alergiascheckbox = st.checkbox('há produtos que causam irritação ou alergias', key='alergiascheckbox')
outros = st.checkbox('outro, por favor especifique:', key='outros')
if outros:
    entrada = st.text_area(label='no label', label_visibility='hidden',value=None, key='entrybox', placeholder='Descreva aqui', max_chars=150)

st.title('')
st.title('')
if next_page_button('Próximo'):
    ok = True
    arinterno = [cheiro, fadiga, ressecamento, alergia, qualidadedoar]
    if None in arinterno:
        ok = False
    if outros:
        if entrada == None:
            ok = False
    if ok:
        PeR['id_pergunta'] += ['q3a - sinto cheiros e/ou odores no ambiente', 'q3a - sensação de fadiga e/ou sonolência', 'q3a - sensação de ressecamento nos olhos, nariz e/ou mãos', 'q3a - irritações na pele e/ou alergias', 'q3a - nível de satisfação com o ar interno']
        PeR['resposta'] += arinterno
        PeR['id_pergunta'] += ['q3a - insatifação por cheiros e odores', 'q3a - insatifação por ambiente abafado', 'q3a - insatifação por ar interno muito seco', 'q3a - insatifação por ar interno muito úmido', 'q3a - insatifação por haver poeira que causa irritação ou alergias', 'q3a - insatifação por haver produtos que causam irritação ou alergias']
        PeR['resposta'] += [cheiroscheckbox, abafadocheckbox, arsecocheckbox, arumidocheckbox, poeiracheckbox, alergiascheckbox]
        if outros:
            PeR['id_pergunta'].append('outros motivos')
            PeR['resposta'].append(entrada)
        switch_page('q4')
    else:
        st.error('Responda **todas** as questões para prosseguir')
