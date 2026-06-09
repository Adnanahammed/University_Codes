import csv
import numpy as np

with open('school_2019.csv', 'r', encoding='utf-8') as f:
    lines = csv.reader(f)
    header = next(lines)
    school_data = [line[:] for line in lines]

length = len(school_data)
# Create a zero array to hold [classes, students, teachers]
data_arr = np.zeros((length, 3), dtype='int32')

for i in range(length):
    for j in range(3):
        data_arr[i][j] = school_data[i][j+2]

# Find the row index with the maximum values across columns
max_idx = np.argmax(data_arr, axis=0)

max_class_school = school_data[max_idx[0]][1]
max_class_count = school_data[max_idx[0]][2]

print(f'School with most classes: {max_class_school} ({max_class_count} classes)')