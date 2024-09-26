conver_leroy.py -> contém o pré-processamento das imagens, antes da importação para o Roboflow
novo_dataset_mais_pequeno.py -> contém o processo da diminuição do volume de dados, para a criação de um dataset mais pequeno small_dataset_2, que possui 40% das imagens
text_list_manipulation_1.py; ocr_manipulation.py; excel_json_manipulation_1.py; divide_info.py; coor_manipulation.py -> ficheiros que contêm algumas funções necessárias à implementação da metodologia
metodologia_ocr_aplicado_1_vez.py -> metodologia com uma única utilização única do OCR do Azure, implementada para 1 imagem
metodologia_com_aplicacao_de_ocr_2_vezes.py -> metodologia com duas utilizações do OCR do Azure, implementada para 1 imagem
yolov9_table_detection_.ipynb -> contém o treino do modelo YOLOv9 para a deteção das tabelas, realizado com a máquina virtual com GPU
treino_dos_modelos_com_maquina_virtual.ipynb -> contém o treino dos modelos YOLOv8 de deteção de tabelas por 250 épocas, YOLOv8 deteção de cabeçalhos por 200 épocas e YOLOv8 de deteção da altura das linhas da tabela por 250 épocas
