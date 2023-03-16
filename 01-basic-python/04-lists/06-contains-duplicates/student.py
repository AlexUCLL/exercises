# Write your code here
def contains_duplicates(xs):
    set_list = set(xs)
    if len(set_list)  == len(xs):
        return False
    else:
        return True