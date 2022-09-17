# Filename: Export List of US WSOC 
# Version: 1.0
# Date: Sept 2022
# Description: Scrapes Wikipedia. Exports CSV list of women's soccer programs in the US. 

import pandas as pd

def menu():
    print("\n*** MAIN MENU ***\n\n [1] Create D1 Sheet\n [2] Create D2 Sheet\n [3] Create D3 Sheet\n [4] Create NAIA Sheet\n [5] Quit\n")

def d1():
    wiki_url = 'https://en.wikipedia.org/wiki/List_of_NCAA_Division_I_women%27s_soccer_programs'
    df = pd.read_html(wiki_url)
    df[0].to_csv('wsoc_d1.csv', index=False)
    print("\n....... D1 table created!\n\n")

def d2():
    wiki_url = 'https://en.wikipedia.org/wiki/List_of_NCAA_Division_II_women%27s_soccer_programs'
    df = pd.read_html(wiki_url)
    df[0].to_csv('wsoc_d2.csv', index=False)
    print("\n....... D2 table created!\n\n")

def d3():
    wiki_url = 'https://en.wikipedia.org/wiki/List_of_NCAA_Division_III_institutions'
    df = pd.read_html(wiki_url)
    df[0].to_csv('wsoc_d3.csv', index=False)
    print("\n....... D3 table created!\n\n")

def naia():
    wiki_url = 'https://en.wikipedia.org/wiki/List_of_NAIA_institutions'
    df = pd.read_html(wiki_url)
    df[0].to_csv('wsoc_naia.csv', index=False)
    print("\n....... NAIA table created!\n\n")

while True:
    menu()
    option = input("Enter choice >> ")

    if option=="1":
        d1()
    elif option=="2":
        d2()
    elif option=="3":
        d3()    
    elif option=="4":
        naia()
    elif option=="5":
        print("Goodbye.")
        break
    else:
        menu()
    #except ValueError:
     #   print("Invalid choice. Enter number 1-5.")
exit
