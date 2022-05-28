from threading import Thread
import subprocess

t1 = Thread(target=subprocess.run, args=(["python3", "script.py", "/dev/sdb"],))
t2 = Thread(target=subprocess.run, args=(["python3", "script1.py"],))
t3 = Thread(target=subprocess.run, args=(["python3", "script3.py", "./file","-r", "./rule.yar"],))
t4 = Thread(target=subprocess.run, args=(["python3", "script2.py", "./file","-r", "fast"],))


t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()
