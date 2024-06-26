"""
Author: Juan Antonio Landeros Velazquez
Date: 25/03/2024
Project: E1 Implementation of Lexical Analysis (Automaton and Regular Expression)
purpose of the project
"""
import re

def parse(input_string):
  regex = '^m(a(hdi|qbara|tar|ula)|idri)$'
  match = re.fullmatch(regex, input_string)
  if match is not None: 
    return input_string
  else:
    return None

def accept(parsed_string):
  if parsed_string is not None:
    return 'Yes'
  else: 
    return 'No'
'''
input_strings = str(input())
parsed = parse(input_string)
accepted = accept(parsed)
print('The string is: ', accepted)
'''
inputs = [
  'mahdi',
  'maqbara',
  'matar',
  'maula',
  'midri',
  'mula',
  'maaula',
  'man',
  'mateo',
  'maura',
  'mtar',
  'maqbar',
  'madi',
  'midrii',
  'mala',
  'mirti',
  'matar1',
  'maaaqbaraa',
  'madri',
  'mahaula'
]

for input in inputs:
  parsed = parse(input)
  accepted = accept(parsed)
  print('The string', input, 'is accepted?', accepted)

print()

count = 1 

for input in inputs:
  ans = accept(parse(input))
  if ans:
    print('Test', count, 'passed')
    count = count + 1
'''
ans = accept(parse('mahdi'))
if ans:
  print('\nTest 1 passed')
  count = count + 1
'''
