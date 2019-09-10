import os
import sys
import re
from time import strftime
import ipapi

def main():

    with open("app.log", 'r') as f:
        lines = f.readlines()
    ipSet = set()
    for line in lines:
        ip_candidates = re.findall(r"\b(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\b", line)
        if ip_candidates:
            for candidate in ip_candidates:
                ipSet.add(candidate)
    for ipaddr in ipSet:
        ip_info = ipapi.location(ipaddr)
        print(ip_info['city'], ip_info['longitude'], ip_info['latitude'], ip_info['region'])


if __name__=="__main__":
    main()
