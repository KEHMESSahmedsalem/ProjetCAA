
from moviepy.video.VideoClip import VideoClip
import speech_recognition as sr
import moviepy.editor as mp
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from tkinter import *   
from tkinter import filedialog 

# la foction pour exporter le fichier video
def video(): 
    filename = filedialog.askopenfilename(initialdir = "/", title = "choisir un video", filetypes = (("mp4 files", "*.mp4*"), ("all files", "*.*"))) 
       
    label_file_explorer.configure(text=filename) 

#fonction pour converture un video de langue français en word cloud
def program():
    clip  = mp.VideoFileClip(label_file_explorer["text"]) #l'input de la fichier video
    clip.audio.write_audiofile(r"audio.wav") # convertion de la video en fichier audio.
    r = sr.Recognizer()
    audio = sr.AudioFile("audio.wav")

    #converture l'audio en texte
    with audio as source:
        r.adjust_for_ambient_noise(source)
        audio_file = r.record(source)
        
        result = r.recognize_google(audio_file, language="fr-FR")
    
    #converture le texte en wordcloud
    message = result
    wordcloud = WordCloud(max_words=30, stopwords = STOPWORDS, background_color='white', width=1920, height=1080, min_word_length=4).generate(message)
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()


##fonction pour converture un video de langue Anglais en word cloud
def program1():
    clip  = mp.VideoFileClip(label_file_explorer["text"]) #l'input de la fichier video
    clip.audio.write_audiofile(r"audio.wav") # convertion de la video en fichier audio
    r = sr.Recognizer()
    audio = sr.AudioFile("audio.wav")

    #converture l'audio en texte
    with audio as source:
        r.adjust_for_ambient_noise(source)
        audio_file = r.record(source)

        result = r.recognize_google(audio_file)

    #converture le texte en wordcloud
    message = result
    wordcloud = WordCloud(max_words=30, stopwords = STOPWORDS, background_color='white', width=1920, height=1080, min_word_length=4).generate(message)
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()
       
#creation de la fenetre de l'aplication et ses dimention
application = Tk() 
   
application.title('Generateur wordcloud') 
   
application.geometry("700x400") 

application.resizable(width=False,height=False)

application.config(background = "white") 

#widgets..   
label_file_explorer = Label(application, text = "choisir une video", width = 100, height = 2, fg = "blue")        
button_explore = Button(application, text = "importer", command = video) 
cloudFR = Label(application, text = "Nuage de mots français", width = 20, height = 2, fg = "white", bg="black")
button_fr = Button(application, text = "FR-cloud", command = program)
cloudEN = Label(application, text = "English cloudword", width = 20, height = 2, fg = "white", bg="black")
button_en = Button(application, text = "EN-cloud", command = program1) 
   
label_file_explorer.pack()    
button_explore.pack()
cloudFR.pack(padx=100, pady=10)
button_fr.pack(padx=100)
cloudEN.pack(padx=100, pady=10)
button_en.pack(padx=100)

#boucle  
application.mainloop() 