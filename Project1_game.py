import random

print('Bienvenido al juego "Piedra, papel, tijeras, lagarto o Spock"\n')
print('Deberás elegir una de las 5 opciones para jugar contra la maquina, Qué la suerte esté de tu lado.\n')
print('Reglas del juego:\n')
print('*Piedra aplasta tijeras')
print('*Las tijeras cortan el papel')
print('*El papel envuelve a la piedra')
print('*La piedra machaca al lagarto')
print('*El lagarto envenena a spock')
print('*Spock rompe tijeras')
print('*Las tijeras decapitan al lagarto')
print('*El lagarto se come el papel')
print('*El papel desautoriza a spock')
print('*Spock vaporiza la piedra \n')

user_wins=0
machine_wins=0

options=['piedra','papel','tijeras','lagarto','spock']

while True:
    user_input=input("Selecciona y escribe una de las siguientes opciones piedra/papel/tijeras/lagarto/spock \n o S para salir del juego: ").lower()
    if user_input=="s":
        break
    
    if user_input not in options:
        print('Recuerda que estas son las opciones: '+", ".join(options)+".")
        continue
        
    random_number=random.randint(0,4)
    
    #piedra:0, papel:1, tijeras:2, lagarto:3, spock:4
    
    machine_pick=options[random_number]
    print("La maquina ha elegido",machine_pick+".")
    
    #Escenario de empate en el juego
    
    if user_input==machine_pick:
        print("Es un empate, ninguno suma puntos.")
    
    #Escenarios donde gana el usuario
    
    elif user_input=='piedra' and machine_pick=='tijeras':
        print('¡Ganaste! Sumas un punto. Piedra aplasta tijeras.')
        user_wins+=1
        
    elif user_input=='piedra' and machine_pick=='lagarto':
        print('¡Ganaste! Sumas un punto. Piedra machaca lagarto.')
        user_wins+=1
    
    elif user_input=='papel' and machine_pick=='piedra':
        print('¡Ganaste! Sumas un punto. Papel envuelve a la piedra.')
        user_wins+=1
        
    elif user_input=='papel' and machine_pick=='spock':
        print('¡Ganaste! Sumas un punto. Papel desautoriza a Spock.')
        user_wins+=1
    
    elif user_input=='tijeras' and machine_pick=='papel':
        print('¡Ganaste! Sumas un punto. Las tijeras corta al papel.')
        user_wins+=1
        
    elif user_input=='tijeras' and machine_pick=='lagarto':
        print('¡Ganaste! Sumas un punto. Las tijeras decapita a lagarto.')
        user_wins+=1
        
    elif user_input=='lagarto' and machine_pick=='spock':
        print('¡Ganaste! Sumas un punto. Lagarto envenena a Spock.')
        user_wins+=1
        
    elif user_input=='lagarto' and machine_pick=='papel':
        print('¡Ganaste! Sumas un punto. Lagarto se come el papel.')
        user_wins+=1
        
    elif user_input=='spock' and machine_pick=='tijeras':
        print('¡Ganaste! Sumas un punto. Spock rompe las tijeras.')
        user_wins+=1
        
    elif user_input=='spock' and machine_pick=='piedra':
        print('¡Ganaste! Sumas un punto. Spock vaporiza a la piedra.')
        user_wins+=1
    
    #Escenarios donde gana la maquina contra el usuario
    
    elif machine_pick=='piedra' and user_input=='tijeras':
        print('¡Perdiste! Máquina suma un punto. Piedra aplasta tijeras.')
        machine_wins+=1
        
    elif machine_pick=='piedra' and user_input=='lagarto':
        print('¡Perdiste! Máquina suma un punto. Piedra machaca lagarto.')
        machine_wins+=1
    
    elif machine_pick=='papel' and user_input=='piedra':
        print('¡Perdiste! Máquina suma un punto. Papel envuelve a la piedra.')
        machine_wins+=1
        
    elif machine_pick=='papel' and user_input=='spock':
        print('¡Perdiste! Máquina gana un punto. Papel desautoriza a Spock.')
        machine_wins+=1
    
    elif machine_pick=='tijeras' and user_input=='papel':
        print('¡Perdiste! Máquina gana un punto. Las tijeras cortan al papel.')
        machine_wins+=1
        
    elif machine_pick=='tijeras' and user_input=='lagarto':
        print('¡Perdiste! Máquina gana un punto. Las tijeras decapitan a lagarto.')
        machine_wins+=1
        
    elif machine_pick=='lagarto' and user_input=='spock':
        print('¡Perdiste! Máquina gana un punto. Lagarto envenena a Spock.')
        machine_wins+=1
        
    elif machine_pick=='lagarto' and user_input=='papel':
        print('¡Perdiste! Máquina gana un punto. Lagarto se come el papel.')
        machine_wins+=1
        
    elif machine_pick=='spock' and user_input=='tijeras':
        print('¡Perdiste! Máquina gana un punto. Spock rompe las tijeras.')
        machine_wins+=1
        
    elif machine_pick=='spock' and user_pick=='piedra':
        print('¡Perdiste! Máquina gana un punto. Spock vaporiza a la piedra.')
        machine_wins+=1
        

if user_wins>machine_wins:
    print('Has ganado contra la maquina ¡Felicidades!')
    
elif user_wins==0 and machine_wins==0:
    print('Nadie ganó en esta partida')
    
elif user_wins==machine_wins:
    print('La maquina y tú han empatado')
    
else:
    print('Has perdido contra la maquina ¡Suerte para la próxima!')
    
print('Puntuación final:')
print('Usuario ganó',user_wins,'veces.')
print('Maquina ganó',machine_wins,'veces.')

    


    
    