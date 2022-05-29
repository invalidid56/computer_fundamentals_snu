# invalidid56@snu.ac.kr 작물생태정보연구실 강준서
#
# pysheet <func> (<calc> <value_colname> by <group_colname>) in <filename>

'''
컬럼 이름: colnames(filename)
부분합: subtotal(value_colname, group_colname, filename, calc='mean') 합이 필요할 때에는 calc='sum'ho
컬럼 계산: colsums(column_range, filename, calc='sum') 평균이 필요할 때는 calc='mean'
빈도표: table(colname, filename)
정렬: sortby(colname, filename)
돗수분포표: frequency(colname, ninterval, filename)
행 계산: addcol(formula, filename)
'''
import sys


class Dataframe:
    def __init__(self, columns, rows):
        self._columns = columns
        result = []
        for row in rows:
            temp = []
            for it in row:
                try:
                    temp.append(
                        float(it)
                    )
                except ValueError:
                    temp.append(it)
            result.append(temp)
        self._rows = result

    def __getitem__(self, idx, axis=0):
        return self._rows[idx]

    def __len__(self):
        return len(self._rows)

    def __repr__(self):
        for row in self._rows:
            print('\t'.join([str(r) for r in row]), end='\n')

    def __str__(self):
        line = ''
        l = self.__len__()
        for i, row in enumerate(self._rows):
            if not i == l-1:
                line += ('\t'.join([str(r) for r in row])+'\n')
            else:
                line += ('\t'.join([str(r) for r in row]))
        return line

    def get_column(self, column):
        return [row[self._columns.index(column)] for row in self._rows]

    def subtotal(self, val_col, group_col, calc='mean'):
        gc = self.get_column(group_col)
        vc = self.get_column(val_col)
        groups = list(set(gc))
        result = [[] for _ in groups]
        for g, v in zip(gc, vc):
            result[groups.index(g)].append(v)
        calculations = {
            'mean': lambda x: sum(x)/len(x),
            'sum': sum,
            'freq': len
        }
        temp = []
        for g, r in enumerate(result):
            temp.append([groups[g], calculations[calc](r)])
        result = temp
        return Dataframe(columns=[gc, vc],
                         rows=result)

    def colsums(self, col_range, calc='sum'):
        cols = [int(c)-1 for c in col_range.split('-')]
        cols = list(range(cols[0], cols[1]+1))
        result = [0 for _ in cols]
        for row in self._rows:
            for i, col in enumerate(cols):
                result[i] += row[col]
        if calc == 'sum':
            return Dataframe(columns=['Col', 'Sum'],
                             rows=[[self._columns[c], r] for c, r in zip(cols, result)])
        elif calc == 'mean':
            l = self.__len__()
            return Dataframe(columns=['Col', 'Sum'],
                             rows=[[self._columns[c], r/l] for c, r in zip(cols, result)])
        else:
            print('Calculation Error')
            exit()

    def table(self, column):
        col = self.get_column(column)
        id = list(set(col))
        result = [0 for _ in id]
        for it in col:
            result[id.index(it)] += 1
        return Dataframe(columns=['Ideal', 'Freq'],
                         rows=[(i, f) for i, f in zip(id, result)])

    def sortby(self, column):
        return Dataframe(columns=self._columns,
                         rows=sorted(self._rows, key=lambda x: x[self._columns.index(column)]))

    def frequency(self, column, ninterval):
        col = self.get_column(column)
        section = (min(col), max(col))
        interval = (section[1]-section[0])/ninterval
        breaks = [
            (section[0]+interval*n, section[0]+interval*(n+1)) for n in range(ninterval)
        ]

        def check_interval(n, sections):
            for i, sec in enumerate(sections):
                if i == 0:
                    if sec[0] <= n <= sec[1]:
                        return i
                else:
                    if sec[0] < n <= sec[1]:
                        return i
            return -1
        result = [0 for _ in breaks]
        for it in col:
            result[check_interval(it, breaks)] += 1
        return {'breaks': breaks, 'counts': result}

    def addcol(self, expression):
        result = []
        for row in self._rows:
            for i, colname in enumerate(self._columns):
                if str(type(row[i])) == "<class 'str'>":
                    ex = colname + '=' + "'" + row[i] + "'"
                else:
                    ex = colname + '=' + str(row[i])
                exec(ex)
            newval = eval(expression)
            result.append(row+[newval])
        return Dataframe(columns=self._columns+['NewCol'],
                         rows=result)


class DataframeFromFile(Dataframe):
    def __init__(self, filename):
        with open(filename, 'r') as f:
            if filename.endswith('txt'):
                columns = f.readline().strip().split('\t')
                rows = []
                for line in f:
                    rows.append(line.strip().split('\t'))
            elif filename.endswith('tab'):
                columns = f.readline().strip().split('\t')
                rows = []
                for line in f:
                    rows.append(line.strip().split('\t'))
            elif filename.endswith('dat'):
                columns = [col for col in f.readline().strip().split(' ') if col]
                rows = []
                for line in f:
                    rows.append(
                        [l for l in line.strip().split(' ') if l]
                    )
        super().__init__(columns=columns,
                         rows=rows)


def main(argv):
    func = argv[1]
    if func == 'subtotal':
        calc = argv[2]
        val_col = argv[3]
        gro_col = argv[5]
        filename = argv[7]

        df = DataframeFromFile(filename)
        result = df.subtotal(
            val_col=val_col,
            group_col=gro_col,
            calc=calc
        )
        print(result)

    elif func == 'colsums' or func == 'colmeans':
        calc = 'sum' if argv[2] == 'colsums' else 'mean'
        col_range = argv[-3]
        filename = argv[-1]
        df = DataframeFromFile(filename)
        result = df.colsums(
            col_range=col_range,
            calc=calc
        )
        print(result)

    elif func == 'table':
        col = argv[-3]
        filename = argv[-1]
        df = DataframeFromFile(filename)
        result = df.table(
            column=col
        )
        print(result)

    elif func == 'sort':
        col = argv[-3]
        filename = argv[-1]
        df = DataframeFromFile(filename)
        result = df.sortby(
            column=col
        )
        print(result)

    elif func == 'frequency':
        ninterval = int(argv[-3])
        col = argv[-4]
        filename = argv[-1]
        df = DataframeFromFile(filename)
        result = df.frequency(
            ninterval=ninterval,
            column=col
        )
        for b, c in zip(result['breaks'], result['counts']):
            print("{0} - {1} | {2}".format(b[0], b[1], c))

    elif func == 'hist':
        ninterval = int(argv[-3])
        col = argv[-4]
        filename = argv[-1]
        df = DataframeFromFile(filename)
        result = df.frequency(
            ninterval=ninterval,
            column=col
        )
        for b, c in zip(result['breaks'], result['counts']):
            print("{0} - {1} | ".format(b[0], b[1])+('*'*c))

    elif func == 'addcol':
        exp = argv[-3]
        filename = argv[-1]
        df = DataframeFromFile(filename)
        result = df.addcol(
            expression=exp
        )
        print(result)


if __name__ == '__main__':
    main(sys.argv)
