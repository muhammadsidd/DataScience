import json 
import requests
import time

url = "https://formulae.brew.sh/api/formula.json"
response = requests.get(url)
packages= response.json()
formatted_json = json.dumps(packages, indent=2)
# print(formatted_json)

package_detail = {
    'name':[],
    'description':[],
    '30d':[],
    '90d':[],
    '365d':[],
    'total':[]
}
count= 1
for package in packages:
    package_name = package['name']
    package_desc = package['desc']
    package_url = f"https://formulae.brew.sh/api/formula/{package_name}.json"
    r = requests.get(package_url)
    package_json = r.json()

    installs_30 = package_json["analytics"]["install_on_request"]["30d"][package_name]
    installs_90 = package_json["analytics"]["install_on_request"]["90d"][package_name]
    installs_365 = package_json["analytics"]["install_on_request"]["365d"][package_name]
    total = installs_30+installs_90+installs_365

    package_detail['name'].append(package_name)
    package_detail['description'].append(package_desc)
    package_detail['30d'].append(installs_30)
    package_detail['90d'].append(installs_90)
    package_detail['365d'].append(installs_365)
    package_detail['total'].append(total)
    # time.sleep(r.elapsed.total_seconds())

    count+=1

    print(f"processing record # {count}")



print(package_detail)

