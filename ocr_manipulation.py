# -*- coding: utf-8 -*-
"""ocr_manipulation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1EwACITAJfKpo8GUizzOp5yh_Ym-j9DYm
"""

import os
def extract_ocr_data(folder_path):
    data_list = []

    # Percorrer os ficheiros da diretoria que dá entrada na função
    for filename in os.listdir(folder_path):
        full_path = os.path.join(folder_path, filename)
        if os.path.isfile(full_path) and filename.endswith('.txt'):
            with open(full_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()

                # Lista para guardar os dados deste ficheiro
                file_data = [filename]

                # Processar cada linha no ficheiro de OCR
                for line in lines:
                    if 'BoundingBox' in line and '-' in line:
                        parts = line.split(' - > ')
                        if len(parts) > 1:
                            bbox_part = parts[1]
                            if ':' in bbox_part:
                                bbox_raw = bbox_part.split(': ')[1]
                                bbox = eval(bbox_raw)  # Converter a string de bbox para uma lista
                                text = parts[0].strip()
                                file_data.append([bbox, text])

                data_list.append(file_data)

    return data_list