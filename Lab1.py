"""3.2 ������������ ���� ����� msg ����� �������, ������ �������� ����� ����� � �������������, ������ - ������������ ������� print."""
msg = 'Olena Stetskiv'
msg
print msg

"""3.10 ������� ��������� ��������� msg[::-1]."""
msg[::-1]

"""3.5 �������������� ���� �� �������� �������� ������ ������ msg �� ������� ��� , �� �������, ������� ��������."""
msg[0:5] + ' Olehivna ' + msg[6:]

"""3.12 ����������� �������, ��� �� �� ������� �� ������ ������. �������� ������� �� ����� ��������, ���� ������ ������� �����."""
msg.split('e')

"""3.16 �������� ����� words ��� ������ ������ ���. ������� �������� words.sort() � sorted(words)."""
words = ['one', 'two', 'three', 'four', 'five']
words

sorted(words)
words

words.sort()
words

"""	3.25 ��������� ������� ��� ��� � ������ phrase1 �������������� ����� index()."""
phrase1 = ['Monday', 'Wednesday', 'Friday', 'Sunday']
phrase1

phrase1.index('Friday')

phrase1.index('Monday')

phrase1.index('Wednesday')

phrase1.index('Sunday')

for word in phrase1:
	print word, phrase1.index(word)

""" 3.26 ��������� ����� silly, ��� ���� ������ ������ �newly formed bland ideas are inexpressible in an infuriating way� � �������� �������� �� ������������ � ������ phrase, ���� ���� ������ �� ����� silly ��� �in�."""
silly ='newly formed bland ideas are inexpressible in an infuriating way'
silly

phrase =[]
for word in silly.split():
	if word != 'in':
		phrase.append(word)

phrase

