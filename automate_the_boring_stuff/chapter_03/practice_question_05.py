# If you had a function named bacon() inside a module named spam,
# how would you call it after importing spam?

from spam.bacon import bacon
from big_spam import big_bacon

print(bacon())
print(big_bacon())