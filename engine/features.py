from playsound import playsound
import eel

@eel.expose
##Playsing Assisant sound function
def playAssistantSound():
    music_dir= "D:\\MY PROJECTS\\JARVIS\\www\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)