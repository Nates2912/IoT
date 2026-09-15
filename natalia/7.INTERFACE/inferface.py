import os, customtkinter as ctk
ctk.set_appearance_mode('dark')
#tambem tem light e system


os.system("cls")

#janela --
janela = ctk.CTk()
janela.geometry("500x300")
janela.resizable(False,False)
janela.title("Sistema de acesso - 2026")
janela.iconbitmap('natalia/7.INTERFACE/key_icon_126623.ico')

#corpo da janela --

titulo = ctk.CTkLabel(janela,
                    text="Sistema de LOGIN",
                    text_color="white",
                    font=("papyrus",40))
titulo.pack()

login =ctk.CTkEntry(janela,
                    width=400,
                    height=40,
                    border_color="white",
                    placeholder_text="Digite seu login: ")
login.pack(pady=30)


senha =ctk.CTkEntry(janela,
                    width=400,
                    height=40,
                    border_color='white',
                    placeholder_text="Digite sua senha: ",
                    show = '•')
senha.pack()

botao=ctk.CTkButton(janela,
                    width=200,
                    height=40,
                    text='Acessar',
                    fg_color='white',
                    text_color='black',
                    cursor = 'hand2',
                    font=('papyrus',30))
botao.pack(pady = 20)



janela.mainloop()

