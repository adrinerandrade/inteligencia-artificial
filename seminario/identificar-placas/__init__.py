from Plate import Plate
from Char import Char
import numpy as np
import glob
import cv2

"""
    FURB - Bacharelado em Ciências da Computação
    Inteligencia Artifical
    Implementação do Seminário de Visão Computacional

    Adriner Maranho de Andrade
    Fábio Luiz Fischer
    Jorge Guilherme Kohn
"""

# Define se o algorítmo irá utilizar o pytesseract para detectar o texto das placas
string_detector_enable = True
# Define se o algorítmo irá exibir o recorte das placas
show_cropped_img = True

# link pra download pytesseract https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.0.0.20190526.exe
try:
    import pytesseract
except:
    print('\nNão foi possível carregar o pytesseract. Não será possível detectar o texto das placas')
    string_detector_enable = False

print('\n\n\nO detector de texto pytesseract está', 'habilitado...' if string_detector_enable else 'desabilitado...')
print('A opção de exibir as imagens auxiliares esta', 'habilitada...\n' if show_cropped_img else 'desabilitada...\n')

dataset = [(cv2.imread(file), file) for file in glob.glob("Amostras/*.jpg")]
resultados = []

for img_set in dataset:
    img = img_set[0]
    file = img_set[1]

    cv2.imshow("Imagem Original", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    try:
        if img is not None:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            # Tratamento da imagem para um ganho de definição
            _, saturation, value = cv2.split(gray)
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

            cv2.imshow("TopHat", cv2.morphologyEx(value, cv2.MORPH_TOPHAT, kernel))
            cv2.waitKey(0)
            cv2.destroyAllWindows()

            add = cv2.add(value, cv2.morphologyEx(value, cv2.MORPH_TOPHAT, kernel))
            subtract = cv2.subtract(add, cv2.morphologyEx(value, cv2.MORPH_BLACKHAT, kernel))

            cv2.imshow("BlackHat", cv2.morphologyEx(value, cv2.MORPH_BLACKHAT, kernel))
            cv2.waitKey(0)
            cv2.destroyAllWindows()

            cv2.imshow("Resultado", subtract)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

            blur = cv2.GaussianBlur(subtract, (5, 5), 0)
            thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 19, 9)

            # Tenta buscar contornos na imagem binarizada. Os contornos serão as letras
            _, contours, _ = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
            height, width = thresh.shape
            img_contours = np.zeros((height, width, 3), dtype=np.uint8)
            chars = []

            for i in range(0, len(contours)):
                cv2.drawContours(img_contours, contours, i, (255, 255, 255))
                possibleChar = Char(contours[i])
                if possibleChar.is_valid_char():
                    chars.append(possibleChar)

            if show_cropped_img:
                cv2.imshow("Contornos", img_contours)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

            plates_list = []
            text_summary = []

            for char in chars:
                text = []
                for match in chars:
                    if match == char:
                        continue
                    # Compara caracteristicas entre os dois caracteres
                    c_area = float(abs(match.bbox_area - char.bbox_area)) / float(char.bbox_area)
                    c_width = float(abs(match.bbox_width - char.bbox_width)) / float(char.bbox_width)
                    c_height = float(abs(match.bbox_height - char.bbox_height)) / float(char.bbox_height)
                    # TODO - Utilizar uma IA para calcular um valor otimizado para as constantes.
                    # As constantes foram definidas para atender a maioria dos dados de treinamento
                    if char.euclidian_dist(match) < (char.diagonal_size * 5) and char.angle(match) < 12.0 and c_area < 0.5 and c_width < 0.8 and c_height < 0.2:
                        text.append(match)
                text.append(char)
                # Define um limite de caracteres para o texto, de forma que textos indesejaveis não sejam considerados pelo algoritmo
                if len(text) >= 7:
                    text_summary.append(text)
                    break

            for text in text_summary:
                possiblePlate = Plate(string_detector_enable)
                # Ordena caracteres da imagem horizontamente
                text.sort(key=lambda c: c.center_x)
                # Analisa a imagem original e recorta o espaço ao redor da placa para que apenas o conteudo da placa seja exibido
                # Se tudo der certo, insere a placa para a lista
                possiblePlate.set_img(img, text)
                if possiblePlate.img is not None:
                    plates_list.append(possiblePlate)

            # Exibe o texto da placa, e se habilitado, exibe a imagem recortada da placa
            for plate in plates_list:
                if plate.text is None or not plate.text:
                    print('%s - Texto não reconhecido' % file)
                else:
                    print('%s - %s' % (file, plate.text))
                    resultados.append((file, plate.text))

                if show_cropped_img:
                    plate.show_img()
        else:
            print('%s - Falha ao ler arquivo' % file)
    except:
        print('%s - Falha ao ler arquivo' % file)

