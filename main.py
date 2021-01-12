import os
import sys
import time
from time import sleep
a=os.get_terminal_size()
words="\033[1;31mWelcome Bro\n"
w2="\033[1;32mNo \033[1;33mPain \033[1;31mNo \033[1;37mAgain"
for char in words:
     sleep(0.1)
     sys.stdout.write(char)
     sys.stdout.flush()
for ch in w2:
    sleep(0.1)
    sys.stdout.write(ch)
    sys.stdout.flush()
sleep(3)
os.system("clear")
os.system("clear")
def logo():
    print("""
  \033[1;33m111111111111111111111111111111111111111111111111111111111111
  \033[1;33m111111111111111111111111111111111111111111111111111111111111
  \033[1;33m111111111111111111111111111111111111111111111111111111111111
  \033[1;33m111111111111111111111111111111111111111111111111111111111111
  \033[1;33m11111111111111111111111111111\033[0;3m00\033[1;33m11111111111111111111111111111
  \033[1;33m1111111111111111111111111111\033[0;3m0000\033[1;33m1111111111111111111111111111
  \033[1;33m1111111111111111111111111111\033[0;3m0000\033[1;33m1111111111111111111111111111
  \033[1;33m111111111111111111111111111\033[0;3m000000\033[1;33m111111111111111111111111111
  \033[1;32m111111111111111111\033[0;3m000000000000000000000000\033[1;32m111111111111111111
  \033[1;32m1111111111111111111\033[0;3m0000000000000000000000\033[1;32m1111111111111111111
  \033[1;32m1111111111111111111111\033[0;3m0000000000000000\033[1;32m1111111111111111111111
  \033[1;32m111111111111111111111111\033[0;3m000000000000\033[1;32m111111111111111111111111
  \033[1;32m111111111111111111111111\033[0;3m000000000000\033[1;32m111111111111111111111111
  \033[1;31m11111111111111111111111\033[0;3m00000000000000\033[1;31m11111111111111111111111
  \033[1;31m11111111111111111111111\033[0;3m0000\033[1;31m111111\033[0;3m0000\033[1;31m11111111111111111111111
  \033[1;31m1111111111111111111111\033[0;3m000\033[1;31m1111111111\033[0;3m000\033[1;31m1111111111111111111111
  \033[1;31m111111111111111111111111111111111111111111111111111111111111
  \033[1;31m111111111111111111111111111111111111111111111111111111111111
  \033[1;31m111111111111111111111111111111111111111111111111111111111111
  \033[1;31m111111111111111111111111111111111111111111111111111111111111
""")
def menu():
       logo()

       print("""
                \033[1;33mMyanamr Cyber Youth
               \033[0;331mCreator By Solo Ninja
      \033[0;32mWebsite Link ==> https://mcy.asia
      \033[0;32mPage Link ==> https://www.facebook.com/MCY197
                \033[0;31m(1) Kali
                \033[0;34m(2) Ubuntu
                \033[0;35m(3) Centos
                \033[0;37m(4) Arch
                \033[0;36m(5) Fedora
                \033[0;37m(6) Exit

    """)
       try:
        a=int(input("\033[1;33mMCY\033[0;32m==\033[0;31m> "))
        if a==1:kali()
        elif a==2:ubuntu()
        elif a==3:centos()
        elif a==4:arch()
        elif a==5:fedo()
        elif a==6: exit()
        else:
            print("This Number  No exit.")
            os.system("clear")
            menu()
       except ValueError:
           print("Enter Only Number")
           os.system("clear")
           menu()
def kali():
    os.system("pkg install git -y")
    os.system("git clone https://github.com/Hax4us/Nethunter-In-Termux")
    os.system("cd Nethunter-In-Termux")
    os.system("./kalinethunter")
    kali="For Kali linux Using\n$startkali -r"
    for ka in kali:
        sleep(0.1)
        sys.stdout.write(ka)
        sys.stdout.flush()
    time.sleep(4)
    os.system("clear")
    menu()
def  ubuntu():
    os.system("apt-get install wget -y")
    os.system("apt-get install proot -y")
    os.system("apt-get install git -y")
    os.system("cd ~")
    os.system("git clone https://github.com/MFDGaming/ubuntu-in-termux.git")
    os.system("cd ubuntu-in-termux")
    os.system("chmod +x ubuntu.sh")
    os.system("bash ubuntu.sh -y")
    ub="For Ubuntu Using/n $./startubuntu.sh "
    for u in ub:
        sleep(0.2)
        sys.stdout.write(u)
        sys.stdout.flush()
    time.sleep(4)
    os.system("clear")
    menu()
def centos():
    os.system("apt-get install wget -y")
    os.system("apt-get install proot -y")
    os.system("apt-get instal tar -y")
    os.system("apt-get install git -y")
    os.system("wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Instaler/CentOS/centos.sh")
    os.system("chmod +x centos.sh")
    os.system("bash centos.sh")
    cent="For Centos Using\n $bash start-centos.sh"
    for ct in cent:
        sleep(0.1)
        sys.stdout.write(ct)
        sys.stdout.flush()
    time.sleep(4)
    os.system("clear")
    menu()
def arch():
    os.system("apt-get install wget -y")
    os.system("apt-get install proot -y")
    os.system("apt-get install git -y")
    os.system("wget https://raw.githubusercontent.com/sdrausty/TermuxArch/master/setupTermuxArch.sh")
    os.system("chmod +x setupTermuxArch.sh")
    os.system("bash setupTermuxArch.sh")
    arch="For Arch linux Using\n$startarch"
    for arc in arch:
        sleep(0.2)
        sys.stdout.write(arch)
        sys.stdout.flush()
    time.sleep(4)
    os.system("clear")
    menu()
def fedo():
    os.system("apt install proot -y")
    os.system("apt update && apt install wget -y && /data/data/com.termux/files/usr/bin/wget https://raw.githubusercontent.com/nmilosev/termux-fedora/master/termux-fedora.sh && sh termux-fedora.sh")
    fed="For Fedora linux\n$fedora"
    for fe in fed:
        sleep(0.2)
        sys.stdout.write(fe)
        sys.stdout.flush()
    time.sleep(4)
    os.system("clear")
    menu()
menu()
