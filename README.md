# Interface Gráfica de Segmentação de Cachorros e Gatos
Este é um exemplo de uma interface gráfica simples em Python usando a biblioteca Tkinter, que permite ao usuário carregar uma imagem e segmentá-la para identificar se é um cachorro ou um gato.

## Funcionamento do Código
Importação das Bibliotecas: O código inicia importando as bibliotecas necessárias para a execução do programa. São elas:

<table>
	<li><b>cv2</b>: Biblioteca OpenCV para processamento de imagens.</li>
	<li><b>Tk</b> e <b>filedialog</b>: Parte da biblioteca Tkinter para criar a interface gráfica e lidar com a janela de diálogo de arquivo.</li>
	<li><b>Image</b> e <b>ImageTk</b>: Do módulo PIL (Python Imaging Library) para manipulação de imagens.</li>
</table>

<code>Função carregar_imagem()</code>: Esta função é chamada quando o botão "Carregar Imagem" é clicado. Ela abre uma janela de diálogo de arquivo que permite ao usuário selecionar uma imagem. A imagem selecionada é exibida na interface em um rótulo (Label).
<br>
<code>Função segmentar_imagem()</code>: Esta função é chamada quando o botão "Segmentar" é clicado. Ela ainda não está totalmente implementada, mas será responsável por processar a imagem carregada e identificar se é um cachorro ou um gato.
<br>
<code>Criação da Janela e Elementos</code>: O código cria a janela principal (janela) usando a classe Tk(). Em seguida, cria os elementos da interface, incluindo um texto explicativo, um rótulo para exibir a imagem carregada e dois botões - "Carregar Imagem" e "Segmentar".
<br>
<code>Exibição da Janela</code>: A interface gráfica é exibida chamando o método mainloop() da janela principal. A partir deste ponto, a interface estará funcionando e pronta para interação do usuário.

## Como Utilizar
Execute o código Python em um ambiente que suporta <b>Tkinter</b>.
Clique no botão <b>"Carregar Imagem"</b> para selecionar uma imagem do seu computador.
A imagem selecionada será <i>exibida na interface</i>.
Clique no botão <b>"Segmentar"</b> para iniciar a segmentação da imagem <i>(essa parte ainda precisa ser implementada).</i>