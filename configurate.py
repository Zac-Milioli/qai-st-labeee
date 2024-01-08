from __future__ import annotations
## IMPORTED FUTURE FOR ST_PAGES HIDE PAGES
import streamlit as st 
import smtplib
import email.message
from random import randint


PeR = {'id_pergunta': [], 'resposta': []}
placeholder_img = r'static/placeholder.png'
st.session_state['auth'] = False
authorization_list = ["519249","215333","885531","618511","572447","869808","795177","371314","349847","725307","152101","687085","930430","862644","631116","202600","226685","675900","850068","502866","499124","119076","194394","850663","501970","343110","604899","873815","873732","332027","229599","195539","642693","113458","973402","798801","651854","588405","940423","774287","620429","797880","652906","713421","149751","419936","947997","372791","250261","469589","499024","854435","413249","856289","381478","617604","476102","738816","105552","961946","633041","305899","566873","299503","924671","502313","124981","563472","999154","314874","205129","685368","875393","430502","433164","209055","254352","479366","755502","800045","218490","280180","666648","651533","831232","711813","665228","484822","798532","145640","886177","791129","482785","486436","611493","464165","665697","786134","344894","828499"]

def create_top(big_text_title: str = None, subtitle: str = None, subtitle2: str = None, subsubtitle: str = None, img_url: str = None, use_line: bool = True, use_progress: bool = False, progress_percentage:int = 0):
    st.set_page_config(
    page_title='QAI em Escritórios',
    page_icon = '🖥️',
    layout='wide',
    initial_sidebar_state='collapsed'
    )
    st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
    [data-testid="stToolbarActions"] {
        display: none
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""",
    unsafe_allow_html=True,)
    hide_pages(['QAI', 'q0', 'introq1_sat', 'introq1_insat', 'q1a', 'c0', 'q1b', 'q1c', 'q2', 'q2a', 'q3', 'q3a', 'q4', 'q4a', 'q5', 'q5a', 'hi', 'cg', 'cp', 'sp', 'q6', 'fim'])
    with st.container():
        esquerda, meio, direita = st.columns(3)
        if use_progress:
            meio.progress(progress_percentage)

    with st.container():
        esquerda, meio, direita = st.columns([1.1,1, 1])
        meio.image(r'static/lab_banner.png', width=400)

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
    if use_line:
        st.markdown('---')

def place_left_subtitle(text: str):
    esquerda, direita = st.columns([3,1])
    esquerda.markdown(f'**{text}**')

def next_page_button(name: str, phrase: str = None, aviso: str = None):
    esquerda, direita = st.columns([4,1])
    if phrase:
        esquerda.subheader(phrase)
    if aviso:
        esquerda.info(aviso)
    direita.write('')
    botao = direita.button(label=name)
    return botao

def centered_button(name: str):
    esquerda, meio, direita = st.columns([1.5,1,1])
    botao = meio.button(name)
    return botao

def create_radio(name: str = None, phrase:str = None, extreme_left:str = None, extreme_right:str = None, min:int = 0, max:int = 10, divide:bool = False, key = None, show_values:bool = False, large:bool = False, five_columns_width:list = [1,0.5,0.4,0.6,1], two_columns_width:list = [1,2], selection:list = None, use_list_selection:bool = False, desabilitado: bool = False):
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
                if desabilitado:
                    valor = meio.radio(disabled=True, label='No name', label_visibility='hidden', options=opt, horizontal=True, format_func=(lambda x: ''), index=None, key=key)
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
                valor = st.radio(label='No name', label_visibility='hidden', options=opt, horizontal=True, format_func=(lambda x: ''), index=valor_inicial, key=key)
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

def mail_auth_code(mail_person:str):
    auth_code = authorization_list[randint(0, len(authorization_list)-1)]
    corpo_email = f"""
    <p>Seu código de verificação para o questionário é<p>
    <h1><strong>{auth_code}</strong></h1>
    <p>Esta é uma mensagem automática, não é necessário respondê-la.<p>
    <br>
    <hr>
    <p>Esta é uma mensagem automática, não é necessário respondê-la.</p><br><br>
    <a href="https://labeee.ufsc.br/pt-br/en-welcome"><img src="https://labeee.ufsc.br/sites/default/files/labeee_final_completo_maior.png" width="400" /></a>"""
    msg = email.message.Message()
    msg['Subject'] = f'CÓDIGO DE VERIFICAÇÃO - QAI em escritórios, LabEEE'
    msg['From'] = 'escritorios.qai.bot@gmail.com'
    msg['To'] = mail_person
    password = 'sxux ztfv fsiw aqfp'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    return auth_code

def send_thanks_email(mail_person:str):
    corpo_email = f"""
    <h2>A equipe LabEEE agradece pela participação na pesquisa!</h2>
    <br>
    <hr>
    <p>Esta é uma mensagem automática, não é necessário respondê-la.</p><br><br>
    <a href="https://labeee.ufsc.br/pt-br/en-welcome"><img src="https://labeee.ufsc.br/sites/default/files/labeee_final_completo_maior.png" width="400" /></a>"""
    msg = email.message.Message()
    msg['Subject'] = f'CONFIRMAÇÃO DE PARTICIPAÇÃO - QAI em escritórios, LabEEE'
    msg['From'] = 'escritorios.qai.bot@gmail.com'
    msg['To'] = mail_person
    password = 'sxux ztfv fsiw aqfp'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))


### IMPORTS FROM EXTERNAL MODULES

## STREAMLIT_EXTRAS --> switch page button
def switch_page(page_name: str):
    """
    Switch page programmatically in a multipage app

    Args:
        page_name (str): Target page name
    """
    from streamlit.runtime.scriptrunner import RerunData, RerunException
    from streamlit.source_util import get_pages

    def standardize_name(name: str) -> str:
        return name.lower().replace("_", " ")

    page_name = standardize_name(page_name)

    pages = get_pages("streamlit_app.py")  # OR whatever your main page is called

    for page_hash, config in pages.items():
        if standardize_name(config["page_name"]) == page_name:
            raise RerunException(
                RerunData(
                    page_script_hash=page_hash,
                    page_name=page_name,
                )
            )

    page_names = [standardize_name(config["page_name"]) for config in pages.values()]

    raise ValueError(f"Could not find page {page_name}. Must be one of {page_names}")


## ST_PAGES --> hide pages
import json
from dataclasses import dataclass
from pathlib import Path
from time import sleep

import toml

try:
    from streamlit import _gather_metrics  # type: ignore
except ImportError:

    def _gather_metrics(name, func, *args, **kwargs):
        return func


import streamlit as st
from streamlit import runtime
from streamlit.commands.page_config import get_random_emoji
from streamlit.errors import StreamlitAPIException
from streamlit.watcher import LocalSourcesWatcher

try:
    from streamlit.runtime.scriptrunner import get_script_run_ctx
except ImportError:
    from streamlit.scriptrunner.script_run_context import (  # type: ignore
        get_script_run_ctx,
    )

from streamlit.source_util import _on_pages_changed, get_pages

try:
    from streamlit.source_util import page_icon_and_name
except ImportError:
    from streamlit.source_util import page_name_and_icon  # type: ignore

    def page_icon_and_name(script_path: Path) -> tuple[str, str]:
        icon, name = page_name_and_icon(script_path)
        return name, icon


try:
    from streamlit import cache_resource
except ImportError:
    from streamlit import experimental_singleton as cache_resource

from streamlit.util import calc_md5

def _get_page_hiding_code(pages_to_hide: list[str]) -> str:
    styling = ""
    current_pages = get_pages("")
    section_hidden = False
    for idx, val in enumerate(current_pages.values()):
        page_name = val.get("page_name")
        if val.get("is_section"):
            # Set whole section as hidden
            section_hidden = page_name in pages_to_hide
        elif not val.get("in_section"):
            # Reset whole section hiding if we hit a page thats not in a section
            section_hidden = False
        if page_name in pages_to_hide or section_hidden:
            styling += f"""
                div[data-testid=\"stSidebarNav\"] li:nth-child({idx + 1}) {{
                    display: none;
                }}
            """

    styling = f"""
        <style>
            {styling}
        </style>
    """

    return styling


def _hide_pages(hidden_pages: list[str]):
    """
    For an app that wants to dynmically hide specific pages from the navigation bar.
    Note - this simply uses CSS to hide the menu item, it does not remove the page
    If using this with any security / permissions in mind,
    you also need to block the hidden page from executing
    """

    styling = _get_page_hiding_code(hidden_pages)

    st.write(
        styling,
        unsafe_allow_html=True,
    )


hide_pages = _gather_metrics("st_pages.hide_pages", _hide_pages)