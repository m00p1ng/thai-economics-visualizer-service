import sys
import os.path

PATH = os.path.realpath(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(os.path.dirname(PATH)))

import period_fetcher

if __name__ == '__main__':
    try:
        period_fetcher.main()
    except KeyboardInterrupt:
        print("\n<-- BYE -->")