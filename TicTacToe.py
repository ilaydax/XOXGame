import numpy as np
import pickle
import Agent


class TicTacToe:

    def __init__(self, agent1, agent2):

        self.board = np.zeros((3, 3))
        self.player1 = agent1
        self.player2 = agent2

        self.done = False
        self.gameTable = None

        # first player
        self.playerNum = 1
    
    def reset(self):
        self.board = np.zeros((3, 3))
        self.done = False
        self.gameTable = None
        self.playerNum = 1
        
    def gameBoard(self):
        self.gameTable = str(self.board.reshape(3*3))
        return self.gameTable  
    
    def showBoard(self):
        
        # p1: x   p2: o
        for i in range(0, 3):
            print("-------------")
            out = '| '
            for j in range(0, 3):
                if self.board[i, j] == 1:
                    symbol = 'X'
                if self.board[i, j] == -1:
                    symbol = 'O'
                if self.board[i, j] == 0:
                    symbol = ' '

                out += symbol + ' | '
            print(out)
        print("-------------")

    def winner(self):
        # row
        for i in range(3):
            if sum(self.board[i, :]) == 3:
                self.done = True
                return 1
            if sum(self.board[i, :]) == -3:
                self.done = True
                return -1
            
        # colum
        for i in range(3):
            if sum(self.board[:, i]) == 3:
                self.done = True
                return 1
            if sum(self.board[:, i]) == -3:
                self.done = True
                return -1

        #diagonal
        diagonal_sum1 = sum([self.board[i, i] for i in range(3)])
        diagonal_sum2 = sum([self.board[i, 3-i-1] for i in range(3)])

        if diagonal_sum1 == 3 or diagonal_sum2 == 3:
            self.done = True
            return 1
        if diagonal_sum1 == -3 or diagonal_sum2 == -3:
            #print('-------------------')
            self.done = True
            return -1
    
        #draw
        if len(self.availableStates()) == 0:
            #print('berabere')
            self.done = True
            return 0
    
        self.done = False
        return None

    def availableStates(self):
        States = []
        for i in range(3):
            for j in range(3):
                if self.board[i, j] == 0:
                    States.append((i, j))
        return States

    def updateState(self, coord):
        
        self.board[coord] = self.playerNum
        
        #next player
        self.playerNum = -1 if self.playerNum == 1 else 1

    # sadece oyun doneğinde
    def getReward(self):
        
        result = self.winner()

        if result == 1:
            self.player1.feedReward(1)
            self.player2.feedReward(-1)
        elif result == -1:
            self.player1.feedReward(-1)
            self.player2.feedReward(1)
        else:
            self.player1.feedReward(0.1)
            self.player2.feedReward(0.5)

    #play for training
    def train(self, rounds):
        win1 = 0
        win2 = 0
        for i in range(rounds):
            
            if i % 1000 == 0:
                print('Rounds', i)
            
            
            while not self.done:
                # player 1
                availableStates = self.availableStates()
                
                player1_action = self.player1.act(availableStates, self.board, self.playerNum)
                
                self.updateState(player1_action)
                gameTable = self.gameBoard()
                self.player1.addState(gameTable)

                win = self.winner()
                if win is not None:
                    
                    if win == 1:
                        win1 += 1
                        #print("p1 kazandı")
                    self.getReward()
                    self.player1.reset()
                    self.player2.reset()
                    self.reset()
                    break

                else:
                    
                    availableStates = self.availableStates()
                    
                    player2_action = self.player2.act(availableStates, self.board, self.playerNum)
                    
                    self.updateState(player2_action)
                    gameTable = self.gameBoard()
                    self.player2.addState(gameTable)

                    
                    win = self.winner()
                    if win is not None:
                       
                        if win == -1:
                            win2+=1
                            #print("p2 kazandı")
                        self.getReward()
                        self.player1.reset()
                        self.player2.reset()
                        self.reset()
                        break
        #print('durum sayısı', len(self.player1.states), 'durum sayısı', len(self.player2.states))
        print('win1', win1, 'win2', win2)

    #play with human
    def play_human(self):
        
        while not self.done:
            # player 1
            
            availableStates = self.availableStates()
            board = self.board
            playerNum = self.playerNum
            player1_action = self.player1.act(availableStates, board, playerNum)
            
            self.updateState(player1_action)
            self.showBoard()
            
            win = self.winner()
            
            if win is not None:
                if win == 1:
                    
                    print(self.player1.name, "kazandı!")
                else:
                    print("berabere..")
                
                self.reset()
                break

            else:
                
                availableStates = self.availableStates()
                player1_action = self.player2.act(availableStates, board, playerNum)
                
                self.updateState(player1_action)
                self.showBoard()
                
                win = self.winner()
                
                if win is not None:
                    if win == -1:
                        
                        print(self.player2.name, "kazandı!") 
                    else:
                        print("berabere..")
                    self.reset()
                    break
                
    def play_random(self, rounds):
        
        win1 = 0
        win2 = 0
        for i in range(rounds):
            
            if i % 1000 == 0:
                print('Rounds', i)
                
            while not self.done:
                # player 1
                
                availableStates = self.availableStates()
                board = self.board
                playerNum = self.playerNum
                player1_action = self.player1.act(availableStates, board, playerNum)
                
                self.updateState(player1_action)
                #self.showBoard()
                
                win = self.winner()
                
                if win is not None:
                    
                    if win == 1:
                        win1 += 1                    
                    self.reset()
                    break
    
                else:
                    
                    availableStates = self.availableStates()
                    player1_action = self.player2.act(availableStates, board, playerNum)
                    
                    self.updateState(player1_action)
                    #self.showBoard()
                    
                    win = self.winner()
                    
                    if win is not None:
                        
                        if win == -1:
                            win2 += 1
                        self.reset()
                        break
        print('win1', win1, 'win2', win2)
        

class HumanPlayer:
    def __init__(self, name):
        self.name = name
  
    def act(self, availableStates, board, playerNum):
        while True:
            row = int(input("Satır:"))
            col = int(input("Sütun:"))
            action = (row, col)
            if action in availableStates:
                return action
            
class random:
    
    def __init__(self, name):
        self.name = name
  
    def act(self, availableStates, board, playerNum):
            idx = np.random.choice(len(availableStates))
            action = availableStates[idx]
            return action
              

'''
agent1 = Agent.Agent('Agent1')
agent2 = Agent.Agent('Agent2')

game = TicTacToe(agent1, agent2)
game.train(100000)

agent1.saveAgent()
agent2.saveAgent()

'''
agent1 = Agent.Agent('Agent1')
agent2 = Agent.Agent('Agent2')

agent1.loadAgent("policy_Agent1")
agent1.epsilon = 0

agent2.loadAgent("policy_Agent2")
agent2.epsilon = 0

player = HumanPlayer("Oyuncu")
game = TicTacToe(agent1, player)
game.play_human()

#random = random('random')
#game = TicTacToe(agent2, random)
#game.play_random(10000)





