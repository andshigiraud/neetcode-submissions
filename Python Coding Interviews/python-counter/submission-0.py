from collections import Counter
from typing import Counter as CounterType


def count_chars(s1: str, s2: str) -> CounterType:
    new_count = {}
    for i,n in zip(s1,s2):
        new_count = Counter(s1)
        new_count.update(s2)
    return new_count
  

# do not modify below this line
print(count_chars("hello", "world"))
print(count_chars("hello", "worldhello"))
print(count_chars("areallylongstring", "heyhowisitgoing"))
