import os
import zipfile

# Ask the user to input the path to the ZIP file
path = input("Enter the path where your file at: ")

# Get the archive file name
listaArquivos = []

#verify what files are in the directory
for meta_file in os.listdir(path):
    listaArquivos.append(meta_file) 
    
#Creating a dictionary for all the files in the directory    
contador = 0
dicionarioArquivos = {}

for arquivo in listaArquivos:
    dicionarioArquivos[arquivo] = contador 
    contador += 1

#select one of the files in the directory

for arquivo in dicionarioArquivos:
    if dicionarioArquivos[arquivo] == 1:
        selectedFile = arquivo  

# Abre o arquivo zip em modo de leitura
with zipfile.ZipFile(path, 'r') as zip_ref:
    # Lê o conteúdo do arquivo dentro do zip
    conteudo_arquivo = zip_ref.read(selectedFile)

    # Agora, você pode manipular o conteúdo do arquivo como desejar
    print(conteudo_arquivo.decode('utf-8'))  # Decodifica o conteúdo em UTF-8 (ou outro encoding, se aplicável)
    

exit()
    
def extract_entity_name(filename):
    return filename.split('.')[0]
    
extract_entity_name('Licitacao.txt')
