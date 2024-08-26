 from PIL import Image
import os

def pngs_to_pdfs(pasta_imagens, pasta_pdf_saida):
    
    if not os.path.exists(pasta_pdf_saida):
        os.makedirs(pasta_pdf_saida)

    
    for arquivo in os.listdir(pasta_imagens):
        
        if arquivo.endswith('.png'):
            caminho_completo = os.path.join(pasta_imagens, arquivo)
            
            img = Image.open(caminho_completo)
            
            img_rgb = img.convert('RGB')
            
            nome_pdf = os.path.splitext(arquivo)[0] + '.pdf'
            caminho_pdf_saida = os.path.join(pasta_pdf_saida, nome_pdf)
            
            img_rgb.save(caminho_pdf_saida)


pasta_imagens = r'C:\Users\Desktop\PNG2PDF Converte\img'  
pasta_pdf_saida = r'C:\Users\Desktop\PNG2PDF Converte\pdf'  

pngs_to_pdfs(pasta_imagens, pasta_pdf_saida)
