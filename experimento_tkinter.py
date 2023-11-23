import tkinter as tk

def save_entrada():
    radio_valor = radiovalue.get()
    mensagem = mens.get()
    print(f'\n\n{">"*40}\nMensagem: {mensagem}\nCor escolhida: {radio_valor}\n{">"*40}\n\n')

window = tk.Tk()
window.title('Testando Tkinter')
window.geometry('330x200')

label1 = tk.Label(window, text='TESTE TESTE')

label2 = tk.Label(window, text='Deixe uma mensagem :D')
mens = tk.Entry(window)

label3 = tk.Label(window, text='Qual dessas cores você mais gosta?')
radiovalue = tk.StringVar(value='Nenhuma')
radio1 = tk.Radiobutton(window, variable=radiovalue, value='Preto', text='Preto')
radio2 = tk.Radiobutton(window, variable=radiovalue, value='Branco', text='Branco')
radio3 = tk.Radiobutton(window, variable=radiovalue, value='Azul', text='Azul')
radio4 = tk.Radiobutton(window, variable=radiovalue, value='Verde', text='Verde')
radio5 = tk.Radiobutton(window, variable=radiovalue, value='Vermelho', text='Vermelho')
radio6 = tk.Radiobutton(window, variable=radiovalue, value='Amarelo', text='Amarelo')
radio7 = tk.Radiobutton(window, variable=radiovalue, value='Rosa', text='Rosa')
radio8 = tk.Radiobutton(window, variable=radiovalue, value='Marrom', text='Marrom')
radio9 = tk.Radiobutton(window, variable=radiovalue, value='Roxo', text='Roxo')

botao = tk.Button(window, text='Aperte para salvar entradas', command=save_entrada)


label1.grid(row=0, column=1)
label2.grid(row=1, column=1)
mens.grid(row=2, column=1)
label3.grid(row=3, column=1)

radio1.grid(row=4, column=0) 
radio2.grid(row=4, column=1) 
radio3.grid(row=4, column=2) 
radio4.grid(row=5, column=0) 
radio5.grid(row=5, column=1) 
radio6.grid(row=5, column=2) 
radio7.grid(row=6, column=0) 
radio8.grid(row=6, column=1) 
radio9.grid(row=6, column=2)

botao.grid(row=7, column=1)

window.mainloop()
