import re
from random import randint
_capitalize = lambda word: word.split('-')[0] + ''.join([x.title() for x in word.split('-')[1:]])

_lowerize = lambda str: re.sub('(.)([A-Z][a-z]+)', r'\1-\2', str).lower()

_getRandomNums = lambda f, t, count: [randint(f,t) for i in range(count)]

# print(
#   _lowerize(input())
# )

# print(
#   _capitalize('box-sizing-border-box')
# )

# print(
#   getRandomNums(50, 150 , 10)
# )
class Person:
  def __init__(self, name, surname, age, isMarried):
    self.name = name
    self.surname = surname
    self.age = age
    self.isMarried = isMarried
  def showPerson(self):
    print({
      "name": self.name,
      "surname": self.surname,
      "fullname": f"{self.name}  {self.surname}",
      "is_married": self.isMarried
    })
a = FirstClass()
p1 = Person('Strange', 'Stephen', 99, False)
p1.showPerson()