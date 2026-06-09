try:
    # Attempt to open and read a file
    with open('poem.txt', 'r', encoding='utf-8') as f:
        content = f.readlines()
        for line in content:
            print(line.strip())
            
except FileNotFoundError:
    # Handle the error if the file doesn't exist
    print("Error: Please check the file path. The file could not be found.")