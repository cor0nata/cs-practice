def count_items(values: list) -> dict:
    count = {}
    for value in values:
        count[value] = count.get(value, 0) + 1
    return count
def unique_sorted(values: list) -> list:
    return sorted(set(values))
def common(first: list, second: list) -> list:
    return sorted(set(first) & set(second))
def only_in_first(first: list, second: list) -> list:
    return sorted(set(first) - set(second))
