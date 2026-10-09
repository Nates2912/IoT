import os, customtkinter as ctk
ctk.set_appearance_mode('dark')

janela = ctk.CTk("#1A1C1F")

def calcular():
    n1 = float(nota1.get())
    n2 = float(nota2.get())

    try:
        media = (n1+n2)/2
        if media >= 7:
            situacao = 'APROVADO!'

        elif media >=5 or media <= 6.9:
            situacao = 'RECUPERAÇÃO.'

        else:
            situacao = 'REPROVADO...'


        resultado.configure(text=f'Média: {media:.1f}\nSituação: {situacao}',text_color = 'white')

    except:
        resultado.configure(text='Preencha os campos!')
        
janela.geometry('400x400')
janela.resizable(False,False)
janela.title('RESULTADO ACADÊMICO - PROVA - 09/10/2026')
janela.iconbitmap('natalia/8.PROVA/bluepencil_azul_12512.ico')






titulo_nome = ctk.CTkLabel(janela,
                text='Nome do aluno: ',
                text_color='white',
                font=('sans serif',15))
titulo_nome.pack(anchor = 'w',padx = 25, pady = 5)
nome = ctk.CTkEntry(janela,
                    fg_color="#1C2329",
                    width=350,
                    height = 40,
                    text_color="#778FAC",
                    border_color="#485E7A",
                    placeholder_text_color= "#778FAC",
                    placeholder_text='Digite o nome do aluno')
nome.pack()



titulo_nota1 = ctk.CTkLabel(janela,
                text='1ª Nota: ',
                text_color='white',
                font=('sans serif',15))
titulo_nota1.pack(anchor = 'w',padx = 25, pady = 5)
nota1 = ctk.CTkEntry(janela,
                    fg_color="#1C2329",
                    width=350,
                    height = 40,
                    text_color="#778FAC",
                    border_color="#485E7A",
                    placeholder_text_color= "#778FAC",
                    placeholder_text='Digite a 1ª nota do aluno')
nota1.pack()



titulo_nota2 = ctk.CTkLabel(janela,
                text='2ª Nota: ',
                text_color='white',
                font=('sans serif',15))
titulo_nota2.pack(anchor = 'w',padx = 25, pady = 5)
nota2 = ctk.CTkEntry(janela,
                    fg_color="#1C2329",
                    width=350,
                    height = 40,
                    text_color="#778FAC",
                    border_color="#485E7A",
                    placeholder_text_color= "#778FAC",
                    placeholder_text='Digite a 1ª nota do aluno')
nota2.pack()



botao = ctk.CTkButton(janela,
                    width=350,
                    height=40,
                    text='CALCULAR RESULTADO',
                    fg_color="#22579B",
                    text_color="white",
                    cursor='hand2',
                    font=('serif',15,('bold')),
                    hover_color="#164179",
                    command=calcular)
botao.pack(pady=15)
resultado = ctk.CTkLabel(janela,
                        text='',
                        text_color='white',
                        font=('arial',20))
resultado.pack(pady = 10)

janela.mainloop()
