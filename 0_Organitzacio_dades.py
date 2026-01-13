## Preparació de les dades

#Script per renombrar els arxius anat de les dades dels diferents laboratories de **ABIDE II** afegint l'ID al què pertany 
# i movent-los a la carpeta RAW Data del TFM#
import tarfile
import shutil
import os
# organització dels arxius tal qual es descarreguen:
# Laboratori
#   Arxiu.tar.gz
#       ID_Subjectes
#           session_1
#               anat_1 
#                   anatnii.gz (arxiu a copiar en una altre carpeta amb format ID_Subjecte_anat.nii.gz)
# carpeta on he descarregat les dades dels diferents laboratoris
abide_path = "C:\\_FILES\\98 HOME\\MªAlba\\UOC\\TFM\\ABIDE\\"
# laboratoris seleccionats
abide_folders = ["Barrow Neurological Institude", 
                "ETH Zürich",
                "Institut Pasteur and Robert Debré Hospital",
                "ABIDE\Institut Pasteur and Robert Debré Hospital",
                "Katholieke Universiteit Leuven", 
                "Olin","San Diego State University",
                "Trinity Centre for Health Sciences",#
                "University of California Davis"]

ext1 = ".tar.gz" 
# per processar amb syntheg i tenir totes les dades acumulades en un sol arxiu i no múltiples carpetes
# les imatges a segmentar les he de tenir en la mateixa carpeta
# path on s'han de copiar
new_path = "C:\\_FILES\\98 HOME\\MªAlba\\UOC\\TFM\\ABIDE_RAW\\"
file_to_rename = "anat.nii.gz"

# per cada lab
for lab in abide_folders:
    # generar path lab 
    lab_path = os.path.join(abide_path,lab)
    # buscar arxiu tar.gz del lab
    for root, _, files in os.walk(lab_path):
        # hi ha labs que tenen més d'un arxiu
        for file in files:
            if file.endswith(ext1):
                full_path = os.path.join(root,file)
                print (f"Found: {full_path}")
 
                ID_Folders = []
                lab_name = ""
                # obrir arxiu comprimit i llegir carpetes
                with tarfile.open(full_path,"r:gz") as tar:        
                    matching_files = [member.name for member in tar.getmembers() if file_to_rename in member.name]
                    print("Matching file paths inside tar.gz:", matching_files)
                    repeteated_ID = 0
                    for subjects in matching_files:
                        # guardo el nom del lab per poder fer neteja més tard
                        if (lab_name == ""):
                            lab_name = subjects.split('/')[0]
                        # guardo ID's per renombrar els arxius
                        ID = subjects.split('/')[1]
                        # hi ha algun lab amb més d'un arxiu anat per subjecte
                        if (ID in ID_Folders):
                            repeteated_ID += 1
                            ID_Folders.append(ID + "_" + str(repeteated_ID))
                        else:
                            repeteated_ID = 0
                            ID_Folders.append(ID)
                    print (f"Found: {ID_Folders}")
                    
                    index_ID = 0 
                    for anat_file in matching_files:
                        tar.extract(anat_file,new_path)
                        extracted_file = os.path.join(new_path, anat_file)
                        renamed = os.path.join(new_path,ID_Folders[index_ID] +  "_"  + file_to_rename)
                        index_ID += 1
                        # copiar i renombrar
                        shutil.copy(extracted_file, renamed)
                        print(f"File '{file_to_rename}' copied and renamed to '{renamed}' successfully!")
                    # eliminar el directori on ho ha descomprimit
                    shutil.rmtree(new_path + lab_name, ignore_errors=True)
                    



