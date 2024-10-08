# -*- coding: utf-8 -*-
"""coor_manipulation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17RdYxfWgmnTcENPiq5HskeukP7iH0fO2
"""

# substituir pela função de interseção
def intersects(bbox1, bbox2):
    # Calcula a interseção entre duas caixas delimitadoras
    # bbox no formato [x_min, y_min, x_max, y_max]
    x_left = max(bbox1[0], bbox2[0])
    y_top = max(bbox1[1], bbox2[1])
    x_right = min(bbox1[2], bbox2[2])
    y_bottom = min(bbox1[3], bbox2[3]) #
    # Verifica se existe sobreposição
    return (x_right > x_left+3) and (y_bottom > y_top+3)

def remove_bboxes_without_ocr(ocr_results, resized_coords, nome_ficheiro):
    # Dicionário para guardar os resultados dos OCRs por ficheiro
    ocr_dict = {}
    ocr_dict_ = []
    # Adicionar todas as caixas de OCR para o ficheiro
    for data in ocr_results:
        print(data, 'data')
        bbox = data[0]  # garante que a lista é a correta
        if type(bbox) == list and len(bbox) == 8:  # apenas adiciona no ocr_dict_ as bboxes com o número esperado de elementos
            ocr_dict_.append([bbox[0], bbox[1], bbox[4], bbox[5]])
        else:
            print(f"Erro no formato da bbox : {bbox}")

    # Lista de resultados modificada
    new_resized_coords = []

    x_coords = resized_coords[0]
    y_coords = resized_coords[1]

    # Apenas a primeira linha de y coord
    y_top = y_coords[0]
    y_bottom = y_coords[1] if len(y_coords) > 1 else y_coords[0] + 10  # default height assumido

    if 'Xerox' in nome_ficheiro:
        new_x_coords = x_coords
        print('Não se aplica a condição de cabeçalho vazio')

    else:
        # Lista para armazenar x coords da primeira linha sem bboxes de OCR internas
        new_x_coords = []
        for x_left, x_right in zip(x_coords[:-1], x_coords[1:]):
            bbox = [x_left, y_top, x_right, y_bottom]
            has_inner_ocr = False

            for ocr_bbox in ocr_dict_:
                print(ocr_bbox, bbox)
                if intersects(ocr_bbox, bbox) or intersects(bbox, ocr_bbox):
                    print('tem inter')
                    has_inner_ocr = True
                    break
            if has_inner_ocr:
                new_x_coords.append(x_left) # alterar para x_left
            new_x_coords.append(x_coords[-1])
    new_resized_coords = [new_x_coords, y_coords]
    return new_resized_coords

def intersects_(bbox1, bbox2):
        if not (isinstance(bbox1, list) and isinstance(bbox2, list)):
            print(f"Erro: bbox1 ou bbox2 não são listas: {bbox1}, {bbox2}")
            return False
        x_left = max(bbox1[0], bbox2[0])
        y_top = max(bbox1[1], bbox2[1])
        x_right = min(bbox1[2], bbox2[2])
        y_bottom = min(bbox1[3], bbox2[3])
        return (x_right > x_left) and (y_bottom > y_top)

def remove_unneeded_y_coords(ocr_results, resized_coords):
    x_coords = resized_coords[0]
    y_coords = resized_coords[1]

    ocr_bboxes = []
    for item in ocr_results:

        print(item)
        if isinstance(item[0], list) and len(item[0]) == 8:  # Ajuste para verificar corretamente os dados
            bbox = [item[0][0], item[0][1], item[0][4], item[0][5]]  # Assumindo formato de quatro pontos
            ocr_bboxes.append(bbox)
        else:
            print(f"Formato de bbox não esperado em ocr_data")

        new_y_coords = []
        for i in range(len(y_coords) - 1):
            y_top = y_coords[i]
            y_bottom = y_coords[i + 1]

            line_has_ocr = any(intersects(ocr_bbox, [x_coords[0], y_top, x_coords[-1], y_bottom]) for ocr_bbox in ocr_bboxes)
            new_y_coords.append(y_top)
            if line_has_ocr:
                new_y_coords.append(y_bottom)

        if new_y_coords[-1] != y_coords[-1]:
            last_y_top = y_coords[-2]
            last_y_bottom = y_coords[-1]
            last_line_has_ocr = any(intersects(ocr_bbox, [x_coords[0], last_y_top, x_coords[-1], last_y_bottom]) for ocr_bbox in ocr_bboxes)
            if last_line_has_ocr:
                new_y_coords.append(last_y_bottom)

        resized_coords[1] = new_y_coords

    return resized_coords

def intersects_json(bbox1, bbox2):
    print('box 1', bbox1)
    print('box 2', bbox2)
    if not (isinstance(bbox1, (list, tuple)) and isinstance(bbox2, (list, tuple))):
        raise TypeError("as bbox1 e bbox2 devem ser listas ou tuplos")

    x_left = max(bbox1[0], bbox2[0])
    y_top = max(bbox1[1], bbox2[1])
    x_right = min(bbox1[2], bbox2[2])
    y_bottom = min(bbox1[3], bbox2[3])

    intersection_width = x_right - x_left
    intersection_height = y_bottom - y_top

    return (intersection_width > 15) and (intersection_height > 10)

# Função para verificar a interseção com um limite de 5 pixels
def intersects_content(bbox1, bbox2):
    if not (isinstance(bbox1, (list, tuple)) and isinstance(bbox2, (list, tuple))):
        raise TypeError("As bbox1 e bbox2 devem ser listas ou tuplos")

    x_left = max(bbox1[0], bbox2[0])
    y_top = max(bbox1[1], bbox2[1])
    x_right = min(bbox1[2], bbox2[2])
    y_bottom = min(bbox1[3], bbox2[3])

    intersection_width = x_right - x_left
    intersection_height = y_bottom - y_top

    return (intersection_width > 5) and (intersection_height > 5)

# Função para converter bounding boxes de 8 para 4 coordenadas
def convert_bbox_8_to_4(eight_point_bbox):
    if isinstance(eight_point_bbox, (list, tuple)):
        x_coords = eight_point_bbox[::2]
        y_coords = eight_point_bbox[1::2]
        xmin = min(x_coords)
        xmax = max(x_coords)
        ymin = min(y_coords)
        ymax = max(y_coords)
        return [xmin, ymin, xmax, ymax]
    return

# Função para contar interseções
def contar_intersecoes(bbox, bboxes_list):
    intersecoes = 0
    for bbox2 in bboxes_list:
        if intersects_json(bbox, bbox2):
            intersecoes += 1
    return intersecoes