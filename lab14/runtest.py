import os
import sys
import time
start_time = time.time()

if len(sys.argv) < 2 :
    print("Uso: py runtest.py labXX.py")
    sys.exit()

labfile = sys.argv[1]
if not os.path.exists(labfile) :
    print("Arquivo ", labfile, "não encontrado.")
    sys.exit()
    
i = "1"
testfile = "arq" + "0" + str(i) +"_in.txt"

os.chdir(os.path.dirname(os.path.abspath(__file__)) + "\\")

while (os.path.exists(testfile)) :
    if int(i) < 10:
        i = "0" + str(i)
    resfile = "arq" + str(i) +"_out.txt"
    if not os.path.exists(resfile) :
      print("Arquivo", resfile, "não encontrado.")
      sys.exit()
      
    outfile = "arq" + str(i) +"_res.txt"
    if (os.path.exists(outfile)) :
       answer = input("Arquivo " + outfile + " existente. Pode ser sobrescrito (S/n) ?")
       if answer == "n" or answer == "N" :
         sys.exit()
         
    difffile = "arq" + str(i) +"_diff.txt"
    if (os.path.exists(difffile)) :
       answer = input("Arquivo " + difffile + " existente. Pode ser sobrescrito (S/n) ?")
       if answer == "n" or answer == "N" :
         sys.exit()
         
    os.system("py " + labfile + " < " + testfile + " > " + outfile)
    if os.system("FC " + outfile + " " + resfile + " > " + difffile) == 0 :
       print("Teste ", str(i), ": resultado correto")
    else: 
      print("Teste ", str(i), ": resultado incorreto\n")
      os.system("type " + difffile)
    os.remove(outfile)      
    os.remove(difffile)
    i = int(i) + 1
    if i < 10:
        testfile = "arq" + "0" + str(i) +"_in.txt"
    else:
        testfile = "arq" + str(i) +"_in.txt"

print("--- %s seconds ---" % (time.time() - start_time))
