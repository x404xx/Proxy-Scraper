from banner import *
from scraper import *
from os import system
system('cls')


def main():
    if protocol == 1:
        PROTO = 'http'
        TYPE = '1'
        print(f'\n{symb} {green}Scraping HTTP now..{reset}\n')
        if (proxy := Scraper(PROTO, TYPE, QUANTITY)):
            with open('http.txt', 'w', encoding='utf-8') as result:
                for prox in proxy:
                    print(prox)
                    result.write(f'http://{prox}\n')
                print(f'''
{strg}
        {done}''')

    elif protocol == 2:
        PROTO = 'socks'
        TYPE = '2'
        print(f'\n{symb} {green}Scraping SOCKS now..{reset}\n')
        if (proxy := Scraper(PROTO, TYPE, QUANTITY)):
            with open('socks5.txt', 'w', encoding='utf-8') as result:
                for prox in proxy:
                    print(prox)
                    result.write(f'socks5://{prox}\n')
                print(f'''
{strg}
        {done}''')

    else: print(f'\n{red}Not Exist!{reset}\n')


if __name__ == '__main__':

    print(f'''{title}
{strg}''')

    protocol = int(input(proc))
    quantity = int(input(qtt))
    if quantity == 1: QUANTITY = '0'
    elif quantity == 2: QUANTITY = '1'
    elif quantity == 3: QUANTITY = '2'
    elif quantity == 4: QUANTITY = '3'
    elif quantity == 5: QUANTITY = '4'
    elif quantity == 6: QUANTITY = '5'
    else: print(f'\n{red}Not Exist!{reset}\n')
    main()



