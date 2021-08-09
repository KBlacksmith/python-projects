from os import EX_TEMPFAIL, path

class Book(): 
    def __init__(self):
        self.key = 0
        self.score = -1
        self.name = ''
        self.genre = ''
        self.prev = None
        self.next = None
    def __str__(self): 
        return f'{self.key}#-#{self.score}#-#{self.name}#-#{self.genre}\n'
    def print_book(self)->None: 
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
            while yn != 'n' and yn != 'N': 
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

class BookList(): 
    def __init__(self)->None:
        self.first = None
        self.last = None
        self.main_key = 0
        self.increment = 1
        aux = None
        if(path.exists('series.txt')): 
            with open('series.txt') as f: 
                aux = Book()
                text = f.readline().split('#-#')
                while(text != ['']):
                    aux = Book()
                    aux.key = int(text[0])
                    aux.score = float(text[1])
                    aux.name = text[2]
                    aux.genre = text[3].split('\n')[0]
                    self.insert_book(aux)
                    text = f.readline().split('#-#')
    def insert_book(self, new_book: Book)->None: 
        self.main_key += 1
        new_book.key = self.main_key
        if self.first == None: 
            self.first = new_book
            self.last = new_book
        else: 
            self.last.next = new_book
            new_book.prev = self.last
            self.last = new_book
    def delete_book(self, aux: Book)->None: 
        if(aux!=self.first): 
            aux.prev.next = aux.next
        else: 
            self.first = aux.next
        if(aux != self.last): 
            aux.next.prev = aux.prev
        else: 
            self.last = aux.prev
        temp = aux.next
        while(temp != None): 
            temp.key -= self.increment
            temp = temp.next
        self.main_key -= self.increment
        temp = aux
        aux = None
        del temp
    def search_key(self)->Book: 
        aux = self.first
        keyV = 0
        while True: 
            try: 
                keyV = int(input('Enter the desired series\'s key value: '))
                break; 
            except ValueError: 
                print("Invalid input, try again")
        while(aux != None): 
            if aux.key == keyV: 
                return aux
            else: 
                aux = aux.next
        print("No Series with key value \"{}\" was found".format(keyV))
        return None
    def search_name(self)->Book: 
        aux = self.first
        name = input("Enter the desired series's name: ")
        while(name == ''): 
            print("\"Name\" cannot be empty....")
            name = input("Enter the desired series's name: ")
        while(aux != None): 
            if(aux.name.lower() == name.lower()):
                return aux
            else: 
                aux = aux.next
        print("No Series named \"{}\" was found...".format(name))
        return None
    def search_genre(self)->None: 
        genre = input("Enter the genre you seek: ").lower().capitalize()
        while genre == '': 
            print("\"Genre\" cannot be empty...")
            genre = input("Enter the genre you seek: ").lower().capitalize()
        if self.first != None: 
            aux = self.first
            found = False
            while(aux != None): 
                if(genre in aux.genre.split('/')): 
                    aux.print_book()
                    found = True
                aux = aux.next
            if not found: 
                print("The list has no series that beong to the \"{}\" genre\n".format(genre))
        else: 
            print("No series registered in the system\n")
    def print_list(self)->None: 
        if self.first != None: 
            print("Key\t\tName (Score)")
            aux = self.first
            while(aux != None): 
                aux.print_book()
                aux = aux.next
        else: 
            print("No series registered in the system\n")
    def book_exists(self, new_book: str)->bool: 
        aux = self.first
        while(aux != None): 
            if aux.name.lower() == new_book.lower(): 
                return True
            else: 
                aux = aux.next
        return False
    def partition_by_score(self, f: Book, l: Book)->Book: 
        pivot = l.score
        i = f
        j = f
        while(j != l): 
            if j.score > pivot: 
                self.swap(i, j)
                i = i.next
            j = j.next
        self.swap(i, l)
        return i
    def sort_by_score(self, f: Book, l: Book)->None: 
        if l != None and f != l and f != l.next: 
            pivot = self.partition_by_score(f, l)
            self.sort_by_score(f, pivot.prev)
            self.sort_by_score(pivot.next, l)
    def partition_by_name(self, f: Book, l: Book)->Book: 
        pivot = l.name.lower()
        i = f
        j = f
        while(j != l): 
            if j.name.lower() < pivot: 
                self.swap(i, j)
                i = i.next
            j = j.next
        self.swap(i, l)
        return i
    def sort_by_name(self, f: Book, l: Book)->None: 
        if l != None and f != l and f != l.next: 
            pivot = self.partition_by_name(f, l)
            self.sort_by_name(f, pivot.prev)
            self.sort_by_name(pivot.next, l)
    def swap(self, a: Book, b: Book)->None: 
        name = a.name
        score = a.score 
        genre = a.genre 
        a.name = b.name
        a.score = b.score
        a.genre = b.genre
        b.name = name
        b.score = score
        b.genre = genre
    def update_book(self, aux: Book)->None: 
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
                if self.book_exists(new_name): 
                    print("Duplicate Series, \"{}}\" already exists".format(new_name))
                else: 
                    aux.name = new_name
                    print("Series updated succesfully!\n")
                    aux.display()
            elif opc == 2: 
                new_score = -1
                try: 
                    new_score = float(input("New Score: "))
                    if(new_score<0 or new_score > 10): 
                        print("\"Score\" value must be between 0 and 10")
                    else: 
                        aux.score = new_score
                        print("Book updated succesfully!\n")
                except ValueError: 
                    print("Invalid value, try again...")
                
            elif opc == 3: 
                sub = -1
                while sub != 3: 
                    print("Options\n1.- Add Genre\n2.- Change Genre\n3.- Delete Genre\n4.- Exit")
                    sub = menu_input(1, 4)
                    if sub == 1: 
                        new_genre = ''
                        while(new_genre == ''): 
                            new_genre = input("New genre: ").lower().capitalize()
                        aux.genre+='/'+new_genre
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
                            aux.display()
                        else: 
                            print(f"\"{new_genre}\" not in displayed genres")
            else: 
                print("Returning to main menu")
    def __del__(self)->None: 
        aux = self.first
        with open('series.txt', 'w') as f: 
            while(aux != None): 
                #f.write(str(aux.key)+'#-#'+str(aux.score)+'#-#'+aux.name+'#-#'+aux.genre+'\n')
                f.write(aux.__str__())
                aux = aux.next
    


def sub_menu(aux: Book, m_list: BookList)->None: 
    opc = 0
    while opc != 3: 
        aux.display()
        print("1.- Update Series\n2.- Delete Series\n3.- Exit")
        opc = menu_input(1, 3)
        if opc == 1:
            m_list.update_book(aux)
        elif opc == 2: 
            m_list.delete_book(aux)
            print("Series deleted succesfully")
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

