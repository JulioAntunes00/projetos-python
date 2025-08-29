import tkinter as tk

janela = tk.Tk()

janela.title("Calculadora simples")
janela.geometry("300x400")
janela.resizable(False, False) #impede de alterar tamanho da janela

def adicionar_ao_display(caractere):
    display.insert(tk.END, caractere)


def calcular_resultado():
    try:
        expressao = display.get("1.0", tk.END)
        resultado = eval(expressao)
        limpar_display()
        display.insert(tk.END, str(resultado))
    except Exception as e:
        limpar_display()
        display.insert(tk.END, "Erro")


def limpar_display():
    display.delete("1.0", tk.END)




display = tk.Text(janela, height=2, width=20, font=("Arial", 24))
display.pack(pady=10)
frame_botoes = tk.Frame(janela)
frame_botoes.pack()
botoes = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

linha = 0
coluna = 0

for texto_botao in botoes:
    if texto_botao == '=':
        botao = tk.Button(frame_botoes, text=texto_botao, width=5, height=2, command=calcular_resultado)
    else:
        botao= tk.Button(frame_botoes, text=texto_botao, width=5, height=2, command=lambda t=texto_botao: adicionar_ao_display(t))
    
    botao.grid(row=linha, column=coluna, padx=5, pady=5)
    coluna += 1
    if coluna > 3:
        coluna = 0
        linha += 1


botao_limpar = tk.Button(janela, text="C", width=26, height=2, command=limpar_display)
botao_limpar.pack(pady=10)

janela.mainloop()