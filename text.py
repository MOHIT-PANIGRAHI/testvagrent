import itertools
n=int(input())
my_dictionary = {"TOI": 26,"Hindu":20.5,"ET":34,"BM":10.5,"HT":18}
values = my_dictionary.values()
keys = my_dictionary.keys()
result = [seq for i in range(len(values), 0, -1)
              for seq in itertools.combinations(keys, 2)
              if sum(map(my_dictionary.get,seq)) <=n]
def unique(list1):
    unique_list = []
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    # print list
    for x in unique_list:
        print(x)
unique(result)