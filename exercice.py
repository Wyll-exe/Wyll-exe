todo_list = []


# Fonction pour lister les todos - à réaliser
def lister_todos():
    print('Fonctionnalité "lister les todos" à venir')
    for index, todo_create in enumerate(todo_list):
        status = "Fait" if todo_create["Fait"] else "à Faire"
        print(f"{index + 1}. {todo_create['todo']} - {status}")


# Fonction pour créer un todo - à réaliser
def creer_todo():
    print('Fonctionnalité "créer un todo" à venir')
    todo_create = input("Entrer le nom de votre todo: ")
    todo_list.append({"todo": todo_create, "Fait": False})


# Fonction pour modifier le statut d'un todo - à réaliser
def modifier_statut_todo():
    print('Fonctionnalité "modifier le statut d\'un todo" à venir')
    todo_index = int(input("Entrer l'ID du todo à modifier")) - 1
    if 0 <= todo_index < len(todo_list):
        if todo_list[todo_index]["Fait"]:
          todo_list[todo_index]["Fait"] = False
          print("Le todo à maintenant le statut 'à Faire'")
        else:
          todo_list[todo_index]["Fait"] = True
          print("Le todo à maintenant le statut 'Fait'")
    else:
       print("Oups , mauvais ID")



# Fonction pour supprimer un todo - à réaliser
def supprimer_todo():
    print('Fonctionnalité "supprimer un todo" à venir')

    lister_todos()

    todo_index = int(input("Entrer l'ID du todo à modifier")) - 1
    if 0 <= todo_index < len(todo_list):
     todo_delete = todo_list.pop(todo_index)
     print("Le todo a été supprimé")

    else:
      print("Oups , mauvais ID impossibilité de supprimer")
      




# Menu principal
choix = ''
while choix != 'q':
    # Affichage des choix
    print('\n==== Menu principal ====')
    print('1: Lister les todos')
    print('2: Créer un todo')
    print('3: Changer le statut d\'un todo')
    print('4: Supprimer un todo')
    print('q: quitter')
    print('========================')
    # Actions suivant le choix
    choix = input('=> Choix : ')
    match choix:
        case '1': lister_todos()
        case '2': creer_todo()
        case '3': modifier_statut_todo()
        case '4': supprimer_todo()
        case 'q': print('Au revoir')
        case _: print('Choix invalide')
