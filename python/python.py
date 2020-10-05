#!/usr/bin/env python3
# enable debigging
import cgitb
cgitb.enable()
import datetime

print("Contect-Type: text/plain;charset=utf-8")
print("")

def main():
    print("Current datetime:")
    print(datetime.datetime.now())

if __name__ == "__main__":
    main()


