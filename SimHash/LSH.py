import sys
import hashlib

# User defined parameters
k = int(128)        # Length of a hash
b = int(8)          # Number of bands [1 , 8]
r = int(k / b)


def simhash(text):
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


def hash2int(band, current_hash):
    return int(current_hash[band * r: ((band + 1) * r)], 2)


def algorithm_lsh(global_hash_list, N):

    candidates = dict()

    for band in range(b):
        buckets = dict({int: list()})

        for current_id in range(N):
            current_hash = global_hash_list[current_id]

            # Get the bits based on the current band
            value = hash2int(band, current_hash)
            texts_in_bucket = []

            # If there is key "value" in buckets
            if value in buckets:
                texts_in_bucket = buckets.get(value)
                for text_id in texts_in_bucket:
                    if current_id in candidates:
                        candidates[current_id].append(text_id)
                    else:
                        candidates[current_id].append(text_id)
                    if text_id in candidates:
                        candidates[text_id].append(current_id)
                    else:
                        candidates[text_id].append(current_id)
            else:
                texts_in_bucket.clear()

            # Nacin na koji prvo updateam eventualnu listu i onda updateanu listu stavim u dict neovisno jel key (u ovom slucaju value) vec postoji
            texts_in_bucket.append(current_id)
            buckets[value] = texts_in_bucket

    return candidates


def duplicate_detection(binary_hash, indexed_hash, hamming_distance):
    distance = 0
    for x, y in zip(binary_hash, indexed_hash):
        if x != y:
            distance += 1
            if distance > hamming_distance:
                return False
    return True


def query_lsh(query, global_hash_list, candidates):

    sequence_number = int(query.split()[0])
    hamming_distance = int(query.split()[1])
    sumation = 0

    # Get the right binary hash from global hash list
    indexed_hash = global_hash_list[sequence_number]

    # Get the integers representing the potentially equal texts
    list_of_new_candidates = candidates.get(sequence_number, None)
    if list_of_new_candidates is None:
        print(sumation)
    else:
        list_of_new_candidates = list(dict.fromkeys(list_of_new_candidates))        # Remove duplicates from the list
        for i in list_of_new_candidates:
            if duplicate_detection(global_hash_list[i], indexed_hash, hamming_distance):
                sumation += 1
        print(sumation)


def read_file():

    Q = 0       # Number of queries
    N = 0       # Number of inputs

    global_hash_list = list()
    candidates = dict()

    # line_index starts from zero
    for line_index, line in enumerate(sys.stdin):
        read_line = line.strip().rstrip()
        if line_index == 0:
            N = int(read_line)
        elif (line_index > 0) and (line_index <= N):
            global_hash_list.append(simhash(read_line))
        elif line_index == N + 1:
            Q = int(read_line)
            candidates = algorithm_lsh(global_hash_list, N)
        elif (line_index > N + 1) and (line_index < N + 1 + Q + 1):
            query_lsh(read_line, global_hash_list, candidates)


def main():
    read_file()


if __name__ == '__main__':
    main()
