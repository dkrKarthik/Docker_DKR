import os

data_dir = '/home/data'


files = os.listdir(data_dir)
print("List of files in /home/data:")
for file in files:
    print(file)


for file in files:
    with open(os.path.join(data_dir, file), 'r') as f:
        content = f.read()
        print(f"\nContent of {file}:")
        print(content)

        import os


data_dir = '/home/data'


files = os.listdir(data_dir)
print("List of files in /home/data:")
for file in files:
    print(file)


files_to_read = ['IF.txt', 'Limerick-1.txt']
for file in files_to_read:
    with open(os.path.join(data_dir, file), 'r') as f:
        content = f.read()
        print(f"\nContent of {file}:")
        print(content)

