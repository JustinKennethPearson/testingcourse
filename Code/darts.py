class scoreboard:
    """ Implements a score board for a darts game
    """
    def __init__(self):
        self.playerscores = [None,301,301]
        #  turn = 1 or 2 player's turn.    
        self.turn = 1
        self.throws = 0
        self.current_round = 0
    def playerscore(self,player):
        if player == 1 or player == 2:
            if (self.playerscores[player] != 0 ): 
                return(self.playerscores[player])
            else:
                return('WON')
        else:
            raise NameError('player out of range')

    def playerthrown(self,player,multiplier,number):
        #Check if it the right players turn.
        if player != self.turn:
            raise NameError('throw out of turn')
        #Now it is safe to increment the number of throws.
        self.throws = self.throws + 1
        #If we've down 3 throws then it is somebody else's turn.

        #Now work out the score.
        if multiplier == 'double':
              number = number*2
        elif multiplier == 'triple':
            number = number*3
        #Change the current score.
        self.playerscores[player] -= number
        self.current_round += number
        #If we have done 3 throws then
        # 1) we need to flip
        # 2) we need to our score is -ve.
        # 3) We need to reset the current_score to 0.
        if (self.throws == 3):
            self.throws = 0
            #This if statement flips the players turn.
            if (self.turn == 1):
                self.turn = 2
            else:
                self.turn = 1
            #Now we check if our score is -ve
            if self.playerscores[player] < 0:
                self.playerscores[player] += self.current_round
            #Now reset the current_round
            self.current_round = 0
        #That's the end of the 3 throws logic.


    

