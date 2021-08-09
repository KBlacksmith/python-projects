from os import path

class Entry(): 
    def __init__(self):
        self.key = 0
        self.score = -1
        self.name = ''
        self.genre = ''
        self.prev = None
        self.next = None
    def print_entry(self)->None: 
        print('{}\t\t{} ({})'.format(self.key, self.name, self.score))
    def display(self)->None: 
        print("Key: "+str(self.key))
        print("Name: "+self.name)
        print("Score: "+str(self.score))
        if self.genre == '': 
            print("Genre: N/A")
        else: 
            print("Genre: "+self.genre)
    def capture_data(self)->None: 
        confirm = ''
        while confirm != 'y' and confirm != 'yes': 
            self.name = input("Name: ")
            while(self.name == ''): 
                print("\"Name\" value cannot be empty")
                self.name = input("Name: ")
            while True: 
                try: 
                    self.score = float(input("Score: "))
                    if(self.score >= 0 and self.score <= 10): 
                        break
                except ValueError: 
                    print("Invalid value, try again...")
                print("\"Score\" value must be between 0 and 10")
            yn = ''
            self.genre = input("Genre: ").lower().capitalize()
            while yn != 'n' and yn != 'no': 
                if(self.genre == ''): 
                    break
                subgenre = ''
                yn = input("Does {} belong to one more genre? Y/n: ".format(self.name)).lower()
                while yn != 'y' and yn != 'n' and yn != 'yes' and yn != 'no': 
                    yn = input("Y/n: ").lower()
                if yn == 'yes' or yn == 'y': 
                    print("Name: {}".format(self.name))
                    print("Score: {}".format(self.score))
                    print("Genre: {}".format(self.genre))
                    subgenre = input("Enter the other genre: ").lower().capitalize()
                    while subgenre == '': 
                        print("\"Genre\" cannot be empty")
                        subgenre = input("Enter the other genre: ").lower().capitalize()
                    self.genre+="/"+subgenre
            print("\nInfo: ")
            print("Name: {}".format(self.name))
            print("Score: {}".format(self.score))
            print("Genre: {}".format(self.genre))
            confirm = input("Do you confirm this information? Y/n: ").lower()
            while confirm not in ['y', 'yes', 'n', 'no']: 
                confirm = input("Y/n: ")
def sub_menu(aux: Entry, m_list: list)->None: 
    opc = 0
    while opc != 3: 
        aux.display()
        print("1.- Update Entry\n2.- Delete Entry\n3.- Exit")
        opc = menu_input(1, 3)
        if opc == 1:
            update_entry(m_list, aux)
        elif opc == 2: 
            delete_entry(m_list, aux)
            print("Entry deleted succesfully")
            break
        else: 
            print("Returning to main menu...")


def menu_input(low: int, high: int)->int: 
    menu = 0
    while True: 
        try: 
            menu = int(input("Choose option: "))
            if menu >= low and menu <= high: 
                return menu
            else: 
                print("Choose a value between {} and {}".format(low, high))
        except ValueError: 
            print("Invalid input, try again")

def insert_entry(m_list: list, new_entry: Entry)->None: 
    if len(m_list) == 0: 
        new_entry.key = 1
    else: 
        new_entry.key = m_list[len(m_list)-1].key +1
    m_list.append(new_entry)
def entry_exists(m_list: list, new_entry: str)->bool: 
    for e in m_list: 
        if e.name.lower() == new_entry.lower(): 
            return True
    return False
def search_key(m_list: list)->Entry:
    key = 0
    while True: 
        try: 
            key = int(input("Enter the desired series\'s key value: "))
            break
        except ValueError: 
            print("Invalid input, try again")
    for e in m_list: 
        if e.key == key: 
            return e
    print("Noe entry with key value \"{}\" was found".format(key))
    return None
def search_name(m_list: list)->Entry: 
    name = input("Enter the desired series's name: ")
    while(name == ''): 
        print("\"Name\" cannot be empty....")
        name = input("Enter the desired series's name: ")
    for e in m_list: 
        if e.name.lower() == name.lower(): 
            return e
    print("No entry named \"{}\" was found".format(name))
    return None
def print_list(m_list: list())->None: 
    if len(m_list) != 0: 
        print("Key\t\tName (Score)")
        for e in m_list: 
            e.print_entry()
    else: 
        print("No series registered in the system")
def search_genre(m_list: list)->None: 
    genre = input("Enter the genre you seek: ").lower().capitalize()
    while genre == '': 
        print("\"Genre\" cannot be empty...")
        genre = input("Enter the genre you seek: ").lower().capitalize()
    if len(m_list) != 0: 
        found = False
        for e in m_list: 
            if genre in e.genre.split('/'): 
                e.print_entry()
                found = True
        if not found: 
            print("The list has no series that belong to the \"{}\" genre".format(genre))
    else: 
        print("No series registered in the system")
def swap(a: Entry, b: Entry)->None: 
    name = a.name
    score = a.score
    genre = a.genre
    a.name = b.name
    a.score = b.score
    a.genre = b.genre
    b.name = name
    b.score = score
    b.genre = genre

def partition_by_score(m_list: list, first: int, last: int)->int: 
    pivot = m_list[last].score
    i = first
    for j in range(first, last): 
        if m_list[j].score > pivot: 
            swap(m_list[i], m_list[j])
            i+=1
    swap(m_list[i], m_list[last])
    return i
def sort_by_score(m_list: list, first: int, last: int)->None: 
    if first < last: 
        pivot = partition_by_score(m_list, first, last)
        sort_by_score(m_list, first, pivot-1)
        sort_by_score(m_list, pivot+1, last)
def partition_by_name(m_list: list, first: int, last: int)->int: 
    pivot = m_list[last].name.lower()
    i = first
    for j in range(first, last): 
        if m_list[j].name.lower() < pivot: 
            swap(m_list[i], m_list[j])
            i+=1
    swap(m_list[i], m_list[last])
    return i
def sort_by_name(m_list: list, first: int, last: int)->None: 
    if first < last: 
        pivot = partition_by_name(m_list, first, last)
        sort_by_name(m_list, first, pivot-1)
        sort_by_name(m_list, pivot+1, last)
def create_list(m_list: list)->None: 
    if(path.exists('series.txt')): 
        with open('series.txt') as f:
            text =f.readline().split('#-#')
            while(text != ['']): 
                aux = Entry()
                aux.key = int(text[0])
                aux.score = float(text[1])
                aux.name = text[2]
                aux.genre = text[3].split('\n')[0]
                insert_entry(m_list, aux)
                text = f.readline().split('#-#')
def delete_entry(m_list: list, aux: Entry)->None: 
    position = aux.key-1
    m_list.remove(aux)
    for i in range(position, len(m_list)): 
        m_list[i].key-=1
    temp = aux
    aux = None
    del temp
def destroy_list(m_list: list)->None: 
    with open('series.txt', 'w') as f: 
        for e in m_list: 
            f.write(str(e.key)+'#-#'+str(e.score)+'#-#'+e.name+'#-#'+e.genre+'\n')
def update_entry(m_list: list, aux: Entry)->None: 
    opc = 0
    while opc != 4: 
        aux.display()
        print("Which value do you wish to update?")
        print("1.- Name\n2.- Score\n3.- Genre\n4.- None")
        opc = menu_input(1, 4)
        if opc == 1: 
            new_name = ''
            while new_name == '': 
                new_name = input("Enter the new name: ")
            if entry_exists(m_list, new_name) and new_name.lower() != aux.name: 
                print("Duplicate entry, \"{}\" already exists".format(new_name))
            else: 
                aux.name = new_name
                print("Entry updated succesfully!\n")
        elif opc ==2: 
            new_score = -1
            try: 
                new_score = float(input("New Score: "))
                if(new_score<0 or new_score > 10): 
                    print("\"Score\" value must be between 0 and 10")
                else: 
                    aux.score = new_score
                    print("Entry updated succesfully!\n")
            except ValueError: 
                print("Invalid value, try again...")
        elif opc == 3: 
            sub = -1
            while sub != 4: 
                print("Options\n1.- Add Genre\n2.- Change Genre\n3.- Delete Genre\n4.- Exit")
                sub = menu_input(1, 4)
                if sub == 1: 
                    new_genre = ''
                    while(new_genre == ''): 
                        new_genre = input("New genre: ").lower().capitalize()
                    if aux.genre != '': 
                        aux.genre+='/'
                    aux.genre += new_genre
                    aux.display()
                elif sub == 2: 
                    new_genre = ''
                    while(new_genre == ''): 
                        new_genre = input("New genre: ").lower().capitalize()
                    aux.genre = new_genre
                    aux.display()
                elif sub == 3: 
                    subgenres = aux.genre.split('/')
                    new_genre = ''
                    print(f"{aux.name}\n")
                    print("Genres: ")
                    print(subgenres)
                    while(new_genre == ''): 
                        new_genre = input("Select the genre to be deleted: ").lower().capitalize()
                    if new_genre in subgenres: 
                        subgenres.remove(new_genre)
                        aux.genre = ''
                        for sub_g in subgenres: 
                            if sub_g != subgenres[0]: 
                                aux.genre += '/'
                            aux.genre += sub_g
                        print("Genre deleted succesfully!")
                    else: 
                        print(f"\"{new_genre}\" not in displayed genres")
        else: 
            print("Returning to main menu")
