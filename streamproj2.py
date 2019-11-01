import shutil #Import für Copy Befehle
import os
import datetime

src_path = "C:/Users/Windoof/Desktop/PYTHON_PROJEKTE/Copyfiles/Sourcefolder/" #Source Pfad
dst_path = "C:/Users/Windoof/Desktop/PYTHON_PROJEKTE/Copyfiles/Destinationfolder/" #Destination Pfad

print(os.listdir(src_path))
print("")

if not os.path.exists(dst_path):
    os.mkdir(dst_path)

for item in os.listdir(src_path): #für jedes "item" in "src_path" tue...
    s = os.path.join(src_path, item) #beschreibe Variable "s" und joine das item an den Source Pfad 
    d = os.path.join(dst_path, item) #beschreibe Variable "d" und joine das item an den destination Pfad
    
    #ORDNER
    if os.path.isdir(s): #Wenn der gejointe Pfad mit dem Item ein Ordner ist dann...
        if os.path.isdir(d): #if os.path.isdir(dst_path + item): #wenn der Pfad ein Directory ist und besteht...

            print(item + " existiert bereits 1") #gebe den namen aus und sage "existiert bereits"
        else:
            shutil.copytree(s, d, symlinks=True) #wenn nicht "d" kein directory kopiere die Datei
            print(item + " kopiert 1") #gebe den Namen des Items und sage "Kopiert".
    
    #ALLE ANDEREN DATEIEN
    else:
        if os.path.exists(d):
            print(item + " existiert bereits 2")
        else:
            shutil.copyfile(s,d)
            print(item + " kopiert 2")

#Hier fängt der Quelltext nach der For-Schleife an...
print("Ende")