# print(dir(dict))

# a={}
# print(type(a))      # <class 'dict'>

# b={
#     1:'Python'
# }
# print(b[1])         # Python
# print(b[2])         # KeyError: 2

# v={
#     1:'Python',
#     2:'Java',
#     3:'C'
# }
# print(v[1])         # Python
# print(v[2])         # Java
# print(v[3])         # C
# print(v[4])         # KeyError: 4


# perfume={
#     'a':'Axe',
#     'f':'Fog',
#     'v':'Vip 919'
# }
# print(perfume['v'])     # Vip 919
# print(perfume['f'])     # Fog
# print(perfume['g'])     # KeyError: 'g'

# perfume={
#     'a':'Axe',
#     'f':'Fog',
#     1:'RB',
#     'v':'Vip 919'
# }
# print(perfume.keys())       # dict_keys(['a', 'f', 1, 'v'])
# print(perfume.values())     # dict_values(['Axe', 'Fog', 'RB', 'Vip 919'])
# perfume.clear()
# print(perfume)          # {}


'''pop()'''
# perfume={
#     'a':'Axe',
#     'f':'Fog',
#     1:'RB',
#     'v':'Vip 919'
# }
# perfume.pop(1)
# perfume.pop('f')
# print(perfume)          # {'a': 'Axe', 'v': 'Vip 919'}


'''popitem()'''
# perfume={
#     'a':'Axe',
#     'f':'Fog',
#     1:'RB',
#     'v':'Vip 919'
# }
# perfume.popitem()
# print(perfume)         # {'a': 'Axe', 'f': 'Fog', 1: 'RB'}


'''fromkeys()'''
# a=[1,2,3,4]
# print(a.fromkeys())         # AttributeError: 'list' object has no attribute 'fromkeys'

# perfume={
#     'a':'Axe',
#     'f':'Fog',
#     1:'RB',
#     'v':'Vip 919'
# }
# a=[1,2,3,4]
# print(perfume.fromkeys(a))      # {1: None, 2: None, 3: None, 4: None}
# print(perfume.fromkeys(a,'Pass'))       # {1: 'Pass', 2: 'Pass', 3: 'Pass', 4: 'Pass'}



# a=[101,204,304,575]
# print(dict.fromkeys(a,'A+'))        # {101: 'A+', 204: 'A+', 304: 'A+', 575: 'A+'}
# print(dict.fromkeys(a,'Pass'))      # {101: 'Pass', 204: 'Pass', 304: 'Pass', 575: 'Pass'}


'''update()'''
# perfume={
#     'a':'Axe',
#     'f':'Fog',
#     1:'RB',
#     'v':'Vip 919'
# }
# perfume.update({'f':'Fog'})
# print(perfume)                  # {'a': 'Axe', 'f': 'Fog', 1: 'RB', 'v': 'Vip 919'}
#                                 # if no changes in the update then it will return the same else returns the updated output for the key.
# perfume.update({'f':'Fogg'})
# print(perfume)                  # {'a': 'Axe', 'f': 'Fogg', 1: 'RB', 'v': 'Vip 919'}
# perfume.update({'m':'manj'})
# print(perfume)                  # {'a': 'Axe', 'f': 'Fogg', 1: 'RB', 'v': 'Vip 919', 'm': 'manj'}


'''setdefault()'''
# perfume={
#     'a':'Axe',
#     'f':'Fog',
#     1:'RB',
#     'v':'Vip 919'
# }
# perfume.setdefault({'f':'fox'})         # TypeError: unhashable type: 'dict'  # should not use { } flower brackets.
# perfume.setdefault('f':'fox')             # SyntaxError: invalid syntax         # should not use : colon.
# perfume.setdefault('f','fox')
# print(perfume)                  # {'a': 'Axe', 'f': 'Fog', 1: 'RB', 'v': 'Vip 919'}   # it returned the same, no update is made as the key is already present, it returned the default value of the key.
# perfume.setdefault('n','nova')
# print(perfume)                    # {'a': 'Axe', 'f': 'Fog', 1: 'RB', 'v': 'Vip 919', 'n': 'nova'}        # if the key is not there, then it adds the key value pair at the end of the dictionary.


'''items()'''
# perfume={
#     'a':'Axe',
#     'f':'Fog',
#     1:'RB',
#     'v':'Vip 919'
# }
# print(perfume.items())          # dict_items([('a', 'Axe'), ('f', 'Fog'), (1, 'RB'), ('v', 'Vip 919')])


'''get()'''
# perfume={
#     'a':'Axe',
#     'f':'Fog',
#     1:'RB',
#     'v':'Vip 919'
# }
# print(perfume.get(1))       # RB
# print(perfume.get(2))       # None
# print(perfume.get[1])       # TypeError: 'builtin_function_or_method' object is not subscriptable
# print(perfume[1])           # RB
# print(perfume[2])           # KeyError: 2
