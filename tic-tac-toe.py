#3 en raya

import random
import os
import socket
import sys
import time

reb = "\033[0;37;40m"
interw = "\033[5;37;40m"


def limpiar():
	if os.name == 'posix':
		time.sleep(1)
		os.system("clear")
	else:
		time.sleep(1)
		os.system("cls")

def drawBoard(board):
    print('\n   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
 
def inputPlayerLetter():

    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Cual quieres elegir X o O?')
        letter = input().upper()
 
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']
 
def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'
 
def playAgain():
	while True:
		print('quieres jugar otra vez? (S/N)')
		opt = input().lower()
		if opt == "s":
			return True
		elif opt == "n":
			print("Adios...")
			main()
		else:
			print("Error")
 
def makeMove(board, letter, move):
    board[move] = letter
 
def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or 
    (bo[4] == le and bo[5] == le and bo[6] == le) or 
    (bo[1] == le and bo[2] == le and bo[3] == le) or 
    (bo[7] == le and bo[4] == le and bo[1] == le) or 
    (bo[8] == le and bo[5] == le and bo[2] == le) or
    (bo[9] == le and bo[6] == le and bo[3] == le) or 
    (bo[7] == le and bo[5] == le and bo[3] == le) or 
    (bo[9] == le and bo[5] == le and bo[1] == le)) 
 
def getBoardCopy(board):
    dupeBoard = []
 
    for i in board:
        dupeBoard.append(i)
 
    return dupeBoard
 
def isSpaceFree(board, move):
    return board[move] == ' '
 
def getPlayerMove(board):
	try:
	    move = ' '
	    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
	        print('cual es tu siguiente movimineto? (1-9)')
	        move = input(">>> ")
	    return int(move)
	except KeyboardInterrupt:
			main() 



def chooseRandomMoveFromList(board, movesList):
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
 
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):

    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
 
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i
 
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    if isSpaceFree(board, 5):
        return 5

    return chooseRandomMoveFromList(board, [2, 4, 6, 8])


def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

 
def game():

	while True:
	   
	    theBoard = [' '] * 10
	    playerLetter, computerLetter = inputPlayerLetter()
	    turn = whoGoesFirst()
	    print('El jugador ' + turn + ' es el primero en empezar')
	    gameIsPlaying = True
	 
	    while gameIsPlaying:
	        if turn == 'player':
	            limpiar()
	            drawBoard(theBoard)
	            print("Jugador 1")
	            move = getPlayerMove(theBoard)
	            makeMove(theBoard, playerLetter, move)
	 
	            if isWinner(theBoard, playerLetter):
	                limpiar()
	                drawBoard(theBoard)
	                print(interw+'\nJugador 1 gana\n'+reb)
	                gameIsPlaying = False
	            else:
	                if isBoardFull(theBoard):
	                    limpiar()
	                    drawBoard(theBoard)
	                    print('El juego esta en empate!')
	                    break
	                else:
	                    turn = 'computer'
	 
	        else:
	            limpiar()
	            drawBoard(theBoard)
	            print("\nJugador 2")                
	            move = getPlayerMove(theBoard)
	            makeMove(theBoard, computerLetter, move)
	 
	            if isWinner(theBoard, computerLetter):
	                limpiar()
	                drawBoard(theBoard)
	                print(interw+'\njugador 2 gana.\n'+reb)
	                gameIsPlaying = False
	            else:
	                if isBoardFull(theBoard):
	                    limpiar()
	                    drawBoard(theBoard)
	                    print('El juego esta en empate')
	                    break
	                else:
	                    turn = 'player'
	 
	    if not playAgain():
	       	main()

def gamebot():
	 
	while True:
	    
	    theBoard = [' '] * 10
	    playerLetter, computerLetter = inputPlayerLetter()
	    turn = whoGoesFirst()
	    print('El jugador ' + turn + ' es el primero en empezar')
	    gameIsPlaying = True
	 
	    while gameIsPlaying:
	        if turn == 'player':
	           
	            limpiar()
	            print("Jugador 1")
	            drawBoard(theBoard)
	            move = getPlayerMove(theBoard)
	            makeMove(theBoard, playerLetter, move)
	 
	            if isWinner(theBoard, playerLetter):
	                drawBoard(theBoard)
	                print(interw+'\nJugador 1 gana\n'+reb)
	                gameIsPlaying = False
	            else:
	                if isBoardFull(theBoard):
	                    drawBoard(theBoard)
	                    print('El juego esta en empate!')
	                    break
	                else:
	                    turn = 'computer'
	 
	        else:
	           
	            limpiar()
	            print("\nBot")
	            drawBoard(theBoard)
	            move = getComputerMove(theBoard, computerLetter)
	            makeMove(theBoard, computerLetter, move)

	            if isWinner(theBoard, computerLetter):
	                limpiar()
	                drawBoard(theBoard)
	                print(interw+'\nBot gana\n'+reb)
	                gameIsPlaying = False
	            else:
	                if isBoardFull(theBoard):
	                    limpiar()
	                    drawBoard(theBoard)
	                    print('El juego esta en empate')
	                    break
	                else:
	                    turn = 'player'
	 
	    if not playAgain():
	        main()

def servers(HOST="127.0.0.1", PORT=5050):
	try:
		s = socket.socket()
		
		
		s.bind((HOST, PORT))
		s.listen(1)
		c = None
	except OSError:
		port = input("puerto a usar: ")
		servers(PORT=int(port))
	while True:
		
		if c is None:
			print("Para copiar selecciona ip:port y usa ctrl+shift+c")
			print("Escuchando en {}:{}".format(HOST, PORT))
			print('Esperando conexion...')
			c, addr = s.accept()
			print('Conectado!')
		else:
			while True:
			    
			    theBoard = [' '] * 10
			    playerLetter, computerLetter = ['X', 'O']
			    turn = 'player'
			    
			    gameIsPlaying = True
			 
			    while gameIsPlaying:
			        
			        if turn == 'player':
			            
			            limpiar()
			            print("Eres el Jugador 1")
			            print('El Jugador 1 es el primero en empezar')
			            drawBoard(theBoard)
			            print("\nJugador 1")
			            move = getPlayerMove(theBoard)
			            print(move)
			            makeMove(theBoard, playerLetter, move)
			            c.send(bytes(str(move).encode('utf-8')))
			 
			            if isWinner(theBoard, playerLetter):
			                limpiar()
			                drawBoard(theBoard)
			                print(interw+'\nJugador 1 gana\n'+reb)
			                gameIsPlaying = False
			            else:
			                if isBoardFull(theBoard):
			                    limpiar()
			                    drawBoard(theBoard)
			                    print('El juego esta en empate!')
			                    break
			                else:
			                    turn = 'computer'
			 
			        else:
			            
			            limpiar()
			            drawBoard(theBoard)
			            print("\nJugador 2")
			            print("Esperando movimineto...")
			            move = c.recv(1024).decode('utf-8')
			            print(move)
			            makeMove(theBoard, computerLetter, int(move))
			 
			            if isWinner(theBoard, computerLetter):
			                limpiar()
			                drawBoard(theBoard)
			                print(interw+'\njugador 2 gana.\n'+reb)
			                gameIsPlaying = False
			            else:
			                if isBoardFull(theBoard):
			                    limpiar()
			                    drawBoard(theBoard)
			                    print('El juego esta en empate')
			                    break
			                else:
			                    turn = 'player'
			 
			    if not playAgain():
			        main()

def clientes():
	try:
		opt1 = input("Url servidor ip:puerto : ")
		HOST, PORT = opt1.split(":")
	except ValueError:
		print("\nError ip:puerto no valido\n")
		clientes()
	try:
		s = socket.socket()
		s.connect((HOST, int(PORT)))
		print('Conectado a ', HOST)
	except ConnectionRefusedError:
		print("Error, no se puede conectar con el servidor!")
		main()


	while True:
	    
	    theBoard = [' '] * 10
	    playerLetter, computerLetter = ['X', 'O']
	    turn = 'player'
	    gameIsPlaying = True
	 
	    while gameIsPlaying:
	        if turn == 'player':
	           
	            limpiar()
	            print("Eres el Jugador 2")
	            print('El Jugador 1 es el primero en empezar')
	            drawBoard(theBoard)
	            print("\nJugador 1")
	            print("Esperando movimiento...")
	            move = s.recv(1024).decode('utf-8')
	            try:
	            	makeMove(theBoard, playerLetter, int(move))
	            except ValueError:
	            	print("Jugador desconectado..")
	            	main()
	 
	            if isWinner(theBoard, playerLetter):
	                limpiar()
	                drawBoard(theBoard)
	                print(interw+'\nJugador 1 gana\n'+reb)
	                gameIsPlaying = False
	            else:
	                if isBoardFull(theBoard):
	                    limpiar()
	                    drawBoard(theBoard)
	                    print('El juego esta en empate!')
	                    break
	                else:
	                    turn = 'computer'
	 
	        else:
	            
	            limpiar()
	            drawBoard(theBoard)
	            print("\nJugador 2")
	            move = getPlayerMove(theBoard)

	            makeMove(theBoard, computerLetter, int(move))
	            s.send(bytes(str(move).encode('utf-8')))
	 
	            if isWinner(theBoard, computerLetter):
	                limpiar()
	                drawBoard(theBoard)
	                print(interw+'\njugador 2 gana.\n'+reb)
	                gameIsPlaying = False
	            else:
	                if isBoardFull(theBoard):
	                    limpiar()
	                    drawBoard(theBoard)
	                    print('El juego esta en empate')
	                    break
	                else:
	                    turn = 'player'
	 
	    if not playAgain():
	        main()
def info():
	print("Para ayudarme sigueme en: \n 	https://instagram.com/_p1ngu1n0_")

def main():
	__author__ = "p1ngu1n0"

	if sys.version_info[0] == 3:
		limpiar()
		print("""
							
	   |   |	3 en raya
	 X | O | O
	   |   |	  Clasico:
	-----------	    1) 1 vs bot				
	   |   |	    2) 1 vs 1
	 O | X | X		
	   |   |	  Multijugador:
	-----------	    3) server
	   |   |	    4) cliente
	 X | O | X
	   |   |	 5) Info
	   		 6) Salir
""")

		try:
			while True:

				op = input(">>> ")
				if op == "1":
				    gamebot()
				elif op == "2":
				    game()
				elif op == "3":
				    servers()
				elif op == "4":
				    clientes()
				elif op == "5":
					info()
				elif op == "6":
					print("\nAdios :D")
					limpiar()
					sys.exit()
				else:
				    print("No existe esa opcion.")


		except KeyboardInterrupt:
			print("\nAdios :D")
			limpiar()
			sys.exit()
	else:
		print("\nEste juego aun no tiene soporte python 2\n")
		limpiar()

if __name__ == '__main__':
	main()

