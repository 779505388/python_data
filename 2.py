import requests
from lxml import etree
def get_html(ip='197.25.55.11'):
    url='https://ip.cn/index.php?ip=%s' % ip
    html=requests.get(url)
    page=etree.HTML(html.text)
    return page.xpath('/html/body/div/div[4]/div/p[2]/code/text()')
print(get_html('197.25.5.10'))