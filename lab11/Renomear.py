import os 
arquivos = os.listdir()     
caminho = os.getcwd()
for arquivo in arquivos: 
    if arquivo.find(".in") != -1:
        os.rename(caminho + "\\" + arquivo, caminho + "\\" + arquivo.replace(".in", "_in.txt"))
    elif arquivo.find(".out") != -1:
        os.rename(caminho + "\\" + arquivo, caminho + "\\" + arquivo.replace(".out", "_out.txt"))


     
    
