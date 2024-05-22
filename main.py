import printIcons as p
import Exceptions as e
def main():
    global ls
    p.load()
    choose = input("Pick a Choice:\n 1-Print all icons. 2-Search icons by keywordFirst\n")
    if choose == "1":
        ls=p.print_all_icons()
    elif choose == "2":
        ls=p.search_icons_by_keyword()
        if len(ls)==0:
            return
    else:
        raise e.WrongChoiceException("insert 1 or 2")
    i = int(input("insert index to display icon\n")) - 1
    if len(ls) > i and i >= 0:
        print(ls[i])
    p.display_icon(ls[i])

if __name__ == '__main__':
    main()