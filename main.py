import cv2
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

imagem_carregada = None

def carregar_imagem():
    global imagem_carregada
    file_path = filedialog.askopenfilename()
    if file_path:
        imagem = Image.open(file_path)
        imagem = imagem.resize((300, 300))  # Redimensione a imagem para exibir na interface
        img_label.imagem = ImageTk.PhotoImage(imagem)
        img_label.config(image=img_label.imagem)
        imagem_carregada = file_path  # Armazene o caminho da imagem carregada na variável global

def segmentar_imagem():
    global imagem_carregada
    if not imagem_carregada:
        return

    imagem = cv2.imread(imagem_carregada)
    # Implemente aqui a lógica de processamento de imagem para segmentar a imagem
    # Você pode utilizar técnicas de detecção de objetos, classificação ou qualquer outro método adequado para identificar se é um cachorro ou gato
    # Como exemplo, você pode utilizar um modelo previamente treinado para classificar a imagem

    # Exemplo de como exibir o resultado na janela:
    resultado = "Cachorro"  # Supondo que o resultado foi "Cachorro", você pode substituir isso com o resultado real
    resultado_label.config(text=f"Resultado da Segmentação: {resultado}")

# Crie a janela principal
janela = Tk()
janela.title("Segmentação de Cachorros e Gatos")

# Crie os elementos da interface
texto = Label(janela, text="Suba uma foto de cachorro ou gato")
texto.pack()

img_label = Label(janela)
img_label.pack()

botao_carregar = Button(janela, text="Carregar Imagem", command=carregar_imagem)
botao_carregar.pack()

botao_segmentar = Button(janela, text="Segmentar", command=segmentar_imagem)
botao_segmentar.pack()

resultado_label = Label(janela, text="Resultado da Segmentação: ")
resultado_label.pack()

# Inicie a janela principal
janela.mainloop()
