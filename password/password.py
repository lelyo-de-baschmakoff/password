import hashlib
import json

def verify_password(password):
    length = len(password) >= 8
    uppercase = any(c.isupper() for c in password)
    lowercase = any(c.islower() for c in password)
    digit = any(c.isdigit() for c in password)
    special_char = any(c in '!@#$%^&*' for c in password)
    
    return length and uppercase and lowercase and digit and special_char

def affexigencemdp():
    print("Exigences de sécurité du mot de passe :")
    print("1. Il doit contenir au moins huit caractères.")
    print("2. Il doit contenir au moins une lettre majuscule.")
    print("3. Il doit contenir au moins une lettre minuscule.")
    print("4. Il doit contenir au moins un chiffre.")
    print("5. Il doit contenir au moins un caractère spécial (!, @, #, $, %, ^, &, *).")

def hash_password(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

def save_passwords(passwords):
    with open("passwords.json", "w") as file:
        json.dump(passwords, file)

def load_passwords():
    try:
        with open("passwords.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def add_password(passwords):
    while True:
        new_password = input("Entrez le nouveau mot de passe : ")

        if verify_password(new_password):
            hashed_password = hash_password(new_password)
            service_name = input("Entrez le nom du service : ")

            if service_name in passwords:
                existing_password = passwords[service_name]
                if existing_password == hashed_password:
                    print("Ce mot de passe existe déjà pour ce service.")
                    break
                else:
                    print("Service existant mais mots de passe différents. Ajout en cours.")
            else:
                print("Nouveau service, ajout en cours.")


            passwords[service_name] = hashed_password
            save_passwords(passwords)
            print("Mot de passe ajouté avec succès.")
            break
        else:
            print("Le mot de passe ne respecte pas les exigences de sécurité.")
            print("Veuillez choisir un nouveau mot de passe.")

def display_passwords(passwords):
    if passwords:
        print("Mots de passe enregistrés :")
        for service, _ in passwords.items():
            print(f"- {service}")
    else:
        print("Aucun mot de passe enregistré.")

def main():
    passwords = load_passwords()

    while True:
        print("\nQue souhaitez-vous faire ?")
        print("1. Ajouter un nouveau mot de passe")
        print("2. Afficher les mots de passe enregistrés")
        print("3. Quitter")

        choice = input("Choix : ")

        if choice == "1":
            affexigencemdp()
            add_password(passwords)
        elif choice == "2":
            display_passwords(passwords)
        elif choice == "3":
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
