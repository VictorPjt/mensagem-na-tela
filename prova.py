import tkinter as tk
from tkinter import messagebox

# Função para exibir a mensagem em uma nova janela
def mostrar_mensagem():
    nome = nome_entry.get()
    mensagem = mensagem_entry.get()
    
    if nome and mensagem:
        # Criar uma nova janela para exibir a mensagem
        mensagem_window = tk.Toplevel(root)
        mensagem_window.title("Mensagem Enviada")
        mensagem_window.geometry("300x150")  # Definir as dimensões da janela
        
        # Criar rótulos para exibir o nome e a mensagem
        nome_label = tk.Label(mensagem_window, text=f"Nome: {nome}", font=("Helvetica", 14))
        mensagem_label = tk.Label(mensagem_window, text=f"Mensagem: {mensagem}", font=("Helvetica", 12))
        
        nome_label.pack(pady=10)
        mensagem_label.pack(pady=10)
    else:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")

# Criar a janela principal
root = tk.Tk()
root.title("João victor")

# Definir as dimensões da janela principal
root.geometry("400x300")

# Rótulo e entrada para o nome
nome_label = tk.Label(root, text="Nome:", font=("Helvetica", 14))
nome_label.pack(pady=10)
nome_entry = tk.Entry(root, font=("Helvetica", 12))
nome_entry.pack()

# Rótulo e entrada para a mensagem
mensagem_label = tk.Label(root, text="Mensagem:", font=("Helvetica", 14))
mensagem_label.pack(pady=10)
mensagem_entry = tk.Entry(root, font=("Helvetica", 12))
mensagem_entry.pack()

# Botão para enviar a mensagem
enviar_button = tk.Button(root, text="Enviar", command=mostrar_mensagem, font=("Helvetica", 14))
enviar_button.pack(pady=20)



# Iniciar a GUI
root.mainloop()