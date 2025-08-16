print('Hello World')

print('You must be the legendary god that comes from the sky')

print('We have been waiting for you for a long time')

print('Our legend says you will be very tasty with mustard')

# ERROR Examples
# print 'We will have a feast tonight unless you say
# good-bye
# if you don't mind, I need to leave
# quit()

x = 6
print(x)

y = x * 7
print(y)

# Example program from chapter 1
name = input('Enter file: ')
handle = open(name, 'r')
counts = dict()

for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word, count in list(counts.items()):
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)