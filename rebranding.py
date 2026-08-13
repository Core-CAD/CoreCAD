import os
import shutil
import base64

# 1. Cria um arquivo SVG (Vetor) 100% preto
black_svg = '<svg xmlns="http://www.w3.org/2000/svg" width="128" height="128"><rect width="100%" height="100%" fill="black"/></svg>'
with open("black_temp.svg", "w") as f:
    f.write(black_svg)

# 2. Cria um arquivo PNG (Pixel) 100% preto usando código Base64 (sem precisar baixar nada)
black_png_b64 = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII="
with open("black_temp.png", "wb") as f:
    f.write(base64.b64decode(black_png_b64))

# 3. Palavras-chave que indicam logos e splash screens
alvos = ['freecad.svg', 'freecad.png', 'splash', 'logo', 'background']

contador = 0

# 4. Varre todas as pastas dentro de 'src' (onde fica o código)
print("Iniciando a busca por ícones...")
for root, dirs, files in os.walk('src'):
    for file in files:
        nome_min = file.lower()
        
        # Se o nome do arquivo contém alguma das palavras-chave
        if any(alvo in nome_min for alvo in alvos):
            caminho_completo = os.path.join(root, file)
            
            # Substitui por preto se for SVG
            if nome_min.endswith('.svg'):
                shutil.copy("black_temp.svg", caminho_completo)
                print(f"✅ Substituído (SVG): {file}")
                contador += 1
                
            # Substitui por preto se for PNG
            elif nome_min.endswith('.png'):
                shutil.copy("black_temp.png", caminho_completo)
                print(f"✅ Substituído (PNG): {file}")
                contador += 1

# 5. Limpa os arquivos temporários criados
os.remove("black_temp.svg")
os.remove("black_temp.png")

print(f"\n🚀 Sucesso! {contador} imagens do FreeCAD foram transformadas em um quadrado preto.")