from re import findall, search

from bs4 import BeautifulSoup as bs
from httpx import Client
from user_agent import generate_user_agent as gua


class SpysOne:
    SCRIPT_PATTERN = r'javascript">(.*?);<'
    PROXY_PATTERN = r'spy14>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?"\+(.*?)\)<'
    DATE_TIME_PATTERN = r'spy14>(\d{2}-\w{3}-\d{4})</font> (\d{2}:\d{2}) <font class=spy5>([(]\d{1,2} \w{4,5} \w{3}[)])'

    def __init__(
        self,
        proxy_type: str,
        proxy_number: str,
        quantity: str,
        info: bool=False
        ):

        self.proxy_type = proxy_type
        self.proxy_number = proxy_number
        self.quantity = quantity
        self.info = info
        self.client = Client(timeout=30)
        self.payload = {'data': {}}
        self.base_url = f'https://spys.one/en/{self.proxy_type}-proxy-list/'
        self.client.headers.update({
            'Host': 'spys.one',
            'User-Agent': gua(),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5'
        })

    def scrape(self):
        response = self.client.get(self.base_url)
        soup = bs(response.content, 'lxml')
        self._handle_form(soup)
        get_list = self._get_proxy_list(self.base_url)
        yield from self._parse_proxy_results(get_list)

    def __del__(self):
        self.client.close()

    def _handle_form(
        self, soup
        ):

        form = self._find_form(soup)
        self.payload.update(form.attrs)
        self._update_input_fields(form)
        self._update_select_fields(form)

    def _find_form(
        self, soup
        ):

        form_selector = f'form[action*="{self.proxy_type}-proxy-list"]'
        return soup.select_one(form_selector)

    def _update_input_fields(
        self, form
        ):

        for input_tag in form.find_all('input'):
            self.payload['data'][input_tag['name']] = input_tag.get('value', '')

    def _update_select_fields(
        self, form
        ):

        for select_tag in form.find_all('select'):
            self.payload['data']['xf5'] = self.proxy_number
            if select_tag.previous_sibling.text.strip() == 'Show':
                self.payload['data'][select_tag['name']] = self.quantity
            else:
                self.payload['data'][select_tag['name']] = select_tag.option['value']

    def _get_proxy_list(
        self, url
        ):

        response = self.client.post(url, data=self.payload['data'])
        return response.text

    def _parse_proxy_results(
        self, get_list
        ):

        if (script := search(self.SCRIPT_PATTERN, get_list)):
            for key, value in self._extract_globals(script.group(1)):
                globals()[key] = int(value) if value.isdigit() else eval(value)

            if (proxy_matches := findall(self.PROXY_PATTERN, get_list)) and (date_time_matches := findall(self.DATE_TIME_PATTERN, get_list)):
                for proxy_data, date_time_data in zip(proxy_matches, date_time_matches):
                    proxy, port = self._parse_proxy(proxy_data)
                    date, time, taken = self._parse_date_time(date_time_data)
                    if self.info:
                        yield f'{proxy}:{port} - {date} - {time} {taken}'
                    else:
                        yield f'{proxy}:{port}'

    def _extract_globals(
        self, script
        ):

        globals_list = script.split(';')
        for item in globals_list:
            key, value = item.split('=')
            yield key.strip(), value.strip()

    def _parse_proxy(
        self, proxy_data
        ):

        proxy, port_script = proxy_data
        port = ''.join([str(eval(part)) for part in port_script.split('+')])
        return proxy, port

    def _parse_date_time(
        self, date_time_data
        ):

        date, time, taken = date_time_data
        return date, time, taken
