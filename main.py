import random
from click import clear

from words import words
from clipart import logo, stages

class Game:
    random_word_pick = random.choice(words);
    fill_list = []
    lives = 6
    game_end = False
    is_visible_fill = True
    is_visible_stage = True

    def header(self):
        print(f"{logo}\n\n")
        # for testing
        print(f"Word to guess {self.random_word_pick}\n")

    def display(self):
        display = " ".join(self.fill_list)
        if self.is_visible_fill:
            print(f"Your puzzle\n{display}\n")
        if self.is_visible_stage:
            print(stages[self.lives])

    def on(self):
        exit_game = False
        
        while not exit_game:
            for _ in range(0, len(self.random_word_pick)):
                    self.fill_list.append("_")
    
            self.header()
            self.display()
    
            while not self.game_end:
                input_letter = input("Guess a letter: ")
                guess_letter = input_letter[0]
        
                clear()
                self.header()
        
                if guess_letter in self.fill_list:
                    print(f"{guess_letter} existed. Please try another with letter.\n")
                    
                for position in range(len(self.random_word_pick)):
                    if self.random_word_pick[position] == guess_letter:
                        self.fill_list[position] = guess_letter
        
                if guess_letter not in self.random_word_pick:
                    self.lives -= 1
        
                    print(f"{guess_letter} is not match. {self.lives} {'live' if self.lives <= 1 else 'lives'} remaining.\n")
        
                    if self.lives < 1:
                        self.game_end = True
                        self.is_visible_fill = False
                        print("Oh...gosh... you died!\n")
        
                if "_" not in self.fill_list:
                    print("Hooray, you win!\n")
                    self.game_end = True
                    self.is_visible_stage = False
        
                self.display()
    
            if self.to_continue():
                clear()
                
                self.random_word_pick = random.choice(words);
                self.fill_list = []
                self.lives = 6
                self.game_end = False
                self.is_visible_fill = True
                self.is_visible_stage = True
            else:
                clear()
                
                exit_game = True
                return "Goodbye!"
                        
    def to_continue(self):
            print("\n\n-----------------------------------------------\n")
            to_continue = input('Play again?\nPress any key to continue or type "no" to exit.\n').lower()
        
            return to_continue != "no" 
        

hangman = Game()
print(hangman.on())