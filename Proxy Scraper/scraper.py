import re
import httpx
from banner import *
from bs4 import BeautifulSoup as bs
from user_agent import generate_user_agent as gua


def Scraper(PROTO, TYPE, QUANTITY):

    url = f'https://spys.one/en/{PROTO}-proxy-list/'
    headers = {'Host': 'spys.one',
               'User-Agent': gua(),
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
               'Accept-Language': 'en-US,en;q=0.5'}
    payload = {'data': {}}

    soup = bs(httpx.get(url, headers=headers).content, 'lxml')
    for form in soup.findAll('form'):

        #! Update Form Attrs
        if f'{PROTO}-proxy-list' in form['action']:
            payload.update(form.attrs)

            #! Get Input Name {xpp[SHOW], xf1[ANON], xf2[SSL], xf4[PORT], xf5[TYPE], xf3[CHKDATE]}
            for inp in form.findAll('input'):
                payload['data'].update({inp['name']: inp.get('value') if inp.get('value') != None else ''})

            #! Get Type
            for sel in form.findAll(['select']):
                payload['data'].update({'xf5': f'{TYPE}'})

                #! Show Proxies = 30[0] 100[1] 200[2] 300[4] 500[5]
                if sel.previous_sibling.text.strip() == 'Show': payload['data'].update({sel['name']: f'{QUANTITY}'})
                else: payload['data'].update({sel['name']: sel.option['value']})

    getList = httpx.post(url, data=payload['data'], headers=headers).text
    if (gLob := re.search(r"<\/table><script.*>([^'].*);<\/script>", getList)):
        for i in [i.split('=') for i in gLob.group(1).split(';')]:
            if i[1].isdigit(): globals()[i[0]] = int(i[1])
            else: globals()[i[0]] = eval(i[1])

        if (proxi := re.findall(r"(?:<td\s[^>]*?><font\sclass\=spy14>(.*?)<script.*?\"\+(.*?)\)<\/script)", getList)) and (dtt := re.findall(r"<td colspan=1><font class\=spy1><font class\=spy14>(.*?)</font> (\d+[:]\d+) <font class\=spy5>([(]\d+ \w+ \w+[)])", getList)):
            for (proxy, port), (date, time, taken) in zip(proxi, dtt):
                yield f"{proxy}:{''.join([str(eval(i)) for i in port.split('+')])} - {date} - {' '.join([time, taken])}"

        return None
    return None

