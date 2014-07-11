#!/usr/bin/python
import re
from urllib import urlopen

content = urlopen('http://www.quasco.de').read()

pattern1 = '\s*(?i)href\s*=\s*(\"([^"]*\")|\'[^\']*\'|([^\'">\s]+))'
pattern2 = "\s*(?i)href\s*=\s*(\\\"([^\"]*\\\")|'[^']*'|([^'\">\s]+))"
pattern3 =  "\\s*(?i)href\\s*=\\s*(\"([^\"]*\")|'[^']*'|([^'\">\\s]+))"
pattern4 = "/<a href=\"(.*)\">(.*)<\/a>/"
pattern5 = "([\d\w-.]+?\.(a[cdefgilmnoqrstuwz]|b[abdefghijmnorstvwyz]|c[acdfghiklmnoruvxyz]|d[ejkmnoz]|e[ceghrst]|f[ijkmnor]|g[abdefghilmnpqrstuwy]|h[kmnrtu]|i[delmnoqrst]|j[emop]|k[eghimnprwyz]|l[abcikrstuvy]|m[acdghklmnopqrstuvwxyz]|n[acefgilopruz]|om|p[aefghklmnrstwy]|qa|r[eouw]|s[abcdeghijklmnortuvyz]|t[cdfghjkmnoprtvwz]|u[augkmsyz]|v[aceginu]|w[fs]|y[etu]|z[amw]|aero|arpa|biz|com|coop|edu|info|int|gov|mil|museum|name|net|org|pro)(\b|\W(?<!&|=)(?!\.\s|\.{3}).*?))(\s|$)"
#print ''
#print re.findall(pattern ,content)


regex = re.compile(pattern5)
print ''
#print regex.findall(content)
for rw in regex.findall(content):
	print rw[1]
