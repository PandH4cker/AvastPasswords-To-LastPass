#!/usr/bin/python3

import json, sys, csv
from colorama import Fore, Style

def main(argc: int, argv: list):
    if (argc < 2):
        print(f'[{Fore.RED}-{Style.RESET_ALL}] You need to specify a json file.')
        print(f'[{Fore.GREEN}+{Style.RESET_ALL}] Usage: {argv[0]} [json filepath]')
        exit(1)

    with open('passwd.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['url', 'type', 'username', 'password', 'hostname', 'extra', 'name', 'grouping'])
        json_filepath = argv[1]
        with open(json_filepath) as f:
            data = json.load(f)
        
        logins = data['logins']
        
        for l in logins:
            writer.writerow([l['url'], '', l['loginName'], l['pwd'], '', l['note'], l['custName'], ''])


if __name__ == "__main__":
    main(len(sys.argv), sys.argv)