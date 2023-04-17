def rle_encode(data):
    data = iter(data)
    try:
        last = next(data)
        count = 1
        for inf in data:
            if inf == last:
                count += 1
            else:
                yield(last,count)
                last = inf
                count = 1
        yield(last, count)
    except StopIteration:
        pass

def rle_decode(data):
    for inf, count in data:
        for _ in range(count):
            yield inf
