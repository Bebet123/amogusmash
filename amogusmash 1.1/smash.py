import pygame

pygame.init()
pygame.joystick.init()



exit = False
larghezza = 1600
altezza = 800
size = (larghezza,altezza)
size2 = (larghezza*1.5,altezza*1.5)



clock = pygame.time.Clock()
schermo = pygame.display.set_mode(size)
telecamera = pygame.Surface(size,pygame.SRCALPHA)

pygame.display.set_caption("AMOGUSMASH")
sfondo=pygame.image.load("assets/background.jpg").convert_alpha()
sfondopausa=pygame.image.load("assets/backgroundblur.png").convert_alpha()
sfondo= pygame.transform.scale(sfondo, size)
sfondopausa= pygame.transform.scale(sfondopausa, (larghezza,altezza))
off=pygame.image.load("assets/OFF.png").convert_alpha()
on=pygame.image.load("assets/ON.png").convert_alpha()
off= pygame.transform.scale(off, (100,50))
on= pygame.transform.scale(on, (100,50))
piattaforma = pygame.image.load("assets/piattaforma.png") 
piattaforma = pygame.transform.scale(piattaforma, (830,50))
rect_piattaforma= piattaforma.get_rect()
rect_piattaforma.center = telecamera.get_rect().center

spawn = pygame.image.load("assets/piattaformaspawn.png").convert_alpha()
spawn= pygame.transform.scale(spawn, (150,25))
cursor = pygame.image.load("assets/cursor.png").convert_alpha()
cursor= pygame.transform.scale(cursor, (46,60))

menùnapoli = pygame.image.load("assets/NAPOLIMENU.jpeg").convert_alpha()
menùnapoli= pygame.transform.scale(menùnapoli, (larghezza,altezza))

sfondofine2=pygame.image.load("assets/red.png").convert_alpha()
sfondofine2= pygame.transform.scale(sfondofine2, (larghezza,altezza))

sfondofine1=pygame.image.load("assets/blu.jpg").convert_alpha()
sfondofine1= pygame.transform.scale(sfondofine1, (larghezza,altezza))





counter = 0

saltoconlevetta = False #impostazioni
fpscounterr = False
sens = 0.3

with open("settings.txt", "r") as f:
    content = f.read()
    lines = content.split("\n")
    saltoconlevetta = False
    fpscounterr = False
    for line in lines:
        if line.startswith("saltoconlevetta="):
            value = line.split("=")[1]
            saltoconlevetta = bool(int(value))
        elif line.startswith("fpscounterr="):
            value = line.split("=")[1]
            fpscounterr = bool(int(value))
        elif line.startswith("sens="):
            value = line.split("=")[1]
            sens = float(value)

PosX = 200
PosY = 20

slider_x = 790
slider_y = 680

valore_reale = sens*100
valore_minimo = 0
valore_massimo = 100

cico = (valore_reale - valore_minimo) / (valore_massimo - valore_minimo) * (PosX - 10)

rect_base = pygame.Rect(slider_x + 5, slider_y + 5, cico, PosY - 10)

rect_basee = pygame.Rect(slider_x + 5, slider_y, cico, PosY )


p = False
menùù = True

imp = (128,255,0)
red = (255,0,0)
blue = (0,0,255)

stile0=pygame.font.Font('assets/font/Impostograph-Regular.ttf',90)
stile1=pygame.font.Font('assets/font/Impostograph-Regular.ttf',50)
stile2=pygame.font.Font('assets/font/Impostograph-Regular.ttf',100)
stile3 = pygame.font.Font(None, 90)
stile4 = pygame.font.Font(None, 60)


piattaformar = pygame.Rect(300, 600, 1000, 50)
piattaformara = pygame.Rect(385, 600, 830, 50)
piatt1 = pygame.Rect(300, 600, 85, 30)
piatt2 = pygame.Rect(1215, 600, 85, 30)

rect_text = pygame.Rect(690, 380, 200, 60)
rect_menù = pygame.Rect(690, 380, 200, 60)
saltooo = pygame.Rect(820, 600, 100, 50)
onoff = pygame.Rect(820, 500, 100, 50)
rect_menùesci = pygame.Rect(747, 480, 80, 60)
menùprincipale = pygame.Rect(690, 280, 340, 60)

escii = pygame.Rect(1347, 480, 80, 60)
continuee = pygame.Rect(1290, 380, 200, 60)

rect_controller = pygame.Rect(747, 600, 80, 60)



start = False
starttimer = 240
finevar = False

afferrato2 = False
afferrato1 = False

afferrato = False

effettomorte = [
        
            pygame.image.load("assets/morte/a (1).png").convert_alpha(),
            pygame.image.load("assets/morte/a (2).png").convert_alpha(),
            pygame.image.load("assets/morte/a (3).png").convert_alpha(),
            pygame.image.load("assets/morte/a (4).png").convert_alpha(),
            pygame.image.load("assets/morte/a (6).png").convert_alpha(),
            pygame.image.load("assets/morte/a (6).png").convert_alpha(),
            pygame.image.load("assets/morte/a (7).png").convert_alpha(),
            pygame.image.load("assets/morte/a (8).png").convert_alpha(),
            pygame.image.load("assets/morte/a (9).png").convert_alpha(),
            pygame.image.load("assets/morte/a (10).png").convert_alpha(),
            pygame.image.load("assets/morte/a (11).png").convert_alpha(), 
            pygame.image.load("assets/morte/a (12).png").convert_alpha(),
            pygame.image.load("assets/morte/a (13).png").convert_alpha(), 
    ]
effettomorte = [ pygame.transform.scale(image, (600, 300)) for image in effettomorte ]

xmouse1 = 1000
ymouse1 = 400
mouse1 = (xmouse1,ymouse1)
xmouse2 = 900
ymouse2 = 400
mouse2 = (xmouse2,ymouse2)



pygame.mouse.set_visible(False)

#musica
pygame.mixer.pre_init(44100,-16,2,512)
pygame.mixer.set_num_channels(64)

music = pygame.mixer.music.load("assets/suoni-amongus/THEME.mp3")

jumpsound = pygame.mixer.Sound("assets/suoni-amongus/SALTO.mp3")
jumpsound.set_volume(0.05)
mortesound = pygame.mixer.Sound("assets/suoni-amongus/MORTE.mp3")
startsound = pygame.mixer.Sound("assets/suoni-amongus/3,2,1,GO.mp3")
endsound = pygame.mixer.Sound("assets/suoni-amongus/amogus-FINE.mp3")
selectsound = pygame.mixer.Sound("assets/suoni-amongus/select.mp3")
colpitosound = pygame.mixer.Sound("assets/suoni-amongus/COLTELLATA.mp3")
finesound = pygame.mixer.Sound("assets/suoni-amongus/FINE.mp3")
smashsound = pygame.mixer.Sound("assets/suoni-amongus/SMASH.mp3")
smashsound.set_volume(0.5)


x1 = 500
y1 = 530
velocitax1 = 0
velocitay1 = 0
gravity1 = 0.5
player_left_frame1 = 0
move1 = "stand"
direction1 = "neutral" #neutral #top #down #left #right
face1 = False #False se destra True si sinistra
player_right_frame1 = 0
player_jump_frame1 = 0
salti1 = 2 
jump_partivle_frame1 = 0
morte_frame1 = 0
particlepos1 = (0,0)
ledge1 = 0
ledgeframe1 = 0
xmorte1 = 0
ymorte1 = 0
dmorte1 = "null"
zuccaa1 = 0
balersas1 = 0
spawning1 = False
canmove1 = True
shieldhealth1 = 50
shielded1 = False
angolo1 = 430
attackframe1 = 0
attackindex1 = 0
yattack1 = 0
xattack1 = 0
player1_sprites = []
#0 stand 1 jump 2 land 3 standleft 4 jumpleft 5 landleft 6 particle 7 grab  8 grableft 
#9 attackright 10 attackleft 11 attackup 12 attackdown 13 pugnaleright 14 pugnaleleft 15 ballo
player1_right = []
player1_left = []
frameballo1 = 0
palle1 = 0
morto1 = False
percentuale1 = 0
vite1 = 3
lag1 = 0
knockbackframes1 = 0   
knockbackused1 = 0
velgrav1 = 0

x2 = 1000
y2 = 530
velocitax2 = 0
velocitay2 = 0
gravity2 = 0.5
player_left_frame2 = 0
move2 = "stand"
direction2 = "neutral" #neutral #top #down #left #right
face2 = True #False se destra True si sinistra
player_right_frame2 = 0
player_jump_frame2 = 0
salti2 = 2 
jump_particle_frame2 = 0
morte_frame2 = 0
particlepos2 = (0,0)
ledge2 = 0
ledgeframe2 = 0
xmorte2 = 0
ymorte2 = 0
dmorte2 = "null"
zuccaa2 = 0
balersas2 = 0
spawning2 = False
canmove2 = True
shieldhealth2 = 50
shielded2 = False
angolo2 = 430
attackframe2 = 0
attackindex2 = 0
yattack2 = 0
xattack2 = 0
player2_sprites = []
#0 stand 1 jump 2 land 3 standleft 4 jumpleft 5 landleft 6 particle 7 grab  8 grableft 
#9 attackright 10 attackleft 11 attackup 12 attackdown 13 pugnaleright 14 pugnaleleft 15 ballo
player2_right = []
player2_left = []
frameballo2 = 0
palle2 = 0
morto2 = False
percentuale2 = 0
vite2 = 3
lag2 = 0
knockbackframes2 = 0   
knockbackused2 = 0
velgrav2 = 0

player1 = pygame.Rect(x1, y1,50,70)
player2 = pygame.Rect(x2, y2,50,70)
vince = 0   #vince rosso 1 vince blu 2
vince_frame = 0


# FUNZIONI


def loadplayer1(dirc):
    global player1_sprites,player1_right,player1_left
    player_stand_right = pygame.image.load(dirc+"/stand.png").convert_alpha()
    player_stand_right = pygame.transform.scale(player_stand_right, (50, 70))   
  
    player_jump_right = pygame.image.load(dirc+"/jump.png").convert_alpha()
    player_jump_right = pygame.transform.scale(player_jump_right, (50, 70))   
    
    player_land_right= pygame.image.load(dirc+"/duck.png").convert_alpha()
    player_land_right = pygame.transform.scale(player_land_right, (50, 70))   
    
    player_grab_right= pygame.image.load(dirc+"/ledgegrab.png").convert_alpha()
    player_grab_right = pygame.transform.scale(player_grab_right, (50, 30))   
    player_grab_right = pygame.transform.rotate(player_grab_right,-5)
   
    
    player_stand_left = pygame.transform.flip(player_stand_right, True, False)
    
    player_jump_left = pygame.transform.flip(player_jump_right, True, False)
    
    player_land_left = pygame.transform.flip(player_land_right, True, False)
    
    player_grab_left = pygame.transform.flip(player_grab_right, True, False)
    
    
    player_jump_particle = pygame.image.load(dirc+"/jump_particle.png").convert_alpha()
    player_jump_particle = pygame.transform.scale(player_jump_particle, (100, 100))   
    player_jump_particle = pygame.transform.flip(player_jump_particle, False, True)

    attack_stance_right = pygame.image.load(dirc+"/attaccougo-2.png").convert_alpha()
    attack_stance_right = pygame.transform.scale(attack_stance_right,(50,70))
    attack_stance_left = pygame.transform.flip(attack_stance_right,True,False)
    
    attack_up = pygame.image.load(dirc+"/attaccougo-3.png").convert_alpha()
    attack_up = pygame.transform.scale(attack_up,(50,70))
    
    attack_down = pygame.image.load(dirc+"/attaccougo-1.png").convert_alpha()
    attack_down = pygame.transform.scale(attack_down,(70,60))
    ballo = [
        
            pygame.image.load(dirc+"/frame1.png").convert_alpha(),
            pygame.image.load(dirc+"/frame2.png").convert_alpha(),
            pygame.image.load(dirc+"/frame3.png").convert_alpha(),
            pygame.image.load(dirc+"/frame4.png").convert_alpha(),
            pygame.image.load(dirc+"/frame5.png").convert_alpha(),
            pygame.image.load(dirc+"/frame6.png").convert_alpha(),
    ]
    ballo = [ pygame.transform.scale(image, (100, 100)) for image in ballo ]
    
    pugnaleright = pygame.image.load(dirc +"/Pugnale.png").convert_alpha()
    pugnaleright = pygame.transform.scale(pugnaleright,(75,15))
    pugnaleleft = pygame.transform.flip(pugnaleright, True, False)
    

    
    player1_right = [
    pygame.image.load(dirc+"/walk01.png").convert_alpha(),
    pygame.image.load(dirc+"/walk02.png").convert_alpha(),
    pygame.image.load(dirc+"/walk03.png").convert_alpha(),
    pygame.image.load(dirc+"/walk04.png").convert_alpha(),
    pygame.image.load(dirc+"/walk05.png").convert_alpha(),
    pygame.image.load(dirc+"/walk06.png").convert_alpha(),
    pygame.image.load(dirc+"/walk07.png").convert_alpha(),
    pygame.image.load(dirc+"/walk08.png").convert_alpha(),
    pygame.image.load(dirc+"/walk09.png").convert_alpha(),
    pygame.image.load(dirc+"/walk10.png").convert_alpha(),
    pygame.image.load(dirc+"/walk11.png").convert_alpha(),
    ]
    player1_right = [ pygame.transform.scale(image, (50, 70)) for image in player1_right ]
    
    player1_left = [ pygame.transform.flip(image, True, False) for image in player1_right ]
    
    player1_sprites =[
        player_stand_right,
        player_jump_right,
        player_land_right,
        player_stand_left,
        player_jump_left,
        player_land_left,
        player_jump_particle,
        player_grab_right,
        player_grab_left,
        attack_stance_right,
        attack_stance_left,
        attack_up,
        attack_down,
        pugnaleright,
        pugnaleleft,
        ballo
    ]
    
def MovimentoGravità1():
    global x1,y1,player_jump_frame1,player_left_frame1,player_right_frame1,move1,salti1,jump_partivle_frame1,particlepos1,morto1,menùù,direction1,face1
    global player1,morte_frame1,spawning1,ledge1,ledgeframe1,ymorte1,xmorte1,zuccaa1,balersas1,dmorte1,joystick1,canmove1,vite1,velocitax1,velocitay1,invicframe1,percentuale1
    
    player1 = pygame.Rect(x1, y1,50,70)
    jump = False
    m = 0
    k = 0    
    
    #joystick1
    horiz_move1 = round(joystick1.get_axis(0),2)
    vert_move1 = round(joystick1.get_axis(1),2)
    
    if canmove1:
        if horiz_move1<-sens:
            if velocitax1 > -10 and velocitax1<=0 :
                velocitax1 += horiz_move1
            if face1 == False:
                velocitax1 = 0 
            move1 = "walk"
            direction1 = "left"
            face1 = True
        else:
            m = m + 1
            
        if horiz_move1>sens:
            if velocitax1 < 10 and velocitax1>=0:
                velocitax1 += horiz_move1
            if face1 == True:
                velocitax1 = 0 
            move1 = "walk"
            direction1 = "right"
            face1 = False 
        else:
            m = m + 1
        
        if vert_move1>sens:
            if ((y1 < 530 or x1<335 or x1>1215) or (y1>=640)) and player_jump_frame1==0:
                y1 += 10
            direction1 = "down"
        else:
            k = k + 1
        if vert_move1<-sens:
            direction1 = "up"
        else:
            k = k + 1
            
        
        if joystick1buttons(joystick1,0)  or joystick1buttons(joystick1,1)   or (saltoconlevetta and (vert_move1<-sens)):
            jump = True
            
    
    x1 += velocitax1
    
    y1 += velocitay1
        
    
    
        
    if m == 2 or morte_frame1!= 0 or canmove1==False:
        move1 = "stand"
    
    if velocitax1 > 0:
        velocitax1 -= 0.5
    elif velocitax1 < 0:
        velocitax1 += 0.5 
            
    if k == 2 and m == 2:
        direction1 = "neutral"
    
    x1 = round(x1)
    y1 = round(y1)
        
    if (pygame.Rect.colliderect(piattaformara, player1) and pygame.Rect.colliderect(piatt1, player1)):
        ledge1= 1
            
    elif (pygame.Rect.colliderect(piattaformara, player1) and pygame.Rect.colliderect(piatt2, player1)):
        ledge1= 2
        
    if pygame.Rect.colliderect(piattaformara, player1) :
        if y1 > 530 and y1<600:
            y1 = 530
        else:
            if invicframe1 == 0:
                y1 = 650
            else:
                y1 = 530
        
        
    if ledge1 == 1:
        ledge1 = 3
        ledgeframe1 = 20
        invicframe1 = 40
            
    elif ledge1 == 2:
        ledge1= 4
        ledgeframe1 = 20
        invicframe1 = 40
    
    if ledge1 == 3:
        telecamera.blit(player1_sprites[7],(365,575))
        y1 = 580
        x1 = 330
    
            
    elif ledge1 == 4:
        telecamera.blit(player1_sprites[8],(1175,575))
        y1 = 580
        x1 = 1220
        
        
        
    
    if (ledgeframe1<=0 and ledge1!=0) and (move1=="walk" or jump == True or knockbackframes1!= 0):
        if ledge1 == 3:
            if not face1:
                y1 = 530
                x1 = 385
            ledge1 = 0
            
        elif ledge1 == 4:
            if face1:
                y1 = 530
                x1 = 1165
            ledge1 = 0
            
            
        if move1 == "walk" or jump:
            invicframe1 = 5    
        print(ledgeframe1,ledge1)
        print(move1,jump,knockbackframes1)

    ledgeframe1-=1

        
    
    if ((y1 < 530 or x1<335 or x1>1215) or (y1>=640)) and not spawning1:
        if velocitay1 < 7:
            velocitay1 += gravity1
          
        move1 = "land"
    else:
        velocitay1 = 0
    
    
    if player_jump_frame1 > 0:
        y1 = y1 - velocitay1- 7
        move1 = "jump"
        player_jump_frame1 -= 1

    if y1 == 530  and (x1>335 and x1<1215) or ledge1!=0 or spawning1:
        salti1 = 2

    
    if jump:
        if ((y1==530 and (x1>335 and x1<1215)) or (salti1>0 and move1 == "land" and player_jump_frame1 == 0)) and not spawning1:
            jumpsound.play()
            player_jump_frame1 = 20
            salti1 = salti1 - 1
            jump_partivle_frame1 = 10
            particlepos1 = (x1-20,y1+30)
    
    if  jump_partivle_frame1>0:
        jump_partivle_frame1 -= 1
        telecamera.blit(player1_sprites[6],particlepos1)  
           
           
           
    if morto1:
        morte_frame1 = 300
        
    
    
    if morte_frame1 >0:
        if morte_frame1<=300 and morte_frame1>=240:
            
            joystick1.rumble(1,1,5)
                
            if morte_frame1>=263:
                if dmorte1 == "left":
                    telecamera.blit(effettomorte[ zuccaa1], (-100,ymorte1-125))
                    if balersas1 == 2:
                        zuccaa1 = (zuccaa1 + 1) % len(effettomorte)
                        balersas1 = 0
                    else:
                        balersas1 = balersas1 + 1
                    
                    
                elif dmorte1 == "right":
                    ferretti = effettomorte
                    ferretti = [ pygame.transform.rotate(image,180) for image in ferretti ]
                    
                    telecamera.blit(ferretti[zuccaa1], (1200,ymorte1-115))
                    if balersas1 == 2:
                        zuccaa1 = (zuccaa1 + 1) % len(effettomorte)
                        balersas1 = 0
                    else:
                        balersas1 = balersas1 + 1
                    
                    
                elif dmorte1 == "up":
                    ferretti = effettomorte
                    ferretti = [ pygame.transform.rotate(image,270) for image in ferretti ]
                    
                    telecamera.blit(ferretti[ round(zuccaa1)], (xmorte1-125,-100))
                    if balersas1 == 2:
                        zuccaa1 = (zuccaa1 + 1) % len(effettomorte)
                        balersas1 = 0
                    else:
                        balersas1 = balersas1 + 1
                    
                elif dmorte1 == "down":
                    ferretti = effettomorte
                    ferretti = [ pygame.transform.rotate(image,90) for image in ferretti ]
                    
                    telecamera.blit(ferretti[ round(zuccaa1)], (xmorte1-125,300))
                    if balersas1 == 2:
                        zuccaa1 = (zuccaa1 + 1) % len(effettomorte)
                        balersas1 = 0
                    else:
                        balersas1 = balersas1 + 1
                    
            x1 = xmorte1
            y1 = ymorte1   
                    
            
            
        elif (morte_frame1<240 or (m == 1 and m!=0)) and vince_frame == 0:
            telecamera.blit(spawn,(725,300))
            x1 = 775
            y1 = 230
            spawning1 = True
            invicframe1 = 100
            if (m == 1 and m!=0) and morte_frame1<180:
                morte_frame1 = 1
                invicframe1 = 20
        morte_frame1 -=1
        morto1 = False
    else:
        spawning1 = False
    
    
   
    
    if y1>1000 and morte_frame1==0:
        print("morto a ",x1,"down")
        
        morto1 = True
        ymorte1 = y1
        xmorte1 = x1
        if xmorte1>1450:
            xmorte1 = 1450
        elif xmorte1<100:
            xmorte1 = 100
        dmorte1 = "down"
    if y1<-200 and morte_frame1==0:
        print("morto a ",x1,"up")
        
        morto1 = True
        dmorte1 = "up"
        ymorte1 = y1
        xmorte1 = x1
        if xmorte1>1450:
            xmorte1 = 1450
        elif xmorte1<100:
            xmorte1 = 100
    if x1>1800 and morte_frame1==0:
        print("morto a ",y1,"side right")
        
        morto1= True
        ymorte1 = y1
        xmorte1 = x1
        dmorte1 = "right"
        if ymorte1>650:
            ymorte1 = 650
        elif ymorte1<100:
            ymorte1 = 100
    if x1<-200 and morte_frame1==0:
        print("morto a ",y1,"side left")
        
        ymorte1 = y1
        xmorte1 = x1
        morto1 = True
        dmorte1 = "left"
        if ymorte1>650:
            ymorte1 = 650
        elif ymorte1<100:
            ymorte1 = 100
    if morto1 and morte_frame1==0:
        mortesound.play()
        vite1 = vite1 - 1
        percentuale1 = 0
    
def attacchiplayer1():
    global x1,y1,direction1,shieldhealth1,canmove1,shielded1,angolo1,move1,attackframe1,attackindex1,yattack1,xattack1,lag1,rect_attacco1
    #joybutton y = 0 x = 1 a = 2 b = 3 l = 4 r = 5 pause = 6
    
    scudo = pygame.Surface((100, 100), pygame.SRCALPHA)
    
    rect_attacco1 = pygame.Rect(-1000,-1000,10,10)

    if  ledge1 ==0 and lag1 == 0:
        if joystick1buttons(joystick1,2)  and not shielded1 and (direction1 == "right" or direction1 == "left" or y1 == 530  and (x1>335 and x1<1215)and not direction1 == "down" and not direction1 == "up") : #jab /foward tilt / foward air
            if not face1:
                angolo1 = 270
            else:
                angolo1 = 90 
            attackframe1 = 18
            if direction1 == "right" or  not face1:
                attackindex1 = 0 
            if direction1 == "left"or  face1:
                attackindex1 = 4
            lag1= 25
            
        elif joystick1buttons(joystick1,2) and not shielded1 and direction1 == "down" and y1 == 530  and (x1>335 and x1<1215): #down tilt
            attackframe1 = 10
            
            if (direction1 == "down" and not face1):
                attackindex1 = 1
            if (direction1 == "down" and  face1):
                attackindex1 = 5
                
            lag1= 25
            if not face1:
                yattack1 = y1 + 55
                xattack1 = x1
            else:
                yattack1 = y1 + 55
                xattack1 = x1 - 25
                
        elif joystick1buttons(joystick1,2)  and not shielded1 and direction1 == "up": #up tilt
            attackframe1 = 18
            attackindex1 = 2
            angolo1 = 180
            lag1= 25

        elif joystick1buttons(joystick1,2) and not shielded1 and direction1 == "down" and ((y1 < 530 or x1<335 or x1>1215) or (y1>=640)): #down air
            attackframe1 = 18
            attackindex1 = 3
            angolo1 = 360
            lag1= 25
            
        elif  joystick1buttons(joystick1,2) and not shielded1 and direction1 == "neutral" and  ((y1 < 530 or x1<335 or x1>1215) or (y1>=640)):
            if face1:
                attackindex1 = 6
            else:
                attackindex1 = 7
            attackframe1 = 24
            angolo1 = 280
            lag1= 30
            
        elif  joystick1buttons(joystick1,7) and not shielded1 and y1 == 530  and (x1>335 and x1<1215):
            move1 = "ballo"
            canmove1 = False
            
           
        elif shielded1 and not (joystick1buttons(joystick1,4) and shieldhealth1 >0):
            lag1 = 15
            
            shielded1 = False
                
        elif joystick1buttons(joystick1,4) and shieldhealth1 >0:
            canmove1 = False
            shielded1 = True
            shieldhealth1 = shieldhealth1 - 0.2                                         #scudo
            pygame.draw.circle(scudo, (0, 0, 255, 128), (50, 50), shieldhealth1)
            telecamera.blit(scudo, (x1-25, y1-15))      
            
        else:
            canmove1 = True
            shielded1 = False
            
        if not shielded1:
            if shieldhealth1 < 50:
                shieldhealth1 = shieldhealth1 + 0.5
            if shieldhealth1 > 50:
                shieldhealth1 = 50
                
        if shieldhealth1 < 0:
            shieldhealth1 = 0 
    
            
        
        
         
    
    if attackframe1 > 0 and attackindex1==0:
        
       
        pivot = [x1+50,y1+20]
        offset = pygame.math.Vector2(40, 0)
        move1 = "attackside"
        rotated_image, rect_attacco1 = rotate(player1_sprites[13], angolo1, pivot, offset)
        telecamera.blit(rotated_image, rect_attacco1)  
        
        canmove1 = False
        angolo1 += 10
        attackframe1 -=1

    elif attackframe1 > 0 and attackindex1==4 :
       
        pivot = [x1,y1+20]
        offset = pygame.math.Vector2(-40, 0)
        move1 = "attackside"
        rotated_image, rect_attacco1 = rotate(player1_sprites[14], angolo1, pivot, offset)
        telecamera.blit(rotated_image, rect_attacco1)  
        
        
        canmove1 = False
        angolo1 -= 10
        attackframe1 -=1
            
            
    if attackframe1 > 0 and attackindex1==1:
        xattack1 += 5
        telecamera.blit(player1_sprites[13], (xattack1,yattack1)) 
        rect_attacco1 = pygame.Rect(xattack1, yattack1, 75, 15)
        
        canmove1 = False
        attackframe1 -=1
            
    elif attackframe1 > 0 and attackindex1==5:
        xattack1 -= 5
        telecamera.blit(player1_sprites[14], (xattack1,yattack1)) 
        rect_attacco1 = pygame.Rect(xattack1, yattack1, 75, 15)
            
        canmove1 = False
        attackframe1 -=1
    
    if attackframe1 > 0 and attackindex1==2:
       
        pivot = [x1+25,y1]
        offset = pygame.math.Vector2(40, 0)
        move1 = "attackup"
        rotated_image, rect_attacco1 = rotate(player1_sprites[13], angolo1, pivot, offset)
        telecamera.blit(rotated_image, rect_attacco1)  
        
        canmove1 = False
        angolo1 += 10
        attackframe1 -=1
        
    if attackframe1 > 0 and attackindex1==3:
        
        pivot = [x1+25,y1+75]
        offset = pygame.math.Vector2(40, 0)
        move1 = "attackdown"
        rotated_image, rect_attacco1 = rotate(player1_sprites[13], angolo1, pivot, offset)
        telecamera.blit(rotated_image, rect_attacco1)  
        
        canmove1 = False
        angolo1 += 10
        attackframe1 -=1
        
    if attackframe1 > 0 and attackindex1==6:
        
        
        pivot = [x1+25,y1+35]
        offset = pygame.math.Vector2(40, 0)
        move1 = "neutralair"
        rotated_image, rect_attacco1 = rotate(pygame.transform.flip(player1_sprites[13],False,True), angolo1, pivot, offset)
        telecamera.blit(rotated_image, rect_attacco1)  
        
        canmove1 = False
        angolo1 -= 15
        attackframe1 -=1
        
    if attackframe1 > 0 and attackindex1==7:
        
        
        pivot = [x1+25,y1+35]
        offset = pygame.math.Vector2(40, 0)
        move1 = "neutralair"
        
        rotated_image, rect_attacco1 = rotate(player1_sprites[13], angolo1, pivot, offset)
        telecamera.blit(rotated_image, rect_attacco1)  
        
        canmove1 = False
        angolo1 += 15
        attackframe1 -=1
        
        
    if lag1>0:
        lag1 -= 1
    


zucca1 = 0 
zucca2 = 0 
def blitplayer1():
    
    
    global player1,player_left_frame1,player_right_frame1,shielded1,shieldhealth1,canmove1,frameballo1,palle1,zucca1
    if morte_frame1 < 240 and (vince_frame == 0 or vince == 2 ):
        if zucca1 == 2 or invicframe1 == 0:
            if move1 == "walk":
                if face1:
                    telecamera.blit(player1_left[ player_left_frame1 ], (x1,y1))
                            
                    player_left_frame1 = (player_left_frame1 + 1) % len(player1_left)  
                else:
                    telecamera.blit(player1_right[ player_right_frame1 ], (x1,y1))
                
                    player_right_frame1 = (player_right_frame1 + 1) % len(player1_right)       
                
            elif move1 == "jump":
                if face1:
                    telecamera.blit(player1_sprites[4], (x1,y1))
                    
                else:
                    telecamera.blit(player1_sprites[1], (x1,y1))
                    
            elif move1 == "land":
                if face1:
                    telecamera.blit(player1_sprites[5], (x1,y1))
                    
                else:
                    telecamera.blit(player1_sprites[2], (x1,y1))
                    
            elif move1 == "stand":
                if face1:
                    telecamera.blit(player1_sprites[3], (x1,y1))
                    
                else:
                    telecamera.blit(player1_sprites[0], (x1,y1))
                    
            elif move1 == "attackside":
                if face1:
                    telecamera.blit(player1_sprites[10], (x1,y1))
                else:
                    telecamera.blit(player1_sprites[9], (x1,y1))
            elif move1 == "attackup":  
                telecamera.blit(player1_sprites[11], (x1,y1)) 
            elif move1 == "attackdown":
                telecamera.blit(player1_sprites[12], (x1-10,y1))   
            elif move1 == "ballo":
                telecamera.blit(player1_sprites[15][frameballo1],(x1-25,y1-10))
                if palle1 == 0:
                    frameballo1 +=1
                    palle1 = 2
                else:
                    palle1 = palle1 - 1
                    
                if frameballo1 > len(player1_sprites[15])-1:
                    frameballo1 = 0     
            elif move1 == "neutralair":
                pivot = [x1+25,y1+35]
                offset = pygame.math.Vector2(0, 0)
                playerblite, player1 = rotate(player1_sprites[0], angolo1, pivot, offset)      
                telecamera.blit(playerblite, player1)
            zucca1 = 0
        else:
            zucca1 += 1




        
        
    

        
    

    
    
def loadplayer2(dirc):
    global player2_sprites,player2_right,player2_left
    player_stand_right = pygame.image.load(dirc+"/stand.png").convert_alpha()
    player_stand_right = pygame.transform.scale(player_stand_right, (50, 70))   
  
    player_jump_right = pygame.image.load(dirc+"/jump.png").convert_alpha()
    player_jump_right = pygame.transform.scale(player_jump_right, (50, 70))   
    
    player_land_right= pygame.image.load(dirc+"/duck.png").convert_alpha()
    player_land_right = pygame.transform.scale(player_land_right, (50, 70))   
    
    player_grab_right= pygame.image.load(dirc+"/ledgegrab.png").convert_alpha()
    player_grab_right = pygame.transform.scale(player_grab_right, (50, 30))   
    player_grab_right = pygame.transform.rotate(player_grab_right,-5)
   
    
    player_stand_left = pygame.transform.flip(player_stand_right, True, False)
    
    player_jump_left = pygame.transform.flip(player_jump_right, True, False)
    
    player_land_left = pygame.transform.flip(player_land_right, True, False)
    
    player_grab_left = pygame.transform.flip(player_grab_right, True, False)
    
    
    player_jump_particle = pygame.image.load(dirc+"/jump_particle.png").convert_alpha()
    player_jump_particle = pygame.transform.scale(player_jump_particle, (100, 100))   
    player_jump_particle = pygame.transform.flip(player_jump_particle, False, True)

    attack_stance_right = pygame.image.load(dirc+"/attaccougo-2.png").convert_alpha()
    attack_stance_right = pygame.transform.scale(attack_stance_right,(50,70))
    attack_stance_left = pygame.transform.flip(attack_stance_right,True,False)
    
    attack_up = pygame.image.load(dirc+"/attaccougo-3.png").convert_alpha()
    attack_up = pygame.transform.scale(attack_up,(50,70))
    
    attack_down = pygame.image.load(dirc+"/attaccougo-1.png").convert_alpha()
    attack_down = pygame.transform.scale(attack_down,(70,60))
    ballo = [
        
            pygame.image.load(dirc+"/frame1.png").convert_alpha(),
            pygame.image.load(dirc+"/frame2.png").convert_alpha(),
            pygame.image.load(dirc+"/frame3.png").convert_alpha(),
            pygame.image.load(dirc+"/frame4.png").convert_alpha(),
            pygame.image.load(dirc+"/frame5.png").convert_alpha(),
            pygame.image.load(dirc+"/frame6.png").convert_alpha(),
    ]
    ballo = [ pygame.transform.scale(image, (100, 100)) for image in ballo ]
    
    pugnaleright = pygame.image.load(dirc +"/Pugnale.png").convert_alpha()
    pugnaleright = pygame.transform.scale(pugnaleright,(75,15))
    pugnaleleft = pygame.transform.flip(pugnaleright, True, False)
    

    
    player2_right = [
    pygame.image.load(dirc+"/walk01.png").convert_alpha(),
    pygame.image.load(dirc+"/walk02.png").convert_alpha(),
    pygame.image.load(dirc+"/walk03.png").convert_alpha(),
    pygame.image.load(dirc+"/walk04.png").convert_alpha(),
    pygame.image.load(dirc+"/walk05.png").convert_alpha(),
    pygame.image.load(dirc+"/walk06.png").convert_alpha(),
    pygame.image.load(dirc+"/walk07.png").convert_alpha(),
    pygame.image.load(dirc+"/walk08.png").convert_alpha(),
    pygame.image.load(dirc+"/walk09.png").convert_alpha(),
    pygame.image.load(dirc+"/walk10.png").convert_alpha(),
    pygame.image.load(dirc+"/walk11.png").convert_alpha(),
    ]
    player2_right = [ pygame.transform.scale(image, (50, 70)) for image in player2_right ]
    player2_left = [ pygame.transform.flip(image, True, False) for image in player2_right ]
    
    player2_sprites =[
        player_stand_right,
        player_jump_right,
        player_land_right,
        player_stand_left,
        player_jump_left,
        player_land_left,
        player_jump_particle,
        player_grab_right,
        player_grab_left,
        attack_stance_right,
        attack_stance_left,
        attack_up,
        attack_down,
        pugnaleright,
        pugnaleleft,
        ballo
    ]
    
def MovimentoGravità2():
    
    global x2,y2,player_jump_frame2,player_left_frame2,player_right_frame2,move2,salti2,jump_particle_frame2,particlepos2,menùù,direction2,face2,invicframe2,velgrav2
    global player2,morte_frame2,spawning2,ledge2,ledgeframe2,ymorte2,xmorte2,zuccaa2,balersas2,dmorte2,joystick1,canmove2,morto2,vite2,velocitay2,velocitax2,percentuale2
    
    player2 = pygame.Rect(x2, y2,50,70)
    jump = False
    m = 0
    k = 0    
    
    #joystick1
    horiz_move2 = round(joystick2.get_axis(0),2)
    vert_move2 = round(joystick2.get_axis(1),2)
    
    if canmove2:
        if horiz_move2<-sens:
            if velocitax2 > -10 and velocitax2<=0 :
                velocitax2 += horiz_move2
            if face2 == False:
                velocitax2 = 0 
            move2 = "walk"
            direction2 = "left"
            face2 = True
        else:
            m = m + 1
            
        if horiz_move2>sens:
            if velocitax2 < 10 and velocitax2>=0:
                velocitax2 += horiz_move2
            if face2 == True:
                velocitax2 = 0 
            move2 = "walk"
            direction2 = "right"
            face2 = False 
        else:
            m = m + 1
        
        if vert_move2>sens:
            if ((y2 < 530 or x2<335 or x2>1215) or (y2>=640)) and player_jump_frame2==0:
                y2 += 10
            direction2 = "down"
        else:
            k = k + 1
        if vert_move2<-sens:
            direction2 = "up"
        else:
            k = k + 1
            
        
        if joystick1buttons(joystick2,0)  or joystick1buttons(joystick2,1)   or (saltoconlevetta and (vert_move2<-sens)):
            jump = True
            
    y2 += velocitay2
    x2 += velocitax2
   
    
    
        
    if m == 2 or morte_frame2!= 0 or canmove2==False:
        move2 = "stand"
    
    if velocitax2 > 0:
        velocitax2 -= 0.5
    elif velocitax2 < 0:
        velocitax2 += 0.5   
    if k == 2 and m == 2:
        direction2 = "neutral"
    
    x2 = round(x2)
    y2 = round(y2)
    
    
        
    if (pygame.Rect.colliderect(piattaformara, player2) and pygame.Rect.colliderect(piatt1, player2)):
        ledge2= 1
            
    elif (pygame.Rect.colliderect(piattaformara, player2) and pygame.Rect.colliderect(piatt2, player2)):
        ledge2= 2
        
    if pygame.Rect.colliderect(piattaformara, player2) :
        if y2 > 530 and y2<600:
            y2 = 530
        else:
            if invicframe2 == 0:
                y2 = 650
            else:
                y2 = 530
        
        
    if ledge2 == 1:
        ledge2 = 3
        ledgeframe2 = 20
        invicframe2 = 40 
            
    elif ledge2 == 2:
        ledge2= 4
        ledgeframe2 = 20
        invicframe2 = 40 
    
    
    if ledge2 == 3:
        telecamera.blit(player2_sprites[7],(365,575))
        y2 = 580
        x2 = 330
    
            
    elif ledge2 == 4:
        telecamera.blit(player2_sprites[8],(1175,575))
        y2 = 580
        x2 = 1220
        
        
        
    
    if (ledgeframe2<=0 and ledge2!=0) and (move2=="walk" or jump == True or knockbackframes2!= 0):
        if ledge2== 3:
            if not face2:
                y2 = 530
                x2 = 385
            ledge2= 0
            
        elif ledge2== 4:
            if face2:
                y2 = 530
                x2 = 1165
            ledge2= 0
            
        if move2 == "walk" or jump:
            invicframe2 = 5    
         
        
   
    ledgeframe2-=1

        
    
    if ((y2 < 530 or x2<335 or x2>1215) or (y2>=640)) and not spawning2:
        if velocitay2 < 7:
            velocitay2 += gravity2
        
        move2 = "land"
        
    else:
        velocitay2 = 0
        
    
    if player_jump_frame2 > 0:
        y2 = y2 - velocitay2 - 7
        move2 = "jump"
        player_jump_frame2 -= 1

    if y2 == 530  and (x2>335 and x2<1215) or ledge2!=0 or spawning2:
        salti2 = 2
   
    
    if jump:
        if ((y2==530 and (x2>335 and x2<1215)) or (salti2>0 and move2 == "land" and player_jump_frame2 == 0)) and not spawning2:
            jumpsound.play()
            player_jump_frame2 = 20
            salti2 = salti2 - 1
            jump_particle_frame2 = 10
            particlepos2 = (x2-20,y2+30)
    
    if  jump_particle_frame2>0:
        jump_particle_frame2 -= 1
        telecamera.blit(player2_sprites[6],particlepos2)     
    
    
    if morto2:
        morte_frame2 = 300
    if morte_frame2 >0:
        if morte_frame2<=300 and morte_frame2>=240:
            
            joystick2.rumble(1,1,5)
                
            if morte_frame2>=263:
                if dmorte2 == "left":
                    telecamera.blit(effettomorte[ zuccaa2], (-100,ymorte2-125))
                    if balersas2 == 2:
                        zuccaa2 = (zuccaa2 + 1) % len(effettomorte)
                        balersas2 = 0
                    else:
                        balersas2 = balersas2 + 1
                    
                    
                elif dmorte2 == "right":
                    ferretti = effettomorte
                    ferretti = [ pygame.transform.rotate(image,180) for image in ferretti ]
                    
                    telecamera.blit(ferretti[zuccaa2], (1200,ymorte2-115))
                    if balersas2 == 2:
                        zuccaa2 = (zuccaa2 + 1) % len(effettomorte)
                        balersas2 = 0
                    else:
                        balersas2 = balersas2 + 1
                    
                    
                elif dmorte2 == "up":
                    ferretti = effettomorte
                    ferretti = [ pygame.transform.rotate(image,270) for image in ferretti ]
                    
                    telecamera.blit(ferretti[ round(zuccaa2)], (xmorte2-125,-100))
                    if balersas2 == 2:
                        zuccaa2 = (zuccaa2 + 1) % len(effettomorte)
                        balersas2 = 0
                    else:
                        balersas2 = balersas2 + 1
                    
                elif dmorte2 == "down":
                    ferretti = effettomorte
                    ferretti = [ pygame.transform.rotate(image,90) for image in ferretti ]
                    
                    telecamera.blit(ferretti[ round(zuccaa2)], (xmorte2-125,300))
                    if balersas2 == 2:
                        zuccaa2 = (zuccaa2 + 1) % len(effettomorte)
                        balersas2 = 0
                    else:
                        balersas2 = balersas2 + 1
            x2 = xmorte2
            y2 = ymorte2
               
                    
            
            
        elif (morte_frame2<240 or (m == 1 and m!=0)) and vince_frame == 0:
            telecamera.blit(spawn,(725,300))
            x2 = 775
            y2 = 230
            spawning2 = True
            invicframe2 = 100
            if (m == 1 and m!=0) and morte_frame2<180:
                morte_frame2 = 1
                invicframe2 = 20
        
        morte_frame2 -=1
        
        morto2 = False
    else:
        spawning2 = False
    
    
   
    
    if y2>1000 and morte_frame2==0:
        print("morto a ",x2,"down")
       
        morto2 = True
        ymorte2 = y2
        xmorte2 = x2
        if xmorte2>1450:
            xmorte2 = 1450
        elif xmorte2<100:
            xmorte2 = 100
        dmorte2 = "down"
    if y2<-200 and morte_frame2==0:
        print("morto a ",x2,"up")
        
        morto2 = True
        dmorte2 = "up"
        ymorte2 = y2
        xmorte2 = x2
        if xmorte2>1450:
            xmorte2 = 1450
        elif xmorte2<100:
            xmorte2 = 100
    if x2>1800 and morte_frame2==0:
        print("morto a ",y2,"side right")
        
        morto2= True
        ymorte2 = y2
        xmorte2 = x2
        dmorte2 = "right"
        if ymorte2>650:
            ymorte2 = 650
        elif ymorte2<100:
            ymorte2 = 100
    if x2<-200 and morte_frame2==0:
        print("morto a ",y2,"side left")
       
        ymorte2 = y2
        xmorte2 = x2
        morto2 = True
        dmorte2 = "left"
        if ymorte2>650:
            ymorte2 = 650
        elif ymorte2<100:
            ymorte2 = 100
    if morto2 and morte_frame2==0:
        mortesound.play()
        percentuale2 = 0
        vite2 = vite2 - 1
    
def attacchiplayer2():
    global x2,y2,direction2,shieldhealth2,canmove2,shielded2,angolo2,move2,attackframe2,attackindex2,yattack2,xattack2,lag2,rect_attacco2
    #joybutton y = 0 x = 1 a = 2 b = 3 l = 4 r = 5 pause = 6
    
    scudo = pygame.Surface((100, 100), pygame.SRCALPHA)
    
    rect_attacco2 = pygame.Rect(-1000,-1000,10,10)
        
        
    
        
        

        
  
    if lag2 == 0 and ledge2 ==0:
        if joystick1buttons(joystick2,2) and not shielded2 and (direction2 == "right" or direction2 == "left" or  y2 == 530  and (x2>335 and x2<1215)and not direction2 == "down" and not direction2 == "up") : #jab
            if not face2:
                angolo2 = 270
            else:
                angolo2 = 90 
            attackframe2 = 18
            if direction2 == "right" or  not face2:
                attackindex2 = 0 
            if direction2 == "left"or  face2:
                attackindex2 = 4
            lag2= 25
            
            
        elif joystick1buttons(joystick2,2) and not shielded2 and direction2 == "down" and y2 == 530  and (x2>335 and x2<1215): #down tilt
            attackframe2 = 10
            
            if (direction2 == "down" and not face2):
                attackindex2 = 1
            if (direction2 == "down" and  face2):
                attackindex2 = 5
                
            lag2= 25
            if not face2:
                yattack2 = y2 + 55
                xattack2 = x2
            else:
                yattack2 = y2 + 55
                xattack2 = x2 - 25
                
        elif joystick1buttons(joystick2,2) and not shielded2 and direction2 == "up": #up tilt
            attackframe2 = 18
            attackindex2 = 2
            lag2= 23
            angolo2 = 180

        elif joystick1buttons(joystick2,2) and not shielded2 and direction2 == "down" and not (y2 == 530  and (x2>335 and x2<1215)): #down air
            attackframe2 = 18
            attackindex2 = 3
            angolo2 = 360
            lag2= 23
            
        elif  joystick1buttons(joystick2,7) and not shielded2 and y2 == 530  and (x2>335 and x2<1215):
            move2 = "ballo"
            canmove2 = False
            
        elif  joystick1buttons(joystick2,2) and not shielded2 and direction2 == "neutral" and  ((y2 < 530 or x2<335 or x2>1215) or (y2>=640)):
            if face2:
                attackindex2 = 6
            else:
                attackindex2 = 7
            attackframe2 = 24
            angolo2 = 280
            lag2= 30
            
        elif shielded2 and not (joystick1buttons(joystick2,4) and shieldhealth2 >0):
            lag2 = 15
            
            shielded2 = False
    
        elif joystick1buttons(joystick2,4) and shieldhealth2 >0:
            canmove2 = False
            shielded2 = True
            shieldhealth2 = shieldhealth2 - 0.2                                         #scudo
            pygame.draw.circle(scudo, (255, 0, 0, 128), (50, 50), shieldhealth2)
            telecamera.blit(scudo, (x2-25, y2-15))      
            
        else:
            canmove2 = True
            shielded2 = False
            
        if not shielded2:
            if shieldhealth2 < 50:
                shieldhealth2 = shieldhealth2 + 0.5
            if shieldhealth2 > 50:
                shieldhealth2 = 50
                
        if shieldhealth2 < 0:
            shieldhealth2 = 0 
    
    
    
    if attackframe2 > 0 and attackindex2==0:
        
        
        pivot = [x2+50,y2+20]
        offset = pygame.math.Vector2(40, 0)
        move2 = "attackside"
        rotated_image, rect_attacco2 = rotate(player2_sprites[13], angolo2, pivot, offset)
        telecamera.blit(rotated_image, rect_attacco2)  
          
        canmove2 = False
        angolo2 += 10
        attackframe2 -=1

    elif attackframe2 > 0 and attackindex2==4:
        
       
        pivot = [x2,y2+20]
        offset = pygame.math.Vector2(-40, 0)
        move2 = "attackside"
        rotated_image, rect_attacco2 = rotate(player2_sprites[14], angolo2, pivot, offset)
        telecamera.blit(rotated_image, rect_attacco2)  
        
        canmove2 = False
        angolo2 -= 10
        attackframe2 -=1
            
            
    if attackframe2 > 0 and attackindex2==1:
        
        xattack2 += 5
        telecamera.blit(player2_sprites[13], (xattack2,yattack2)) 
        rect_attacco2 = pygame.Rect(xattack2, yattack2, 75, 15)
        
        canmove2 = False
        attackframe2 -=1
            
    elif attackframe2 > 0 and attackindex2==5:
        xattack2 -= 5
        telecamera.blit(player2_sprites[14], (xattack2,yattack2)) 
        rect_attacco2 = pygame.Rect(xattack2, yattack2, 75, 15)
         
        canmove2 = False
        attackframe2 -=1
    
    if attackframe2 > 0 and attackindex2==2:
        
        pivot = [x2+25,y2]
        offset = pygame.math.Vector2(40, 0)
        move2 = "attackup"
        rotated_image, rect_attacco2 = rotate(player2_sprites[13], angolo2, pivot, offset)
        telecamera.blit(rotated_image, rect_attacco2)  
          
        canmove2 = False
        angolo2 += 10
        attackframe2 -=1
        
    if attackframe2 > 0 and attackindex2==3:
        
        pivot = [x2+25,y2+75]
        offset = pygame.math.Vector2(40, 0)
        move2 = "attackdown"
        rotated_image, rect_attacco2 = rotate(player2_sprites[13], angolo2, pivot, offset)
        telecamera.blit(rotated_image, rect_attacco2)  
          
        canmove2 = False
        angolo2 += 10
        attackframe2 -=1
        
    if attackframe2 > 0 and attackindex2==6:
        
       
        pivot = [x2+25,y2+35]
        offset = pygame.math.Vector2(40, 0)
        move2 = "neutralair"
        rotated_image, rect_attacco2 = rotate(pygame.transform.flip(player2_sprites[13],False,True), angolo2, pivot, offset)
        telecamera.blit(rotated_image, rect_attacco2)  
        
        canmove2 = False
        angolo2 -= 15
        attackframe2 -=1
        
    if attackframe2 > 0 and attackindex2==7:
        
        
        pivot = [x2+25,y2+35]
        offset = pygame.math.Vector2(40, 0)
        move2 = "neutralair"
        rotated_image, rect_attacco2 = rotate(pygame.transform.flip(player2_sprites[13],False,True), angolo2, pivot, offset)
        telecamera.blit(rotated_image, rect_attacco2)  
        
        canmove2 = False
        angolo2 += 15
        attackframe2 -=1
        
    if lag2>0:
        lag2 -= 1
        
def blitplayer2():
    global player2,player_left_frame2,player_right_frame2,shielded2,shieldhealth2,canmove2,frameballo2,palle2,zucca2
    if morte_frame2 < 240 and (vince_frame == 0 or vince ==  1):
        if zucca2 == 2 or invicframe2 == 0:
            if move2 == "walk":
                if face2:
                    telecamera.blit(player2_left[ player_left_frame2 ], (x2,y2))
                            
                    player_left_frame2 = (player_left_frame2 + 1) % len(player2_left)  
                else:
                    telecamera.blit(player2_right[ player_right_frame2 ], (x2,y2))
                
                    player_right_frame2 = (player_right_frame2 + 1) % len(player2_right)       
                
            elif move2 == "jump":
                if face2:
                    telecamera.blit(player2_sprites[4], (x2,y2))
                    
                else:
                    telecamera.blit(player2_sprites[1], (x2,y2))
                    
            elif move2 == "land":
                if face2:
                    telecamera.blit(player2_sprites[5], (x2,y2))
                    
                else:
                    telecamera.blit(player2_sprites[2], (x2,y2))
                    
            elif move2 == "stand":
                if face2:
                    telecamera.blit(player2_sprites[3], (x2,y2))
                    
                else:
                    telecamera.blit(player2_sprites[0], (x2,y2))
                    
            elif move2 == "attackside":
                if face2:
                    telecamera.blit(player2_sprites[10], (x2,y2))
                else:
                    telecamera.blit(player2_sprites[9], (x2,y2))
            elif move2 == "attackup":  
                telecamera.blit(player2_sprites[11], (x2,y2)) 
            elif move2 == "attackdown":
                telecamera.blit(player2_sprites[12], (x2-10,y2))   
            elif move2 == "ballo":
                telecamera.blit(player2_sprites[15][frameballo2],(x2-25,y2-10))
                if palle2 == 0:
                    frameballo2 +=1
                    palle2 = 2
                else:
                    palle2 = palle2 - 1
                    
                if frameballo2 > len(player2_sprites[15])-1:
                    frameballo2 = 0             
            elif move2 == "neutralair":
                pivot = [x2+25,y2+35]
                offset = pygame.math.Vector2(0, 0)
                playerblite, player2 = rotate(player2_sprites[0], angolo2, pivot, offset)      
                telecamera.blit(playerblite, player2)
            zucca2 = 0
        else:
            zucca2 += 1
        
knockbacks = {"0":[(2,-1),2,5,70,120],
             "4":[(-2,-1),2,5,70,120],
             "1":[(1,-2),2,7,80,120],
             "5":[(-1,-2),2,7,80,120],
             "2":[(0,-2),5,6,120,95],
             "3":[(0,2),5,6,150,300],
             "6":[(4,-1),2,5,90,120],
             "7":[(-4,-1),2,5,90,120]
             
             }

invicframe2 = 0 
invicframe1 = 0 
movesused2 = []
movesused1 = []
staleness1 = 1
staleness2 = 1
def collissioniattacchi():
    global velgrav1,invicframe1,velgrav2,knockbackused2,knockbackframes1,movesused1,movesused2,staleness1,staleness2
    global percentuale1,percentuale2,velocitax1,lag1,lag2,velocitay1,x1,y1,x2,y2,knockbackframes2,knockbackused1,velocitay2,shieldhealth1,velocitax2,shieldhealth2,invicframe2
    if player2.colliderect(rect_attacco1):
        if knockbackframes2 == 0 :
            if invicframe2 == 0:
                arrayattacco = knockbacks[str(attackindex1)]
                if attackindex1 in movesused1:
                    staleness1 = 0.7
                else:
                    staleness1 = 1
                if shielded2 and shieldhealth2>5:
                    shieldhealth2 -= arrayattacco[2]*2*staleness1
                    invicframe2 = 10
                    lag1 = 30
                else:
                    percentuale2 += arrayattacco[2]*staleness1
                    knockbackframes2 = round((arrayattacco[1] + arrayattacco[1]*percentuale2//arrayattacco[3])*staleness1)
                    invicframe2 = knockbackframes2 + 20
                    knockbackx = (arrayattacco[0][0] + round(arrayattacco[0][0]*(percentuale2/arrayattacco[3]),2))*staleness1
                    knockbacky = (arrayattacco[0][1] + round(arrayattacco[0][1]*(percentuale2/arrayattacco[3]),2))*staleness1
                    knockbackused1 = (knockbackx,knockbacky)
                    colpitosound.play()
                if percentuale2 > arrayattacco[4]:
                    if vite2 == 1:
                        smashsound.play()
                movesused1.append(attackindex1)
                if len(movesused1)>3:
                    movesused1.pop(0)
                
    
    
            
    if knockbackframes2 > 0:
        velocitax2 += knockbackused1[0]
        velocitay2 += knockbackused1[1]
        knockbackframes2 -= 1
    
    if player1.colliderect(rect_attacco2):
        if knockbackframes1 == 0 :
            if invicframe1 == 0:
                arrayattacco = knockbacks[str(attackindex2)]
                if attackindex2 in movesused2:
                    staleness2 = 0.7
                else:
                    staleness2 = 1
                if shielded1 and shieldhealth1>5:
                    shieldhealth1 -= arrayattacco[2]*2*staleness2
                    invicframe1 = 10
                    lag2 = 30
                else:
                    percentuale1 += arrayattacco[2]*staleness2
                    knockbackframes1 = round((arrayattacco[1] + arrayattacco[1]*percentuale1//arrayattacco[3])*staleness2)
                    invicframe1 = knockbackframes1 + 20
                    knockbackx = arrayattacco[0][0] + round(arrayattacco[0][0]*(percentuale1/arrayattacco[3]),2) *staleness2
                    knockbacky = arrayattacco[0][1] + round(arrayattacco[0][1]*(percentuale1/arrayattacco[3]),2) *staleness2
                    knockbackused2 = (knockbackx,knockbacky)
                    colpitosound.play()
                if percentuale2 > arrayattacco[4]:
                    if vite2 == 1:
                        smashsound.play()
                movesused2.append(attackindex2)
                if len(movesused2)>3:
                    movesused2.pop(0)
                
    if knockbackframes1 > 0:
        velocitax1 += knockbackused2[0]
        velocitay1 += knockbackused2[1]
        knockbackframes1 -= 1
        
    if invicframe2 > 0:
        invicframe2 -= 1
    if invicframe1 > 0:
        invicframe1 -= 1
    
    
    


collega = False
def disegna_campo():
    global vince_frame,vince,percentuale1,percentuale2
    
    
    percentuale1 = round(percentuale1,2)
    percentuale2 = round(percentuale2,2)
    
    
    
    if fpscounterr == True:
        schermo.blit(fps,(20,0))
        
    if percentuale1 < 20:
        testo_percentuale1 = stile3.render(str(percentuale1) + "%", True, (255, 255, 255))
    elif percentuale1 < 50:
        testo_percentuale1 = stile3.render(str(percentuale1) + "%", True, (255, 255, 0))
    elif percentuale1 < 100:
        testo_percentuale1 = stile3.render(str(percentuale1) + "%", True, (255, 165, 0))
    elif percentuale1 >= 100:
        testo_percentuale1 = stile3.render(str(percentuale1) + "%", True, (255, 0, 0))
    schermo.blit(testo_percentuale1, (120, altezza - 100))

    if percentuale2 < 20:
        testo_percentuale2 = stile3.render(str(percentuale2) + "%", True, (255, 255, 255))
    elif percentuale2 < 50:
        testo_percentuale2 = stile3.render(str(percentuale2) + "%", True, (255, 255, 0))
    elif percentuale2 < 100:
        testo_percentuale2 = stile3.render(str(percentuale2) + "%", True, (255, 165, 0))
    elif percentuale2 >= 100:
        testo_percentuale2 = stile3.render(str(percentuale2) + "%", True, (255, 0, 0))
    schermo.blit(testo_percentuale2, (larghezza - 180, altezza - 100))
    schermo.blit(player1_sprites[0], (40, altezza - 120))
    schermo.blit(player2_sprites[0], (larghezza - 260, altezza - 120))
    
    


    if vite1 == 3:
        pygame.draw.circle(schermo,red,(50,775),10,10)
        pygame.draw.circle(schermo,red,(75,775),10,10)
        pygame.draw.circle(schermo,red,(100,775),10,10)
    if vite1 == 2:
        pygame.draw.circle(schermo,red,(50,775),10,10)
        pygame.draw.circle(schermo,red,(75,775),10,10)
    if vite1 == 1:
        pygame.draw.circle(schermo,red,(50,775),10,10)
    if vite1 == 0 and vince_frame == 0:
        
        vince_frame = 240
        vince = 1
        
    if vite2 == 3:
        pygame.draw.circle(schermo,blue,(1350,775),10,10)
        pygame.draw.circle(schermo,blue,(1375,775),10,10)   
        pygame.draw.circle(schermo,blue,(1400,775),10,10)  
    if vite2 == 2:
        pygame.draw.circle(schermo,blue,(1350,775),10,10)
        pygame.draw.circle(schermo,blue,(1375,775),10,10)    
    if vite2 == 1:
        pygame.draw.circle(schermo,blue,(1350,775),10,10)
    if vite2 == 0 and vince_frame == 0:
        
        vince_frame = 240
        vince = 2 
    
     
def Main():
    global start,starttimer,x1,x2,y1,y2
    schermo.blit(sfondo,(0,0))
    
    
    if starttimer == 240:
        startsound.play()
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
    
    if starttimer < 60 and starttimer != 0:
        scrittastart = stile3.render("GO!",True,imp,)
        
        schermo.blit(scrittastart,(800-47,400-30))
        starttimer -=1
    elif starttimer != 0 :
        schermo.blit(piattaforma,piattaformara)
        schermo.blit(player1_sprites[0],(500,530))
        schermo.blit(player2_sprites[3],(1000,530))
        disegna_campo()
        
    if starttimer == 60:
        pygame.mixer.music.unpause()
    
        
    
    
    if starttimer < 60:
        blitplayer1()
        blitplayer2()
        MovimentoGravità1()
        MovimentoGravità2()
        attacchiplayer1()
        attacchiplayer2()
        collissioniattacchi()
        
        telecamera.blit(piattaforma,piattaformara)
        zoom = pygame.transform.scale(telecamera,(2400,1200))
        
        
            
            
        
        
      
       
        
        if morte_frame1<=300 and morte_frame1>=240:
            x1zoom = xmorte1
            y1zoom = ymorte1
        elif morte_frame2<=300 and morte_frame2>=240:
            x2zoom = xmorte2
            y2zoom = ymorte2
            
        x1zoom = x1
        x2zoom = x2
        y1zoom = y1
        y2zoom = y2
        
        
            
            
        zoomx = (x1zoom+35 + x2zoom+35) // 2
        zoomy = (y1zoom+35 + y2zoom+35) // 2
        if zoomx < 550:
            zoomx = 550
            
        if zoomx > 1050:
            zoomx = 1050
            
        if zoomy > 450:
            zoomy = 450
        if zoomy < 300:
            zoomy = 300
            
        
        schermo.blit(zoom,(-zoomx*1.5+800,-zoomy*1.5+400))
        disegna_campo()
        
        
        
    else:
        scrittastart = stile3.render(str(round(starttimer//60)),True,imp,)
        schermo.blit(scrittastart,(800-17,400-30))
        starttimer -=1
    
def collegacontroller(state):
    global menùù,collega,joystick2
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
    menùù = False
    schermo.fill((255,255,255))
    scritta = stile4.render("INSERISCI "+str(2-pygame.joystick.get_count())+ " CONTROLLER ",True,red)
    
    
    schermo.blit(scritta,(517,380))
    schermo.blit(p_esci_controller,rect_controller)
    if pygame.joystick.get_count() == 0:
        Mousemove1()
    if pygame.joystick.get_count() == 1:
        Joymove1()
        joystick2 = joystick1
    elif pygame.joystick.get_count() >= 2:
        if state == "menu":
            menùù = True
        if state == "pause":
            menùù = True
        if state == "game":
            menùù = True
        collega = False
        pygame.mixer.music.unpause()
    
    
    
def menùfine():
    if vince == 1:
        schermo.blit(sfondofine1,(0,0))
    if vince == 2:
        schermo.blit(sfondofine2,(0,0))
    schermo.blit(p_menùfine,continuee)
    schermo.blit(p_esci,escii)
    cursormove()
        
def menù():
    global x1,y1,x2,y2,starttimer,player1,player2,vince_frame,vite1,vite2,vince,spawning2,spawning1,face1,face2,morte_frame1,morte_frame2,move2,move1,direction1,direction2,percentuale1,percentuale2
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.play(-1)
    schermo.blit(menùnapoli,(0,0))
    schermo.blit(p_menù,rect_menù)
    schermo.blit(p_menùesci,rect_menùesci)
    starttimer = 240
    player1 = pygame.Rect(x1, y1,50,70)
    player2 = pygame.Rect(x2, y2,50,70)
    vince_frame = 0
    vite1 = 3
    vite2 = 3
    spawning1 = False
    spawning2 = False
    face2 = True
    face1 = False
    morte_frame1 = 0
    morte_frame2 = 0
    percentuale1 = 0
    percentuale2 = 0
    move2 = "stand"
    direction2 = "neutral"
    move1 = "stand"
    direction1 = "neutral"
    x1 = 500
    y1 = 530
    x2 = 1000
    y2 = 530
    
    cursormove()

def Pausa():
    schermo.blit(sfondopausa,(0,0))
    schermo.blit(p_pausa,rect_text)
    schermo.blit(fps,(20,0))
    schermo.blit(Saltoconle,(400,485))
    schermo.blit(fpscounter,(555,585))
    schermo.blit(menùscritta,menùprincipale)
    
    if saltoconlevetta:
        schermo.blit(on,onoff)
    else:
        schermo.blit(off,onoff)
    if fpscounterr:
        schermo.blit(on,saltooo)
    else:
        schermo.blit(off,saltooo)
        
    Slider()
    cursormove()
    
    
def rotate(surface, angle, pivot, offset):
    rotated_image = pygame.transform.rotozoom(surface, -angle, 1)
    rotated_offset = offset.rotate(angle)  
    rect = rotated_image.get_rect(center=pivot+rotated_offset)
    return rotated_image, rect 

def Slider():
    pygame.draw.rect(schermo, (255, 255, 255), (slider_x-5, slider_y, PosX+10, PosY))
    rect_base.width = max(cico, 5)
    rect_basee.width = max(cico, 5)
    pygame.draw.rect(schermo, imp, rect_base)
    pygame.draw.circle(schermo,imp, (slider_x + cico + 5, slider_y + PosY // 2), 10) 
    value_label = stile0.render("Sens: ", True, imp)
    value_label_label = stile4.render(str(valore_reale/100)+" :", True, imp)
    schermo.blit(value_label, (550, 670))
    schermo.blit(value_label_label, (650, 670))

def Joymove1():
    global mouse1,xmouse1,ymouse1
    horiz_move1 = round(joystick1.get_axis(0),2)
    vert_move1 = round(joystick1.get_axis(1),2)
    if horiz_move1<-0.2:
        xmouse1 = xmouse1 + horiz_move1*10
    if horiz_move1>0.2:
        xmouse1 = xmouse1 + horiz_move1*10
    if vert_move1>0.2:
        ymouse1 = ymouse1 + vert_move1*10
    if vert_move1<-0.2:
        ymouse1 = ymouse1 + vert_move1*10
    mouse1 = (xmouse1,ymouse1)
    schermo.blit(cursor,mouse1)
    
        
def Joymove2():
    global mouse2,xmouse2,ymouse2
    horiz_move1 = round(joystick2.get_axis(0),2)
    vert_move1 = round(joystick2.get_axis(1),2)
    if horiz_move1<-0.2:
        xmouse2 = xmouse2 + horiz_move1*10
    if horiz_move1>0.2:
        xmouse2 = xmouse2 + horiz_move1*10
    if vert_move1>0.2:
        ymouse2 = ymouse2 + vert_move1*10
    if vert_move1<-0.2:
        ymouse2 = ymouse2 + vert_move1*10
    mouse2 = (xmouse2,ymouse2)
    schermo.blit(cursor,mouse2)
    
def Mousemove1():
    global mouse1
    mouse1 = pygame.mouse.get_pos()
    schermo.blit(cursor,mouse1)
               
def cursormove():
    global collega,joystick1,joystick2,state
    if pygame.joystick.get_count() >= 2:
        Joymove1()
        Joymove2()
    else:
        if menùù == True:
            state = "menu"
        elif p:
            state = "pause"
        
        elif finevar:
            state = "end"
        else:
            state = "game"
        collega = True
        
state = "null"

#joybutton y = 0 x = 1 a = 2 b = 3 l = 4 r = 5 pause = 6  7 = dance
def joystick1buttons(joystick1,button):
    if joystick1.get_name() == "Nintendo Switch Joy-Con (R)" or joystick1.get_name() == "Nintendo Switch Joy-Con (L)":
        if joystick1.get_button(3) and button == 0:
            return True
        elif joystick1.get_button(2) and button == 1:
            return True
        elif joystick1.get_button(0) and button == 2:
            return True
        elif joystick1.get_button(1) and button == 3:
            return True
        elif joystick1.get_button(9) and button == 4:
            return True
        elif joystick1.get_button(0) and button == 5:
            return True
        elif joystick1.get_button(6) and button == 6:
            return True
        else:
            return False
    
    if joystick1.get_name() == "usb gamepad":
        if joystick1.get_button(3) and button == 0:
            return True
        elif joystick1.get_button(0) and button == 1:
            return True
        elif joystick1.get_button(1) and button == 2:
            return True
        elif joystick1.get_button(2) and button == 3:
            return True
        elif joystick1.get_button(4) and button == 4:
            return True
        elif joystick1.get_button(6) and button == 5:
            return True
        elif joystick1.get_button(9) and button == 6:
            return True
        else:
            return False
    
    if joystick1.get_name() == "Xbox 360 Controller":
        if joystick1.get_button(2) and button == 0:
            return True
        elif joystick1.get_button(3) and button == 1:
            return True
        elif joystick1.get_button(1) and button == 2:
            return True
        elif joystick1.get_button(0) and button == 3:
            return True
            
        elif (joystick1.get_button(4) or joystick1.get_button(5)) and button == 5:
            return True
        elif (joystick1.get_axis(4)>sens or joystick1.get_axis(5)>sens) and button == 4:
            return True
            
        elif joystick1.get_button(7)and button == 6:
            return True
        elif joystick1.get_hat(0)[1] == 1 and button == 7:
            return True
        else:
            return False
        
    if joystick1.get_name() == "Nintendo Switch Pro Controller":
        if joystick1.get_button(3) and button == 0:
            return True
        elif joystick1.get_button(2) and button == 1:
            return True
        elif joystick1.get_button(0) and button == 2:
            return True
        elif joystick1.get_button(1) and button == 3:
            return True
        elif (joystick1.get_axis(4)>0 or joystick1.get_axis(5)>0) and button == 4:
            return True
        elif (joystick1.get_button(0) or joystick1.get_button(9)) and button == 5:
            return True
        elif joystick1.get_button(6) and button == 6:
            return True
        elif joystick1.get_button(11) and button == 7:
            return True
        else:
            return False
        
    if joystick1.get_name() == "Pro Controller":
        if joystick1.get_button(3) and button == 0:
            return True
        elif joystick1.get_button(2) and button == 1:
            return True
        elif joystick1.get_button(1) and button == 2:
            return True
        elif joystick1.get_button(0) and button == 3:
            return True
        elif (joystick1.get_button(4) or joystick1.get_button(5)) and button == 5:
            return True
        elif (joystick1.get_button(6) or joystick1.get_button(7)) and button == 4:
            return True
        elif joystick1.get_button(9) and button == 6:
            return True
        
        elif joystick1.get_hat(0)[1] == 1 and button == 7:
            return True
        else:
            return False









# CODICE





loadplayer1("amogusred")
loadplayer2("amogusblu")



while exit== False:
    telecamera = pygame.Surface(size,pygame.SRCALPHA)
    sens = valore_reale/100
    fpscounter =stile0.render("FPS counter:", True, imp) 
    fps=stile4.render(str(round(clock.get_fps())), True, imp)
    Saltoconle=stile0.render("Salto con levettA:", True, imp)
    
    if (menùprincipale.collidepoint(mouse1) or menùprincipale.collidepoint(mouse2)) and p:
        menùscritta = stile2.render("Menu principale", True, red)
    else:
        menùscritta = stile0.render("Menu principale", True, imp)
         
    if (rect_text.collidepoint(mouse1) or rect_text.collidepoint(mouse2)) and p :
        p_pausa=stile2.render("CONTINUA", True, red) 
    else:
        p_pausa=stile0.render("CONTINUA", True, imp) 
          
    if (rect_menù.collidepoint(mouse1) or rect_menù.collidepoint(mouse2)) and  menùù:
        p_menù=stile2.render("COMBATTI", True, red)
    else:
        p_menù=stile0.render("COMBATTI", True, imp)
              
    if (rect_menùesci.collidepoint(mouse1) or rect_menùesci.collidepoint(mouse2)) and menùù:
        p_menùesci=stile2.render("ESCI", True, red)  
    else:
        p_menùesci=stile0.render("ESCI", True, imp)  
    
    if (escii.collidepoint(mouse1) or escii.collidepoint(mouse2)) and  finevar:
        p_esci=stile2.render("ESCI", True, red)
    else:
        p_esci=stile0.render("ESCI", True, imp)
              
    if (continuee.collidepoint(mouse1) or continuee.collidepoint(mouse2)) and finevar:
        p_menùfine=stile2.render("RIVINCITA", True, red)  
    else:
        p_menùfine=stile0.render("RIVINCITA", True, imp) 
        
    if rect_controller.collidepoint(mouse1) and  collega:
        p_esci_controller=stile2.render("ESCI", True, red)
    else:
        p_esci_controller=stile0.render("ESCI", True, imp)
   
   
    
    
    
    try:
        joystick1 = pygame.joystick.Joystick(0)
        joystick2 = pygame.joystick.Joystick(1)
    except:
        collega = True
    
    if collega == True:
        collegacontroller(state)
    elif menùù == True:
        menù()
    elif p:
        Pausa()
        
    elif finevar:
        menùfine()
        pygame.mixer.music.stop()
    else:
        if vince_frame>0:
            vince_frame -= 1
            canmove2 = False
            canmove1 = False
            
        if vince_frame == 0 or vince_frame > 30 :
            Main()

        else:
            endsound.play()
            finevar = True
            
        if vince_frame > 0 and vince_frame<180 :
            finescritta = stile3.render("FINE!",True,imp,)
            schermo.blit(finescritta,(800-80,400-30))
        if vince_frame == 180:
            finesound.play()
    
    
    
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit = True
        
        if i.type == pygame.MOUSEBUTTONDOWN or (i.type==pygame.JOYBUTTONDOWN and joystick1buttons(joystick1,2)):
            if rect_menù.collidepoint(mouse1)  and  menùù:
                selectsound.play()
                menùù = False  
            if rect_text.collidepoint(mouse1)  and  p:
                selectsound.play()
                p = False
            if onoff.collidepoint(mouse1)  and p:
                selectsound.play()
                saltoconlevetta = not saltoconlevetta
            if saltooo.collidepoint(mouse1)  and  p :
                selectsound.play()
                fpscounterr = not fpscounterr
            if menùprincipale.collidepoint(mouse1) and p:
                selectsound.play()
                menùù = True
            if rect_menùesci.collidepoint(mouse1) and menùù:
                selectsound.play()
                exit = True
            if continuee.collidepoint(mouse1) and finevar:
                selectsound.play()
                finevar = False
                menùù = True
            if escii.collidepoint(mouse1) and finevar:
                selectsound.play()
                finevar = False
                exit = True
            if rect_controller.collidepoint(mouse1) and collega:
                exit = True
            
        if i.type == pygame.MOUSEBUTTONDOWN or (i.type==pygame.JOYBUTTONDOWN and  joystick1buttons(joystick2,2)):
            if rect_menù.collidepoint(mouse2) and  menùù:
                menùù = False
                selectsound.play()
            if rect_text.collidepoint(mouse2) and  p:
                p = False
                selectsound.play()
            if onoff.collidepoint(mouse2) and p:
                saltoconlevetta = not saltoconlevetta
                selectsound.play()
            if saltooo.collidepoint(mouse2) and  p :
                fpscounterr = not fpscounterr
                selectsound.play()
            if menùprincipale.collidepoint(mouse2) and p:
                menùù = True
                selectsound.play()
            if rect_menùesci.collidepoint(mouse2) and menùù:
                exit = True
                selectsound.play()
            if continuee.collidepoint(mouse2) and finevar:
                finevar = False
                menùù = True
                selectsound.play()
            if escii.collidepoint(mouse2) and finevar:
                finevar = False
                exit = True
                selectsound.play()
                
                
                
                
                
        if i.type == pygame.MOUSEBUTTONDOWN or i.type==pygame.JOYBUTTONDOWN:
            
            if i.type==pygame.JOYBUTTONDOWN:
                if (joystick1buttons(joystick2,2) and p):
                    if rect_basee.collidepoint(mouse2):
                        afferrato2 = True
                        
                if (joystick1buttons(joystick1,2) and p):
                    if rect_basee.collidepoint(mouse1):
                        afferrato1 = True
                        
            if i.type==pygame.MOUSEBUTTONDOWN:
                if i.button == 1 and p: 
                    if rect_basee.collidepoint(mouse2):
                        afferrato2 = True
                        
        if i.type == pygame.MOUSEBUTTONUP:
            if i.button == 1:
                afferrato1 = False
                afferrato2 = False
        elif i.type==pygame.JOYBUTTONUP:
            afferrato1 = False
            afferrato2 = False
                
                
          
        
        if afferrato1:
            Nuovocico = mouse1[0] - slider_x - 5
            cico = max(0, min(Nuovocico, PosX - 10))
            valore_reale = int((cico / (PosX - 10)) * (valore_massimo - valore_minimo) + valore_minimo)
            rect_base.width = cico
        elif afferrato2:
            Nuovocico = mouse2[0] - slider_x - 5
            cico = max(0, min(Nuovocico, PosX - 10))
            valore_reale = int((cico / (PosX - 10)) * (valore_massimo - valore_minimo) + valore_minimo)
            rect_base.width = cico       
        
            
            
                   
                   
                   
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_ESCAPE:
                p = not p
        if i.type==pygame.JOYBUTTONDOWN:
            if joystick1buttons(joystick1,6) or joystick1buttons(joystick2,6):
                p = not p
                      
    pygame.display.update()
                             
    clock.tick(60)
    
    
with open("settings.txt", "w") as f:
    f.write("saltoconlevetta=" + str(int(saltoconlevetta)) + "\n")
    f.write("fpscounterr=" + str(int(fpscounterr)) + "\n")
    f.write("sens=" + str(sens) + "\n")
        
 
pygame.quit()
