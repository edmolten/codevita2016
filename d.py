import math
import collections

def func_sum(group_column_index,aggre_column_index,rows):
    h = {}
    for row in rows:
        column_group = row[group_column_index]
        column_aggre = float(row[aggre_column_index])
        if column_group not in h:
            h[column_group] = column_aggre
        else:
            h[column_group] += column_aggre
    return collections.OrderedDict(sorted(h.items()))


def func_average(group_column_index,aggre_column_index,rows):
    h = {}
    for row in rows:
        column_group = row[group_column_index]
        column_aggre = float(row[aggre_column_index])
        if column_group not in h:
            h[column_group] = (column_aggre, 1)
        else:
            sum = h[column_group][0]
            n = h[column_group][1]
            h[column_group] = (sum+column_aggre,n+1)
    for k,v in h.items():
        h[k] = h[k][0]/h[k][1]
    return collections.OrderedDict(sorted(h.items()))


def func_count(group_column_index,aggre_column_index,rows):
    h = {}
    aggres = []
    for row in rows:
        column_group = row[group_column_index]
        column_aggre = row[aggre_column_index]
        if column_group not in h:
            h[column_group] = 0
        aggres.append(column_aggre)
    for aggre in aggres:
        if aggre in h:
            h[aggre] +=1
    return collections.OrderedDict(sorted(h.items()))


def func_invert(group_column_index,aggre_column_index,rows):
    gruopers = set()
    headers = set()
    for row in rows:
        header = row[0]
        column_group = row[group_column_index]
        gruopers.add(column_group)
        headers.add(header)
    gruopers = list(gruopers)
    headers = list(headers)
    gruopers.sort()
    headers.sort()
    h = {}
    for gruper in gruopers:
        output_list = []
        for i in range(len(headers)):
            output_list.append("#")
        h[gruper] = output_list
    for row in rows:
        column_header = row[0]
        header_index = headers.index(column_header)
        column_group = row[group_column_index]
        column_agree = row[aggre_column_index]
        h[column_group][header_index] = column_agree
    return collections.OrderedDict(sorted(h.items()))

def make_rounded_output(h):
    output = ""
    for k,v in h.items():
        grouper = str(k)
        value = str(math.ceil(v))  # magia aca
        output += grouper + " " + value+"\n"
    return output

def make_count_output(h):
    output = ""
    for k,v in h.items():
        grouper = str(k)
        value = str(v)
        output += grouper + " " + value+"\n"
    return output

def make_invert_output(h):
    output = ""
    for k,v in h.items():
        grouper = str(k)
        list_string = ""
        for value in v:
            list_string += " "+value
        output += grouper + list_string+"\n"
    return output

N = int(input())
outputs = []
for i in range(N):
    func = input()
    group_column = int(input())-1
    aggre_column = int(input())-1
    rows = []
    while True:
        row = input()
        if row == "-1":
            break
        rows.append(row.split(" "))
    if func == "Sum":
        h = func_sum(group_column,aggre_column,rows)
        output = make_rounded_output(h)
        outputs.append(output)
    if func=="Count":
        h = func_count(group_column,aggre_column,rows)
        output = make_count_output(h)
        outputs.append(output)
    if func=="Average":
        h = func_average(group_column,aggre_column,rows)
        output = make_rounded_output(h)
        outputs.append(output)
    if func=="Invert":
        h = func_invert(group_column,aggre_column,rows)
        output = make_invert_output(h)
        outputs.append(output)

for output in outputs:
    print(output)
