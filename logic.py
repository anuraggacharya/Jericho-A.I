import win32com.client as wincl
import pyttsx3
import serial
from serial import SerialException
import time

def controlLed(command):
    try:    
        if command=='on':
            
            with serial.Serial('COM3',9600) as arduino:
                text_to_speech('turning on',"Female")
                time.sleep(1)
                arduino.write(b'H')
                #arduino.close()
        else:
            
            with serial.Serial('COM3',9600) as arduino:
                text_to_speech('turning off',"Female")
                arduino.write(b'L')
                #arduino.close()
        arduino.close()
    except SerialException as e: # if port is already opened, close it and open it again and print message
        print(e)
        #arduino.close()
        


def text_to_speech(text, gender):
    """
    Function to convert text to speech
    :param text: text
    :param gender: gender
    :return: None
    """
    voice_dict = {'Male': 0, 'Female': 1}
    code = voice_dict[gender]

    engine = pyttsx3.init()

    # Setting up voice rate
    engine.setProperty('rate', 125)

    # Setting up volume level  between 0 and 1
    engine.setProperty('volume', 0.8)

    # Change voices: 0 for male and 1 for female
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[code].id)

    engine.say(text)
    engine.runAndWait()

