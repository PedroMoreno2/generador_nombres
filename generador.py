# creo el archivo donde voy a meter los nombres:
try:
  gene=open("gene_nombres.txt","x")
except FileExistsError:
  print("el fichero existe todo ok")
gene=open("gene_nombres.txt","w")
gene.write("Esto es una lista de nombres:")
gene.close()
gene=open("gene_nombres.txt")
print(gene.read())
gene.close()
# Ahora a meterle los nombres, primero una string con los nombres:
nombres_str="Paco Pedro Juan Marta Estrella Inma Sogo Tera Piña Aloa"
# Voy a meter la string pero en líneas diferentes, primero la convierto en una lista con el método split:
nombres_lis=nombres_str.split(" ")
#print(nombres_lis)
gene=open("gene_nombres.txt","a")
for nom in nombres_lis:
  gene.write("\n"+nom)
gene.close()
gene=open("gene_nombres.txt")
print(gene.read())
gene.close()
# Ahora la pregunta para que te de un nombre aleatorio:
import random
gene=open("gene_nombres.txt")
gene_lis=gene.readlines()
print(gene_lis)
input("¿Quieres un nombre aleatorio? Pulsa una tecla")
r=random.choice(gene_lis)
# Cuidao que me saca como nombre el "esto es una lista de nombres"...
h=gene_lis.index(r)
if h!=0:
  print(r, "es el nombre que te ha tocado")
else:
  print("Tu nombre es nadie")
gene.close()
# Parece que al convertir el texto en cadena se ha guardado
# el salto de linea, está bien saberlo.

