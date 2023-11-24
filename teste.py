import tkinter as tk
from tkinter import messagebox

class Cliente:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

def salvar_cliente():
    nome = entry_nome.get()
    email = entry_email.get()
    telefone = entry_telefone.get()

    if nome and email and telefone:
        cliente = Cliente(nome, email, telefone)
        lista_clientes.append(cliente)
        messagebox.showinfo("Sucesso", "Cliente salvo com sucesso!")
        limpar_campos()
        exibir_clientes()
    else:
        messagebox.showwarning("Erro", "Por favor, preencha todos os campos.")

def exibir_clientes():
    text.delete("1.0", tk.END)
    for i, cliente in enumerate(lista_clientes, start=1):
        info_cliente = f"{i}. Nome: {cliente.nome}\n   Email: {cliente.email}\n   Telefone: {cliente.telefone}\n"
        text.insert(tk.END, info_cliente)

def excluir_cliente():
    cliente_selecionado = text.tag_ranges(tk.SEL)
    if cliente_selecionado:
        indice_inicial = cliente_selecionado[0].split(".")[0]
        indice_cliente = int(indice_inicial) - 1
        del lista_clientes[indice_cliente]
        exibir_clientes()

def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)

# Inicialização da interface
lista_clientes = []

root = tk.Tk()
root.title("Cadastro de Clientes")

# Widgets
label_nome = tk.Label(root, text="Nome:")
label_nome.grid(row=0, column=0, padx=10, pady=10, sticky=tk.E)
entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1, padx=10, pady=10)

label_email = tk.Label(root, text="Email:")
label_email.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)
entry_email = tk.Entry(root)
entry_email.grid(row=1, column=1, padx=10, pady=10)

label_telefone = tk.Label(root, text="Telefone:")
label_telefone.grid(row=2, column=0, padx=10, pady=10, sticky=tk.E)
entry_telefone = tk.Entry(root)
entry_telefone.grid(row=2, column=1, padx=10, pady=10)

btn_salvar = tk.Button(root, text="Salvar", command=salvar_cliente)
btn_salvar.grid(row=3, column=0, columnspan=2, pady=10)

text = tk.Text(root, height=10, width=50)
text.grid(row=4, column=0, columnspan=2, pady=10)

btn_excluir = tk.Button(root, text="Excluir Selecionado", command=excluir_cliente)
btn_excluir.grid(row=5, column=0, columnspan=2, pady=10)

# Loop principal
root.mainloop()
