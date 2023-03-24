 python_scripts
 Auteur: Sébastien Merrant email: sebastien.merrant@orange.fr
 Demande l'environnement à charger PROD, PPROD,DEV,TEST etc.. 
 redirige sur le bon serveur d'administration avec une connection SSH et le bon user ssh associé


Ce script peut-être intégré dans le .bashrc de votre /home/users

Modifier la liste en fonction de votre environnement. 

environnement= [
SetupEnv("serveur1",("TU","TEST","TNR"),("user1_ssh@")),
SetupEnv("serveur2", ("PPROD","PPROD1","PPROD2"),("user2_ssh@")),
SetupEnv("serveur3",("PROD","PROD01"),("user3_ssh@")),
SetupEnv("serveur4", ("TEST","TEST1","DEV"),("user4_ssh@")),
]
