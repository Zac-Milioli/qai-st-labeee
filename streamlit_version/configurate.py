import streamlit as st 

PeR = {'id_pergunta': [], 'resposta': []}

def create_top(big_text_title: str = None, subtitle: str = None, subtitle2: str = None, subsubtitle: str = None, img_url: str = None):
    st.set_page_config(
    page_title='QAI em Escritórios',
    page_icon = '🖥️'
    )
    with st.container():
        esquerda, meio, direita = st.columns([1,4,1])
        meio.image('https://github.com/Zac-Milioli/Quest_Luiza/blob/master/static/lab_banner.png?raw=true', width=450)
    
    st.title('')

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

def next_page_button(name: str):
    st.title('')
    esquerda, direita = st.columns([4,1])
    botao = direita.button(label=name)
    return botao

def centered_button(name: str):
    st.title('')
    esquerda, meio, direita = st.columns(3)
    botao = meio.button(name)
    return botao

def create_radio_0_10(name: str):
    st.title('')
    valor = st.slider(label=name, min_value=0, max_value=10, step=1)
    return valor

def create_radio_1_5(name: str):
    st.title('')
    valor = st.slider(label=name, min_value=1, max_value=5, step=1)
    return valor
