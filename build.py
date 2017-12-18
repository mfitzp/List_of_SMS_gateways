#!/usr/bin/env python3
# -*- coding: utf-8 -*- #
import csv
import json


keys = ['Country','Region','Carrier','Email-to-SMS','Email-to-MMS','Notes']

gateways = []

with open('email2sms.csv', newline='', encoding='utf-8') as f:
     reader = csv.DictReader(f)
     for row in reader:
        if (row['Status'] != 'XXX' and (row['Email-to-SMS'] or row['Email-to-MMS'])):
            gateways.append({ k.lower():row[k] for k in keys })
            

with open('www/sms.json', 'w') as f:
    json.dump(gateways, f)


        
        