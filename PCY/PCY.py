import sys
from itertools import combinations


def get_frequent_pairs(initial_bucket_list, item_table, bucket_table, threshold,  number_of_buckets):
    pairs = dict()
    number_of_different_items = len(item_table.keys())
    for bucket in initial_bucket_list:
        for (i, j) in combinations(bucket, 2):
            if (item_table.get(i, 0) >= threshold) and (item_table.get(j, 0) >= threshold):
                k = ((i * number_of_different_items) + j) % number_of_buckets
                if bucket_table.get(k, 0) >= threshold:
                    # value = pairs.get((i,j), 0)
                    # pairs.update({(i,j): value + 1})
                    # ili brze
                    pairs[(i, j)] = pairs.get((i, j), 0) + 1
    return pairs


def pair_into_bucket(initial_bucket_list, item_table, threshold, number_of_buckets):
    bucket_table = dict()
    number_of_different_items = len(item_table.keys())
    for bucket in initial_bucket_list:
        for (i, j) in combinations(bucket, 2):
            if (item_table.get(i, 0) >= threshold) and (item_table.get(j, 0) >= threshold):
                k = ((i * number_of_different_items) + j) % number_of_buckets
                # value = bucket_table.get(k, 0)
                # bucket_table.update({k: value + 1})
                # ili brze
                bucket_table[k] = bucket_table.get(k, 0) + 1
    return bucket_table


# First iteration
def fill_item_table(initial_bucket_list):
    item_table = dict()
    for bucket in initial_bucket_list:
        for i in bucket:
            # value = item_table.get(int(i), 0)
            # item_table.update({int(i): value + 1})
            # ili brze
            item_table[int(i)] = item_table.get(int(i), 0) + 1

    return item_table


def read_file():
    N = 0       # number of values
    b = 0       # number of buckets (pretinaca)
    threshold = 0

    initial_bucket_list = list()

    for line_index, line in enumerate(sys.stdin):
        read_line = line.rstrip().strip()
        if line_index == 0:
            N = int(read_line)
        elif line_index == 1:
            s = float(read_line)    # ratio [0, 1]
            threshold = N * s
        elif line_index == 2:
            b = int(read_line)
        elif line_index > 2 and line_index <= N + 3:
            initial_bucket_list.append([int(i) for i in read_line.split()])

    return initial_bucket_list, b, threshold


def output_print(item_table, pairs, threshold):

    freq_candidates = 0     # m value
    total_pairs = len(pairs)

    # Count the frequency candidates
    for i in item_table:
        if item_table.get(i, 0) >= threshold:
            freq_candidates += 1

    # Print necessary values
    print(int(freq_candidates * (freq_candidates - 1) / 2))
    print(total_pairs)

    # Print sorted pairs
    for x in sorted(pairs.values(), reverse=True):
        print(x)


def main():
    initial_bucket_list, number_of_buckets, threshold = read_file()
    item_table = fill_item_table(initial_bucket_list)
    bucket_table = pair_into_bucket(initial_bucket_list, item_table, threshold, number_of_buckets)
    pairs = get_frequent_pairs(initial_bucket_list, item_table, bucket_table, threshold, number_of_buckets)
    output_print(item_table, pairs, threshold)


if __name__ == '__main__':
    main()
