from os import name, system

from api import SpysOne
from banner import (
    Colored,
    ARROW,
    DONE,
    PROTOCOL_MENU,
    QUANTITY_MENU,
    SYMBOL,
    TITLE,
)


def scraper(info=False):
    protocol_mapping = {
        1: ('1', 'http', 'http.txt', 'http://'),
        2: ('2', 'socks', 'socks5.txt', 'socks5://')
    }
    quantity_mapping = {
        1: '0',
        2: '1',
        3: '2',
        4: '3',
        5: '4',
        6: '5'
    }

    system('cls' if name == 'nt' else 'clear')
    print(f'{TITLE}\n{ARROW}')

    protocol_option = int(input(PROTOCOL_MENU))
    if protocol_option in protocol_mapping:
        proxy_number, proxy_type, file_name, prefix = protocol_mapping[protocol_option]       
        quantity_option = int(input(QUANTITY_MENU))
        quantity = quantity_mapping.get(quantity_option)
        
        print(f'\n{SYMBOL} {Colored.GREEN}Scraping {proxy_type.upper()} now..{Colored.RESET}\n')
        
        with open(file_name, 'w', encoding='utf-8') as file:
            proxies = SpysOne(proxy_type, proxy_number, quantity, info)
            if (result := proxies.scrape()):
                for proxy in result:
                    print(proxy)
                    file.write(f'{prefix}{proxy}\n')
                print(f'\n{ARROW}\n{DONE}')
    else:
        print(f'\n{Colored.RED}Please check your input!{Colored.RESET}\n')


if __name__ == '__main__':
    #! If FALSE (194.233.78.142:49653)
    #! If TRUE (194.233.78.142:49653 - 31-may-2023 - 23:15 (2 hours ago))
    scraper(info=False)
