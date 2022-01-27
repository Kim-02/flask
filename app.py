from django.shortcuts import render
from flask import Flask, render_template, render_template_string, template_rendered
import requests
from bs4 import BeautifulSoup
import urllib3

app = Flask(__name__)

url = f"https://loawa.com/"
r = requests.get(url,headers ={'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"})
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
urllib3.disable_warnings()
soup = BeautifulSoup(r.content,'html.parser')
island_dict ={}
for a in range(1,4):
    name = soup.select_one(f'#main > div:nth-child(2) > div.main-contents.col-lg-6.col-md-8.col-xl-6.pl-0.pr-0 > div:nth-child(2) > div.main-inner-box > ul > li:nth-child({a}) > h4 > span').string
    value = soup.select_one(f'#main > div:nth-child(2) > div.main-contents.col-lg-6.col-md-8.col-xl-6.pl-0.pr-0 > div:nth-child(2) > div.main-inner-box > ul > li:nth-child({a}) > h5').string
    island_dict[name] = value
island_key_list = list(island_dict.keys())

@app.route('/')
def home():
    return render_template("index.html",template_island_dict=island_dict)

if __name__ == '__main__':
    app.run(debug=True)