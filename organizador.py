import os
import shutil

# Caminho da pasta a ser organizada
pasta_a_organizar = "../"  # Substitua com o caminho correto

# Função para organizar arquivos
def organizar():
    # Definir as categorias de arquivos
    categorias = {
        "Imagens": [".jpg", ".png", ".gif", ".jpeg"],
        "Documentos": [".pdf", ".docx", ".txt", ".xls"],
        "vídeos": [".mp4", ".mkv", ".avi"],
    }

    # Verificar se as pastas de categorias existem, se não, criar
    for categoria in categorias.keys():
        categoria_pasta = os.path.join(pasta_a_organizar, categoria)
        if not os.path.exists(categoria_pasta):
            os.makedirs(categoria_pasta)

    # Mover arquivos
    for arquivo in os.listdir(pasta_a_organizar):
        caminho_arquivo = os.path.join(pasta_a_organizar, arquivo)

        if os.path.isfile(caminho_arquivo):
            movido = False
            for categoria, extensoes in categorias.items():
                if any(arquivo.lower().endswith(ext) for ext in extensoes):
                    shutil.move(caminho_arquivo, os.path.join(pasta_a_organizar, categoria, arquivo))
                    movido = True
                    break
            if not movido:
                shutil.move(caminho_arquivo, os.path.join(pasta_a_organizar, "outros", arquivo))

# Executar o organizador
if __name__ == "__main__":
    organizar()
