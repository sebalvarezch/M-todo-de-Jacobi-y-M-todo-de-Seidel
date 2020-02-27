#Cálculo Numérico. Universidad José Antonio Páez
#Sebastián Álvarez, C.I: 26.900.740
import os
import decimal
import numpy
 
def Jacobi():
	
	def Xval(a1, b1, c1, d1, y, z):  #
	    x = ((-(b1*y)-(c1*z)+d1)/a1)   #
	    return x                     #
	                                 #
	def Yval(a2, b2, c2, d2, x, z):  # Formulas para recursividad
	    y = (-(a2*x)-(c2*z)+d2)/b2   #
	    return y                     #
	                                 #
	def Zval(a3, b3, c3, d3, x, y):  #
	    z = (-(a3*x)-(b3*y)+d3)/c3   #
	    return z                     #
	 
	def main():
	    os.system("cls")
	    vals = [[0.0,0.0,0.0],[1.0,1.0,1.0]]
	    cons = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
	    loop_val = 0
	    print("\n    METODO DE JACOBI\n\nA1x + B1y + C1z = D1\n\
	A2x + B2y + C2z = D2\nA3x + B3y + C3z = D3\n\n")
	    cons[0][0] = float(input("\nIngrese A1 > "))   # Constantes para ecuacion 1
	    cons[0][1] = float(input("Ingrese B1 > "))
	    cons[0][2] = float(input("Ingrese C1 > "))
	    cons[0][3] = float(input("Ingrese D1 > "))
	    cons[1][0] = float(input("\nIngrese A2 > "))   # Constantes para ecuacion 2
	    cons[1][1] = float(input("Ingrese B2 > "))
	    cons[1][2] = float(input("Ingrese C2 > "))
	    cons[1][3] = float(input("Ingrese D2 > "))
	    cons[2][0] = float(input("\nIngrese A3 > "))   # Constantes para ecuacion 3
	    cons[2][1] = float(input("Ingrese B3 > "))
	    cons[2][2] = float(input("Ingrese C3 > "))
	    cons[2][3] = float(input("Ingrese D3 > "))
	    os.system("cls")
	    print("Calculando...")
	    while(vals[0] != vals [1]):
	        print(vals[0])
	        vals[1][0] = Xval(cons[0][0], cons[0][1], cons[0][2], cons[0][3],\
	vals[0][1], vals[0][2])
	        vals[1][1] = Yval(cons[1][0], cons[1][1], cons[1][2], cons[1][3],\
	vals[0][0], vals[0][2])
	        vals[1][2] = Zval(cons[2][0], cons[2][1], cons[2][2], cons[2][3],\
	vals[0][0], vals[0][1])
	        print(vals[1])
	        vals[0][0] = Xval(cons[0][0], cons[0][1], cons[0][2], cons[0][3],\
	vals[1][1], vals[1][2])
	        vals[0][1] = Yval(cons[1][0], cons[1][1], cons[1][2], cons[1][3],\
	vals[1][0], vals[1][2])
	        vals[0][2] = Zval(cons[2][0], cons[2][1], cons[2][2], cons[2][3],\
	vals[1][0], vals[1][1])
	 
	    raw_input("\n\nMetodo de Jacobi terminado...")
	 
	main()
	exit()

def Seidel():
	m=int(input('Valor de m:'))
	n=int(input('Valor de n:'))
	matrix = numpy.zeros((m,n))
	x=numpy.zeros((m))

	vector=numpy.zeros((n))
	comp=numpy.zeros((m))
	error=[]

	print ('Método de Gauss-Seidel')
	print ('Introduce la matriz de coeficientes y el vector solución')
	for r in range(0,m):
	    for c in range(0,n):
	        matrix[(r),(c)]=float(input("Elemento a["+str(r+1)+str(c+1)+"] "))
	    vector[(r)]=float(input('b['+str(r+1)+']: '))
	tol=float(input("¿Cual es la tolerancia que deseas? "))
	itera=int(input("¿Cual es el numero maxìmo de iteraciones? "))        
	print ("Método de Gauss-Seidel")

	k=0
	while k < itera:
	    suma=0
	    k=k+1
	    for r in range(0,m):
	        suma=0
	        for c in range(0,n):
	            if (c != r):
	                suma=suma+matrix[r,c]*x[c]               
	        x[r]=(vector[r]-suma)/matrix[r,r]
	        print("x["+str(r)+"]: "+str(x[r]))
	        error[:]    
	    #Comprobación
	for r in range(0,m):
	        suma=0
	        for c in range(0,n):
	            suma=suma+matrix[r,c]*x[c]
	            comp[r]=suma
	            dif=abs(comp[r]-vector[r])
	            error.append(dif)
	            print("Error en x[",r,"]=",error[r])
	        print("iteraciones: " ,k)
	        if all( i<=tol for i in error) == True:
	         break
	        

while True:
	try:
		print("Bienvenido al Algoritmo del Método de Jacobi y el método de Seidel, elaborado por Sebastián Álvarez, C.I: 26.900.740\nCálculo Numérico, Universidad José Antonio Paéz. \nPara resolver el Método de Jacobi, ingrese 1. \nPara resolver el Método de Seidell, ingrese 2")
		valor = int(input("Ingrese el valor: "))
		if valor == 1:
			print("Ha seleccionado resolver el Método de Jacobi. \nRecuerde que debe ser una matriz 3x3 cuya diagonal sea estrictamente dominante.")
			Jacobi()
			print("Fin del programa.")
			break
		elif valor == 2:
			print("Ha seleccionado resolver el Método de Seidel")
			Seidel()
			print("Fin del programa.")
			break
		else:
			print("Valor no válido, intente nuevamente ingresando '1' ó '2'\n")
	except ValueError:
		print("Valor ingresado es inválido. Intente nuevamente. . .\n")

