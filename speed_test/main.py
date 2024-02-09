# importing packages 
import speedtest
import pyttsx3
# Init - pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')    
engine.setProperty('voice', voices[1].id)
greetings= "Welcome sir this is Friday! your internet speed testing assistant"
engine.say(greetings)
print(greetings)
def check_int_speed():
    st = speedtest.Speedtest()
    st.get_best_server()
    
    checking_ds="Checking download speed..."
    engine.say(checking_ds)
    print(checking_ds)
    engine.runAndWait()
    download_speed= st.download()/1_000_000
    check_ds=f"Download Speed: {download_speed: 0.2f} mb Per Second"
    engine.say(check_ds)
    print(f"Download Speed: {download_speed: 0.2f} Mbps")
    engine.runAndWait()

    checking_us="Checking upload speed..."
    engine.say(checking_us)
    print(checking_us)
    engine.runAndWait()
    upload_speed= st.upload()/1_000_000

    check_us=f"Upload Speed: {upload_speed: 0.2f} mb Per Second"
    engine.say(check_us)
    print(f"Upload Speed: {upload_speed: 0.2f} Mbps")
    engine.runAndWait()

if __name__=="__main__": 
    check_int_speed()

ending=" Md Samiul Alam Chakder developed me"
print(ending)
print("Please visit: https://04samiul.netlify.app")



