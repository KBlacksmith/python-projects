import series
mangalist = series.BookList()
aux = None
menu = 0
while(menu!=7): 
    print("<<<<< Manga Database >>>>>")
    print("""1.- Add new entry\n2.- Search by key\n3.- Search entry by name\n4.- Show entry list\n5.- Entries by Genre\n6.- Sort list\n7.- Exit""")
    menu = series.menu_input(1, 7)
    if menu == 1:
        print("<<< New Book Menu >>>")
        aux = series.Book() 
        print("Input the entry's data\n")
        aux.capture_data()
        if not mangalist.book_exists(aux.name): 
            mangalist.insert_book(aux)
            print(f'\"{aux.name}\" stored succesfully!\n')
        else: 
            print("Duplicate entry cannot be stored")
            temp = aux
            aux = None
            del temp
    elif menu == 2: 
        print("<<< Search by Key Menu >>>")
        aux = mangalist.search_key()
        if aux != None: 
            aux.display()
            series.sub_menu(aux, mangalist)
            temp = aux
            aux = None
            del temp
    elif menu == 3: 
        print("<<< Search by Name Menu >>>")
        aux = mangalist.search_name()
        if aux != None: 
            aux.display()
            series.sub_menu(aux, mangalist)
            temp = aux
            aux = None
            del temp
    elif menu == 4: 
        print("<<< Full List >>>")
        mangalist.print_list()
    elif menu == 5: 
        print("<<< Search by Genre >>>")
        mangalist.search_genre()
    elif menu == 6:
        opc = 0
        while opc != 3: 
            print("<<< Sorting Menu >>>")
            print("1.- Sort by Score\n2.- Sort by Name\n3.- Exit")
            opc = series.menu_input(1, 3)
            if opc == 1: 
                mangalist.sort_by_score(mangalist.first, mangalist.last)
                print("Updated List: ")
                mangalist.print_list()
            elif opc == 2: 
                mangalist.sort_by_name(mangalist.first, mangalist.last)
                print("Updated list: ")
                mangalist.print_list()
            else: 
                print("Returning to main menu...")
    else: 
        print("Goodbye!")