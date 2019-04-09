import requests
from lxml import etree
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6756.400 QQBrowser/10.3.2473.400'}

def ip_port(pages = 3):
    """获取ip数据,默认爬三页"""
    https_list= []
    http_list = []
    for page in range(1,pages + 1):
        url= "http://www.ip3366.net/?stype=1&page=%s" % str(page)
        Html_data = requests.get(url,headers = header)
        html = etree.HTML(Html_data.text)
        ip_adrs = html.xpath('//tr/td[1]/text()')
        ports= html.xpath('//tr/td[2]/text()')
        ip_types = html.xpath('//tr/td[4]/text()')
        for ip_adr,port,ip_type in zip(ip_adrs,ports,ip_types):
            if ip_type == 'HTTPS':
                ip ='https://' + ip_adr+':'+port
                https_list.append(ip)
            else:
                 ip ='http://' + ip_adr+':'+port
                 http_list.append(ip)
    return http_list,https_list

def 