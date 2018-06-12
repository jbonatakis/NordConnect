#!/usr/bin/env python3
# A Python script to find the NordVPN server in a given country with the lowest utilization rate (load)

# Author: Jack Bonatakis
# Date: June 2 2018
# Title: NordVPN Server Load Analyzer

import requests
import json
import sys
import os
import argparse

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

def main():
    # Call API endpoint to get data
    url = "https://nordvpn.com/api/server/stats"

    # Read as JSON
    data = requests.get(url).json()

    servers = []

    # Create list of dicts, sort by load, print all servers + their load if load <= 10 (make server load limit sys.argv[2])
    for s in data:
        if s[0:2] in sys.argv:
            server_dict = {"server":s, "load":int(data[s]["percent"])}
            servers.append(server_dict.copy())
        # Provide else statement here. Fails if no country code provided in sys.argv
        # Set up default upon first initiation of program. Save in $XDG_CONFIG_HOME/NordConnect/default

    sorted_servers = sorted(servers, key=lambda k: k["load"])

    # Read sys.argv for number of servers to display. Default 10 if no argument
    #if len(sys.argv) >= 3:
    #    num = int(sys.argv[2])
    #else:
    #    num = 10

    if "-c" in sys.argv and "-udp" in sys.argv:
        protocol = "udp"
        print(color.GREEN + color.BOLD + "Connecting to ", sorted_servers[0]["server"] + " via UDP\n" + color.END)
        connect(sorted_servers, protocol)
    elif "-c" in sys.argv and "-udp" not in sys.argv:
        protocol = "tcp"
        print(color.GREEN + color.BOLD + "Connecting to ", sorted_servers[0]["server"] + " via TCP\n" + color.END)
        connect(sorted_servers, protocol)
    else:
        try:
            num = get_num()
            print_top_servers(sorted_servers, num)
        except ValueError:
            num = 10
            print_top_servers(sorted_servers, num)

def get_num():
    num = int(input("How many servers to show? \n>> "))
    return num

def print_top_servers(sorted_servers, num):
    counter = 0
    for s in sorted_servers:
        if s["load"] >0 and s["load"] <= 10 and counter < num:
            print(color.GREEN + color.BOLD + str(s["server"]).ljust(18, ' ') + ": " + color.END +  str(s["load"]) + "%")
            counter +=1

def connect(sorted_servers, protocol):
    os.system("sudo openvpn /etc/openvpn/ovpn_" + protocol + "/" + str(sorted_servers[0]["server"]) + "." + protocol + ".ovpn")

main()
