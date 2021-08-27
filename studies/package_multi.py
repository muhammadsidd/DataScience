import json
import requests
import time
import threading
from multiprocessing import Pool
import pandas as pd



package_detail = {
    'name': [],
    'description': [],
    '30d': [],
    '90d': [],
    '365d': [],
    'total': []
}
count = 0

def namer(name):
    package_detail['name'].append(name)


def install_30(package_json, name):
    package_detail['30d'].append(package_json["analytics"]["install_on_request"]["30d"][name])


def install_90(package_json, name):
    package_detail['90d'].append(package_json["analytics"]["install_on_request"]["90d"][name])


def install_365(package_json, name):
    package_detail['365d'].append(package_json["analytics"]["install_on_request"]["365d"][name])


def workload(package_url):

    r = requests.get(package_url)

    name = package_url.split('/')[5].split('.')[0]
    
    package_detail['name'].append(name)
    
    package_json = r.json()
    treds = []

    
    thread0 =threading.Thread(target=namer, args = (name,))
    thread1= threading.Thread(target=install_30, args = (package_json, name))
    thread2 = threading.Thread(target=install_90, args = (package_json, name))
    thread3 = threading.Thread(target=install_365, args = (package_json, name))
    
    treds.append(thread0)
    treds.append(thread1)
    treds.append(thread2)
    treds.append(thread3)

    for t in treds:
        t.start()

    for t in treds:
        t.join()
    print(package_json)
    return name
    
def printer(urls):
    print(urls)

def main():
    url = "https://formulae.brew.sh/api/formula.json"
    response = requests.get(url)
    packages = response.json()
    formatted_json = json.dumps(packages, indent=2)
    # print(formatted_json)


    count = 1

    url_list = []

    for package in packages:

        package_name = package['name']
        package_url = f"https://formulae.brew.sh/api/formula/{package_name}.json"
        url_list.append(package_url)

    with Pool(processes=4) as pool: # or whatever your hardware can support
        namelist = pool.map(workload, url_list)
    
    print(namelist)
    
    
    
if __name__ == '__main__':
    main()
    print(package_detail)
    