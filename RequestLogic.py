import requests
from auto_set import Config


def sendRequest(case):
    r = requests.session()
    # 调试用于fiddler抓包
    proxies = {'http': r'http://localhost:8888', 'https': r'http://localhost:8888'}
    if 'POST' in case:
        url = Config.src_url + case[0]
        # res = r.post(url=Config.src_url + case[0], headers=case[2], data=case[3])
        res = r.post(url=Config.src_url + case[0], headers=case[2], data=case[3], proxies=proxies, verify=False)
    elif 'GET' in case:
        # res = r.get(url=Config.src_url + case[0], headers=case[2], params=case[3])
        res = r.get(url=Config.src_url + case[0], headers=case[2], params=case[3], proxies=proxies, verify=False)
    elif 'PUT' in case:
        # res = r.put(url=Config.src_url + case[0], headers=case[2], params=case[3])
        res = r.put(url=Config.src_url + case[0], headers=case[2], data=case[3], proxies=proxies, verify=False)
    elif 'DELETE' in case:
        # res = r.delete(url=Config.src_url + case[0], headers=case[2], params=case[3])
        res = r.delete(url=Config.src_url + case[0], headers=case[2], data=case[3], proxies=proxies, verify=False)
    return res


if __name__ == '__main__':
    pass
