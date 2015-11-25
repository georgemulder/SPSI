#! /usr/bin/python
# -*- coding: utf-8 -*-

from fractions import gcd
import sys
import collections


# alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
alphabet = "ABCDEFGHIJKLMNNOPQRSTUVWXYZ"





"""
    busca todas las subcadenas de longitud 'l' en 'text'
    modifica la variable global lista_ocurrencias, añadiendo la distancia entre dichas repeticiones.
"""
def findsubs(text, l, lista_ocurrencias):
    for i in range(len(text)-l):
        subcadena = text[i:i+l]
        found = text[i+l:].find(subcadena)
        if found != -1 and len(subcadena)<4:
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
    
"""
excluye caracteres de text que no estan en el alfabeto alphabet
"""            
def filter(text):
    ctext = ""
    for c in text:
        c = c.upper()
        if c in alphabet:
            ctext += c
    return ctext

def imprime(cadena):
    for i in range(len(cadena)):
        sys.stdout.write(cadena[i])
    print("")

def ktest(text):
    lista_ocurrencias = []
    ctext = filter(text)        

    """
    el tamaño máximo de una cadena que se puede repetir en el texto tiene 
    de tamaño como máximo la longitud del texto / 2. Empieza desde esa longitud hacia abajo.
    """
    for l in range(len(text)/2,2,-1):
        findsubs (ctext, l, lista_ocurrencias)
    
    mcd = reduce(gcd,lista_ocurrencias) #cálculo del máximo común divisor
    print "Posible longitud de la clave = " + str(mcd)
    if mcd ==1:
        print "El programa no es concluyente. De la distancia entre subcadenas repetidas no se puede extraer un tamaño de clave"
        return 0
    print ""

    """
    dividir el texto en x cadenas, siendo x el mcd
    """ 
    i=0
    cadena=[[] for x in range(mcd)]  
    end = False
    for i in range(0, (len(ctext)/mcd)):
        j=0
        if i == 0:
            for j in range(0,mcd):
                cadena[j].append(ctext[j])
        else:
            for j in range(0,mcd):
                if i*mcd+j<len(ctext):
                    cadena[j].append(ctext[i*mcd+j])
                    
    for i in range(len(cadena)):
        sys.stdout.write("cadena[" + str(i) + "]== ")
        for j in range(len(cadena[i])):
            sys.stdout.write(cadena[i][j])
        print ""
    print ""

    """
    contar las letras que más se repiten en cada una de las cadenas
    """ 
    ocurrencias=0
    char1=''
    char2=''
    char3=''
    maxocurrencias1=0
    maxocurrencias2=0
    maxocurrencias3=0
    clave1=[]
    clave2=[]
    clave3=[]
    letra1=""
    letra2=""
    letra3=""

    vocurrencias=[[] for x in range(mcd)] #ocurrencias de cada caracter c en cada subcadena 
    for i in range(0, mcd):
        for c in alphabet:
            ocurrencias = cadena[i].count(c);
            vocurrencias[i].append(ocurrencias)
            # if ocurrencias > maxocurrencias1:
            #   if maxocurrencias1 > maxocurrencias2:
            #       if maxocurrencias2 > maxocurrencias3:
            #           maxocurrencias3 = maxocurrencias2
            #           char3 = char2
            #           maxocurrencias2 = maxocurrencias1
            #           char2 = char1
            #   maxocurrencias1 = ocurrencias
            #   char1=c
            # elif ocurrencias > maxocurrencias2:
            #   if maxocurrencias2 > maxocurrencias3:
            #       maxocurrencias3 = maxocurrencias2
            #       char3 = char2
            #   maxocurrencias2 = ocurrencias
            #   char2=c
            # elif ocurrencias > maxocurrencias3:
            #   maxocurrencias3 = ocurrencias
            #   char3=c

        # print "1º caracter mas repetido de cadena[" + str(i) + "] = " + char1 + " -> " + str(maxocurrencias1) + " veces"
        # print "2º caracter mas repetido de cadena[" + str(i) + "] = " + char2 + " -> " + str(maxocurrencias2) + " veces"
        # print "3º caracter mas repetido de cadena[" + str(i) + "] = " + char3 + " -> " + str(maxocurrencias3) + " veces"
        # clave1.append(char1)
        # clave2.append(char2)
        # clave3.append(char3)
        # char1 = ''
        # char2 = ''
        # char3 = ''
        # maxocurrencias1 = 0
        # maxocurrencias2 = 0
        # maxocurrencias3 = 0
        maximo=0
        letra1=""
        letra2=""
        letra3=""
        maxocurrencias1=0
        maxocurrencias2=0
        for k in range(0, len(alphabet)):
            # print vocurrencias[i][k]
            cantidad = vocurrencias[i][k%len(alphabet)];
            cantidad +=vocurrencias[i][(k+4)%len(alphabet)]
            cantidad +=vocurrencias[i][(k+15)%len(alphabet)]
            # sys.stdout.write("¿¿¿" + str(cantidad) + "mayor que " + str(maximo) + "??? ")
            if cantidad > maximo:
                # print "si"
                maximo=cantidad
                letra1=alphabet[k]
                letra2=alphabet[(k+4)%len(alphabet)]
                letra3=alphabet[(k+15)%len(alphabet)]
            # else:
                # print "no"
        # print "0 + 4 + 15"
        print letra1
        print letra2
        print letra3        






        """
        Cálculo del íncide de coincidencia
        """
        N = len(cadena[i])
        freqs = collections.Counter( cadena[i] )
        freqsum = 0.0

        for letter in alphabet:
            freqsum += freqs[ letter ] * ( freqs[ letter ] - 1 )

        IC = freqsum / (N*(N-1))

        print "Indice de coincidencia de cadena[" + str(i) + "] %.3f" % IC, "({})".format( IC )
        print ""

    """
    imprimir las claves
    """ 
    sys.stdout.write("CLAVE 1 = ")
    imprime(letra1)
    sys.stdout.write("CLAVE 2 = ")
    imprime(letra2)
    sys.stdout.write("CLAVE 3 = ")
    imprime(letra3)

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


