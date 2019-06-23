# link pra download pytesseract https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.0.0.20190526.exe
try:
    import pytesseract
except:
    print('\nNão foi possível carregar o pytesseract. Não será possível detectar o texto das placas')
import math
import cv2

"""
    FURB - Bacharelado em Ciências da Computação
    Inteligencia Artifical
    Implementação do Seminário de Visão Computacional

    Adriner Maranho de Andrade
    Fábio Luiz Fischer
    Jorge Guilherme Kohn
"""

class Plate:
    def __init__(self, string_detector_enable=True, pytesseract_path=r'C:\Program Files\Tesseract-OCR\tesseract.exe'):
        self.string_detector_enable = string_detector_enable
        self.img = None
        self.text = None
        if self.string_detector_enable:
            # Seta caminho de instalação para o pytesseract
            pytesseract.pytesseract.tesseract_cmd = pytesseract_path

    def show_img(self):
        cv2.imshow("plate", self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def set_img(self, original_img, chars, width_margin=1.15, height_margin=1.5):
        # calculate the center point of the plate
        center_x = (chars[0].center_x + chars[len(chars) - 1].center_x) / 2.0
        center_y = (chars[0].center_y + chars[len(chars) - 1].center_y) / 2.0

        # calculate plate width and height
        width = int((chars[len(chars) - 1].bbox_x + chars[len(chars) - 1].bbox_width - chars[0].bbox_x) * width_margin)
        height = int((sum(c.bbox_height for c in chars) / len(chars)) * height_margin)

        # Calcula o angulo de correção do texto para aplicar na imagem
        opp = chars[len(chars) - 1].center_y - chars[0].center_y
        hyp = chars[0].euclidian_dist(chars[len(chars) - 1])
        angle = math.asin(opp / hyp) * (180.0 / math.pi)
        rotate = cv2.getRotationMatrix2D((center_x, center_y), angle, 1.0)
        img_rotate = cv2.warpAffine(original_img, rotate, (original_img.shape[1], original_img.shape[0]))

        # Recorta a imagem original para que a região da placa seja centralizada
        self.img = cv2.getRectSubPix(img_rotate, (width, height), (center_x, center_y))

        # Utiliza o pytesseract para identificar o conteudo em texto na imagem recortada
        if self.string_detector_enable:
            self.text = pytesseract.image_to_string(self.img)
        else:
            print("o detector de texto esta dasabilitado")
