import streamlit as st 
from streamlit_extras.switch_page_button import switch_page
from st_pages import hide_pages
import smtplib
import email.message
    

PeR = {'id_pergunta': [], 'resposta': []}
participante = {'Email': ''}
level_hierarchy = {'num': []}
placeholder_img = r'static\placeholder.png'

def create_top(big_text_title: str = None, subtitle: str = None, subtitle2: str = None, subsubtitle: str = None, img_url: str = None):
    st.set_page_config(
    page_title='QAI em Escritórios',
    page_icon = '🖥️',
    layout='wide'
    )
    hide_pages(['QAI', 'q0', 'introq1_sat', 'introq1_insat', 'q1a', 'c0', 'q1b', 'q1c', 'q2', 'q2a', 'q3', 'q3a', 'q4', 'q4a', 'q5', 'q5a', 'hi', 'cg', 'cp', 'sp', 'q6', 'fim'])
    with st.container():
        esquerda, meio, direita = st.columns(3)
        meio.image(r'static\lab_banner.png', width=400)

    with st.container():
        esquerda, direita = st.columns(2, gap='medium')
        if big_text_title:
            esquerda.title(big_text_title)
        if subtitle:
            esquerda.subheader(subtitle)
        if subtitle2:
            esquerda.subheader(subtitle2)
        if subsubtitle:
            esquerda.write(subsubtitle)
        if img_url:
            direita.image(img_url, width=600)
    
    st.markdown('---')

def place_left_subtitle(text: str):
    esquerda, direita = st.columns([3,1])
    esquerda.markdown(f'**{text}**')

def next_page_button(name: str, phrase: str = ''):
    esquerda, direita = st.columns([4,1])
    esquerda.subheader(phrase)
    direita.write('')
    botao = direita.button(label=name)
    return botao

def centered_button(name: str):
    esquerda, meio, direita = st.columns([1.5,1,1])
    botao = meio.button(name)
    return botao

def create_radio(name: str = None, phrase:str = None, extreme_left:str = None, extreme_right:str = None, min:int = 0, max:int = 10, divide:bool = False, key = None, show_values:bool = False, large:bool = False, five_columns_width:list = [1,0.5,0.4,0.6,1], two_columns_width:list = [1,2], selection:list = None, use_list_selection:bool = False):
    if use_list_selection:
        opt = selection
    else:
        opt = range(min, max+1)
    if large:
        esquerda, direita = st.columns(two_columns_width)
        if phrase:
            esquerda.title('')
            esquerda.write(phrase)
        if name:
            if show_values:
                valor = direita.radio(label=name, options=opt, horizontal=True, index=None, key=key)
            else:
                valor = direita.radio(label=name, options=opt, horizontal=True, format_func=(lambda x: ''), index=None, key=key)
        else:
            if show_values:
                valor = direita.radio(label='No name', label_visibility='hidden', options=opt, horizontal=True, index=None, key=key)
            else:
                valor = direita.radio(label='No name', label_visibility='hidden', options=opt, horizontal=True, format_func=(lambda x: ''), index=None, key=key)
    elif divide:
        esquerda, vazio, meioesquerda, meio, meiodireita = st.columns(five_columns_width)
        if phrase:
            esquerda.title('')
            esquerda.write(phrase)
        if extreme_left:
            meioesquerda.title('')
            meioesquerda.caption(extreme_left)
        if extreme_right:
            meiodireita.title('')
            meiodireita.caption(extreme_right)
        if name:
            if show_values:
                valor = meio.radio(label=name, options=opt, horizontal=True, index=None, key=key)
            else:
                valor = meio.radio(label=name, options=opt, horizontal=True, format_func=(lambda x: ''), index=None, key=key)
        else:
            if show_values:
                valor = meio.radio(label='No name', label_visibility='hidden', options=opt, horizontal=True, index=None, key=key)
            else:
                valor = meio.radio(label='No name', label_visibility='hidden', options=opt, horizontal=True, format_func=(lambda x: ''), index=None, key=key)
    else:
        if name:
            if show_values:
                valor = st.radio(label=name, options=opt, horizontal=True, index=None, key=key)
            else:
                valor = st.radio(label=name, options=opt, horizontal=True, format_func=(lambda x: ''), index=None, key=key)
        else:
            if show_values:
                valor = st.radio(label='No name', label_visibility='hidden', options=opt, horizontal=True, index=None, key=key)
            else:
                valor = st.radio(label='No name', label_visibility='hidden', options=opt, horizontal=True, format_func=(lambda x: ''), index=None, key=key)
    return valor

def nested_radio(name: str = None, text_left:str = None, text_right:str = None, min:int = 0, max:int = 10, key = None, show_values:bool = False, columns_width:list = [0.2,0.6,0.6], selection:list = None, use_list_selection:bool = False):
    esquerda, meio, direita = st.columns(columns_width)
    if use_list_selection:
        opt = selection
    else:
        opt = range(min, max+1)
    if text_left:
        esquerda.write('')
        esquerda.write('')
        esquerda.caption(text_left)
    if text_right:
        direita.write('')
        direita.write('')
        direita.caption(text_right)
    if name:
        if show_values:
            valor = meio.radio(label=name, options=opt, horizontal=True, index=None, key=key)
        else:
            valor = meio.radio(label=name, options=opt, horizontal=True, format_func=(lambda x: ''), index=None, key=key)
    else:
        if show_values:
            valor = meio.radio(label='No name', label_visibility='hidden', options=opt, horizontal=True, index=None, key=key)
        else:
            valor = meio.radio(label='No name', label_visibility='hidden', options=opt, horizontal=True, format_func=(lambda x: ''), index=None, key=key)
    return valor

def mail_me(mail_person:str, perguntas_e_respostas:dict):
    corpo_email = f'{perguntas_e_respostas}'
    msg = email.message.Message()
    msg['Subject'] = f'RESPOSTAS DE {mail_person}'
    msg['From'] = 'escritorios.qai.bot@gmail.com'
    msg['To'] = 'escritorios.qai.bot@gmail.com'
    password = 'sxux ztfv fsiw aqfp'
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()

    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
