import math as mt

def menu():
  menu='''
-----------------------------------------
|                Menú                   |
|                                       |
|  1. Aproximar Nueva Longitud de Arco  |
|  2. Finalizar Programa                |
-----------------------------------------
  '''
  print(menu)

msj1='''
Bienvenido

El objetivo de este programa es aproximar la longitud de la traza entre el cilindro x^2 + y^2 = a^2, a > 0, y el plano x + y + 2z = 8 mediante una Suma de Riemman.'''

print(msj1)
opcion=''

while opcion != '2':
  
  menu()
  opcion=input('Seleccione una opción: ')
  
  if opcion not in ['1','2']:
    
    print('\n- Ingreso inválido -')
    
  elif opcion == '1':

    print('')
    a='' #Radio
    n='' #Sub-Intervalos
    validador1=True
    validador2=True
    
    while validador1:
      a=input("Ingrese el valor del radio 'a' (cm): ")
      if a.count('.') == 0 or a.count('.') == 1:
        aCopy=a.replace('.','')
        if aCopy.isdigit() and aCopy != '0':
            validador1=False
    a=float(a)
    
    while validador2:
      n=input('Ingrese la cantidad de sub-intervalos: ')
      if n.isdigit() and n != '0':
        validador2=False
    n=int(n)
    
    i=1
    sumatoria=0
    
    while i<=n:
        funcionSumando=mt.sqrt(5-mt.sin(((4*mt.pi)/n)*i))
        sumatoria+=funcionSumando
        i+=1
      
    longitudDeArco=((a*mt.pi)/n)*sumatoria
    msj2=f'Longitud de Arco: {round(longitudDeArco,4)} (cm)'
    print(msj2)