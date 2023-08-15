import numpy as np
import pickle

class Agent:
    
    def __init__(self, name):

          self.name = name
          self.states = []  
          self.states_value = {}
          
          self.lr = 0.1
          self.epsilon = 0.3
          self.gamma = 0.9
          
    def reset(self):
        self.states = []
  
    def gameTable(self, board):
        gameTable = str(board.reshape(3*3))
        return gameTable
    
    def act(self, availableStates, currentBoard, symbol):
        
        if np.random.uniform(0,1) <= self.epsilon:
            idx = np.random.choice(len(availableStates))
            action = availableStates[idx]
        else:
            max_value = -999
            for p in availableStates:
                nextBoard = currentBoard.copy()
                nextBoard[p] = symbol
                nextGameTable = self.gameTable(nextBoard)
                value = 0 if self.states_value.get(nextGameTable) is None else self.states_value.get(nextGameTable)
                if value >= max_value:
                    max_value = value
                    action = p
        
        #if self.epsilon > 0.1:
            #self.epsilon -= 0.05
        return action
  
    def addState(self,state):
        self.states.append(state)

    def feedReward(self,reward):
    
        for st in reversed(self.states):
      
            if self.states_value.get(st) is None:
                self.states_value[st] = 0
      
            self.states_value[st] += self.lr*(self.gamma*reward - self.states_value[st])
      
            reward = self.states_value[st]
      
    def saveAgent(self):
        #print(self.states_value)
        fw = open('policy_' + str(self.name), 'wb')
        pickle.dump(self.states_value, fw)
        fw.close()

    def loadAgent(self, file):
        fr = open(file, 'rb')
        self.states_value = pickle.load(fr)
        fr.close()

