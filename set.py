set1 = {'A', 'B', 'C', 'D'}
set2 = {'C', 'D', 'E', 'F'}

union = set1 | set2 # 합집합
print( union )
# set(['A', 'C', 'B', 'E', 'D', 'F'])

intersection = set1 & set2 # 교집합
print( intersection )
# set(['C', 'D'])

complement = set1 - set2 # 차집합
print( complement )
# set(['A', 'B'])

sym_diff = set1 ^ set2 # 대칭 차집합 (union - intersection)
print( sym_diff )
# set(['A', 'B', 'E', 'F'])
