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

    # Use o modelo de detecção de objetos YOLO V3 para detectar objetos na imagem
    detector = cv2.dnn.readNetFromDarknet("yolov3.cfg", "yolov3.weights")
    classes = ["person", "dog", "cat"]
    colors = [(0, 255, 0), (0, 0, 255), (255, 0, 0)]

    # Detecte objetos na imagem
    detections = detector.detect(imagem, 0.5, 0.4)

    # Desenhe os retângulos ao redor dos objetos detectados
    for detection in detections:
        x, y, w, h = detection[2:6]
        confidence = detection[6]
        label = classes[detection[5]].upper()
        color = colors[detection[5]]

        cv2.rectangle(imagem, (x, y), (x + w, y + h), color, 2)
        cv2.putText(imagem, label, (x, y + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # Exiba a imagem segmentada na janela
    img_label.imagem = ImageTk.PhotoImage(imagem)
    img_label.config(image=img_label.imagem)

    # Exemplo de como exibir o resultado na janela:
    resultado = "Cachorro" if "dog" in label else "Gato"
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