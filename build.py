#!/usr/bin/env python3
# -*- coding: utf-8 -*- #
import csv

html = '''
<table id="smstable">
<thead>
<tr>
<th>Country</th>
<th>Region</th>
<th>Carrier</th>
<th>Format</th>
<th>Mail/Web-to-SMS Gateway</th>
<th>Notes</th>
<th>SMS-to-Email Gateway</th>
<th>Notes</th>
<th>Reference</th>
</tr>
</thead>
<tbody>
'''

with open('email2sms.csv', 'r') as f:
    csvfile = csv.reader(f)
    for row in csvfile:
        html += '<tr>'
        
        for col in row:
            
            if 'http' in col:
                col = '<a href="%s">%s</a>' % (col, col)
            elif '@' in col:
                col = '<a href="mailto:%s">%s</a>' % (col, col)
        
            html += '<td>%s</td>' % col        
    
        html += '</tr>\n'

html += '</body></table>'

with open('email2sms.html', 'w') as f:
    f.write(html)
    