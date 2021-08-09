import improved
mangalist = []
aux = None
menu = 0
improved.create_list(mangalist)
while(menu!=7): 
    print("<<<<< Manga Database >>>>>")
    print("""1.- Add new entry\n2.- Search by key\n3.- Search entry by name\n4.- Show entry list\n5.- Entries by Genre\n6.- Sort list\n7.- Exit""")
    menu = improved.menu_input(1, 7)
    if menu == 1:
        print("<<< New Entry Menu >>>")
        aux = improved.Entry() 
        print("Input the entry's data\n")
        aux.capture_data()
        if not improved.entry_exists(mangalist, aux.name): 
            improved.insert_entry(mangalist, aux)
            print(f'\"{aux.name}\" stored succesfully!\n')
            aux = None
        else: 
            print("Duplicate entry cannot be stored")
            temp = aux
            aux = None
            del temp
    elif menu == 2: 
        print("<<< Search by Key Menu >>>")
        aux = improved.search_key(mangalist)
        if aux != None: 
            aux.display()
            improved.sub_menu(aux, mangalist)
            temp = aux
            aux = None
            del temp
    elif menu == 3: 
        print("<<< Search by Name Menu >>>")
        aux = improved.search_name(mangalist)
        if aux != None: 
            aux.display()
            improved.sub_menu(aux, mangalist)
            temp = aux
            aux = None
            del temp
    elif menu == 4: 
        print("<<< Full List >>>")
        improved.print_list(mangalist)
    elif menu == 5: 
        print("<<< Search by Genre >>>")
        improved.search_genre(mangalist)
    elif menu == 6:
        opc = 0
        while opc != 3: 
            print("<<< Sorting Menu >>>")
            print("1.- Sort by Score\n2.- Sort by Name\n3.- Exit")
            opc = improved.menu_input(1, 3)
            if opc == 1: 
                improved.sort_by_score(mangalist, 0, len(mangalist)-1)
                print("Updated List: ")
                improved.print_list(mangalist)
            elif opc == 2: 
                improved.sort_by_name(mangalist, 0, len(mangalist)-1)
                print("Updated list: ")
                improved.print_list(mangalist)
            else: 
                print("Returning to main menu...")
    else: 
        print("Goodbye!")
        improved.destroy_list(mangalist)