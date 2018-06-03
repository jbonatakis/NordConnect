#!/usr/bin/env python3
# A Python script to find the NordVPN server in a given country with the lowest utilization rate (load)

# Author: Jack Bonatakis
# Date: June 2 2018
# Title: NordVPN Server Load Analyzer

import requests
import json
import sys

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

# Call API endpoint to get data
url = "https://nordvpn.com/api/server/stats"

# Read as JSON
data = requests.get(url).json()

servers = []

# Create list of dicts, sort by load, print all servers + their load if load <= 10 (make server load limit sys.argv[2])
for s in data:
    if s[0:2] == sys.argv[1]:
        server_dict = {"server":s, "load":int(data[s]["percent"])}
        servers.append(server_dict.copy())

sorted_servers = sorted(servers, key=lambda k: k["load"])

# Read sys.argv for number of servers to display. Default 10 if no argument
if len(sys.argv) >= 3:
    num = int(sys.argv[2])
else:
    num = 10

counter = 0

for s in sorted_servers:
    if s["load"] >0 and s["load"] <= 10 and counter < num:
        print(color.GREEN + color.BOLD + str(s["server"]).ljust(18, ' ') + ": " + color.END +  str(s["load"]) + "%")
        counter +=1
