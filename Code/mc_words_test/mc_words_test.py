import speech_recognition as sr
import pyttsx3
from playsound import playsound
import random
import os
import mcpi.minecraft as minecraft

#YOUR INFO GOES HERE
playername = "CLMilkshake"
path = os.path.dirname(os.path.abspath(__file__)) + "/bad_word.mp3"
print(path)


r = sr.Recognizer()

print("\n\nStarting CLMilkshake's Voice recognition... One moment\n\n")

try:
    mc = minecraft.Minecraft.create(address = "69.169.174.140", port = 7777)
    mc.postToChat("Initalizing " + playername + "... Don't say any no-no words now :D")
except TimeoutError as e:
    raise Exception("\n\n The server isn't up :( \n") from e

EntityList = mc.getPlayerEntityIds()
PlayerNumber = len(EntityList)


GiantList = [
    
    "and",
    "the",
    "funny",
    "creeper",
    "lava",
    "scared",
    "dead",
    "I",
    "you",
    "troglodite",
    "run",
    "that",
    "wood",
    "mine",
    "craft",
    "diamonds",
    "crafting",
    "dragon",
    "eye",
    "nether",
    "no",
    "yes",
    "gosh",
    "women",
    "blocks",
    "milkshake",
    "iron",
    "village",
    "food",
    "me",
    "end",
    "zero",
    "0",
    "277",
    "coke",
    "discord",
    "show",
    "run",
    "world",
    "seed",
    "game",
    "word",
    "help",
    "think",
    "watch",
    "leave",
    "give",
    "look",
    "walk",
    "about",
    "item",
    "child",
    "tree"
]

no1 = random.choice(GiantList)
no2 = random.choice(GiantList)
no3 = random.choice(GiantList)
no4 = random.choice(GiantList)
no5 = random.choice(GiantList)
no6 = random.choice(GiantList)
no7 = random.choice(GiantList)
no8 = random.choice(GiantList)
no9 = random.choice(GiantList)
no10 = random.choice(GiantList)


def record_text():
    
    while(1):
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2)
                
                audio2 = r.listen(source2, phrase_time_limit=3)
                
                MyText = r.recognize_google(audio2)
                #print("audio2 = ", audio2)
                print("MyText = ", MyText)
                return MyText
            
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            
        except sr.UnknownValueError:
            print("\n <!> idk what you said XD <!> \n")
    return


while(1):
    text = record_text()
    
    
    
    no = []
    no.extend((no1, no2, no3, no4, no5, no6, no7, no8, no9, no10)) 
    
    if [g for g in no if g in text]:
        print("You said a no-no word :(") 
        playsound(path)
        
        
        # Send the command to the server
        mc.postToChat(playername + " said '" + text + "'")
        EntityList = mc.getPlayerEntityIds()
        PlayerNumber = len(EntityList)
        
        if PlayerNumber == 1:
            pos1 = EntityList
            pos1 = mc.entity.getPos(pos1)
            mc.setBlock(pos1, 11)
        if PlayerNumber == 2:
            pos1, pos2 = EntityList
            pos1 = mc.entity.getPos(pos1)
            pos2 = mc.entity.getPos(pos2)
            mc.setBlock(pos1, 11)
            mc.setBlock(pos2, 11)
        if PlayerNumber == 3:
            pos1, pos2, pos3 = EntityList
            pos1 = mc.entity.getPos(pos1)
            pos2 = mc.entity.getPos(pos2)
            pos3 = mc.entity.getPos(pos3)
            mc.setBlock(pos1, 11)
            mc.setBlock(pos2, 11)
            mc.setBlock(pos3, 11)
        if PlayerNumber == 4:
            pos1, pos2, pos3, pos4 = EntityList
            pos1 = mc.entity.getPos(pos1)
            pos2 = mc.entity.getPos(pos2)
            pos3 = mc.entity.getPos(pos3)
            pos4 = mc.entity.getPos(pos4)
            mc.setBlock(pos1, 11)
            mc.setBlock(pos2, 11)
            mc.setBlock(pos3, 11)
            mc.setBlock(pos4, 11)
            



        #print(EntityList)
        
    #print(text)