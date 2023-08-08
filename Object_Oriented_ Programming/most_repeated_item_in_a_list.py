import statistics


def item(lst):
    return statistics.mode(lst)


lst = ["femi", "seun", "segun", "timi", "Ayo", "seun"]
print(item(lst))
