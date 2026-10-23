import customtkinter as ctk, qrcode
from PIL import Image, ImageTk

ctk.set_appearance_mode('dark')

janela = ctk.CTk()
janela.geometry('450x500')
janela.title('Sistema Gerador de QRCODE')
janela.resizable(False,False)

imagem_qr = None


titulo = ctk.CTkLabel(janela,
                    text='Sistema Gerador de QRCODE',
                    text_color='white',
                    font=('Arial',30))
titulo.pack (pady = 10)

entrada = ctk.CTkEntry(janela,
                    width=300,
                    height=40,
                    placeholder_text='Digite a URL ou o PIX',
                    placeholder_text_color='silver',
                    border_color='white')
entrada.pack(pady=10)

botao = ctk.CTkButton(janela,
                    width=200,
                    height=40,
                    fg_color='black',
                    text='Gerar QR CODE',
                    font=('Arial',30),
                    text_color='white',
                    hover_color='navy',
                    cursor='hand2')
botao.pack(pady=10)

resultado = ctk.CTkLabel(janela,
                        text='')
resultado.pack(pady=20)

janela.mainloop()