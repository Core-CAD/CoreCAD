import os

# Conteúdo SVG totalmente preto (256x256 px)
SVG_PRETO = '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="256" height="256" viewBox="0 0 256 256">
    <rect width="256" height="256" fill="#000000"/>
</svg>'''

# Tenta usar a biblioteca PIL (Pillow) para gerar PNGs/ICOs pretos em alta resolução
try:
    from PIL import Image
    HAS_PIL = True
except ImportError:
    HAS_PIL = False

# Byte estático para PNG 100% preto caso o PIL não esteja instalado
PNG_1X1_BLACK = (
    b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x00\x00\x00\x003a\x7f\xca'
    b'\x00\x00\x00\nIDATx\x9cc`\x00\x00\x00\x02\x00\x01H\xaf\xa4q\x00\x00\x00\x00IEND\xaeB`\x82'
)

def criar_imagem_preta(caminho_arquivo):
    extensao = os.path.splitext(caminho_arquivo)[1].lower()
    
    if extensao == '.svg':
        with open(caminho_arquivo, 'w', encoding='utf-8') as f:
            f.write(SVG_PRETO)
    elif extensao in ['.png', '.ico', '.xpm', '.bmp']:
        if HAS_PIL:
            img = Image.new('RGB', (256, 256), color='black')
            img.save(caminho_arquivo)
        else:
            with open(caminho_arquivo, 'wb') as f:
                f.write(PNG_1X1_BLACK)

def varrer_e_substituir(diretorio_raiz):
    substituidos = 0
    # Termos usados nos nomes dos arquivos de logos e telas do FreeCAD
    termos_alvo = ['freecad', 'logo', 'splash', 'brand', 'about', 'app-icon']

    print(f"Iniciando varredura em: {diretorio_raiz}...\n")

    for pasta_atual, subpastas, arquivos in os.walk(diretorio_raiz):
        # Ignora totalmente a pasta do Git para não quebrar o histórico
        if '.git' in pasta_atual:
            continue

        for arquivo in arquivos:
            nome_minusculo = arquivo.lower()
            extensao = os.path.splitext(nome_minusculo)[1]

            if extensao in ['.svg', '.png', '.ico', '.xpm', '.bmp']:
                # Verifica se o nome do arquivo contém algum termo de logo/branding
                if any(termo in nome_minusculo for termo in termos_alvo):
                    caminho_completo = os.path.join(pasta_atual, arquivo)
                    try:
                        criar_imagem_preta(caminho_completo)
                        print(f"[OK] Substituído por preto: {arquivo}")
                        substituidos += 1
                    except Exception as e:
                        print(f"[ERRO] Falha ao substituir {arquivo}: {e}")

    print(f"\nConcluído! Total de {substituidos} arquivos de imagens substituídos por telas/ícones pretos.")

if __name__ == "__main__":
    diretorio_projeto = os.path.dirname(os.path.abspath(__file__))
    varrer_e_substituir(diretorio_projeto)