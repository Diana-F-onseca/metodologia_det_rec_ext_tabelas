# -*- coding: utf-8 -*-
"""novo_dataset_mais_pequeno.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1z-5gXVXbla6FVH1nVaRx5QeR1HO2wjyy
"""

import os
import random
import shutil

def random_files_list(directory, percentage=0.4):
    # Obter todos os nomes dos ficheiros na diretoria com extensões
    all_files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    # Determinar o número de ficheiros a serem incluídos
    num_files = int(len(all_files) * percentage)

    # Selecionar os ficheiros aleatoriamente
    selected_files = random.sample(all_files, num_files)

    # Remover a extensão dos ficheiros
    return [os.path.splitext(f)[0] for f in selected_files]

base_dir = 'all_images_yolov8__'
dest_dir = 'small_dataset'

############################3 Treino

# Diretorias de origem específicas para a pasta de treino
image_dir = os.path.join(base_dir, 'train', 'images')
label_dir = os.path.join(base_dir, 'train', 'labels')

# Criar as pastas de destino se ainda não existirem
os.makedirs(os.path.join(dest_dir, 'train', 'images'), exist_ok=True)
os.makedirs(os.path.join(dest_dir, 'train', 'labels'), exist_ok=True)

# Função para copiar ficheiros
def copy_files(file_basenames, source_folder, destination_folder, file_extension):
    for basename in file_basenames:
        full_file_name = os.path.join(source_folder, basename + file_extension)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, destination_folder)
        else:
            print(f"Ficheiro não encontrado: {full_file_name}")

# Lista de nomes dos ficheiros das imagens selecionadas aleatoriamente sem extensão
random_file_basenames = random_files_list(image_dir)

# Copiar as imagens e as etiquetas para as diretorias
copy_files(random_file_basenames, image_dir, os.path.join(dest_dir, 'train', 'images'), '.jpg')
copy_files(random_file_basenames, label_dir, os.path.join(dest_dir, 'train', 'labels'), '.txt')

############################################### Conjunto de validação
# conjunto de validação
image_dir = os.path.join(base_dir, 'valid', 'images')
label_dir = os.path.join(base_dir, 'valid', 'labels')

# pastas de destino
os.makedirs(os.path.join(dest_dir, 'valid', 'images'), exist_ok=True)
os.makedirs(os.path.join(dest_dir, 'valid', 'labels'), exist_ok=True)

# lista com os nomes sem extensão dos ficheiros de imagem selecionados aleatoriamente
random_file_basenames = random_files_list(image_dir)

# Copiar os ficheiros das imagens e das etiquetas
copy_files(random_file_basenames, image_dir, os.path.join(dest_dir, 'valid', 'images'), '.jpg')
copy_files(random_file_basenames, label_dir, os.path.join(dest_dir, 'valid', 'labels'), '.txt')

################################################ Conjunto de teste
# pasta 'test'
image_dir = os.path.join(base_dir, 'test', 'images')
label_dir = os.path.join(base_dir, 'test', 'labels')

# criar pastas de destino
os.makedirs(os.path.join(dest_dir, 'test', 'images'), exist_ok=True)
os.makedirs(os.path.join(dest_dir, 'test', 'labels'), exist_ok=True)

# lista com os nomes dos ficheiros das imagens selecionadas aleatoriamente
random_file_basenames = random_files_list(image_dir)

# Copiar os ficheiros das imagens e das etiquetas para as diretorias correspondentes
copy_files(random_file_basenames, image_dir, os.path.join(dest_dir, 'test', 'images'), '.jpg')
copy_files(random_file_basenames, label_dir, os.path.join(dest_dir, 'test', 'labels'), '.txt')

import os

def count_files(directory):
    # Lista com todos os ficheiros da diretoria passada como parâmetro
    files = [file for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]
    return len(files), files

# Diretorias para as imagens e para as etiquetas
images_dir = 'small_dataset/train/images'
labels_dir = 'small_dataset/train/labels'

# Numero de ficheiros em cada diretoria
num_images, image_files = count_files(images_dir)
num_labels, label_files = count_files(labels_dir)

print(num_images)
print(num_labels)

# Diretorias de imagens e etiquetas
images_dir = 'all_images_yolov8__/train/images'
labels_dir = 'all_images_yolov8__/train/labels'

# Numero de ficheiros em cada diretoria
num_images, image_files = count_files(images_dir)
num_labels, label_files = count_files(labels_dir)

print(num_images)
print(num_labels)


########## Validação
images_dir = 'small_dataset/valid/images'
labels_dir = 'small_dataset/valid/labels'

# Numero de ficheiros nas diretorias
num_images, image_files = count_files(images_dir)
num_labels, label_files = count_files(labels_dir)

print(num_images)
print(num_labels)

images_dir = 'all_images_yolov8__/valid/images'
labels_dir = 'all_images_yolov8__/valid/labels'


num_images, image_files = count_files(images_dir)
num_labels, label_files = count_files(labels_dir)

print(num_images)
print(num_labels)


# Teste################################

images_dir = 'small_dataset/test/images'
labels_dir = 'small_dataset/test/labels'

num_images, image_files = count_files(images_dir)
num_labels, label_files = count_files(labels_dir)

print(num_images)
print(num_labels)

images_dir = 'all_images_yolov8__/test/images'
labels_dir = 'all_images_yolov8__/test/labels'

num_images, image_files = count_files(images_dir)
num_labels, label_files = count_files(labels_dir)

print(num_images)
print(num_labels)
