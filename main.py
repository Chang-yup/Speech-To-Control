import sys
from pyparsing import Word
import speech_recognition as sr
import winsound as sd
import datetime
import WordDictList
import time
from pywinauto.application import Application

# 0. COMMON CLASS
class COMMON:
    #search
    def searchWord(self, text, targetlist): # 음성 텍스트에서 명령어 추출
        for target in targetlist:
            if text.find(target)!=-1:
                return ...
        return 0
    
    def beep(self,mode):
        if mode=="ready":
            sd.Beep(1000,200)
            sd.Beep(1500,200)
            sd.Beep(2000,200)
        elif mode=="done":
            sd.Beep(1000,200)
            sd.Beep(2000,200)
        elif mode=="error":
            sd.Beep(3000,600)
        elif mode=="exit":
            sd.Beep(2000,200)
            sd.Beep(1500,200)
            sd.Beep(1000,200)
        elif mode=="listening":
            sd.Beep(400,100)
    
# 1. STT state
class STATE_STT(COMMON):
    r = sr.Recognizer()
    m = sr.Microphone()
    
    def __init__(self, language):
        self.language=language
        
    def STT(self):
        text=""
        while True:
            with self.m as source:
                print("명령어 수신중 : ")
                try:
                    audio = self.r.listen(source,timeout=1)
                    text=self.r.recognize_google(audio_data=audio, language=self.language)
                except:
                    COMMON.beep("listening")
                    
                if text!="":
                    text=text.lower()
                    print(text)
                    return text
                
# 2. Application Call State
class STATE_APPCALL(COMMON):
    def __init__(self,text):
        self.text = text
        self.app=0
        
    def StartApp(self,appvalue):
        appvalue=COMMON.searchWord(self.text,WordDictList.appList)
        try:
            app = Application(backend="win32").start(appvalue)
        except:
            COMMON.beep("error")
            print("실행하려는 어플리케이션이 설치되지 않았거나 기본 위치에 없습니다. 다시 시도해주세요.")
        
    def ConnectApp(self,appvalue):
        while (self.app==0):
            try:
                self.app = Application(backend="win32").connect(title_re=)
            except:
                self.StartApp(appvalue)
                time.sleep(1)
        
    def AppCall(self):
        appvalue=COMMON.searchWord(self.text,WordDictList.AppList)
        app=self.ConnectApp(appvalue)
        return app
        
# 3. Action State
class STATE_ACTION(COMMON):
    def __init__(self,app,text):
        self.app=app
        self.text=text
        
    def Action(self):
        actionvalue=COMMON.searchWord(self.text,WordDictList.ActionList)
        if actionvalue=="":
              
# 4. Main Class
def main(language):
    rundate = datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S')
    while True:
        text=STATE_STT(language).STT()
        app=STATE_APPCALL(text).AppCall()
        STATE_ACTION(app,text).Action()
        
if __name__=="__main__":
    sys.exit(main("ko-KR"))