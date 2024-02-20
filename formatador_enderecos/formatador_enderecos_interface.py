from tkinter import *
from tkinter import Tk, StringVar, ttk
from formatador_enderecos_funcao import address_formater, list_of_addresses

def on_button_click():
    selected_address = combobox.get()
    formatted_address = address_formater(selected_address)
    result_text.config(state='normal')
    result_text.delete("1.0", END)  # Limpa o conteúdo anterioraa
    result_text.insert(END, formatted_address)
    result_text.config(state='disabled')

# Criação da interface gráfica
window = Tk()
window.title("Formatador de Endereço")
window.geometry("400x300")

# Combobox para selecionar um item da lista
combobox = ttk.Combobox(window, values=list_of_addresses, width=40)
combobox.place(x=50, y=20)

# Botão para acionar a formatação e exibição
button = Button(window, text="Formatar Endereço", command=on_button_click)
button.place(x=50, y=60)

# Textbox para exibir o resultado
result_text = Text(window, width=40, height=10, state='disabled')
result_text.place(x=50, y=100)

# Inicia o loop principal
window.mainloop()