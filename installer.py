import os
print("""
  __     _                                      ______  ___ _____ 
 / _|   | |                                     | ___ \/ _ \_   _|
| |_ ___| |__  _ __ _____   ________ _ __  _   _| |_/ / /_\ \| |  
|  _/ _ \ '_ \| '__/ _ \ \ / /______| '_ \| | | |    /|  _  || |  
| ||  __/ |_) | | |  __/\ V /       | |_) | |_| | |\ \| | | || |  
|_| \___|_.__/|_|  \___| \_/        | .__/ \__, \_| \_\_| |_/\_/  
                                    | |     __/ |                 
                                    |_|    |___/                  
                     __             ___    ___                   
 __                 /\ \__         /\_ \  /\_ \                  
/\_\    ___     ____\ \ ,_\    __  \//\ \ \//\ \      __   _ __  
\/\ \ /' _ `\  /',__\\ \ \/  /'__`\  \ \ \  \ \ \   /'__`\/\`'__\
 \ \ \/\ \/\ \/\__, `\\ \ \_/\ \L\.\_ \_\ \_ \_\ \_/\  __/\ \ \/ 
  \ \_\ \_\ \_\/\____/ \ \__\ \__/.\_\/\____\/\____\ \____\\ \_\ 
   \/_/\/_/\/_/\/___/   \/__/\/__/\/_/\/____/\/____/\/____/ \/_/ 
                                                                 
                                                                 
""")
print("[1]Linux [2]Windows")
OS=int(input("ENTER YOUR Operating system : "))
if OS==1:
	os.system("python3 -m pip install click")
	os.system("apt-get install espeak &> /dev/null")
	os.system("espeak -s 10 'now you can run febrev pyrat in your system'")	
	os.system("python3 febrev-pyRAT-linux.py")

else:
	print("python febrev-pyRAT-windows.py")
