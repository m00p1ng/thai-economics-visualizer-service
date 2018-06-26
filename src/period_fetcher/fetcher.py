import os
import requests
import hashlib
from datetime import datetime
from .database import Database as db

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
}


class Fetcher:
    def __init__(self, field, output, headers=None):
        self.field = field
        self.output = output
        if headers == None:
            self.headers = HEADERS
        else:
            self.headers = headers

    def start(self):
        print(f"Fetching {self.field['url']}")
        res = requests.get(self.field['url'], headers=self.headers)

        content_hash = hashlib.sha256(res.text.encode('utf-8')).hexdigest()
        filename = self.field['url'].split('/')[-1].split('.')
        
        table_name = filename[0] + '_' + content_hash[:6]

        if self._is_updated(content_hash, res.content, table_name):
            print("Database updated")
        else:
            print(f"Not update yet")
        print()
    
    def _is_updated(self, content_hash, content, table_name):
        if db.fetch_link.find_one({'hash': content_hash}) == None:
            print(f"Data updated")

            link = db.fetch_link.find_one({"en": self.field['en']})
            if link is not None:
                link['hash'] = content_hash,
                link['latest_update'] = datetime.now(),
                db.fetch_link.save(link)
            self.save(content, self.field['url'], table_name)
            return True
        return False

    def save(self, content, url, table_name):
        file_path = os.path.splitext(os.path.split(url)[-1])
        extension = ''
        if len(file_path) == 2:
            extension = file_path[1]
        else:
            extension = '.html'

        filename = table_name + extension
        filepath = os.path.join(self.output, filename)
        with open(filepath, 'wb') as f:
            f.write(content)
