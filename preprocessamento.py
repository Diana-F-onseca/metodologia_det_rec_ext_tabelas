# -*- coding: utf-8 -*-

import os
from pdf2image import convert_from_path
from PIL import Image, ImageOps

# Cria uma pasta para o caso de ainda não existir
def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# Rotação diretamente nas imagens se a imagem deve ser rodada 90º
def rotate_image_if_necessary(image, should_rotate):
    if should_rotate:
        return image.rotate(90, expand=True)
    else:
        return image

# Rotação diretamente nas imagens se a imagem deve ser rodada 180º
def rotate_image_oliveira(image, should_rotate_180):
    if should_rotate_180:
        return image.rotate(180, expand=True)
    else:
        return image

# Rotação diretamente nas imagens se a imagem deve rodar 270º
def rotate_image_270(image, should_rotate_270):
    if should_rotate_270:
        return image.rotate(270, expand=True)
    else:
        return image

# Recortar a imagem ao meio e considerar apenas o lado esquerdo
def recortar_metade_esquerda(image):
    # Obtém as dimensões da imagem
    width, height = image.size

    # Define a caixa de corte para a metade esquerda da imagem
    left_box = (0, 0, width//2, height)

    # Recorta a imagem
    left_half = image.crop(left_box)

    return left_half

# Função que converte pdf em jpeg
def convert_pdf_to_jpeg(pdf_folder_path, output_folder_path):
    create_directory_if_not_exists(output_folder_path)
    pdf_files = [f for f in os.listdir(pdf_folder_path) if f.endswith('.pdf')]
    if not pdf_files:
        print("Nenhum ficheiro PDF encontrado.")
        return

    for pdf_file in pdf_files:
        pdf_path = os.path.join(pdf_folder_path, pdf_file)
        print(f"A processar o ficheiro: {pdf_file}")

        try:
            images = convert_from_path(pdf_path)
            for i, image in enumerate(images):

                should_rotate = pdf_file.upper().startswith('ISB')

                image = rotate_image_if_necessary(image, should_rotate)

                should_rotate_leroi_1 = pdf_file.startswith('B-64542152')
                image = rotate_image_270(image, should_rotate_leroi_1)

                should_rotate_leroi_2 = pdf_file.startswith('Campingaz')
                image = rotate_image_if_necessary(image, should_rotate_leroi_2)

                should_rotate_oliveira = pdf_file.startswith('Oliveira')
                image = rotate_image_oliveira(image, should_rotate_oliveira)

                should_rotate_180_leroi = pdf_file.startswith('P-PEGACOL-CIMENTOSCOLALDA_2')
                image = rotate_image_oliveira(image, should_rotate_180_leroi)

                should_rotate_180_leroi_2 = pdf_file.startswith('XeroxScan_05122023120303')
                image = rotate_image_oliveira(image, should_rotate_180_leroi_2)

                if pdf_file.startswith('P-BIOMA-ARTEVASI_1'):
                    image = recortar_metade_esquerda(image)

                output_filename = f'{os.path.splitext(pdf_file)[0]}_page_{i+1}.jpeg'
                output_image_path = os.path.join(output_folder_path, output_filename)
                width, height = image.size
                conv_height = height
                conv_width = width

                # Redimensiona a imagem, com a manutenção da proporção e ajusta-a para caber numa caixa
                resized_image = ImageOps.pad(image, (conv_width, conv_height), color='white')

                # Guarda a imagem
                resized_image.save(output_image_path, 'JPEG')

                image_dimensions = resized_image.size
                print(f"Dimensões da imagem {output_filename}: {image_dimensions}")
        except Exception as e:
            print(f"Erro ao converter {pdf_file}: {e}")

# Define os caminhos para as pastas de PDFs e de imagens
current_directory = os.getcwd()
pdf_folder = os.path.join(current_directory, "leroiExamples/")
output_folder = os.path.join(current_directory, "leroiExamples/pdf_jpeg_/")

# converte as páginas dos pdfs em imagens JPEG
convert_pdf_to_jpeg(pdf_folder, output_folder)

import os
import shutil
# cria uma nova pasta, se não existir, e copia todos os ficheiros da pasta de origem para a pasta de destino
# recebe o caminho da pasta de origem e o caminho da pasta de destino
def copiar_ficheiros_para_nova_pasta(origem, destino):

    # Cria o diretoria de destino se ele não existir
    if not os.path.exists(destino):
        os.makedirs(destino)
        print(f"Pasta '{destino}' criada.")

    # Lista todos os ficheiros na diretoria de origem e copia cada um para a diretoria de destino
    for ficheiro in os.listdir(origem):
        caminho_completo_origem = os.path.join(origem, ficheiro)
        caminho_completo_destino = os.path.join(destino, ficheiro)

        # Verifica se é um ficheiro antes de copiar
        if os.path.isfile(caminho_completo_origem):
            shutil.copy2(caminho_completo_origem, caminho_completo_destino)
            print(f"ficheiro '{ficheiro}' copiado para '{destino}'.")

# Define as diretorias das pastas de origem e destino
pasta_origem = "/home/diana/projeto/leroiExamples/pdf_jpeg_"
pasta_destino = "/home/diana/projeto/leroiExamples/leroy_bad_files_removed"

# Chama a função que copia ficheiros
copiar_ficheiros_para_nova_pasta(pasta_origem, pasta_destino)

# método que remove uma imagem de uma pasta, recebe 1 pasta e o nome do ficheiro a remover
def remover_imagem(pasta, nome_imagem):
    caminho_completo = os.path.join(pasta, nome_imagem)

    # Verifica se o ficheiro existe, para não dar erros
    if os.path.exists(caminho_completo):
        # Remove a imagem
        os.remove(caminho_completo)
        print(f"A imagem '{nome_imagem}' foi removida com sucesso de '{pasta}'.")
    else:
        print(f"A imagem '{nome_imagem}' não foi encontrada em '{pasta}'.")

folder = "/home/diana/projeto/leroiExamples/leroy_bad_files_removed"
images_list = ["20231103105843214_page_40.jpeg","BRILLIANTAG.TR_1_page_27.jpeg", "BRILLIANTAG.TR_1_page_29.jpeg", "BRILLIANTAG.TR_2_page_2.jpeg",
               "BRILLIANTAG.TR_2_page_4.jpeg", "BRILLIANTAG.TR_2_page_23.jpeg","BRILLIANTAG.TR_3_page_7.jpeg",
               "BRILLIANTAG.TR_3_page_11.jpeg","BRILLIANTAG.TR_3_page_15.jpeg", "Catral-04092023_page_3.jpeg",
               "Catral-04092023_page_1.jpeg","daaa-trq-v7-21_page_1.jpeg","BRILLIANTAG.TR_1_page_17.jpeg",
               "BRILLIANTAG.TR_1_page_15.jpeg","BE0433026509_page_2.jpeg","DE123841657_page_40.jpeg",
               "DE123841657_page_112.jpeg", "DE123841657_page_101.jpeg",
               "DE123841657_page_4.jpeg","DE123841657_page_5.jpeg","DE123841657_page_9.jpeg",
               "DE123841657_page_13.jpeg","DE123841657_page_17.jpeg","DE123841657_page_18.jpeg",
               "DE123841657_page_23.jpeg","DE123841657_page_24.jpeg","DE123841657_page_28.jpeg",
               "DE123841657_page_34.jpeg","DE123841657_page_35.jpeg","DE123841657_page_47.jpeg",
               "DE123841657_page_52.jpeg","DE123841657_page_41.jpeg","DE123841657_page_46.jpeg",
               "DE123841657_page_55.jpeg","DE123841657_page_56.jpeg","DE123841657_page_61.jpeg",
               "DE123841657_page_65.jpeg","DE123841657_page_69.jpeg","DE123841657_page_75.jpeg",
               "DE123841657_page_79.jpeg","DE123841657_page_83.jpeg","DE123841657_page_96.jpeg",
               "DE123841657_page_102.jpeg","DE123841657_page_108.jpeg","DE123841657_page_113.jpeg",
               "DE123841657_page_117.jpeg","DE123841657_page_118.jpeg","DE123841657_page_123.jpeg",
               "DE123841657_page_127.jpeg","DE123841657_page_131.jpeg","DE123841657_page_135.jpeg",
               "DE123841657_page_139.jpeg","DE123841657_page_140.jpeg","DE123841657_page_145.jpeg",
               "DE123841657_page_150.jpeg","DE123841657_page_155.jpeg", "DE123841657_page_160.jpeg",
               "DE123841657_page_161.jpeg","DE123841657_page_60.jpeg","DE123841657_page_87.jpeg",
               "DE123841657_page_95.jpeg",
               "EGGERHOLWERKSTOFFEWISMAR_1_page_3.jpeg", "ESB65907727_page_2.jpeg",
               "ESB65907727_page_70.jpeg", "ESB65907727_page_72.jpeg","ESB65907727_page_74.jpeg",
               "ESB86594736_page_8.jpeg","ESB86594736_page_17.jpeg", "ESB86594736_page_20.jpeg",
               "ESB86594736_page_27.jpeg","ESB86594736_page_33.jpeg",
               "ESB96356886_page_38.jpeg","ESB96356886_page_41.jpeg","ESB96356886_page_45.jpeg",
               "ESN6241090G_page_2.jpeg",
               "FR39435380241_page_2.jpeg","FR39435380241_page_4.jpeg","FR39435380241_page_5.jpeg",
               "FR39435380241_page_6.jpeg","FR39435380241_page_8.jpeg","FR39435380241_page_10.jpeg",
               "FR39435380241_page_12.jpeg","FR39435380241_page_14.jpeg","FR39435380241_page_16.jpeg",
               "FR39435380241_page_18.jpeg","FR39435380241_page_20.jpeg","FR39435380241_page_22.jpeg",
               "FR39435380241_page_24.jpeg","FR39435380241_page_26.jpeg","FR39435380241_page_28.jpeg",
               "FR39435380241_page_30.jpeg","FR39435380241_page_32.jpeg","FR39435380241_page_34.jpeg",
               "FR39435380241_page_36.jpeg","FR39435380241_page_38.jpeg","FR39435380241_page_40.jpeg",
               "FR39435380241_page_42.jpeg","FR39435380241_page_44.jpeg","FR39435380241_page_27.jpeg",
               "FR39435380241_page_37.jpeg","ISOLTUBEXS.L._S05_1_page_1.jpeg","FR62318867770_page_1.jpeg"
               "IT00123220352_page_2.jpeg","IT00123220352_page_4.jpeg","IT00123220352_page_13.jpeg",
               "IT00123220352_page_15.jpeg","IT00123220352_page_18.jpeg","IT00123220352_page_22.jpeg",
               "IT00123220352_page_24.jpeg","IT00123220352_page_26.jpeg","IT00123220352_page_6.jpeg",
               "P-DYRUP-TINTASDYRUPS.ATR_1_page_2.jpeg","IT00123220352_page_20.jpeg","IT00123220352_page_28.jpeg",
               "IT00860500438_page_7.jpeg","IT00860500438_page_12.jpeg","IT00860500438_page_16.jpeg",
               "IT00860500438_page_18.jpeg","IT02722730419_page_9.jpeg","IT02722730419_page_17.jpeg",
               "IT02722730419_page_23.jpeg","IT02722730419_page_44.jpeg","IT02722730419_page_59.jpeg",
               "IT02722730419_page_75.jpeg","P-BIOMA-ARTEVASI_1_page_33.jpeg","P-BIOMA-ARTEVASI_1_page_41.jpeg",
               "P-BIOMA-ARTEVASI_1_page_52.jpeg","Rubicer_page_2.jpeg","FR39435380241_page_27.jpeg",
               "P-DYRUP-TINTASDYRUPS.ATR_2_page_3.jpeg","P-DYRUP-TINTASDYRUPS.ATR_2_page_5.jpeg","P-DYRUP-TINTASDYRUPS.ATR_2_page_10.jpeg",
               "P-DYRUP-TINTASDYRUPS.ATR_2_page_12.jpeg","P-DYRUP-TINTASDYRUPS.ATR_2_page_16.jpeg","P-DYRUP-TINTASDYRUPS.ATR_2_page_18.jpeg",
               "P-DYRUP-TINTASDYRUPS.ATR_2_page_20.jpeg","P-DYRUP-TINTASDYRUPS.ATR_2_page_25.jpeg","P-DYRUP-TINTASDYRUPS.ATR_2_page_28.jpeg",
               "P-DYRUP-TINTASDYRUPS.ATR_2_page_31.jpeg","P-DYRUP-TINTASDYRUPS.ATR_2_page_33.jpeg","P-DYRUP-TINTASDYRUPS.ATR_2_page_36.jpeg",
               "P-DYRUP-TINTASDYRUPS.ATR_2_page_39.jpeg",
               "P-HENKELIBERICAUNIPESLDA_1_page_16.jpeg",
               "P-HENKELIBERICAUNIPESLDA_2_page_8.jpeg",
               "POLIMARKSRL_2_page_8.jpeg", "POLIMARKSRL_2_page_14.jpeg",
               "P-PEGACOL-CIMENTOSCOLALDA_3_page_3.jpeg",
               "P-RUBICERLDATR_1_page_1.jpeg","P-RUBICERLDATR_1_page_3.jpeg","P-RUBICERLDATR_2_page_1.jpeg",
               "P-RUBICERLDATR_2_page_3.jpeg", "P-RUBICERLDATR_3_page_1.jpeg", "P-RUBICERLDATR_3_page_4.jpeg",
               "P-TESAPORTUGALS_10_2_page_2.jpeg",
               "P-TESAPORTUGALS_10_3_page_2.jpeg",
               "RIOMAS.L.TR_1_page_2.jpeg","RIOMAS.L.TR_2_page_2.jpeg","RIOMAS.L.TR_3_page_2.jpeg",
               "RIOMAS.L.TR_31_page_2.jpeg",
               "Roca_page_55.jpeg","Roca_page_91.jpeg",
               "SAARPORKLAUSECKHARDTGMB_1_page_2.jpeg","SAARPORKLAUSECKHARDTGMB_3_page_2.jpeg",
               "Sarpoor-guia02082023_page_4.jpeg","Sarpoor-guia02082023_page_6.jpeg",
               "SPAXTORNILLERIAS.A.U_2_page_2.jpeg",
               "TEXATHENEA_1_page_24.jpeg","TEXATHENEA_1_page_26.jpeg","TEXATHENEA_1_page_28.jpeg",
               "TEXATHENEA_1_page_42.jpeg",
               "XeroxScan_18122023075149_page_29.jpeg"
               ]
for image_name in images_list:
    remover_imagem(folder, image_name)
