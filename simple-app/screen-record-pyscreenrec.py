import pyscreenrec, time
recorder = pyscreenrec.ScreenRecorder()

recorder.start_recording('rec.mp4', 30)
print("record starting")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass

print("recording stop")
recorder.stop_recording() 


