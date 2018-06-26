import os
import time
from glob import glob
from .database import Database as db
from .fetcher import Fetcher
from .extractor.extractor import Extractor


OUTPUT = os.path.join(os.path.expanduser('~'), 'Desktop', 'source_table')
def main():
    db.connect('thai-econ')

    if not os.path.exists(OUTPUT):
        os.makedirs(OUTPUT)

    # file_list = glob(OUTPUT + '/*')

    # for file in file_list:
    #     print(file)
    #     with open(file) as f:
    #         ext = Extractor(f.read())


    while(True):
        fetch_all(OUTPUT)

        interval = 3600

        print(f'Wait for {interval} seconds')
        time.sleep(interval)
        

def fetch_all(output):
    fetch_link = db.fetch_link.find()
    for field in fetch_link:
        fetch = Fetcher(field, OUTPUT)
        fetch.start()


    
