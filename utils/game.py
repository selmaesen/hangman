
import re

class Hangman:
    def __init__ (self, good_word):
        
        self.good_word = good_word
        self.life = 5
        self.bad_guessed_letters = []
        self.turn_count = 0
        self.error_count = 0
        self.good_answers = 0
        
        self.well_guessed_letters = ""
        for n in range (len(good_word)):
            self.well_guessed_letters += "_ " # creates the sample of the word that will be guessed
    
    
    def play(self):
    #this fuction is the main function to decide the validity of each attemt put the guessed letters in right positions
        guess = input("Enter a letter:")
        self.turn_count += 1
        pattern = "([A-z])"
        
        if re.match(pattern, guess) and len(guess) == 1: # the format of the input from a gamer (one leter)
            print ("Thanks! it is a letter")
            
            if guess in self.good_word:
                
                for i in range(len(self.good_word)):
                    
                    if guess == self.good_word[i]:
                        index = i*2   # "*2" because I use a blank after "_" in the format. That makes the index double
                        self.well_guessed_letters = self.well_guessed_letters[:index] + guess + self.well_guessed_letters[index + 1:]    
                        print (self.well_guessed_letters)
                        self.good_answers += 1
                        
            else:
                self.bad_guessed_letters.append(guess)
                self.error_count += 1
                self.life -= 1 
        else:
            print ("Try again")
        # we need to see the overview after each attempt
        print (f"The word is: {self.well_guessed_letters}, {self.bad_guessed_letters} are not in the word, {self.life} life you left, {self.error_count} times you missed in {self.turn_count} turns") 
    
    def game_over(self):
    # when you have finished the allowed attempts which is 5
        print ("game over")
        
    def well_played(self):
    # when you win
        print (f"You found the word: {self.good_word} in {self.turn_count} turns with {self.error_count} errors!")
        
    
    def start_game(self):
    # this makes a loop until the word is guessed or the allowed attempts are finished
        while self.life > 0: 
            self.play()
            if  "_" not in self.well_guessed_letters:
                self.well_played()
                break
        else:
            self.game_over()
        
        
