import os
import shutil
import webbrowser
import time
import urllib.request
import subprocess
import platform
import tempfile  # Add this import

RED = "\033[91m"
ENDC = "\033[0m"
GREEN = "\033[92m"

BANNIERE = [
    "░▒▓███████▓▒░░▒▓████████▓▒░▒▓███████▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓████████▓▒░",
    "░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░         ",
    "░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░         ",
    "░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░         ",
    "░▒▓█▓▒░░▒▓█▓▒░▒▓██████▓▒░ ░▒▓███████▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓██████▓▒░    ",
    "░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░        ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░         ",
    "░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░        ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░         ",
    "░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░        ░▒▓█▓▒░    ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░"
]

def print_centered(text):
    columns = shutil.get_terminal_size().columns
    print(f"{text:^{columns}}")

def afficher_banniere():
    print_centered(RED)
    for ligne in BANNIERE:
        print_centered(ligne)
    print_centered(ENDC)

def menu_principal():
    print_centered("\nBienvenue dans NeptuneHub !")
    print_centered(RED)
    print_centered("1. Réparer Solara")
    print_centered("2. Installer Bloxstrap")
    print_centered("3. Rejoindre le serveur")
    print_centered("0. Quitter")
    print_centered(ENDC)

def supprimer_fichiers_temporaires():
    nom_utilisateur = os.getenv('USERNAME')
    dossier_temporaire = fr'C:\Users\{nom_utilisateur}\AppData\Local\Temp'
    
    try:
        for fichier in os.listdir(dossier_temporaire):
            chemin_complet = os.path.join(dossier_temporaire, fichier)
            
            if os.path.isfile(chemin_complet):
                os.remove(chemin_complet)
            elif os.path.isdir(chemin_complet):
                shutil.rmtree(chemin_complet)
                
        print(f"Tous les fichiers temporaires dans {dossier_temporaire} ont été supprimés avec succès.")
        
    except Exception as e:
        time.sleep(2)
        print("Solara Réparer relancer Solara \nbon jeu !")

def supprimer_fichiers_temporaires():
    nom_utilisateur = os.getenv('USERNAME')
    dossier_temporaire = fr'C:\Users\{nom_utilisateur}\AppData\Local\Temp'
    
    try:
        for fichier in os.listdir(dossier_temporaire):
            chemin_complet = os.path.join(dossier_temporaire, fichier)
            try:
                if os.path.isfile(chemin_complet):
                    os.remove(chemin_complet)
                elif os.path.isdir(chemin_complet):
                    shutil.rmtree(chemin_complet)
                print(f"Supprimé : {chemin_complet}")
            except Exception as e:
                print(f"Erreur en supprimant {chemin_complet}: {e}")

        print(f"{GREEN}Tous les fichiers temporaires De solara ont été supprimés avec succès.{ENDC}")
    except Exception as e:
        print(f"{RED}Erreur en accédant au dossier temporaire : {e}{ENDC}")

def supprimer_fichiers_solara(drive_letter):
    for root, _, files in os.walk(f"{drive_letter}:\\"):
        for file in files:
            if "solara" in file.lower():
                try:
                    os.remove(os.path.join(root, file))
                    print(f"Supprimé : {os.path.join(root, file)}")
                except OSError as e:
                    print(f"Erreur en supprimant {os.path.join(root, file)}: {e}")

def nettoyer_pc():
    supprimer_fichiers_temporaires()
    drive_letter = input("Entrez la lettre de votre disque local pour nettoyer les fichiers 'solara' (par défaut C) : ") or "C"
    supprimer_fichiers_solara(drive_letter)
    print("Tous les fichiers ont été supprimés avec succès.")

def bloxstrap_deja_installe():
    user_folder = os.path.expanduser("~")
    play_roblox_shortcut = os.path.join(user_folder, "AppData", "Roaming", "Microsoft", "Windows", "Start Menu", "Programs", "Play Roblox.lnk")
    return os.path.exists(play_roblox_shortcut)

def installer_bloxstrap():
    if bloxstrap_deja_installe():
        print("Bloxstrap est déjà installé sur votre système. Aucune action supplémentaire requise.")
        return
    
    url_download = "https://github.com/pizzaboxer/bloxstrap/releases/download/v2.6.1/Bloxstrap-v2.6.1.exe"
    temp_dir = tempfile.gettempdir()
    file_path = os.path.join(temp_dir, "Bloxstrap-v2.6.1.exe")
    
    print("Téléchargement de Bloxstrap...")
    urllib.request.urlretrieve(url_download, file_path)
    print("Téléchargement terminé.")

    print("Installation de Bloxstrap...")
    if platform.system() == "Windows":
        try:
            subprocess.run(file_path, check=True)
            print("Installation réussie.")
        except subprocess.CalledProcessError as e:
            print(f"Erreur lors de l'installation : {e}")
    else:
        print("L'installation automatique n'est pas supportée sur ce système.")
        print(f"Veuillez installer Bloxstrap manuellement depuis {url_download}")

def rejoindre_discord():
    url_discord = "https://discord.gg/"
    webbrowser.open(url_discord)

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        afficher_banniere()
        menu_principal()
        choix = input("Choisissez une option : ").strip()
        if choix == "1":
            supprimer_fichiers_temporaires()
        elif choix == "2":
            installer_bloxstrap()
        elif choix == "3":
            rejoindre_discord()
        elif choix == "0":
            print("Merci d'avoir utilisé NeptuneHub !")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")
        input("\nAppuyez sur Entrée pour continuer...")

if __name__ == "__main__":
    main()
