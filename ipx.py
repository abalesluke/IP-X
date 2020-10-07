import os, sys, random, time, colorama
from colorama import Fore

version = "1.5"
country = ["Albania",",Greece","Portugal","Argentina","Hong_Kong"
,"Romania","Australia","Hungary","Serbia"
,"Austria","Iceland","Singapore","Belgium"
,"India","Slovakia","Bosnia_And_Herzegovina"
,"Indonesia","Slovenia","Brazil"
,"Ireland","South_Africa"
,"Bulgaria","Israel","South_Korea"
,"Canada","Italy","Spain"
,"Chile","Japan","Sweden"
,"Costa_Rica","Latvia","Switzerland"
,"Croatia","Luxembourg","Taiwan"
,"Cyprus","Malaysia","Thailand"
,"Czech_Republic","Mexico","Turkey"
,"Denmark","Moldova","Ukraine"
,"Estonia","Netherlands","United_Kingdom"
,"Finland","New_Zealand","United_States"
,"France","North_Macedonia"]

print("""\033[1;31;40m

██╗██████╗      ██╗  ██╗
██║██╔══██╗     ╚██╗██╔╝
██║██████╔╝█████╗╚███╔╝ 
██║██╔═══╝ ╚════╝██╔██╗ 
██║██║          ██╔╝ ██╗
╚═╝╚═╝          ╚═╝  ╚═╝
                        

""")
print(Fore.GREEN+"Coded by: Anikin Luke")
print("Type 'help' to show commands")

while True:
    
    ui = str(input(Fore.YELLOW+">")).lower()
    if(ui == "start"):
        print("Press ctrl + C to cancel/stop changing")
        time.sleep(3.5)
        while True:
            for i in range(1):
                ran = random.choices(country)
                os.system(f"nordvpn connect {''.join(ran)}")
                for i in range(20):
                    print(i)
                    time.sleep(1)
                os.system("clear")
                          
                          
    elif(ui == "help"):
        print("""
=============================================
+|        IP-X coded by Anikin Luke        |+
=============================================
+|     COMMANDS            Decription      |+
+|-----------------------------------------|+
+|     start   --  To Start changing your  |+
+|                 every 20sec,note! i wont|+
+|                 work if nordvpn is not  |+
+|               installed in your terminal|+
+|     About   --  To show dev info.       |+
+|     Exit    --  To quit the program.    |+
+|     Help    -- To show commands         |+
+|    update   --   Comming soon! no       |+
+|     update command not working yet      |+
 ===========================================


""")
        
    elif(ui == "about"):
        print(f"""
    =============================================
    +|             About this tool             |+
    =============================================
    +|              This Tool Is               |+
    +|               Is Created                |+
    +|                   By                    |+
    +|            Anikin Luke Abales           |+
    +|  for SudoCentercorp team CyberHackers   |+
    +|-----------------------------------------|+
    +| Tool name: IP-X /IpChanger every 20sec  |+
    +| Use To Generate Credit card info's      |+
    +| Tool version: {version}                       |+
    +|-----------------------------------------|+
    +|                Contact                  |+
    +|        Facebook-Group                   |+
    +|  facebook.com/groups/sudocyberhackers   |+
    +|--------------^--------^-----------------|+
    +|   Email: Anonnewshacker@gmail.com       |+
    +|   Github: abalesluke                    |+
    +|                                         |+
    +|                 Note!                   |+
    +|   This tool is now available on github  |+
    +|   so please dont republish it on github |+
    +|   i do not autorized you to edit this   |+
    +|   tool or republish it on github.       |+
    +|                                         |+
    +|         Editing or changing the         |+
    +|       name of the coder or developer    |+
    +|        wont make you a programmer.      |+
    +|                                         |+
    +|        [+]Respect the coder's[+]        |+
     ===========================================  

""")
    
    elif(ui =="exit"):
        print(Fore.WHITE+"goodbye..")
        break
    
    else:
        print("Error! command not found!")
        print("Try typing 'help'")
    
    
    
    
