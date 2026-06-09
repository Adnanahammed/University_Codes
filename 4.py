import csv

file_in = open('month_temp.csv', 'r', encoding='utf-8')
file_out = open('month_temp2.csv', 'w', encoding='utf-8', newline='')

lines = csv.reader(file_in)
writer = csv.writer(file_out)

writer.writerow(['Date', 'Min Temp', 'Max Temp', 'Temp Difference'])
next(lines) # Skip the header row

for line in lines:
    temp_diff = float(line[4]) - float(line[3])
    formatted_diff = format(temp_diff, '.1f')
    writer.writerow([line[1], float(line[3]), float(line[4]), formatted_diff])

print('File writing complete!')

file_in.close()
file_out.close()