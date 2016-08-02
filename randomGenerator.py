#!/usr/bin/env python
'''
	Generador de cadenas aleatorias al estilo de pattern_create de metasploit
	el primer argumento sera el numero de caracteres
'''

import string
import random
import sys
import time

cadena = ''

def id_generator(size=6, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
	random.seed(time.time())
	return ''.join(random.choice(chars) for _ in range(size))

def hexconverter():
	global cadena
	print '[+] In case you have an error, copy here the hexadecimal number complete (with 0x): '
	resultado = raw_input()

	if '0x' in resultado:
		resultado = resultado.replace('0x','')
	if 'x' in resultado:
		resultado = resultado.replace('x','')

	if len(resultado) == 8:
		cad = resultado
		resultado = cad[6] + cad[7] + cad[4] + cad[5] + cad[2] + cad[3] + cad[0] + cad[1]
	print '[!] String that caused the error: '+resultado.decode("hex")
	resultadoSTR = resultado.decode("hex")
	print '[!] String that caused the error start at: '+str(cadena.find(resultadoSTR)) + ' this is the maximum bytes that accepts buffer'

if __name__ == '__main__':

	if len(sys.argv) != 2:
		print '[-] USAGE: %s SIZE' % (sys.argv[0])
		sys.exit(-1)
	try:
		size = int(sys.argv[1])
	except Exception as e:
		print '[-] ERROR: '+str(e)
		sys.exit(-1)

	cadena = id_generator(size=size)
	print cadena
	hexconverter()

