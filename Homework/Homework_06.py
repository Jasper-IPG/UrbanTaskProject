# 1st task
my_dict = {'Pavel': 1971, 'Alex': 1985, 'Max': 1997}
print('Dict:', my_dict)
print('Existing value:', my_dict['Alex'])
print('Not existing value:', my_dict.get('John'))
my_dict.update({'Tim': 1974, 'Patrick': 1965})
part_dict = my_dict.pop('Max')
print('Deleted value:', part_dict)
print('Modified dictionary:', my_dict)

# 2nd task
my_set = {(3, 5, 7), 'car', 4.5, 4, 8, 15, 'train', 'plane', 4.5, 3.2, 8, 4, 2, 'car'}
print('Set:', my_set)
new_set = {33, 'bus'}
my_set.update(new_set)
my_set.remove((3, 5, 7))
print('Modified set:', my_set)
