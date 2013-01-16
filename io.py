import csv
import os
import time

'''
   CSV support
'''

print
print "---- Example: csv import and export ---- "
print

records = \
[
    { "username": "alfred", "user_id": 1 }, 
    { "username": "becky", "user_id": 2 }, 
    { "username": "charlie", "user_id": 3 }, 
    { "username": "david", "user_id": 4 }, 
    { "username": "le' lee", "user_id": 5 }, 
    { "username": "ferry, flora", "user_id": 6 }
]

def write_to_csv(file_name, records, field_names = None):
    print "writing %d records to %s" % (len(records), file_name)
    if not field_names:  # extract if field names are not provided from the first record
        keys = records[0].keys()
        keys.sort()
        field_names = keys

    with open(file_name, 'wb') as file:
        writer = csv.DictWriter(file, fieldnames = field_names,
        quotechar='\'')
        
        header = dict( (k, k) for k in field_names )
        writer.writerow(header)

        for record in records:
            writer.writerow(record)


def read_from_csv(file_name):
    print "reading records to %s" % (file_name)
    records = []
    with open(file_name, 'rb') as file:
        reader = csv.DictReader(file, quotechar='\'')
        records = [record for record in reader]
    
    return records

file_name = 'csv-write-%d.txt' % time.time()

write_to_csv(file_name, records)
returned_records = read_from_csv(file_name)

for record in returned_records:
    print record
