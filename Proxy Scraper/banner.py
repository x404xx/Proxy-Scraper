from colored import attr, fg
from ui import Center, Colors, Colorate


#! Colored code
yellow = fg("yellow")
white = fg("white")
blue = fg(20)
cyan = fg('cyan')
green = fg(46)
red = fg("red")
purple = fg("purple_1a")
grey = fg("grey_27")
org = fg('orange_red_1')
bold = attr("bold")
reset = attr("reset")


logo = r'''
 █▀▄ █▀▄ ▄▀▄ ▀▄▀ ▀▄▀   ▄▀▀ ▄▀▀ █▀▄ ▄▀▄ █▀▄ ██▀ █▀▄  
 █▀  █▀▄ ▀▄▀ █ █  █    ▄██ ▀▄▄ █▀▄ █▀█ █▀  █▄▄ █▀▄ ▄
'''

txt = r'BY: ══ᵂʰᵒᴬᴹ!'
bann = (Colorate.Diagonal(Colors.red_to_yellow, Center.XCenter(logo)))
text = (Colorate.Horizontal(Colors.black_to_white, Center.XCenter(txt)))

title = f'''
{bann}
    {text}
'''

symb = f'{purple}{bold}[:>]{reset}'
strg = f'{grey}{"»" * 70}{reset}'
srch = f'\n⏳ {white}Now searching..{reset}\n'
done = f"\n\t🏁 {org}DONE..!{reset}\n"

proc = f'''
{purple}{bold}[1] {reset}{blue}{bold}HTTP{reset}
{purple}{bold}[2] {reset}{blue}{bold}SOCKS{reset}

{white}📍 Please choose:{reset} '''

qtt = f'''
{purple}{bold}[1] {reset}{blue}{bold}30{reset}
{purple}{bold}[2] {reset}{blue}{bold}50{reset}
{purple}{bold}[3] {reset}{blue}{bold}100{reset}
{purple}{bold}[4] {reset}{blue}{bold}200{reset}
{purple}{bold}[5] {reset}{blue}{bold}300{reset}
{purple}{bold}[6] {reset}{blue}{bold}500{reset}

{white}📍 How many:{reset} '''
