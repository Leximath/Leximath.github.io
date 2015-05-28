import re
from sys import argv

fn = argv[1]
fi = open(fn)
fo = open(fn[:-4] + '.html', 'w')

fo.write('<table id="recap" cellspacing="0" class="mytable" >\n')

#Header
fo.write('<tr>')
for item in fi.next().split(';'):
    fo.write('<th>')
    fo.write(item)
    fo.write('</th>\n')
fo.write('</tr>\n')

#Rows
for line in fi:
    fo.write('<tr>')
    for item in line.split(';'):
        fo.write('<td>')
        fo.write(item)
        fo.write('</td>\n')
    fo.write('</tr>')

#End
fo.write('</table>\n')

fo.close()
