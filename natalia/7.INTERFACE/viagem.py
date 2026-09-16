import os, customtkinter as ctk
ctk.set_appearance_mode('dark')

os.system('cls')

#funcoes
def calcular():
    d = int(distancia.get())
    c = float(consumo.get())
    p = float(precoCombustivel.get())
    
    formula = (d/c)*p
    
    resultado.configure(text=f'O valor para a viagem é de R${formula:.2f}')

#janela
janela = ctk.CTk()

janela.geometry('500x400')
janela.resizable(False,False)
janela.title('Calculadora de Viagem - 16/09/2026')
janela.iconbitmap('natalia/7.INTERFACE/key_icon_126623.ico')

#corpo
titulo = ctk.CTkLabel(janela,
                    text='APP VIAGEM',
                    text_color='white',
                    font=('verdanna',40,('bold')))
titulo.pack(pady=20)


#distancia da viagem
distancia = ctk.CTkEntry(janela,
                        width=300,
                        height=40,
                        border_color='white',
                        placeholder_text='Digite a distância da viagem em Kilometros(Km)')
distancia.pack(pady=15)

#consumo do veiculo
consumo = ctk.CTkEntry(janela,
                        width=300,
                        height=40,
                        border_color='white',
                        placeholder_text='Digite o consumo do seu veículo')
consumo.pack()

#preco do combustivel
precoCombustivel = ctk.CTkEntry(janela,
                        width=300,
                        height=40,
                        border_color='white',
                        placeholder_text='Digite o preço atual do combustível')
precoCombustivel.pack(pady=15)


botao = ctk.CTkButton(janela,
                    width=170,
                    height=40,
                    border_width=2,
                    border_color='red',
                    text='Calcular Gasto',
                    fg_color='pink',
                    text_color='black',
                    cursor = 'hand2',
                    font=('arial',15),
                    command=calcular)
botao.pack(pady = 10)

resultado = ctk.CTkLabel(janela,
                        text='',
                        text_color='white',
                        font=('arial',20))
resultado.pack(pady=10)



janela.mainloop()