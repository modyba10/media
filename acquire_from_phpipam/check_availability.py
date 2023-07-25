import subprocess

# Adresse IP à vérifier
ip_address = "10.35.4.13"

# Fonction pour effectuer un ping et vérifier l'état de l'adresse IP
def is_ip_address_alive(ip_address):
    # Commande de ping pour vérifier l'état de l'adresse IP
    ping_command = ["ping", "-c", "1", ip_address]
    
    # Exécute la commande de ping
    try:
        subprocess.check_output(ping_command)
        return True  # Si la commande de ping s'exécute avec succès, l'adresse IP est en ligne (alive)
    except subprocess.CalledProcessError:
        return False  # Si la commande de ping échoue, l'adresse IP est hors ligne (offline)

# Vérifie si l'adresse IP est en ligne ou hors ligne
if is_ip_address_alive(ip_address):
    print(f"L'adresse IP {ip_address} est en ligne (alive).")
else:
    print(f"L'adresse IP {ip_address} est hors ligne (offline).")
