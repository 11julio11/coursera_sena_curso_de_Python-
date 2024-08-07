# menu = ['espresso', 'mocha','latte','capuccino','cortado','americano']

# def find_coffee(coffee):
#     if coffee[0] == 'c':
#         return coffee

# # map_coffee = map(find_coffee, menu)
# # print(map_coffee)
# # for x in map_coffee:
# #     print(x)

# filter_coffee = filter(find_coffee, menu)
# print(filter_coffee)
# for x in filter_coffee:
#     print(x)

from ntpath import join


a = [[96],[69]]
print ("".join(list (map (str, a))))


z = ["alpha","bravo","charlie"]
new_z = [i[0]*2 for i in z]
print(new_z)