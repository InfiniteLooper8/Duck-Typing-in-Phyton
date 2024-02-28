class Duck:
  def swim(self):
      print("The duck is swimming")

  def fly(self):
      print("The duck is flying")


class Swan:
  def swim(self):
      print("The swan is swimming")

  def fly(self):
      print("The swan is flying")


class Albatross:
  def swim(self):
      print("The albatross is swimming")

  def fly(self):
      print("The albatross is flying")
class Duck:
  def fly(self):
      print("The duck is flying")

  def swim(self):
      print("The duck is swimming")


class Pigeon:
  def fly(self):
      print("The pigeon is flying")

numbers = [1, 2, 3]
person = ("Jane", 25, "Python Dev")
letters = "abc"
ordinals = {"one": "first", "two": "second", "three": "third"}
even_digits = {2, 4, 6, 8}
collections = [numbers, person, letters, ordinals, even_digits]

for collection in collections:
    for value in collection:
        print(value)

from collections.abc import Collection


def mean(grades: Collection) -> float:
    return sum(grades) / len(grades)