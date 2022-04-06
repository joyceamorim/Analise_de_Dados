import re
import csv

with open(file='D:\Curso EBAC\Leitura de Arquivos\Extrair_Email_Regex/nubank.txt', mode= 'r', encoding= 'utf8') as arquivo:
    texto = arquivo.read()

emails_extraidos = re.findall('\S+@\S+', texto)
print(emails_extraidos)


with open(file='D:\Curso EBAC\Leitura de Arquivos\Extrair_Email_Regex/email_nubank.csv', mode='w', encoding= 'utf8') as arquivo:
    escritor_csv = csv.writer(arquivo, delimiter=',')
    escritor_csv.writerow(list(map(lambda email_extraido: [email_extraido], emails_extraidos)))