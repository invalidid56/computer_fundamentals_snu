# make_html.py
# read data and draw table in html
# 2022-14673 강준서

import sys


def main(filedir):
    file = open(filedir, mode='r')
    theads = file.readline().split(',')

    data = []
    for line in file:
        toks = line.split(',')
        for i, tok in enumerate(toks):
            if i == 0:
                toks[i] = int(tok)
            elif i > 1:
                toks[i] = float(tok)
        data.append(toks)

    # Head
    print('''
    <html>
        <head>
            <style>
      table, th, td {
	  border: 1px solid darkgray;
	  border-collapse: collapse;
      }
      th {
	  background-color: lightgray;
      }
    </style>
        </head>''')

    # Body
    color = ['hotpink', 'lightblue', 'gray', 'cyan', 'magenta', 'green', 'purple']
    print('''
    <body>
    <table style="border: 1px solid black;">
    <thead>
    <tr>
    ''')
    for thead in theads:
        print("<th>{0}</th>".format(thead))
    print('''
    </tr>
    </thead>
    <tbody>''')

    for i, row in enumerate(data):
        print('<tr>')
        for j, col in enumerate(row):
            if j > 1:
                l = '''<td><div style="background-color: {0}; width: {1}px">{2}</div></td>'''.format(color[j-2], col*50, col)
            else:
                l = '''<td>{0}</td>'''.format(col)
            print(l)
        print('</tr>')
    print('''</tbody>
        </table>''')


if __name__ == '__main__':
    main(sys.argv[1])
