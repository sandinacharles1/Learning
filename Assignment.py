from hashlib import sha256
import sys

def hashing(file):
    results = {}
    with open(file, 'r', encoding='utf-8') as f: #open in binary since
        for line in f:
            line = line.strip()
            if not line : continue
            encoded = sha256(line.encode('utf-8')).hexdigest()
            if encoded not in results : results[encoded] = set()
            results[encoded].add(line)
    return results


def convert(hash_results):
    integers = {}
    for encoded, lines in hash_results.items():
        hash_int = int(encoded, 16)
        if hash_int not in integers : integers[hash_int] = set()
        for line in lines: integers[hash_int].add(line)
    return integers

if __name__ == "__main__":
    file = hashing("wordcount.txt")
    integers = convert(file)
    
    print("-" * 70)
    print("Hash Codes:")
    print("-" * 70)
    for key, value in file.items():
        print(f"{key}: {value}")
    
    print("-" * 70)
    print("Integers:")
    print("-" * 70)
    for key, value in integers.items():
        print(f"{key}: {value}")
