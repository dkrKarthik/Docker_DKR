import os
import socket
from collections import Counter


data_dir = '/home/data'


output_file = '/home/output/result.txt'


os.makedirs(os.path.dirname(output_file), exist_ok=True)


files = os.listdir(data_dir)
print("List of files in /home/data:")
for file in files:
    print(file)


total_words = 0
for file_name in ['IF.txt', 'Limerick-1.txt']:
    with open(os.path.join(data_dir, file_name), 'r') as f:
        content = f.read()
        words = content.split()
        num_words = len(words)
        total_words += num_words
        print(f"\nTotal number of words in {file_name}: {num_words}")


print(f"\nGrand total number of words: {total_words}")


if 'IF.txt' in files:
    with open(os.path.join(data_dir, 'IF.txt'), 'r') as f:
        content = f.read()
        words = content.split()
        word_counts = Counter(words)
        top_words = word_counts.most_common(3)
        print("\nTop 3 words with maximum number of counts in IF.txt:")
        for word, count in top_words:
            print(f"{word}: {count}")


hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print(f"\nIP address of the machine: {ip_address}")


with open(output_file, 'w') as f:
    f.write("List of files in /home/data:\n")
    for file in files:
        f.write(f"{file}\n")
    f.write("\n")
    for file_name in ['IF.txt', 'Limerick-1.txt']:
        with open(os.path.join(data_dir, file_name), 'r') as file_content:
            content = file_content.read()
            words = content.split()
            num_words = len(words)
            f.write(f"Total number of words in {file_name}: {num_words}\n")
    f.write(f"\nGrand total number of words: {total_words}\n")
    if 'IF.txt' in files:
        f.write("\nTop 3 words with maximum number of counts in IF.txt:\n")
        for word, count in top_words:
            f.write(f"{word}: {count}\n")
    f.write(f"\nIP address of the machine: {ip_address}\n")


with open(output_file, 'r') as f:
    print("\nOutput written to result.txt:")
    print(f.read())
