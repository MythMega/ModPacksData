#!/usr/bin/env python3
import os

def main():
    # Ouvre (ou crée) le fichier pack.txt en mode "append"
    with open("pack.txt", "a", encoding="utf-8") as pack_file:
        # Parcourt tous les fichiers du répertoire courant
        for filename in os.listdir("."):
            # Vérifie que le fichier se termine par ".jar"
            if filename.endswith(".jar"):
                # Récupère le nom du fichier sans l'extension
                filename_without_ext = os.path.splitext(filename)[0]
                # Construit l'URL en insérant le nom complet du fichier
                url = f"https://github.com/MythMega/ModPacksData/raw/refs/heads/master/CobbleForge1.21/{filename}"
                # Crée la ligne au format demandé
                line = f"{filename_without_ext};{url};required;0\n"
                # Écrit la ligne dans pack.txt
                pack_file.write(line)
                print(f"Ligne ajoutée pour {filename}")

if __name__ == "__main__":
    main()
