import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
engine.setProperty("rate", 150)
engine.setProperty("volume", 0.9)
engine.setProperty("voice", "com.microsoft.speech.synthesis.voiceinfo.409.409.409.en-US.ZiraPro")

recognizer = sr.Recognizer()

def ouvir_microfone():
    with sr.Microphone() as source:
        print("Diga algo:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            texto = recognizer.recognize_google(audio, language="pt-BR")
            print("Você disse:", texto)
            return texto.lower()
        except sr.UnknownValueError:
            print("Não foi possível entender o áudio")
            return None

def falar(texto):
    engine.say(texto)
    engine.runAndWait()

falar("Olá! Como posso ajudar?")

while True:
    print("Esperando comando...")
    comando = ouvir_microfone()
    
    if comando:
        if "olá" in comando:
            falar("Olá! Como posso ajudar?")
        elif "tchau" in comando:
            falar("Até logo!")
            break
        else:
            falar("Desculpe, não entendi o comando.")
