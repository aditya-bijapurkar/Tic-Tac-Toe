board=["-","-","-",
       "-","-","-",
       "-","-","-"]

opt='i'
def opt_MS():
    global opt
    option=True
    while option==True:
        print("""\nfor MultiPlayer type: 'M',
for SinglePlayer type: 'S'""")
        opt=input()
        if opt=='M' or opt=='m':
            if opt=='m':
                opt='M'
            option=False
        elif opt=='S' or opt=='s':
            if opt=='s':
                opt='S'
            option=False
        else:
            print("Enter correct choice: 'M' or 'S'")
    return opt


check = True
gameGoing=True


player1='i'
player2='i'
currentPlayer='i'


def getName():
    global player1, player2, currentPlayer
    player1=input("Player 1, Enter your name: ")
    player2=input("Player 2, Enter your name: ")
    currentPlayer=player1

def getNameSP():
    global player1, player2, currentPlayer
    player1=input("Player 1, Enter your name: ")
    player2="Computer"
    currentPlayer=player1


def showBoard():
    print(" | ",board[0]," ",board[1]," ",board[2]," | ")
    print(" | ",board[3]," ",board[4]," ",board[5]," | ")
    print(" | ",board[6]," ",board[7]," ",board[8]," | ")



choice1=0
choice2=0
choiceS=0



def choice():
    global choice1, choice2, choiceS
    trychoice=True
    getName()
    while trychoice:
        print("\n",player1,": Choose 'X' or 'O':  ")
        choice1=input()
        if choice1=='X' or choice1=='x':
            print(player1,": 'X'","       ", player2, ": 'O'")
            if choice1=='x':
                choice1='X'
            trychoice=False
        elif choice1=='O' or choice1=='o':
            print(player1,": 'O'","       ", player2, ": 'X'")
            if choice1=='o':
                choice1='O'
            trychoice=False
        else:
            print("Enter correct choice")
    
    if choice1=='X' or choice1=='x':
        choice2='O'
    if choice1=='O'or choice1=='o':     
       choice2='X'
    choiceS=choice1


def choiceSP():
    global choice1, choice2, choiceS
    trychoice=True
    getNameSP()
    while trychoice:
        print("\n"+player1+": Choose 'X' or 'O':  ")
        choice1=input()
        if choice1=='X' or choice1=='x':
            print(player1,": 'X'","       ", player2, ": 'O'")
            if choice1=='x':
                choice1='X'
            trychoice=False
        elif choice1=='O' or choice1=='o':
            print(player1,": 'O'","       ", player2, ": 'X'")
            if choice1=='o':
                choice1='O'
            trychoice=False
        else:
            print("Enter correct choice")
    
    if choice1=='X' or choice1=='x':
        choice2='O'
    if choice1=='O'or choice1=='o':     
       choice2='X'
    choiceS=choice1



def switchPlayer():
    global currentPlayer, choiceS
    if currentPlayer==player1:
        currentPlayer=player2
        choiceS=choice2
    elif currentPlayer==player2:
        currentPlayer=player1  
        choiceS=choice1



def writeChoice():
    choice()
    elem=[]
    test=0
    while check==True:
        print("\n"+currentPlayer+"'s chance")
        element=input("Where do you want to play? (enter 1-9): ")
        if element not in ['0','1','2','3','4','5','6','7','8','9']:
            print("Enter correct option") 
        else: 
            element=int(element)
        if element in range(1,10): 
            if element not in elem:
                element-=1
                board[element]=choiceS
                element+=1
                elem.append(element)
                test+=1
                showBoard()
                checkWinner()
                if gameGoing==False:
                   check==False
                   print("\n     ",currentPlayer, """ Won!
      Game Over!!""")
                   break
                elif test>8:
                   check==False
                   break
                else:
                   switchPlayer()
            else:   
                print("\nCant write there, choose another place!")
                showBoard()
        else:
            print("choose a number between 1-9")
    
    
# for single player game!
import random
import time

def writeChoiceSP():
    choiceSP()
    elem=[]
    test=0
    while check==True:
        if currentPlayer==player1:
            print("\n"+currentPlayer+"'s chance")
            element=input("Where do you want to play? (enter 1-9): ")
            if element not in ['0','1','2','3','4','5','6','7','8','9']:
                print("Enter correct option") 
            else: 
                element=int(element)
            if element in range(1,10): 
                if element not in elem:
                    element-=1
                    board[element]=choiceS
                    element+=1
                    elem.append(element)
                    test+=1
                    showBoard()
                    checkWinner()
                    if gameGoing==False:
                       check==False
                       print("\n     "+currentPlayer, """ Won!
      Game Over!!""")
                       break
                    elif test>8:
                       check==False
                       break
                    else:
                       switchPlayer()
                else:   
                    print("\nCant write there, choose another place!")
                    showBoard()
            else:
                print("choose a number between 1-9")
        
        if currentPlayer==player2:
            checkWinner()
            if gameGoing==False:
                break
            comp_test=True
            while comp_test:    
                comp_elem=random.randint(1,9)
                if comp_elem not in elem:
                    comp_elem-=1
                    board[comp_elem]=choiceS
                    comp_elem+=1
                    elem.append(comp_elem)
                    comp_test=False
                    test+=1
                    print("\n"+currentPlayer,"'s chance")
                    time.sleep(0.7)
                    print(currentPlayer+": played at position:",comp_elem)
                    showBoard()
                    checkWinner()
                    if gameGoing==False:
                       check==False
                       comp_test=False
                       print("\n     ",currentPlayer, """ Won!
      Game Over!!""")
                       break
                    elif test>8:
                       comp_test=False
                       check==False
                       break
                    else:
                       switchPlayer()


def checkWinner():
    global gameGoing
    if board[0]==board[1]==board[2]!='-':
        gameGoing=False
    elif board[3]==board[4]==board[5]!='-':
        gameGoing=False
    elif board[6]==board[7]==board[8]!='-':
        gameGoing=False
    elif board[0]==board[3]==board[6]!='-':
        gameGoing=False
    elif board[1]==board[4]==board[7]!='-':
        gameGoing=False
    elif board[2]==board[5]==board[8]!='-':
        gameGoing=False
    elif board[0]==board[4]==board[8]!='-':
        gameGoing=False
    elif board[2]==board[4]==board[6]!='-':
        gameGoing=False



def tie():
    if gameGoing==True:
       if '-' not in board:
          print("""\n   It is a tie!
   Game Over!!""")


def playMP():
    writeChoice()
    tie()
def playSP():
    writeChoiceSP()
    tie()



def playGame():
    print("""       | 1 2 3 |
       | 4 5 6 |
       | 7 8 9 |""")
    val=opt_MS()
    if val=='M':
        playMP()
    if val=='S':
        playSP()

def resetGame():
    global board, option, opt, check, gameGoing, player1, player2, currentPlayer, choice1, choice2, choiceS, Continue, trychoice, elem, test
    board = ["-","-","-",
             "-","-","-",
             "-","-","-"]
    option=True
    opt='i'
    check = True
    gameGoing=True
    player1='i'
    player2='i'
    currentPlayer='i'
    choice1=0
    choice2=0
    choiceS=0
    trychoice=True
    elem=[]
    test=0
    Continue=True


if __name__=="__main__":
    Continue=True
    while Continue==True:
        game_choice=True
        while game_choice:
            print("\n1: Play new game")
            print("2: Exit")
            a=input("\nEnter a choice: ")
            if a not in ['1','2']:
                print("\nEnter correct choice.")
            else:
                a=int(a)
                game_choice=False
        if a == 1:
            resetGame()
            playGame()
        if a == 2:
            print("\nExiting...")
            time.sleep(1.5)
            print("Thanks for playing")
            Continue=False