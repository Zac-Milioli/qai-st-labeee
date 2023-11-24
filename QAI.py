import tkinter as tk
from tkinter import messagebox

#Variables
title_style = ('Inter', 27)
text_style = ('Inter', 12)
subtitle_style = ('Inter', 17)
title_padding_y = 40
text_padding_x = 50
text_padding_y = 10
button_padding_y = 50
frame_paddding_y = 40
background_color = '#F2F2F2'
text_color = 'black'
entry_background = '#C5FFC0'
button_background = '#A9D18E'
radio_background = '#C4C4C4'
button_text_color = 'white'


#Objects
class PeR:
    def __init__(self, pergunta: list = [], resposta: list = [], json_to_send: dict = None):
        self.pergunta: list = pergunta
        self.resposta: list = resposta
        self.json_to_send: dict = json_to_send
    
    def save_PeR(self):
        dataframeable = {'Perguntas': self.pergunta, 'Respostas': self.resposta}
        self.json_to_send = dataframeable

    def mail_to_luiza(self, name, person_email):
        # Email Luiza: luizatdecastro@gmail.com
        title = f'RESPOSTAS QAI DE {name}'
        body_text = self.json_to_send

#Funções
def login_user():
    nome = name_entry.get()
    email = email_entry.get()
    if nome=='' or email=='':
        messagebox.showerror(title='ERRO', message='Você deve inserir todos os dados pedidos')
        return 0
    elif '@' not in email:
        messagebox.showerror(title='ERRO', message='Formato de email inválido')
        return 0
    else:
        user['name'] = nome
        user['email'] = email
        login.destroy()

def save_q0():
    resposta = q0_radio_var.get()
    q0_resposta['value'] = resposta
    if resposta in range(0,7):
        q0_resposta['r'] = True
    quiz.pergunta.append('Q0')
    quiz.resposta.append(resposta)
    q0.destroy()

def save_q1a():
    resposta = opt_var.get()
    if 'eu não tenho uma mesa' in resposta:
        sem_mesa_fixa['r'] = True
    quiz.pergunta.append('Q1a')
    quiz.resposta.append(resposta)
    q1a.destroy()

def save_q1b():
    resposta = opt_var.get()
    if 'não existem janelas' in resposta:
        sem_janelas['r'] = True
    quiz.pergunta.append('Q1b')
    quiz.resposta.append(resposta)
    q1b.destroy()

def save_q1c():
    quiz.pergunta = quiz.pergunta + ['Q1c1', 'Q1c2', 'Q1c3', 'Q1c4', 'Q1c5', 'Q1c6']
    quiz.resposta = quiz.resposta + [q1c1_var.get(), q1c2_var.get(), q1c3_var.get(), q1c4_var.get(), q1c5_var.get(), q1c6_var.get()]
    q1c.destroy()

#Aplicação
quiz = PeR()
user = {'name': None, 'email': None}
has_windows = {'r': False}
has_climatizacao = {'r': False}
sem_janelas = {'r': False}
q0_resposta = {'r': False, 'value': None}
sem_mesa_fixa = {'r': False}

#Login
login = tk.Tk() 
login.title('QAI - Login')
login.attributes('-fullscreen',True)
login.configure(bg=background_color)
banner_file = tk.PhotoImage(file=r'static\lab_banner.png', master=login)
banner = tk.Label(login, image=banner_file, bg=background_color)
banner.pack()
login_frame = tk.Frame(bg=background_color)
login_frame.pack(pady=frame_paddding_y)

titulo = tk.Label(login_frame, text='LOGIN', bg=background_color, fg=text_color, font=title_style)
titulo.grid(row=1, column=0, pady=title_padding_y, columnspan=2)

login_text = tk.Label(login_frame, text='Preencha com suas informações', font=text_style, bg=background_color, fg=text_color)
login_text.grid(row=2, column=0, pady=text_padding_y, columnspan=2)

name_text = tk.Label(login_frame, text='Nome', bg=background_color, fg=text_color, font=text_style)
name_text.grid(row=3, column=0, pady=text_padding_y)
name_entry = tk.Entry(login_frame, font=text_style, bg=entry_background)
name_entry.grid(row=3, column=1, pady=text_padding_y, sticky='news')

email_text = tk.Label(login_frame, text='Email', bg=background_color, fg=text_color, font=text_style)
email_text.grid(row=4, column=0, pady=text_padding_y, sticky='news')
email_entry = tk.Entry(login_frame, font=text_style, bg=entry_background)
email_entry.grid(row=4, column=1, pady=text_padding_y, sticky='news')

salvar = tk.Button(login_frame, command=login_user, bg=button_background, fg=button_text_color, text='Salvar e iniciar', font=text_style)
salvar.grid(row=5, column=0, columnspan=2, pady=button_padding_y)

login.mainloop()

#Q0
q0 = tk.Tk()
q0.title('QAI')
q0.attributes('-fullscreen',True)
q0.configure(bg=background_color)
banner_file = tk.PhotoImage(file=r'static\lab_banner.png', master=q0)
banner = tk.Label(q0, image=banner_file, bg=background_color)
banner.pack()

top_frame = tk.Frame(bg=background_color)
top_frame.pack(pady=frame_paddding_y)

q0_image_file = tk.PhotoImage(file=r'static\Q0.png', master=top_frame)
q0_image = tk.Label(top_frame, image=q0_image_file, bg=background_color)
q0_image.pack(side='right')

q0_title = tk.Label(top_frame, bg=background_color, fg=text_color, font=title_style, text='Pesquisa de Clima\nOrganizacional')
q0_title.pack(side='left', padx=text_padding_x)

middle1_frame = tk.Frame(bg=background_color)
middle1_frame.pack(pady=frame_paddding_y)

q0_subtitle = tk.Label(middle1_frame, bg=background_color, fg=text_color, font=subtitle_style, text='Como você classifica a sua satisfação com as condições\nfísicas (temperatura, qualidade do ar interno, iluminação e\nacústica) do seu ambiente de trabalho para a realização das\nsuas atividades?')
q0_subtitle.pack(padx=text_padding_x, pady=text_padding_y)

middle2_frame = tk.Frame(bg=background_color)
middle2_frame.pack(pady=frame_paddding_y)

q0_text = tk.Label(middle2_frame, bg=background_color, fg=text_color, font=text_style, text='Em uma escala de 0 a 10:')
q0_text.grid(row=0, column=0, pady=text_padding_y, padx=text_padding_x)

q0_radio_var = tk.IntVar()
q0_radio_0 = tk.Radiobutton(middle2_frame, variable=q0_radio_var, text='0', value='0', bg=radio_background , fg=text_color)
q0_radio_1 = tk.Radiobutton(middle2_frame, variable=q0_radio_var, text='1', value='1', bg=radio_background, fg=text_color)
q0_radio_2 = tk.Radiobutton(middle2_frame, variable=q0_radio_var, text='2', value='2', bg=radio_background, fg=text_color)
q0_radio_3 = tk.Radiobutton(middle2_frame, variable=q0_radio_var, text='3', value='3', bg=radio_background, fg=text_color)
q0_radio_4 = tk.Radiobutton(middle2_frame, variable=q0_radio_var, text='4', value='4', bg=radio_background, fg=text_color)
q0_radio_5 = tk.Radiobutton(middle2_frame, variable=q0_radio_var, text='5', value='5', bg=radio_background, fg=text_color)
q0_radio_6 = tk.Radiobutton(middle2_frame, variable=q0_radio_var, text='6', value='6', bg=radio_background, fg=text_color)
q0_radio_7 = tk.Radiobutton(middle2_frame, variable=q0_radio_var, text='7', value='7', bg=radio_background, fg=text_color)
q0_radio_8 = tk.Radiobutton(middle2_frame, variable=q0_radio_var, text='8', value='8', bg=radio_background, fg=text_color)
q0_radio_9 = tk.Radiobutton(middle2_frame, variable=q0_radio_var, text='9', value='9', bg=radio_background, fg=text_color)
q0_radio_10 = tk.Radiobutton(middle2_frame, variable=q0_radio_var, text='10', value='10', bg=radio_background, fg=text_color)

q0_radio_0.grid(row=0, column=1)
q0_radio_1.grid(row=0, column=2)
q0_radio_2.grid(row=0, column=3)
q0_radio_3.grid(row=0, column=4)
q0_radio_4.grid(row=0, column=5)
q0_radio_5.grid(row=0, column=6)
q0_radio_6.grid(row=0, column=7)
q0_radio_7.grid(row=0, column=8)
q0_radio_8.grid(row=0, column=9)
q0_radio_9.grid(row=0, column=10)
q0_radio_10.grid(row=0, column=11)

next_button = tk.Button(q0, command=save_q0, bg=button_background, fg=button_text_color, font=text_style, text='Próximo')
next_button.pack(side='right', pady=button_padding_y, padx=text_padding_x)

q0.mainloop()

#introQ1
introq1 = tk.Tk()
introq1.title('QAI')
introq1.attributes('-fullscreen',True)
introq1.configure(bg=background_color)
banner_file = tk.PhotoImage(file=r'static\lab_banner.png', master=introq1)
banner = tk.Label(introq1, image=banner_file, bg=background_color)
banner.pack()

top_frame = tk.Frame(bg=background_color)
top_frame.pack(pady=frame_paddding_y)
top_frame_r = tk.Frame(top_frame, bg=background_color)
top_frame_r.pack(side='right')
top_frame_l = tk.Frame(top_frame, bg=background_color)
top_frame_l.pack(side='left')
down_frame = tk.Frame(bg=background_color)
down_frame.pack(pady=title_padding_y)
down_button = tk.Button(down_frame, text='Combinado', bg=button_background, fg=button_text_color, font=text_style, command=introq1.destroy)
down_button.grid(row=0, column=1, padx=text_padding_x)

if q0_resposta['r'] == True:
    title = tk.Label(top_frame_l, text=f'{q0_resposta["value"]}? Essa nota foi baixa :(', font=title_style, bg=background_color, fg=text_color)
    title.grid(row=0, pady=title_padding_y)
    subtitle = tk.Label(top_frame_l, text='Parece que você não está muito\ncontente com a estrutura do\nseu ambiente de trabalho...', bg=background_color, font=subtitle_style, fg=text_color)
    subtitle.grid(row=1, pady=title_padding_y)
    description = tk.Label(top_frame_l, text='Para conseguirmos encontrar uma solução,\nprecisamos descobrir o que está causando\ndesconforto. Assim será possível propor\nsoluções para tornar o seu ambiente de\ntrabalho mais adequado para a\nrealização das suas atividades.', bg=background_color, fg=text_color, font=text_style)
    description.grid(row=2, pady=text_padding_y)
    instaImageFile = tk.PhotoImage(file=r'static\Q1insat.png', master=top_frame_r)
    instaImage = tk.Label(top_frame_r, image=instaImageFile, bg=background_color)
    instaImage.pack()
    down_label = tk.Label(down_frame, text='Você pode nos ajudar a descobrir qual\né o problema respondendo as questões a seguir.', font=subtitle_style, bg=background_color, fg=text_color)
    down_label.grid(row=0, column=0, padx=text_padding_x)
else:
    title = tk.Label(top_frame_l, text=f'{q0_resposta["value"]} é uma ótima avaliação!', font=title_style, bg=background_color, fg=text_color)
    title.grid(row=0, pady=title_padding_y)
    subtitle = tk.Label(top_frame_l, text='Aparentemente, não há problemas\ncom a estrutura do seu ambiente\nde trabalho :)', bg=background_color, font=subtitle_style, fg=text_color)
    subtitle.grid(row=1, pady=title_padding_y)
    instaImageFile = tk.PhotoImage(file=r'static\Q1sat.png', master=top_frame_r)
    instaImage = tk.Label(top_frame_r, image=instaImageFile, bg=background_color)
    instaImage.pack()
    down_label = tk.Label(down_frame, text='Vamos apenas fazer algumas perguntas\npara ter certeza que está tudo bem,\nok?', font=subtitle_style, bg=background_color, fg=text_color)
    down_label.grid(row=0, column=0, padx=text_padding_x) 

introq1.mainloop() 

#Q1a
q1a = tk.Tk()
q1a.title('QAI')
q1a.attributes('-fullscreen',True)
q1a.configure(bg=background_color)
banner_file = tk.PhotoImage(file=r'static\lab_banner.png', master=q1a)
banner = tk.Label(q1a, image=banner_file, bg=background_color)
banner.pack()

top_frame = tk.Frame(bg=background_color)
top_frame.pack()

elements_frame = tk.Frame(bg=background_color)
elements_frame.pack()

down_frame = tk.Frame(bg=background_color)
down_frame.pack(fill='x', pady=title_padding_y )
down_button = tk.Button(down_frame, text='Próximo', bg=button_background, fg=button_text_color, font=text_style, command=save_q1a)
down_button.pack(side='right', padx=text_padding_x)

title = tk.Label(top_frame, text='O seu ambiente de trabalho', font=title_style, bg=background_color, fg=text_color)
title.pack(padx=text_padding_x, pady=title_padding_y)

subtitle = tk.Label(top_frame, text='Por favor selecione o tipo de layout do escritório que\nrepresenta o seu ambiente de trabalho.', font=subtitle_style, bg=background_color, fg=text_color)
subtitle.pack( padx=text_padding_x, pady=text_padding_y)

opt_var = tk.StringVar()

privada = tk.Label(elements_frame, text='sala privada:', font=subtitle_style, bg=background_color, fg=text_color)
privada.grid(row=1, column=0, padx=text_padding_x)

indiv_image_file = tk.PhotoImage(file=r'static\placeholder.png', master=elements_frame)
indiv_image = tk.Label(elements_frame, image=indiv_image_file, bg=background_color)
indiv_image.grid(row=0, column=1, padx=text_padding_x, pady=text_padding_y)

individual_radio = tk.Radiobutton(elements_frame, text='individual', variable=opt_var, value='individual', font=text_style, bg=background_color, fg=text_color)
individual_radio.grid(row=1, column=1)

compartilhada_image_file = tk.PhotoImage(file=r'static\placeholder.png', master=elements_frame)
compartilhada_image = tk.Label(elements_frame, image=compartilhada_image_file, bg=background_color)
compartilhada_image.grid(row=0, column=2, padx=text_padding_x, pady=text_padding_y)

compartilhada_radio = tk.Radiobutton(elements_frame, font=text_style,bg=background_color, fg=text_color, text='compartilhada com um\nou mais colegas', variable=opt_var, value='compartilhada com um ou mais colegas')
compartilhada_radio.grid(row=1, column=2)

planta_aberta = tk.Label(elements_frame, text='planta aberta:', font=subtitle_style, bg=background_color, fg=text_color)
planta_aberta.grid(row=3, column=0, padx=text_padding_x)

sem_divisoria_image_file = tk.PhotoImage(master=elements_frame, file=r'static\placeholder.png')
sem_divisoria_image = tk.Label(elements_frame, image=sem_divisoria_image_file, bg=background_color)
sem_divisoria_image.grid(row=2, column=1, padx=text_padding_x, pady=text_padding_y)

sem_divisoria = tk.Radiobutton(elements_frame, text='sem divisórias', font=text_style, bg=background_color, fg=text_color, variable=opt_var, value='sem divisórias')
sem_divisoria.grid(row=3, column=1, padx=text_padding_x)

com_divisorias_baixas_image_file = tk.PhotoImage(master=elements_frame, file=r'static\placeholder.png')
com_divisorias_baixas_image = tk.Label(elements_frame, image=com_divisorias_baixas_image_file, bg=background_color)
com_divisorias_baixas_image.grid(row=2, column=2, padx=text_padding_x, pady=text_padding_y)

com_divisorias_baixas = tk.Radiobutton(elements_frame, text='com divisórias baixas: consigo\nvisualizar meus colegas\ne entorno mesmo estando\nsentado(a)', font=text_style, bg=background_color, fg=text_color, variable=opt_var, value='com divisórias baixas: consigo visualizar meus colegas e entorno mesmo estando sentado(a)')
com_divisorias_baixas.grid(row=3, column=2, padx=text_padding_x)

com_divisorias_altas_image_file = tk.PhotoImage(master=elements_frame, file=r'static\placeholder.png')
com_divisorias_altas_image = tk.Label(elements_frame, image=com_divisorias_altas_image_file, bg=background_color)
com_divisorias_altas_image.grid(row=2, column=3, padx=text_padding_x, pady=text_padding_y)

com_divisorias_altas = tk.Radiobutton(elements_frame, text='com divisórias altas: preciso me\nlevantar para visualizar meus\n colegas e entorno', font=text_style, bg=background_color, fg=text_color, variable=opt_var, value='com divisórias altas: preciso me levantar para visualizar meus colegas e entorno')
com_divisorias_altas.grid(row=3, column=3, padx=text_padding_x)

sem_localizacao_fixa = tk.Label(elements_frame, text='sem localização fixa:', font=subtitle_style, bg=background_color, fg=text_color)
sem_localizacao_fixa.grid(row=5, column=0, padx=text_padding_x)

sem_localizacao_fixa_image_file = tk.PhotoImage(file=r'static\placeholder.png', master=elements_frame)
sem_localizacao_fixa_image = tk.Label(elements_frame, image=sem_localizacao_fixa_image_file, bg=background_color)
sem_localizacao_fixa_image.grid(row=4, column=1, padx=text_padding_x, pady=text_padding_y)

sem_localizacao_fixa_radio = tk.Radiobutton(elements_frame, text='eu não tenho uma mesa designada\npara mim, posso escolher\ndiariamente a minha estação\nde trabalho', variable=opt_var, value='eu não tenho uma mesa designada para mim, posso escolher diariamente a minha estação de trabalho', font=text_style, bg=background_color, fg=text_color)
sem_localizacao_fixa_radio.grid(row=5, column=1)

q1a.mainloop()

#Q1b
q1b = tk.Tk()
q1b.title('QAI')
q1b.attributes('-fullscreen',True)
q1b.configure(bg=background_color)
banner_file = tk.PhotoImage(file=r'static\lab_banner.png', master=q1b)
banner = tk.Label(q1b, image=banner_file, bg=background_color)
banner.pack()

top_frame = tk.Frame(bg=background_color)
top_frame.pack()

elements_frame = tk.Frame(bg=background_color)
elements_frame.pack()

down_frame = tk.Frame(bg=background_color)
down_frame.pack(fill='x', pady=title_padding_y )
down_button = tk.Button(down_frame, text='Próximo', bg=button_background, fg=button_text_color, font=text_style, command=save_q1b)
down_button.pack(side='right', padx=text_padding_x)

title = tk.Label(top_frame, text='Proximidade a janelas', font=title_style, bg=background_color, fg=text_color)
title.pack(padx=text_padding_x, pady=title_padding_y)

subtitle = tk.Label(top_frame, text='Existem janelas e/ou outras áreas envidraçadas no\nseu ambiente de trabalho?', font=subtitle_style, bg=background_color, fg=text_color)
subtitle.pack( padx=text_padding_x, pady=title_padding_y)

opt_var = tk.StringVar()

sim_ver_exterior_image_file = tk.PhotoImage(master=elements_frame, file=r'static\placeholder.png')
sim_ver_exterior_image = tk.Label(master=elements_frame, image=sim_ver_exterior_image_file, bg=background_color)
sim_ver_exterior_image.grid(row=0, column=0, padx=text_padding_x, pady=text_padding_y)

sim_ver_exterior_radio = tk.Radiobutton(elements_frame, variable=opt_var, value='sim, consigo ver o exterior mesmo quando estou sentado(a) em minha estação de trabalho', text='sim, consigo ver o exterior mesmo\nquando estou sentado(a) em\nminha estação de trabalho', bg=background_color, fg=text_color, font=text_style)
sim_ver_exterior_radio.grid(row=1, column=0, padx=text_padding_x)

sim_nao_ver_exterior_image_file = tk.PhotoImage(master=elements_frame, file=r'static\placeholder.png')
sim_nao_ver_exterior_image = tk.Label(master=elements_frame, image=sim_nao_ver_exterior_image_file, bg=background_color)
sim_nao_ver_exterior_image.grid(row=0, column=1, padx=text_padding_x, pady=text_padding_y)

sim_nao_ver_exterior_radio = tk.Radiobutton(elements_frame, variable=opt_var, value='sim, porém estão muito afastadas da minha estação de trabalho', text='sim, porém estão muito afastadas\nda minha estação de trabalho', bg=background_color, fg=text_color, font=text_style)
sim_nao_ver_exterior_radio.grid(row=1, column=1, padx=text_padding_x)

nao_ver_exterior_image_file = tk.PhotoImage(master=elements_frame, file=r'static\placeholder.png')
nao_ver_exterior_image = tk.Label(master=elements_frame, image=nao_ver_exterior_image_file, bg=background_color)
nao_ver_exterior_image.grid(row=0, column=2, padx=text_padding_x, pady=text_padding_y)

nao_ver_exterior_radio = tk.Radiobutton(elements_frame, variable=opt_var, value='não existem janelas ou outras áreas envidraçadas no meu ambiente de trabalho', text='não existem janelas ou outras áreas\nenvidraçadas no meu ambiente de trabalho', bg=background_color, fg=text_color, font=text_style)
nao_ver_exterior_radio.grid(row=1, column=2, padx=text_padding_x)

q1b.mainloop() 

#Q1c
q1c = tk.Tk()
q1c.title('QAI')
q1c.attributes('-fullscreen',True)
q1c.configure(bg=background_color)
banner_file = tk.PhotoImage(file=r'static\lab_banner.png', master=q1c)
banner = tk.Label(q1c, image=banner_file, bg=background_color)
banner.pack()

top_frame = tk.Frame(bg=background_color)
top_frame.pack()

elements_frame = tk.Frame(bg=background_color)
elements_frame.pack(pady=frame_paddding_y)

down_frame = tk.Frame(bg=background_color)
down_frame.pack(fill='x', pady=title_padding_y )
down_button = tk.Button(down_frame, text='Próximo', bg=button_background, fg=button_text_color, font=text_style, command=save_q1c)
down_button.pack(side='right', padx=text_padding_x)

title = tk.Label(top_frame, text='Onde você passa mais tempo?', font=title_style, bg=background_color, fg=text_color)
title.pack(padx=text_padding_x, pady=title_padding_y)

subtitle = tk.Label(top_frame, text='Em um dia típico de trabalho, com que frequência você\nestima que utilize...', font=subtitle_style, bg=background_color, fg=text_color)
subtitle.pack( padx=text_padding_x, pady=title_padding_y)

sempre = tk.Label(elements_frame, font=subtitle_style, bg=background_color, fg=text_color, text='sempre')
sempre.grid(row=0, column=1, padx=text_padding_x, pady=text_padding_y)
muitasvezes = tk.Label(elements_frame, font=subtitle_style, bg=background_color, fg=text_color, text='muitas\nvezes')
muitasvezes.grid(row=0, column=2, padx=text_padding_x, pady=text_padding_y)
asvezes = tk.Label(elements_frame, font=subtitle_style, bg=background_color, fg=text_color, text='às vezes')
asvezes.grid(row=0, column=3, padx=text_padding_x, pady=text_padding_y)
poucasvezes = tk.Label(elements_frame, font=subtitle_style, bg=background_color, fg=text_color, text='poucas\nvezes')
poucasvezes.grid(row=0, column=4, padx=text_padding_x, pady=text_padding_y)
nunca = tk.Label(elements_frame, font=subtitle_style, bg=background_color, fg=text_color, text='nunca')
nunca.grid(row=0, column=5, padx=text_padding_x, pady=text_padding_y)
naopossui = tk.Label(elements_frame, font=subtitle_style, bg=background_color, fg=text_color, text='não\npossui')
naopossui.grid(row=0, column=6, padx=text_padding_x, pady=text_padding_y)

q1c1 = tk.Label(elements_frame, bg=background_color, fg=text_color, font=text_style, text='Sua estação de trabalho?')
q1c1.grid(row=1, column=0, pady=text_padding_y, padx=text_padding_x)
q1c1_var = tk.StringVar()
q1c1_radio_0 = tk.Radiobutton(elements_frame, variable=q1c1_var, value='sempre', bg=background_color , fg=text_color)
q1c1_radio_1 = tk.Radiobutton(elements_frame, variable=q1c1_var, value='muitas vezes', bg=background_color, fg=text_color)
q1c1_radio_2 = tk.Radiobutton(elements_frame, variable=q1c1_var, value='às vezes', bg=background_color, fg=text_color)
q1c1_radio_3 = tk.Radiobutton(elements_frame, variable=q1c1_var, value='poucas vezes', bg=background_color, fg=text_color)
q1c1_radio_4 = tk.Radiobutton(elements_frame, variable=q1c1_var, value='nunca', bg=background_color, fg=text_color)
q1c1_radio_5 = tk.Radiobutton(elements_frame, variable=q1c1_var, value='não possui', bg=background_color, fg=text_color)
q1c1_radio_0.grid(row=1, column=1)
q1c1_radio_1.grid(row=1, column=2)
q1c1_radio_2.grid(row=1, column=3)
q1c1_radio_3.grid(row=1, column=4)
q1c1_radio_4.grid(row=1, column=5)
q1c1_radio_5.grid(row=1, column=6)

q1c2 = tk.Label(elements_frame, bg=background_color, fg=text_color, font=text_style, text='Estações de trabalho rotativas e/ou não-fixas?')
q1c2.grid(row=2, column=0, pady=text_padding_y, padx=text_padding_x)
q1c2_var = tk.StringVar()
q1c2_radio_0 = tk.Radiobutton(elements_frame, variable=q1c2_var, value='sempre', bg=background_color , fg=text_color)
q1c2_radio_1 = tk.Radiobutton(elements_frame, variable=q1c2_var, value='muitas vezes', bg=background_color, fg=text_color)
q1c2_radio_2 = tk.Radiobutton(elements_frame, variable=q1c2_var, value='às vezes', bg=background_color, fg=text_color)
q1c2_radio_3 = tk.Radiobutton(elements_frame, variable=q1c2_var, value='poucas vezes', bg=background_color, fg=text_color)
q1c2_radio_4 = tk.Radiobutton(elements_frame, variable=q1c2_var, value='nunca', bg=background_color, fg=text_color)
q1c2_radio_5 = tk.Radiobutton(elements_frame, variable=q1c2_var, value='não possui', bg=background_color, fg=text_color)
q1c2_radio_0.grid(row=2, column=1)
q1c2_radio_1.grid(row=2, column=2)
q1c2_radio_2.grid(row=2, column=3)
q1c2_radio_3.grid(row=2, column=4)
q1c2_radio_4.grid(row=2, column=5)
q1c2_radio_5.grid(row=2, column=6)

q1c3 = tk.Label(elements_frame, bg=background_color, fg=text_color, font=text_style, text='Áreas específicas para desenvolver atividades em grupo e/ou dinâmicas?')
q1c3.grid(row=3, column=0, pady=text_padding_y, padx=text_padding_x)
q1c3_var = tk.StringVar()
q1c3_radio_0 = tk.Radiobutton(elements_frame, variable=q1c3_var, value='sempre', bg=background_color , fg=text_color)
q1c3_radio_1 = tk.Radiobutton(elements_frame, variable=q1c3_var, value='muitas vezes', bg=background_color, fg=text_color)
q1c3_radio_2 = tk.Radiobutton(elements_frame, variable=q1c3_var, value='às vezes', bg=background_color, fg=text_color)
q1c3_radio_3 = tk.Radiobutton(elements_frame, variable=q1c3_var, value='poucas vezes', bg=background_color, fg=text_color)
q1c3_radio_4 = tk.Radiobutton(elements_frame, variable=q1c3_var, value='nunca', bg=background_color, fg=text_color)
q1c3_radio_5 = tk.Radiobutton(elements_frame, variable=q1c3_var, value='não possui', bg=background_color, fg=text_color)
q1c3_radio_0.grid(row=3, column=1)
q1c3_radio_1.grid(row=3, column=2)
q1c3_radio_2.grid(row=3, column=3)
q1c3_radio_3.grid(row=3, column=4)
q1c3_radio_4.grid(row=3, column=5)
q1c3_radio_5.grid(row=3, column=6)

q1c4 = tk.Label(elements_frame, bg=background_color, fg=text_color, font=text_style, text='Áreas específicas para desenvolver atividades individuais e/ou focadas?')
q1c4.grid(row=4, column=0, pady=text_padding_y, padx=text_padding_x)
q1c4_var = tk.StringVar()
q1c4_radio_0 = tk.Radiobutton(elements_frame, variable=q1c4_var, value='sempre', bg=background_color , fg=text_color)
q1c4_radio_1 = tk.Radiobutton(elements_frame, variable=q1c4_var, value='muitas vezes', bg=background_color, fg=text_color)
q1c4_radio_2 = tk.Radiobutton(elements_frame, variable=q1c4_var, value='às vezes', bg=background_color, fg=text_color)
q1c4_radio_3 = tk.Radiobutton(elements_frame, variable=q1c4_var, value='poucas vezes', bg=background_color, fg=text_color)
q1c4_radio_4 = tk.Radiobutton(elements_frame, variable=q1c4_var, value='nunca', bg=background_color, fg=text_color)
q1c4_radio_5 = tk.Radiobutton(elements_frame, variable=q1c4_var, value='não possui', bg=background_color, fg=text_color)
q1c4_radio_0.grid(row=4, column=1)
q1c4_radio_1.grid(row=4, column=2)
q1c4_radio_2.grid(row=4, column=3)
q1c4_radio_3.grid(row=4, column=4)
q1c4_radio_4.grid(row=4, column=5)
q1c4_radio_5.grid(row=4, column=6)

q1c5 = tk.Label(elements_frame, bg=background_color, fg=text_color, font=text_style, text='Salas de conferência e/ou reunião?')
q1c5.grid(row=5, column=0, pady=text_padding_y, padx=text_padding_x)
q1c5_var = tk.StringVar()
q1c5_radio_0 = tk.Radiobutton(elements_frame, variable=q1c5_var, value='sempre', bg=background_color , fg=text_color)
q1c5_radio_1 = tk.Radiobutton(elements_frame, variable=q1c5_var, value='muitas vezes', bg=background_color, fg=text_color)
q1c5_radio_2 = tk.Radiobutton(elements_frame, variable=q1c5_var, value='às vezes', bg=background_color, fg=text_color)
q1c5_radio_3 = tk.Radiobutton(elements_frame, variable=q1c5_var, value='poucas vezes', bg=background_color, fg=text_color)
q1c5_radio_4 = tk.Radiobutton(elements_frame, variable=q1c5_var, value='nunca', bg=background_color, fg=text_color)
q1c5_radio_5 = tk.Radiobutton(elements_frame, variable=q1c5_var, value='não possui', bg=background_color, fg=text_color)
q1c5_radio_0.grid(row=5, column=1)
q1c5_radio_1.grid(row=5, column=2)
q1c5_radio_2.grid(row=5, column=3)
q1c5_radio_3.grid(row=5, column=4)
q1c5_radio_4.grid(row=5, column=5)
q1c5_radio_5.grid(row=5, column=6)

q1c6 = tk.Label(elements_frame, bg=background_color, fg=text_color, font=text_style, text='Fica fora do escritório, em atividades externas?')
q1c6.grid(row=5, column=0, pady=text_padding_y, padx=text_padding_x)
q1c6_var = tk.StringVar()
q1c6_radio_0 = tk.Radiobutton(elements_frame, variable=q1c6_var, value='sempre', bg=background_color , fg=text_color)
q1c6_radio_1 = tk.Radiobutton(elements_frame, variable=q1c6_var, value='muitas vezes', bg=background_color, fg=text_color)
q1c6_radio_2 = tk.Radiobutton(elements_frame, variable=q1c6_var, value='às vezes', bg=background_color, fg=text_color)
q1c6_radio_3 = tk.Radiobutton(elements_frame, variable=q1c6_var, value='poucas vezes', bg=background_color, fg=text_color)
q1c6_radio_4 = tk.Radiobutton(elements_frame, variable=q1c6_var, value='nunca', bg=background_color, fg=text_color)
q1c6_radio_5 = tk.Radiobutton(elements_frame, variable=q1c6_var, value='não possui', bg=background_color, fg=text_color)
q1c6_radio_0.grid(row=5, column=1)
q1c6_radio_1.grid(row=5, column=2)
q1c6_radio_2.grid(row=5, column=3)
q1c6_radio_3.grid(row=5, column=4)
q1c6_radio_4.grid(row=5, column=5)
q1c6_radio_5.grid(row=5, column=6)

q1c.mainloop()

#End
quiz.save_PeR()


print(user)
print(quiz.json_to_send)