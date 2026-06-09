import csv

with open('pharm_2019.csv', 'r', encoding='utf-8') as f:
    lines = csv.reader(f)
    header = next(lines)
    
    city = 'Suncheon-si'
    total_count = 0
    recent_count = 0
    
    for line in lines:
        if line[1] == city:
            total_count += 1
            # Check if opened after Sept 1, 2014
            if int(line[3]) > 20140901: 
                recent_count += 1
                
    print(f'Total pharmacies in {city}: {total_count}')
    print(f'Pharmacies opened within 5 years: {recent_count}')