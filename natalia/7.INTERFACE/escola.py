import os, customtkinter as ctk
ctk.set_appearance_mode('dark')

os.system('cls')


def calcular():
    n1 = float(nota1.get())
    n2 = float(nota2.get())
    n3 = float(nota3.get())

    media = (n1+n2+n3)/3

    if media >= 5:
        situacao = 'APROVADO!'
    else:
        situacao = 'REPROVADO.'
        
    
    resultado.configure(text=f'Sua média é: {media:.1f}\nVocê foi {situacao}')

janela = ctk.CTk()

janela.geometry('600x450')
janela.resizable(False,False)
janela.title('SISTEMA SENAI - 30/09/2026')

#CORPO
titulo = ctk.CTkLabel(janela,
                text='Sistema Escolar',
                text_color='yellow',
                font=('arial',40))
titulo.pack(pady=10)


#nota1
nota1 = ctk.CTkEntry(janela,
                    width=350,
                    height=40,
                    border_color='yellow',
                    placeholder_text='Digite a sua nota na 1ª Unidade')
nota1.pack(pady=30)

#nota2
nota2 = ctk.CTkEntry(janela,
                    width=350,
                    height=40,
                    border_color='yellow',
                    placeholder_text='Digite a sua nota na 2ª Unidade')
nota2.pack()

#nota 3
nota3 = ctk.CTkEntry(janela,
                    width=350,
                    height=40,
                    border_color='yellow',
                    placeholder_text='Digite a sua nota na 3ª Unidade')
nota3.pack(pady=30)

botao = ctk.CTkButton(janela,
                    width=200,
                    height=40,
                    text='Resultado',
                    fg_color='yellow',
                    text_color='black',
                    cursor='hand2',
                    font=('arial',15),
                    command=calcular)
botao.pack(pady=15)

resultado = ctk.CTkLabel(janela,
                        text='',
                        text_color='white',
                        font=('arial',20))
resultado.pack(pady=10)

janela.mainloop()