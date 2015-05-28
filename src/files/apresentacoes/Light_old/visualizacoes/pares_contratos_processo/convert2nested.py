from sys import argv
import csv
import json

def get_children(node, fp, i1, i2, iv):

    ifile = open(fp, 'rb')
    reader = csv.reader(ifile)
    #reader.next()

    children = []
    for line in list(reader):
        item1 = line[int(i1)].strip()
        item2 = line[int(i2)].strip()
        value = line[int(iv)].strip()
        #print i1, line[int(i1)]
        #print i2, line[int(i2)]
        #print iv, line[int(iv)]
        #raw_input()
        if item1 == node.split(' ---')[0]:
            children.append({"name":item2, "size": int(value.strip())})

    return children

def get_last_level(fp2, left, right):

    ifile = open(fp2, 'rb')
    reader = csv.reader(ifile)
    reader.next()

    children = []

    left_item = 0
    right_item = 2
    left_item_desc = 1
    right_item_desc = 3
    value_item = 5

    for row in reader:
        if row[left_item].strip() == left and row[right_item].strip() == right:
            item = row[left_item_desc].strip()
            item += '  => '
            item += row[right_item_desc].strip()
            value = row[value_item].strip()
            children.append({"name":item, "size": int(value)})

    return children


def last_level(dic, fp2):
    for c in dic['children']:
        for c2 in c['children']:
            left = c['name'].split('---')[0].strip()
            right = c2['name'].split('---')[0].strip()

            l = pareto_local(get_last_level(fp2, left, right), cut=0.5, minimum = 2000)
            c2['children'] = l
    return dic

def pareto_local(listing, cut=1, minimum=0):
    total = sum(item['size'] for item in listing)
    listing.sort(key=lambda x: x["size"], reverse=True)
    l, list_sum = [], 0
    for item in listing:
        if list_sum < total * cut and item['size'] > minimum:
            item['name'] = item['name'] + ' --- {} ({:.2f})'.format(item['size'],float(item['size'])/total)
            l.append(item)
            list_sum += item['size']
    return l

def convert(*items):

    fp = items[1] #arquivo de entrada grosso 
    node = items[2].strip() #tipo da nota de interesse
    fo = items[3] #aquivo de saida
    i1 = items[4]#i1 is the first item
    i2 = items[5]#i1 is the second item
    iv = items[6] # valor da aresta 
    fp2 = items[7] #arquivo de entrada fino

    sons = get_children(node, fp, i1, i2, iv)
    sons = pareto_local(sons, cut=0.8)
    for son in sons:
        c = get_children(son["name"], fp, i1, i2,iv)
        print son["name"], c 
        c = pareto_local(c, cut=0.8)
        print c
        son["children"] = c
        #son["children"] = pareto_local(get_children(son["name"], fp, i1, i2,iv))

    dic = {"name": node, "children": sons}


    dic = last_level(dic, fp2)

    with open(fo, 'wb') as fp:
        json.dump(dic, fp)

if __name__=="__main__":
    convert(*argv)
