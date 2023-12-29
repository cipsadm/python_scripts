Mon code


import subprocess
import string
import random
import sys
import os


def code_app_existe(code_app ):
     command= "id " +  code_app
     try:
          returncode  =subprocess.check_call(command , shell=True)
          return True
     except subprocess.CalledProcessError as e:
          if e.returncode == 0:

             return 0
          else:
             print(e.output)
             return False


def create_code_app(code, param_user, code_app ):
    if code == True:
        print("utilisateur " + code_app +  " existe sur cette environnement  ")
        exit(0)
    else:
        print("useradd -d " +   param_user + code_app +  " -s "  + param_user + code_app +  " en cours de creation")
        # Commande pour creer un nouvel utilisateur avec un repertoire personnel
        useradd = "useradd -d " +   param_user + code_app +  " -s "  +  "/bin/sh" + " " + code_app

        try:
            subprocess.check_call(useradd , shell=True)
        except subprocess.CalledProcessError as e:
            if e.returncode == 0:
                print("useradd")
        try:
                usermod = "usermod -a -G adm,users " +  code_app
                subprocess.check_call(usermod , shell=True )
        except subprocess.CalledProcessError as e:
            if e.returncode == 0:
                print("usermod")

        try:

                chmod = "chmod 755 " +  param_user + code_app
                print(chmod)
                subprocess.check_call(chmod , shell=True )
        except subprocess.CalledProcessError as e:
            if e.returncode == 0:
                print("chmod -o+rx ")


            else:
                print(e.output)


def user_lock(code, param_user):

    if code == False:
        print("utilisateur " + " " + code_app + " non present  ")
    else:
        """print("Utilisateur " +  code_app +  " en cours de verrouillage")
        # Commande verrouiller le compte code_app
        usermod = "usermod "  + code_app + " " + " --shell "  + param_user

        try:
            subprocess.check_call(usermod , shell=True)
        except subprocess.CalledProcessError as e:
            if e.returncode == 0:
                print("Le user " + code_app +  " est maintenant en /sbin/nologin") """
        print("Compte" + " " + code_app + " present ")

        try:
             passwd  = "passwd -e " +  code_app
             subprocess.check_call(passwd , shell=True )
        except subprocess.CalledProcessError as e:
             if e.returncode == 0:
                print("compte mis en expiration")

             else:
                print(e.output)


def create_env(code_app,env):
   ccx= code_app.split("adm")[0]
   data="/data2/" + ccx + "/" + "pf_" + env + "/socle"
   if not os.path.exists(data):
      os.makedirs(data)
   else:
      print(data + " est deja present")


   chown= " chown -R " + ccx + "adm:"+ccx +"adm" + " /data2/" + ccx
   print(chown)
   try:
        subprocess.check_call(chown , shell=True )

   except subprocess.CalledProcessError as e:
        if e.returncode == 0:
                print("compte en expiration")

        else:
                print(e.output)

   try:

         chmod_env = "chmod 755 " + " /data2/" + ccx
         print(chmod_env)
         subprocess.check_call(chmod_env , shell=True )
   except subprocess.CalledProcessError as e:
            if e.returncode == 0:
                print(chmod_env)


            else:
                print(e.output)

   bash_make="/data1/rpm/jboss-admin/product/makePFinstall.ksh"
   param="/data2/" + ccx + "/pf_" + env + "/socle"
   bash_exec= bash_make + " " + param

   try:
        subprocess.check_call(bash_exec , shell=True )

   except subprocess.CalledProcessError as e:
        if e.returncode == 0:
                print("make")

        else:
                print(e.output)



   #/data1/rpm/jboss-admin/product/makePFinstall.ksh /data2/"ccx"/pf_"env"/socle


List_directory= [
"/data2/{code_app}/pf_{env}/socle"
,"/data2/homedir/",
"/sbin/nologin ",
"/data1/rpm/jboss-admin/product/makePFinstall.ksh"
]


#Test du nombre de parametre
if len(sys.argv) < 3  or  len(sys.argv) > 3:
    print("Usage: python createUserEnv code_app env")
    exit(1)

else:
    code_app = sys.argv[1]
    env = sys.argv[2]


menu = """
 ("1","Creation du compte code_app")
 ("2","Verrouiller le compte code_app ")
 ("3","Creation environnement du code_app)

"""

print(menu)

choix_env =raw_input("choix ")
if choix_env == "1":
    param_user=List_directory[1]
    code =code_app_existe(code_app)
    create_code_app(code, param_user, code_app )


elif choix_env == "2":
    param_user=List_directory[2]
    code=code_app_existe(code_app)
    user_lock(code, param_user)

else:
     print("creation environnement du user")
     create_env(code_app, env)




cryptage = "openssl "+" rand "+" -base64" +" 24 "
print(cryptage)

try:
          subprocess.check_call(cryptage , shell=True)
except subprocess.CalledProcessError as e:
          if e.returncode == 0:
             encode_pass= e.output
             print("generation du password " + encode_pass )
             passwd=" echo '%s' | passswd --stdin %s" % (encode_pass, code_app)

             print(passwd)
          else:
             print(e.output)
