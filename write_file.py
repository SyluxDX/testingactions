""" write file """
import random
import string

letters = "".join(random.choice(string.ascii_lowercase) for i in range(10))

with open(f"filename_{letters}.txt", "w", encoding="utf8") as fp:
  fp.write(''.join(random.choice(string.ascii_lowercase) for i in range(100)))

print(f"Written filename_{letters}.txt") 
