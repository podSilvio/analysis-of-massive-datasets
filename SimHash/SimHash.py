import sys
import hashlib


def simhash(text):
    k = int(128)        # Length of a hash (predefined)
    words = text.split()
    initial_number = [0] * k

    for word in words:
        hashcode = hashlib.md5(word.encode()).hexdigest()
        tmp_var = bin(int(hashcode, 16))[2:].zfill(k)
        for position, value in enumerate(tmp_var):
            if value == '1':
                initial_number[position] += 1
            else:
                initial_number[position] -= 1

    initial_number = [1 if initial_number[i] >= 0 else 0 for i in range(k)]

    # Create string from list
    v = ''.join([str(i) for i in initial_number])
    return v


def duplicate_detection(binary_hash, indexed_hash, hamming_distance):
    distance = 0
    for x, y in zip(binary_hash, indexed_hash):
        if x != y:
            distance += 1
            if distance > hamming_distance:
                return False
    return True


# query is in the form of (i,k), where i is sequence number and k is hamming distance
def simple_query(query, global_hash_list):

    # '-1' because don't add the same hash
    sumation = -1

    sequence_number = int(query.split()[0])
    hamming_distance = int(query.split()[1])

    # Get the right binary hash from global hash list
    indexed_hash = global_hash_list[sequence_number]

    # Iterate through all hashes
    for binary_hash in global_hash_list:
        if duplicate_detection(binary_hash, indexed_hash, hamming_distance):
            sumation += 1
    print(sumation)


# Function that read the whole file and builds list of all hashes
def read_file():
    n = 0
    q = 0

    global_hash_list = list()

    # line_index starts from zero
    for line_index, line in enumerate(sys.stdin):
        read_line = line.strip().rstrip()
        if line_index == 0:
            n = int(read_line)
        elif (line_index > 0) and (line_index <= n):
            global_hash_list.append(simhash(read_line))
        elif line_index == n + 1:
            q = int(read_line)
        elif (line_index > n + 1) and (line_index < n + 1 + q + 1):
            simple_query(read_line, global_hash_list)


def main():
    read_file()


if __name__ == '__main__':
    main()
