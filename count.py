 import re
from itertools import islice, izip
words = re.findall("\w+",
   "the quick person did not realize his speed and the quick person bumped")
print Counter(izip(words, islice(words, 1, None)))

