#pprinting
import pprint
message = ' I t was a birght cold day in April, and the clocks were striking thirteen'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character]+1

pprint.pprint(count)

