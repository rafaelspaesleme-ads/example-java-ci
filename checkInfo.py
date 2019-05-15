import subprocess
import datetime
import os

print "------------------------------------------------------------------"
print "=================================================================="
print "                       EXEMPLO EM PYTHON                          "
print "=================================================================="
print "------------------------------------------------------------------"

currentDateTime = datetime.datetime.strftime(datetime.datetime.now(), '%d/%m/%Y %H:%M:%S')
print "\nData e hora local: " + currentDateTime + "\n\n"

print ">> Lendo arquivo info.txt ..."
f = open("info.txt",'r')
content = f.read()
print ">> Conteudo lido: \n\n"
print content + "\n\n"
f.close()

print ">> Obtendo informacoes sobre o versionamento do arquivo ...\n\n"
