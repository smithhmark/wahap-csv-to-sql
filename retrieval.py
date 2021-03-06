"""
The module encapsulates gathering the needed data.
"""
import argparse
import requests
import os
from datetime import datetime
from urllib.parse import urlparse

ROOT_URL="http://wahapedia.ru/wh40k9ed/Export%20Data%20Specs.xlsx"

def _local_path(url, destination_dir):
    bits = urlparse(url)
    file_name = os.path.basename(bits.path)
    return os.path.join(destination_dir, file_name)

def _parse_time(tm_str):
    return datetime.strptime(tm_str, "%a, %d %b %Y %H:%M:%S %Z")

def get_mod_time(url):
    resp = requests.head(url)
    tm_str = resp.headers.get("Last-Modified")
    return _parse_time(tm_str)

def build_local_cache(urls, destination_dir):
    for url in urls:
        fpath = _local_path(url, destination_dir)
        response = requests.get(url)
        with open(fpath, 'w') as fil:
            fil.write(response.text)

def update_cache(urls, cache_dir, verbose=False, mode='char'):
    dirty_list = []
    for url in urls:
        local_path = _local_path(url, cache_dir)
        if os.path.exists(local_path):
            mtime = datetime.fromtimestamp(os.path.getmtime(local_path))
            remote_mtm = get_mod_time(url)
            if mtime < remote_mtm:
                if verbose:
                    print(f"local file: {local_path} is dirty")
                dirty_list.append( (url, local_path))
            else:
                print(f"local file: {local_path} is clean")
        else:
            if verbose:
                print(f"local file: {local_path} is missing")
            dirty_list.append( (url, local_path))

    for url, local_path in dirty_list:
        if verbose:
            print(f"retreving {local_path} from {url}")
        response = requests.get(url)
        if mode == 'char':
            with open(local_path, 'w') as fil:
                fil.write(response.text)
        else:
            with open(local_path, 'wb') as fil:
                fil.write(response.content)
        tm_str = response.headers.get("Last-Modified")
        mtime = _parse_time(tm_str)
        os.utime(local_path, (mtime.timestamp(), mtime.timestamp()))

def build_parser():
    parser = argparse.ArgumentParser(
            description="Collect Wahapedia CSVs into local_cache")

    parser.add_argument(
            "--location",
            default="data_cache",
            help="the name and path of the SQL file to produce")
    parser.add_argument(
            "-v", "--verbose",
            default=False,
            const=True,
            type=bool,
            nargs='?',
            help="the name and path of the SQL file to produce")
    return parser


if __name__ == '__main__':
    parser = build_parser()
    args = parser.parse_args()

    if not os.path.exists(args.location):
        if args.verbose:
            print("creating local cache: {args.location}")
        os.mkdir(args.location)
    urls = [ROOT_URL]
    update_cache(urls, args.location, verbose=args.verbose)

