# class Dhruvlibrary:
#     def __init__(self,list,name):
#         self.booklist=list
#         self.name=name
#         self.lendDict={}
#
#     def displaybooks(self):
#         print(f"we have following books in our library:{self.name}")
#         for book in self.booklist:
#             print(book)
#
#     def lendbook(self,user,book):
#         if book not in self.lendDict.keys():
#             self.lendDict.update({book:user})
#             print("xyz")
#         else:
#             print("abc")
#
#     def addbook(self,book):
#         self.booklist.append(book)
#         print("book has been added to the book list")
#
#     def returnbook(self,book):
#         self.booklist.remove(book)
# if __name__ == '__main__':
#     dhruv=Dhruvlibrary(['python','c++','ml','data science','harry potter'],"Dhruvrajsinh")
#
#     while(True):
#         print(f"welcome to the {dhruv.name} library. \n enter your choice to continue")
#         print("1.display books")
#         print("2.lend a book")
#         print("3.add a book")
#         print("4.return a book")
#         user_choice=int(input())
#
#         if user_choice==1:
#             dhruv.displaybooks()
#         elif user_choice==2:
#             book=input("enter the name of book you want to lend")
#             name=input("enter your name")
#             dhruv.lendbook(name,book)
#         elif user_choice==3:
#             book=input("enter the name of book you want to add")
#             dhruv.addbook(book)
#         elif user_choice==4:
#             book=input("enter the name of book you want to return")
#             dhruv.returnbook(book)
#         else:
#             print("not a valid option")
#
#         user_choice2=""
#         print("press q to quit and c to continue")
#         while (user_choice2!="q" and user_choice2!="c"):
#             user_choice2=input()
#             if user_choice2=="q":
#                 exit()
#             if user_choice2=="c":
#                 continue




class Library:
    def __init__(self, list, name):
        self.booksList = list
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"We have following books in our library: {self.name}")
        for book in self.booksList:
            print(book)

    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender-Book database has been updated. You can take the book now")
        else:
            print(f"Book is already being used by {self.lendDict[book]}")

    def addBook(self, book):
        self.booksList.append(book)
        print("Book has been added to the book list")

    def returnBook(self, book):
        self.lendDict.pop(book)

if __name__ == '__main__':
    harry = Library(['Python', 'Rich Daddy Poor Daddy', 'Harry Potter', 'C++ Basics', 'Algorithms by CLRS'], "CodeWithHarry")

    while(True):
        print(f"Welcome to the {harry.name} library. Enter your choice to continue")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        user_choice = input()
        if user_choice not in ['1','2','3','4']:
            print("Please enter a valid option")
            continue

        else:
            user_choice = int(user_choice)


        if user_choice == 1:
            harry.displayBooks()

        elif user_choice == 2:
            book = input("Enter the name of the book you want to lend:")
            user = input("Enter your name")
            harry.lendBook(user, book)

        elif user_choice == 3:
            book = input("Enter the name of the book you want to add:")
            harry.addBook(book)

        elif user_choice == 4:
            book = input("Enter the name of the book you want to return:")
            harry.returnBook(book)

        else:
            print("Not a valid option")


        print("Press q to quit and c to continue")
        user_choice2 = ""
        while(user_choice2!="c" and user_choice2!="q"):
            user_choice2 = input()
            if user_choice2 == "q":
                exit()

            elif user_choice2 == "c":
                continue
