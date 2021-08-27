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

def install_30(package_json, name):
    global package_detail
    package_detail['30d'].append(package_json["analytics"]["install_on_request"]["30d"][name])


def install_90(package_json, name):
    global package_detail
    package_detail['90d'].append(package_json["analytics"]["install_on_request"]["90d"][name])


def install_365(package_json, name):
    global package_detail
    package_detail['365d'].append(package_json["analytics"]["install_on_request"]["365d"][name])


def workload(package_url):
    global count
    global package_detail

    r = requests.get(package_url)

    name = package_url.split('/')[5].split('.')[0]
    
    # package_detail['name'].append(name)
    
    # package_json = r.json()
    treds = []
    # package_detail['30d'].append(package_json["analytics"]["install_on_request"]["30d"][name])
    # package_detail['90d'].append(package_json["analytics"]["install_on_request"]["90d"][name])
    # package_detail['365d'].append(package_json["analytics"]["install_on_request"]["365d"][name])

    # thread1= threading.Thread(target=install_30, args = (package_json, name))
    # thread2 = threading.Thread(target=install_90, args = (package_json, name))
    # thread3 = threading.Thread(target=install_365, args = (package_json, name))
    
    # treds.append(thread1)
    # treds.append(thread2)
    # treds.append(thread3)

    # for t in treds:
    #     t.start()

    # for t in treds:
    #     t.join()
    count +=1
    print(package_url, count)
    


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

    with Pool(processes=6) as pool: # or whatever your hardware can support

            # have your pool map the file names to dataframes
            pool.map(workload, url_list)
            




if __name__ == '__main__':
    main()