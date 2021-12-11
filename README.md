Pacman Game In Python
A very buggy game of Pac Man. The game was made with Python 3.8.2 and requires pygame 1.9.6. 
This Game Contains following Features:
•	Pacman have three lives 
•	A score counter display the points a player accumulates 
•	When a player used up their three lives, saved their high score
•	The “enemy” ghosts in the game who follow the Pacman
Libraries Used
•	pygame
•	colorama
•	Game
Libraries Install
•	Pip install pygame
•	Pip install colorama
•	Pip install Game
Instrcution
If you enter the pacman game then you can see this window.











This is our pacman home windows. You have two option to select . If you want to go to game window you may press “Enter” button to go to the game. Otherwise you may press ”S” button to go “QUIT GAME” option.
 











If you wait a few minute you can see the players of the pacman game.












Click the "Enter" button to go to the previous window. “START GAME!” After selecting, you can see the sports window.













You wait a few seconds and then you can play the game using this button.
•	`W` -> Upward Movement
•	`A` -> Leftward Movement
•	`D` -> Downward Movement
•	`S` -> Rightward Movement









When the game is over it automatically comes to the home window.

























Code
These are the main library imports











Controlling the game is the main function of main.py.
def main():
    pygame.init()
    
    display = pygame.display.set_mode((640, 600), pygame.RESIZABLE)
    pygame.display.set_caption("Pac-Man")
    icon_game = pygame.image.load("LogoTiny.png")
    pygame.display.set_icon(icon_game)
    clock = pygame.time.Clock()
    game = Game()

    delta_time = 0.016666666666666666
    
    done = False
    while not done:
        clock.tick(60)/1000
        done = game.process_events()       
        game.run_logic(delta_time)
        game.display_frame(display)
        
    pygame.quit()

if __name__ == "__main__":
    main()

This is the file paths of the pacman game.











The background folder contains background.py. The code can create the home window of the packgame














enemy_sounds.py file has all the sound handling code.
•	Play sound

 def Play_Sound(self):
        if self.sound == "Normal":
            if self.play_sound_normal:
                self.Walking_Ghost_Frightened.stop()
                self.Walking_Ghost_Eaten.stop()
                
                self.Walking_Ghost_Normal = music.Sound("Walking_Ghost", .6)
                
                if not self.stop:
                    self.Walking_Ghost_Normal.play()
                    self.play_sound_normal = False
                
            if self.stop:
                self.Walking_Ghost_Normal.stop()
                self.play_sound_normal = True

                
        if self.sound == "Frightened":
            if self.play_sound_frihgtened:
                self.Walking_Ghost_Normal.stop()
                self.Walking_Ghost_Eaten.stop()
                
                self.Walking_Ghost_Frightened = music.Sound("Walking_Ghost_Frightened", .6)
                
                if not self.stop:
                    self.Walking_Ghost_Frightened.play()
                    self.play_sound_frihgtened = False
                
            if self.stop:
                self.Walking_Ghost_Frightened.stop()
                self.play_sound_frihgtened = True

                
        if self.sound == "Eaten":
            if self.play_sound_eaten:
                self.Walking_Ghost_Frightened.stop()
                self.Walking_Ghost_Normal.stop()
                
                self.Walking_Ghost_Eaten = music.Sound("Walking_Ghost_Eaten", .6)
                
                if not self.stop:
                    self.Walking_Ghost_Eaten.play()
                    self.play_sound_eaten = False
                
            if self.stop:
                self.Walking_Ghost_Eaten.stop()
                self.play_sound_eaten = True



•	Stop sound

def Stop_Sound(self):
        if not True in self.all_enemy_stop:
            self.stop = False

        else:
            self.stop = True

•	Control sound
def Control_Sound(self):
        if not "Frightened_1" in self.all_enemy_mode and not "Frightened_2" in self.all_enemy_mode:
            if not "Eaten" in self.all_enemy_mode:
                self.play_sound_frihgtened = True
                self.play_sound_eaten = True
                self.sound = "Normal"
            
            
            else:
                self.play_sound_normal = True
                self.play_sound_frihgtened = True
                self.sound = "Eaten"
                
        else:
            if not "Eaten" in self.all_enemy_mode:
                self.play_sound_normal = True
                self.play_sound_eaten = True
                self.sound = "Frightened"
            
            
            else:
                self.play_sound_normal = True
                self.play_sound_frihgtened = True
                self.sound = "Eaten"

•	Reset normal Sound
def Reset_Normal_Sound(self):
        if self.sound == "Normal":
            if not self.stop:
                if self.time.time_over():
                    self.time = decoration.Chronometer(60)
                    
                    self.Walking_Ghost_Normal.play()
                    
            if self.stop:
                self.time = decoration.Chronometer(60)
                
        else:
            self.time = decoration.Chronometer(60)


Here is the code of the original window for the player to select options.

 def __init__(self, execobj):
        super().__init__()
        
        self.execobj = execobj
       
        self.image = pygame.Surface((20, 20))
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        
        self.rect = self.image.get_rect()
        
        self.rect.x = 100
        self.rect.y = 700

        decoration.Generate_Decoration("score    hi-score ", 100, 66, (255, 0, 0, 1), "go_up")
        decoration.Generate_Decoration(score.return_hi_score(), 240, 88, (255, 255, 255), "go_up")
        decoration.Generate_Decoration("   00", 100, 88, (255, 255, 255), "go_up")
        decoration.Generate_Decoration("*", 100, 132, (255, 255, 255), "go_up")
        
        decoration.Generate_Decoration("   start game!   ", 180, 286, (255, 255, 255), "go_up")
        decoration.Generate_Decoration(">", 200, 286, (255, 255, 255), "go_up")
        decoration.Generate_Decoration("   quit game    ", 180, 374, (255, 255, 255), "go_up")

The decoration.py file contains control keys of the game.

 def __init__(self, symbol, x, y, color, identifier, s_color):
        super().__init__()
        self.identifier = identifier
        self.symbol =  symbol
        self.wh = (7, 7)
        self.conv = (18, 18)
        
        if self.symbol == 27:
            self.wh = (8, 7)
            self.conv = (20, 18)
            
        if self.symbol == 28:
            self.wh = (8, 8)
            self.conv = (20, 20)
            
        if self.symbol == 29:
            self.wh = (1, 1)
            self.conv = (18, 18)
            
        if self.symbol == 44:
            self.wh = (7, 8)
            self.conv = (18, 20)

        if self.symbol == 45:
            self.wh = (182, 46)
            self.conv = (455, 115)
            
        if self.symbol == 46:
            self.wh = (70, 10)
            self.conv = (175, 25)
            
        if self.symbol == 47:
            self.wh = (14, 13)
            self.conv = (30, 30)
            
        if self.symbol == 50:
            self.wh = (12, 13)
            self.conv = (27, 29)

Score.py contains the code used to calculate the score. This code is used to indicate running scores in the game.
class Score_Part(decoration.Decoration_part):
    def __init__(self, pos, pos_x, pos_y):
        decoration.Decoration_part.__init__(self, 0, 440, 166, (255, 255, 255), "s", False)
        self.pos = pos
        self.pos_x = pos_x
        self.pos_y = pos_y
            
            
    def display(self):
        local_score = str(score)
        if len(local_score) >= 8:
            local_score = "error"

        if len(local_score) == 1:
            local_score = "     00"+local_score
            
        if len(local_score) == 2:
            local_score = "     "+local_score
            
        if len(local_score) == 3:
            local_score = "    "+local_score
            
        if len(local_score) == 4:
            local_score = "   "+local_score
            
        if len(local_score) == 5:
            local_score = "  "+local_score
            
        if len(local_score) == 6:
            local_score = " "+local_score
            
        if len(local_score) == 7:
            local_score = local_score

        
            
        v = list()
        for n in local_score:
            if n == "0":
                n = 31
            if n == "1":
                n = 32
            if n == "2":
                n = 33
            if n == "3":
                n = 34
            if n == "4":
                n = 35
            if n == "5":
                n = 36
            if n == "6":
                n = 37
            if n == "7":
                n = 38
            if n == "8":
                n = 39
            if n == "9":
                n = 40
            if n == " ":
                n = 29
            if n == "e":
                n = 4
            if n == "o":
                n = 14  
            if n == "r":
                n = 17
            
            v.append(n)
            
        local_score = v
        
        self.sheet.set_clip(pygame.Rect(self.sprite_sheet[local_score[self.pos]]+(7, 7)))  # x, y, ancho+1, alto+1
     
        self.image = self.sheet.subsurface(self.sheet.get_clip())

        self.image_pixel_array = pygame.PixelArray(self.image)
        self.image_pixel_array.replace((0, 0, 0, 1), (0, 0, 1, 1))
        
        self.image.set_colorkey((0, 0, 1, 1))
        
        self.image = pygame.transform.scale(self.image, (18, 18))
        
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y
        
    def update(self, delta_time):
        self.display()

def Score():
    x = 440
    y = 166
    for n in range(7):
        score_a = Score_Part(n, x, y)
        all_sprites.add(score_a)
        x += 20
 
This code is used to indicate high scores in the game.
class Hi_Score_Part(decoration.Decoration_part):
    def __init__(self, pos, pos_x, pos_y):
        decoration.Decoration_part.__init__(self, 0, 440, 166, (255, 255, 255), "s", False)
        self.pos = pos
        self.pos_x = pos_x
        self.pos_y = pos_y
            
            
    def display(self):
        local_score = str(hi_score)
        if len(local_score) >= 8:
            local_score = "error"

        if len(local_score) == 1:
            local_score = "     00"+local_score
            
        if len(local_score) == 2:
            local_score = "     "+local_score
            
        if len(local_score) == 3:
            local_score = "    "+local_score
            
        if len(local_score) == 4:
            local_score = "   "+local_score
            
        if len(local_score) == 5:
            local_score = "  "+local_score
            
        if len(local_score) == 6:
            local_score = " "+local_score
            
        if len(local_score) == 7:
            local_score = local_score

        
            
        v = list()
        for n in local_score:
            if n == "0":
                n = 31
            if n == "1":
                n = 32
            if n == "2":
                n = 33
            if n == "3":
                n = 34
            if n == "4":
                n = 35
            if n == "5":
                n = 36
            if n == "6":
                n = 37
            if n == "7":
                n = 38
            if n == "8":
                n = 39
            if n == "9":
                n = 40
            if n == " ":
                n = 29
            if n == "e":
                n = 4
            if n == "o":
                n = 14  
            if n == "r":
                n = 17
            
            v.append(n)
            
        local_score = v
        
        self.sheet.set_clip(pygame.Rect(self.sprite_sheet[local_score[self.pos]]+(7, 7)))  # x, y, ancho+1, alto+1
     
        self.image = self.sheet.subsurface(self.sheet.get_clip())

        self.image_pixel_array = pygame.PixelArray(self.image)
        self.image_pixel_array.replace((0, 0, 0, 1), (0, 0, 1, 1))
        
        self.image.set_colorkey((0, 0, 1, 1))
        
        self.image = pygame.transform.scale(self.image, (18, 18))
        
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y

  
    def update(self, delta_time):
        self.display()



