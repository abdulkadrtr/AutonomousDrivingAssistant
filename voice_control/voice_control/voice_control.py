import rclpy
from rclpy.node import Node
from ackermann_msgs.msg import AckermannDrive
from geometry_msgs.msg import PointStamped
import math
import sys
import numpy as np
import threading
import time
import joblib
import speech_recognition as sr
from gtts import gTTS
import playsound # 1.2.2
import pickle
import os

dizin = os.getcwd()
dizin = dizin + '/src/voice_control/voice_control'

def predict_action(X):
    model = joblib.load(dizin + '/cikisModel.joblib')
    y_pred = model.predict(X)
    return y_pred

with open(dizin + '/model.pickle', 'rb') as f:
    loaded_model = pickle.load(f)

def speak(text):
    tts = gTTS(text=text, lang='tr')
    filename = "temp.mp3"
    filename = os.path.join(dizin, filename)
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def control(text):
    prediction = loaded_model.predict([text])[0]
    return prediction

def targetLocation():
    f = None
    r = sr.Recognizer()
    print("[BILGI] Araç asistanı başlatıldı.")
    text = "Merhaba, Araç asistanınız sizi dinliyor."
    speak(text)
    while True:
        with sr.Microphone() as source:
            print("[BILGI] Dinleniyor..")
            audio_text = r.listen(source, phrase_time_limit=3)
            try:
                text = r.recognize_google(audio_text, language="tr-TR")
                result = control(text)
                if result in ["EV", "HASTANE", "IS"]:
                    if result == "IS":
                        result = "İŞ"
                    voice = "Hedefiniz {} olarak belirlendi.Yola çıkıyorum.".format(result)
                    speak(voice)
                    print("[BILGI] {} Hedefine doğru yola çıkılıyor.".format(result))
                    if result == "EV":
                        f = 1
                    elif result == "HASTANE":
                        f = 2
                    elif result == "IS":
                        f = 3
                    break
                else:
                    print("Anlayamadım.")
            except sr.UnknownValueError:
                print("Üzgünüm, anlayamadım.")
    return f


class ackermannControl(Node):
    def __init__(self):
        super().__init__('Ackermann_Control')
        self.subscription = self.create_subscription(PointStamped,'vehicle/gps',self.gps_callback,10)
        self.publisher = self.create_publisher(AckermannDrive,'cmd_ackermann',10)
        self.flag = 0
        self.i = 0
        self.refX = 0.0
        self.refY = 0.0
        target = targetLocation()
        targetDict = {1: "EV", 2: "HASTANE", 3: "İŞ"}
        print("[BILGI] Park Alanindan Cikiliyor.")
        threading.Thread(target=self.data).start()
    
    def data(self):
        while True:
            if not hasattr(self,'location'):
                time.sleep(0.1)
                continue
            if(self.flag == 0):
                data = np.column_stack((self.location,self.i))
                sonuc = predict_action(data)
                v = sonuc[0][0]
                q = sonuc[0][1]
            if v == 0.0 and q == 0.0 and self.location[0][0] < -2 and self.location[0][1] > 5: 
                print("[BILGI] Park alanindan cikildi.")
                print("[BILGI] Hedefe dogru ilerleniyor")
                v = 3.0
                q = 0.005
                self.flag = 1
            #Bu alanda çoklu koordinata göre hedef belirlenilir. EV , IS , HASTANE gibi. Hedef target degiskenindedir.
            if self.flag == 1 and self.location[0][1] > 23.5:
                text = "Hedefe ulastim."
                speak(text)
                print("[BILGI] Hedefe ulasildi.")
                v = 0.0
                q = 0.0
                self.flag = 2
            msg = AckermannDrive()
            msg.steering_angle = q
            msg.speed = v
            msg.steering_angle_velocity = math.pi/72
            msg.acceleration = 0.5
            self.publisher.publish(msg)
            if self.flag == 2:
                sys.exit()
            time.sleep(0.3)
            self.i = self.i + 1

    def gps_callback(self, msg):
        if self.i == 0:
            self.refX = msg.point.x
            self.refY = msg.point.y
        self.location = [msg.point.x - self.refX , msg.point.y - self.refY]
        self.location = np.array(self.location)
        self.location = self.location.reshape((1,2))

def main(args=None):
    rclpy.init(args=args)
    ackermann_control = ackermannControl()
    rclpy.spin(ackermann_control)
    ackermann_control.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
