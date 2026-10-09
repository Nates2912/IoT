import os, customtkinter as ctk
ctk.set_appearance_mode('dark')

janela = ctk.CTk("#1A1C1F")

janela.geometry('400x400')
janela.resizable(False,False)
janela.title('RESERVA DE HOTEL - PROVA - 09/10/2026')
janela.iconbitmap('natalia/8.PROVA/1497618989-3_85123.ico')


def calcular():
    
    try:
        quantidade_diarias = int(quantidade.get())
        valor_diaria = float(valor.get())
        desconto = 0
        valor_total = 0
            
            
        valor_hospedagem = quantidade_diarias * valor_diaria
        if quantidade_diarias >= 5:
                desconto = valor_hospedagem*0.1
                valor_total = valor_hospedagem - desconto
                

        resultado.configure(text=f'Hospedagem:R${valor_hospedagem:.2f}\nDesconto: R${desconto:.2f}\nValor total: R${valor_total:.2f}',text_color = 'white')
        
        
    except:
            resultado.configure(text='Preencha os campos!')





titulo_nome = ctk.CTkLabel(janela,
                text='Nome do Hóspede: ',
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
                    placeholder_text='Digite o nome do hóspede')
nome.pack()



titulo_quantidade = ctk.CTkLabel(janela,
                text='Quantidade de Diárias: ',
                text_color='white',
                font=('sans serif',15))
titulo_quantidade.pack(anchor = 'w',padx = 25, pady = 5)
quantidade = ctk.CTkEntry(janela,
                    fg_color="#1C2329",
                    width=350,
                    height = 40,
                    text_color="#778FAC",
                    border_color="#485E7A",
                    placeholder_text_color= "#778FAC",
                    placeholder_text='Digite a quantidade de diárias')
quantidade.pack()



titulo_valor = ctk.CTkLabel(janela,
                text='Valor da Diária:',
                text_color='white',
                font=('sans serif',15))
titulo_valor.pack(anchor = 'w',padx = 25, pady = 5)
valor = ctk.CTkEntry(janela,
                    fg_color="#1C2329",
                    width=350,
                    height = 40,
                    text_color="#778FAC",
                    border_color="#485E7A",
                    placeholder_text_color= "#778FAC",
                    placeholder_text='Digite o valor da diária')
valor.pack()



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
