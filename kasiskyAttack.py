#! /usr/bin/python
# -*- coding: utf-8 -*-

from fractions import gcd



alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"


lista_ocurrencias = []

def findsubs(text, l):
	"""
	busca todas las subcadenas de longitud 'l' in 'text'
	"""
	for i in range(len(text)-l):
		subcadena = text[i:i+l]
		found = text[i+l:].find(subcadena)
		if found != -1:
			f = found+i+l
			if i>0 and text[i-1:i+l] == text[f-1:f+l]:
				continue
			if i+l < len(text) and text[i:i+l+1] == text[f:f+l+1]:
				continue            
			print "%-10s %3d " % (subcadena, found+l)
			a = found+l
			lista_ocurrencias.append(a)
			# print lista_ocurrencias[len(lista_ocurrencias)-1]
			#print "%-10s %3d %s" % (subcadena, found+l, str(factor(found+l)))
			   

def ktest(text):
	ctext = ""
	for c in text:
		c = c.upper()
		if c in alphabet:
			ctext += c          

	"""
	el tamaño máximo de una cadena que se puede repetir en el texto tiene 
	de tamaño como máximo la longitud del texto / 2. Empieza desde esa longitud hacia abajo.
	"""
	for l in range(len(text)/2,2,-1):
	    findsubs (ctext, l)    
	mcd = reduce(gcd,lista_ocurrencias)
	print "Posible longitud de la clave = " + str(mcd)
	if mcd ==1:
		print "El programa no es concluyente. De la distancia entre subcadenas repetidas no se puede extraer un tamaño de clave"
		return 0

	"""
	dividir el texto en cadenas  de tamaño MCD
	""" 
	# print "tamaño del texto = " + str(len(ctext))
	i=0
	cadena=[[] for x in range(mcd)] 
	for i in range(0, mcd):
		j=0
		if i == 0:
			for j in range(0,mcd):
				cadena[j].append(ctext[i+j])
				print "cadena[" + str(j) + "]== " + str(cadena[j])
		else:
			for j in range(0,mcd):
				cadena[j].append(ctext[i*mcd+j])
				print "cadena[" + str(j) + "]== " + str(cadena[j])

	
	"""
	contar las letras que más se repiten en cada una de las cadenas
	""" 
	ocurrencias=[[] for x in range(2)] 
	char1=''
	char2=''
	char3=''
	maxocurrencias1=0
	maxocurrencias2=0
	maxocurrencias3=0
	clave1=[]
	clave2=[]
	clave3=[]
	for i in range(0, mcd):
		for c in alphabet:
			ocurrencias = cadena[i].count(c);
			if ocurrencias > maxocurrencias1:
				maxocurrencias1 = ocurrencias
				char1=c
			elif ocurrencias > maxocurrencias2:
				maxocurrencias2 = ocurrencias
				char2=c
			elif ocurrencias > maxocurrencias3:
				maxocurrencias3 = ocurrencias
				char3=c
		print "1º caracter mas repetido de cadena[" + str(i) + "] = " + char1 + " -> " + str(maxocurrencias1) + " veces"
		print "2º caracter mas repetido de cadena[" + str(i) + "] = " + char2 + " -> " + str(maxocurrencias2) + " veces"
		print "3º caracter mas repetido de cadena[" + str(i) + "] = " + char3 + " -> " + str(maxocurrencias3) + " veces"
		print ""
		clave1.append(char1)
		clave2.append(char2)
		clave3.append(char3)
		char1=''
		char2=''
		char3=''
		maxocurrencias1=0
		maxocurrencias2=0
		maxocurrencias3=0

	"""
	imprimir las claves
	""" 
	for i in range(len(clave1)):
		print clave1[i]+ "     " + clave2[i] + "     " + clave3[i]

if __name__ == "__main__":
    def main():
        while True:
            text = raw_input ("Introducir el texto cifrado: \n")
            if len(text) == 0:
                break
            ktest(text)
    main()







# *************************************CADENA DE EJEMPLO AQUÍ*************************************
# PPQCAXQVEKGYBNKMAZUYBNGBALJONITSZMJYIMVRAGVOHTVRAUCTKSGDDWUOXITLAZUVAVVRAZCVKBQPIWPOU
# PPQCAXQV EKGYBNKM AZUYBNGB ALJONITS ZMJYIMVR AGVOHTVR AUCTKSGD DWUOXITL AZUVAVVR AZCVKBQP IWPOU


