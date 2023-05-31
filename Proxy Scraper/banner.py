from colored import attr, fg

from ui import Center, Colorate, Colors


class Colored:
    #! Colored code
    YELLOW = fg('yellow')
    WHITE = fg('white')
    BLUE = fg(20)
    CYAN = fg('cyan')
    GREEN = fg(46)
    RED = fg('red')
    PURPLE = fg('purple_1a')
    GREY = fg('grey_27')
    ORANGE = fg('orange_red_1')
    BOLD = attr('bold')
    RESET = attr('reset')


LOGO = r'''
 █▀▄ █▀▄ ▄▀▄ ▀▄▀ ▀▄▀   ▄▀▀ ▄▀▀ █▀▄ ▄▀▄ █▀▄ ██▀ █▀▄  
 █▀  █▀▄ ▀▄▀ █ █  █    ▄██ ▀▄▄ █▀▄ █▀█ █▀  █▄▄ █▀▄ ▄
'''

BANNER = (Colorate.Diagonal(Colors.red_to_yellow, Center.XCenter(LOGO)))
BY = (Colorate.Horizontal(Colors.black_to_white, Center.XCenter(r'BY: ══ᵂʰᵒᴬᴹ!')))

TITLE = f'''
{BANNER}
    {BY}
'''

SYMBOL = f'{Colored.PURPLE}{Colored.BOLD}[:>]{Colored.RESET}'
ARROW = f'{Colored.GREY}{"»" * 70}{Colored.RESET}'
DONE = f"\n\t🏁 {Colored.ORANGE}DONE..!{Colored.RESET}\n"

PROTOCOL_MENU = f'''
{Colored.PURPLE}{Colored.BOLD}[1] {Colored.BLUE}{Colored.BOLD}HTTP
{Colored.PURPLE}{Colored.BOLD}[2] {Colored.BLUE}{Colored.BOLD}SOCKS

{Colored.WHITE}📍 Please choose:{Colored.RESET} '''

QUANTITY_MENU = f'''
{Colored.PURPLE}{Colored.BOLD}[1] {Colored.BLUE}{Colored.BOLD}30
{Colored.PURPLE}{Colored.BOLD}[2] {Colored.BLUE}{Colored.BOLD}50
{Colored.PURPLE}{Colored.BOLD}[3] {Colored.BLUE}{Colored.BOLD}100
{Colored.PURPLE}{Colored.BOLD}[4] {Colored.BLUE}{Colored.BOLD}200
{Colored.PURPLE}{Colored.BOLD}[5] {Colored.BLUE}{Colored.BOLD}300
{Colored.PURPLE}{Colored.BOLD}[6] {Colored.BLUE}{Colored.BOLD}500

{Colored.WHITE}📍 How many:{Colored.RESET} '''
