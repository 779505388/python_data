"""ip代理池"""
import requests
from lxml import etree
import pymysql
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6756.400 QQBrowser/10.3.2473.400'}


def ip_port(pages=3):
    """获取ip数据,默认爬三页"""
    https_list = []
    http_list = []
    for page in range(1, pages + 1):
        url = "http://www.ip3366.net/?stype=1&page=%s" % str(page)
        Html_data = requests.get(url, headers=header)
        html = etree.HTML(Html_data.text)
        ip_adrs = html.xpath('//tr/td[1]/text()')
        ports = html.xpath('//tr/td[2]/text()')
        ip_types = html.xpath('//tr/td[4]/text()')
        for ip_adr, port, ip_type in zip(ip_adrs, ports, ip_types):
            if ip_type == 'HTTPS':
                ip = 'https://' + ip_adr+':'+port
                https_list.append(ip)
            else:
                ip = 'http://' + ip_adr+':'+port
                http_list.append(ip)
    return http_list, https_list


def test_ip(http, htpps):
    https_list = []
    http_list = []
    for test_http in http:
        try:
            proxies = {'http': test_http}
            data = requests.get('http://www.baidu.com/',
                                headers=header, proxies=proxies, timeout=10)
            http_list.append(test_http)
            print('成功:', test_http)
        except:
            print('失败')

    for test_https in https:
        try:
            proxies = {'https': test_http}
            data = requests.get('https://www.gynl.xyz/',
                                headers=header, proxies=proxies, timeout=10)
            http_list.append(test_https)
            print('成功:', test_https)
        except:
            print('失败')
    return http_list, https_list


def input_ip(http):
    db = pymysql.connect(host="localhost", user="root",
                         password="xxxxxxxxxx", db="ip_data", port=3307)
    cursor = db.cursor()

    sql = """INSERT INTO httpslist(ip) VALUES ('%s')""" % http
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
                    # 如果发生错误则回滚
        db.rollback()
    else:
        print('不存入http')

    db.close()
