import tkinter as tk
from tkinter import messagebox

#Variables
window_size = '900x1000'
title_style = ('Inter', 27)
text_style = ('Inter', 12)
subtitle_style = ('Inter', 16)
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
    quiz.pergunta.append('Q0')
    quiz.resposta.append(resposta)
    q0.destroy()


#Aplicação
quiz = PeR()
user = {'name': None, 'email': None}
has_windows = False
has_climatizacao = False
has_ventilacao = False
execute = True
while execute:
    #Login
    login = tk.Tk()
    login.title('QAI - Login')
    login.geometry(window_size)
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

    salvar = tk.Button(login_frame, command=login_user, bg=button_background, fg=text_color, text='Salvar e iniciar', font=text_style)
    salvar.grid(row=5, column=0, columnspan=2, pady=button_padding_y)

    login.mainloop()

    #Q0
    q0 = tk.Tk()
    q0.title('QAI')
    q0.geometry(window_size)
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

    next_button = tk.Button(q0, command=save_q0, bg=button_background, fg=text_color, font=text_style, text='Próximo')
    next_button.pack(side='right', pady=button_padding_y, padx=text_padding_x)

    q0.mainloop()

    #Q1

    #End
    execute = False
    quiz.save_PeR()


print(user)
print(quiz.resposta)
print(quiz.pergunta)
print(quiz.json_to_send)