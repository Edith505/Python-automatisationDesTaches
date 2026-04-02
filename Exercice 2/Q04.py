try:
    with open("Exercice 2/config.txt", 'r') as conf:
        for i in conf.readline():
            print(i)
        
        while True:
            content = conf.readline()
            if not content:
                break
            print(content)

except FileNotFoundError:
    print("Erreur : Le fichier n'existe pas")