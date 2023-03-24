# Auteur: Sébastien Merrant email:sebastien.merrant@orange.fr
# Suivant l'environnement à selectionner PROD, PPROD,DEV,TEST etc.. 
# Charge le bon serveur Admin avec une connection SSH avec le user ssh associé

import os
              
class SetupEnv:
    def __init__(self,serv: str, env: str, user: str ):
        self.serv =serv
        self.env = env
        self.user= user

    def ViewServ(self):
        
        if choix_env  in self.env:
          connexion_ssh="ssh " + self.user + self.serv
          exec_ssh= "/usr/bin/ssh"
          if os.path.exists(exec_ssh):
                print(f"Command ssh présente sous {exec_ssh}")
                os.system(connexion_ssh)
           
                return True
          else:
                print(f"Command ssh non présente sous {exec_ssh}")
                return True
                       
environnement= [
SetupEnv("serveur1",("TU","TEST","TNR"),("user1_ssh@")),
SetupEnv("serveur2", ("PPROD","PPROD1","PPROD2"),("user2_ssh@")),
SetupEnv("serveur3",("PROD","PROD01"),("user3_ssh@")),
SetupEnv("serveur4", ("TEST","TEST1","DEV"),("user4_ssh@")),
]

count=0
menu="""
Env Disponible: ("TU","TEST","DEV","")
Env Disponible: ("PPROD","XXX","XXX")
Env Disponible: ("PROD","PROD01")
Env Disponible: ("TEST","TEST1","DEV")

exemple choisir TEST
"""
print(menu)

while True:

    choix_env =input("choix de l'environnement: ")
    if choix_env:
         break

for element in environnement:
     if not element.ViewServ():
                count+=1
if count == len(environnement):
      print("L'environnement n'existe pas ")

    
