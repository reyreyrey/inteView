# This is a sample Python script.
from concurrent.futures import ThreadPoolExecutor

import requests
import json

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pool = ThreadPoolExecutor(max_workers=2)
    for i in  range(1,2):
     url='https://jsonplaceholder.typicode.com/posts/'+str(i)+'/comments'
     str = requests.get(url)
     reuslt=str.content
     jsonresult=json.loads(reuslt)
     for t in  jsonresult:
       print(t['email'])
       with open('D:/email.txt', "a") as file:
            file.write(t['email']+'\n')


"""
完成时间2023-4-11 15:30
"""


     # See PyCharm help at https://www.jetbrains.com/help/pycharm/
