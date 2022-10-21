<<<<<<< HEAD
=======
import random
import time
import sys
print('\n')
print('Bienvenido al juego "Piedra, papel, tijeras, lagarto ó Spock"')
print('\n')
bienvenida='''Deberás elegir una de las 5 opciones para jugar contra la máquina. ¡Qué la suerte esté de tu lado!\n
Reglas del juego:'''



def mensaje_con_delay(mensaje, delay_mensaje=0.15, delay_post=0.01):
    for char in mensaje:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay_mensaje)

    time.sleep(delay_post)
    
mensaje_con_delay(bienvenida)   
    

print('\n')
import IPython.display as display
from PIL import Image
display.display(Image.open(r"instrucciones.png"))
print('\n')
user_wins=0
machine_wins=0

options=['piedra','papel','tijeras','lagarto','spock']

while True:
    user_input=input("Selecciona y escribe una de las siguientes opciones piedra/papel/tijeras/lagarto/spock \n ó S para salir del juego: ").lower()
    print('\n')
    if user_input=="s":
        break
    
    if user_input not in options:
        print("\x1b[1;33m"+'Recuerda que éstas son las opciones: '+", ".join(options)+"."+u'\u001b[0m'+'\n')
        print('\n')
        display.display(Image.open(r"error.jpeg"))
        print('\n')
        continue
        
    random_number=random.randint(0,4)
    
    #piedra:0, papel:1, tijeras:2, lagarto:3, spock:4
    
    machine_pick=options[random_number]
    print("La máquina ha elegido",machine_pick+".")
    
    #Escenario de empate en el juego
    
    if user_input==machine_pick:
        print('\u001b[33m'+"Es un empate, ninguno suma puntos."+ u'\u001b[0m'+'\n')
    
    #Escenarios donde gana el usuario
    
    elif user_input=='piedra' and machine_pick=='tijeras':
        print(u'\u001b[38;5;84m'+ '¡Ganaste! Sumas un punto. Piedra aplasta tijeras.'+ u'\u001b[0m'+'\n')
        user_wins+=1
        
    elif user_input=='piedra' and machine_pick=='lagarto':
        print(u'\u001b[38;5;84m'+'¡Ganaste! Sumas un punto. Piedra machaca lagarto.'+ u'\u001b[0m'+'\n')
        user_wins+=1
    
    elif user_input=='papel' and machine_pick=='piedra':
        print(u'\u001b[38;5;84m'+'¡Ganaste! Sumas un punto. Papel envuelve a la piedra.'+ u'\u001b[0m'+'\n')
        user_wins+=1
        
    elif user_input=='papel' and machine_pick=='spock':
        print(u'\u001b[38;5;84m'+'¡Ganaste! Sumas un punto. Papel desautoriza a Spock.'+ u'\u001b[0m'+'\n')
        user_wins+=1
    
    elif user_input=='tijeras' and machine_pick=='papel':
        print(u'\u001b[38;5;84m'+'¡Ganaste! Sumas un punto. Las tijeras corta al papel.'+ u'\u001b[0m'+'\n')
        user_wins+=1
        
    elif user_input=='tijeras' and machine_pick=='lagarto':
        print(u'\u001b[38;5;84m'+'¡Ganaste! Sumas un punto. Las tijeras decapita a lagarto.'+ u'\u001b[0m'+'\n')
        user_wins+=1
        
    elif user_input=='lagarto' and machine_pick=='spock':
        print(u'\u001b[38;5;84m'+'¡Ganaste! Sumas un punto. Lagarto envenena a Spock.'+ u'\u001b[0m'+'\n')
        user_wins+=1
        
    elif user_input=='lagarto' and machine_pick=='papel':
        print(u'\u001b[38;5;84m'+'¡Ganaste! Sumas un punto. Lagarto se come el papel.'+ u'\u001b[0m'+'\n')
        user_wins+=1
        
    elif user_input=='spock' and machine_pick=='tijeras':
        print(u'\u001b[38;5;84m'+'¡Ganaste! Sumas un punto. Spock rompe las tijeras.'+ u'\u001b[0m'+'\n')
        user_wins+=1
        
    elif user_input=='spock' and machine_pick=='piedra':
        print(u'\u001b[38;5;84m''¡Ganaste! Sumas un punto. Spock vaporiza a la piedra.'+ u'\u001b[0m'+'\n')
        user_wins+=1
    
    #Escenarios donde gana la maquina contra el usuario
    
    elif machine_pick=='piedra' and user_input=='tijeras':
        print(u'\u001b[91m'+'¡Perdiste! Máquina suma un punto. Piedra aplasta tijeras.'+ u'\u001b[0m'+'\n')
        machine_wins+=1
        
    elif machine_pick=='piedra' and user_input=='lagarto':
        print(u'\u001b[91m'+'¡Perdiste! Máquina suma un punto. Piedra machaca lagarto.'+ u'\u001b[0m'+'\n')
        machine_wins+=1
    
    elif machine_pick=='papel' and user_input=='piedra':
        print(u'\u001b[91m'+'¡Perdiste! Máquina suma un punto. Papel envuelve a la piedra.'+ u'\u001b[0m'+'\n')
        machine_wins+=1
        
    elif machine_pick=='papel' and user_input=='spock':
        print(u'\u001b[91m'+'¡Perdiste! Máquina gana un punto. Papel desautoriza a Spock.'+ u'\u001b[0m'+'\n')
        machine_wins+=1
    
    elif machine_pick=='tijeras' and user_input=='papel':
        print(u'\u001b[91m'+'¡Perdiste! Máquina gana un punto. Las tijeras cortan al papel.'+ u'\u001b[0m'+'\n')
        machine_wins+=1
        
    elif machine_pick=='tijeras' and user_input=='lagarto':
        print(u'\u001b[91m'+'¡Perdiste! Máquina gana un punto. Las tijeras decapitan a lagarto.'+ u'\u001b[0m'+'\n')
        machine_wins+=1
        
    elif machine_pick=='lagarto' and user_input=='spock':
        print(u'\u001b[91m'+'¡Perdiste! Máquina gana un punto. Lagarto envenena a Spock.'+u'\u001b[0m'+'\n')
        machine_wins+=1
        
    elif machine_pick=='lagarto' and user_input=='papel':
        print(u'\u001b[91m'+'¡Perdiste! Máquina gana un punto. Lagarto se come el papel.'+ u'\u001b[0m'+'\n')
        machine_wins+=1
        
    elif machine_pick=='spock' and user_input=='tijeras':
        print(u'\u001b[91m'+'¡Perdiste! Máquina gana un punto. Spock rompe las tijeras.'+ u'\u001b[0m'+'\n')
        machine_wins+=1
        
    elif machine_pick=='spock' and user_input=='piedra':
        print(u'\u001b[91m'+'¡Perdiste! Máquina gana un punto. Spock vaporiza a la piedra.'+ u'\u001b[0m'+'\n')
        machine_wins+=1
        

if user_wins>machine_wins:
    print('\u001b[38;5;84m''Has ganado contra la máquina ¡Felicidades!'+ u'\u001b[0m')
    print('\n')
    display.display(Image.open(r"feliz.png"))
    print('\n')
    
elif user_wins==0 and machine_wins==0:
    print('\u001b[33m'+'Nadie ganó en esta partida'+u'\u001b[0m')
    print('\n')
    display.display(Image.open(r"empate.jpeg"))
    print('\n')
elif user_wins==machine_wins:
    print('\u001b[33m'+'La máquina y tú han empatado'+ u'\u001b[0m')
    print('\n')
    
else:
    print(u'\u001b[91m'+'Has perdido contra la máquina ¡Suerte para la próxima!'+ u'\u001b[0m')
    print('\n')
    display.display(Image.open(r"loser.png"))
    print('\n')
print('Puntuación final:')
print('Usuario ganó',user_wins,'veces.')
print('Maquina ganó',machine_wins,'veces.')
>>>>>>> 77de5a00445242d2670e2e4ec20912e1d1d13c7c

    