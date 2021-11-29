import json
from os import write
from time import time

#konversi JSON ke array di python
def load_data_from_json(data):
    return json.loads(data)

def load_data_file(filename):
    f = open(filename, "r")
    return load_data_from_json(str(f.read()))

def write_data_file(filename, isinya):
    with open(filename, 'w') as convert_file:
        convert_file.write(json.dumps(isinya))

def load_transaksi_file(filename):
    arr = []
    a_file = open(filename, "r")
    for line in a_file:
        data, op, timestamp, add, val = line.split()
        kamus = {}
        kamus["data"] = data
        kamus["op"] = op
        kamus["timestamp"] = float(timestamp)
        if(kamus["op"]=='W'):
            kamus["value"] = {}
            kamus["value"]["add"] = bool(add)
            kamus["value"]["val"] = int(val)
        arr.append(kamus)
    return (arr)

def OCC(filename, data, transaksi):
    temp_data = data
    for t in transaksi:
        if (t['timestamp']<temp_data[t['data']]["timestamp"]):
            print(f'Maaf, terjadi konflik pada operasi: {t}')
            return
        else:
            if(t['op']=='R' or t['op']=='C'):
                temp_data[t['data']]["timestamp"] = t['timestamp']
            elif(t['op']=='W'):
                temp_data[t['data']]["timestamp"] = t['timestamp']
                if(t['value']['add']==True):
                    temp_data[t['data']]["value"] += t['value']['val']
                else:
                    temp_data[t['data']]["value"] -= t['value']['val']
    print()
    write_data_file(filename, temp_data)
    print("Menulis data pada file....")


if __name__ == "__main__":
    data = load_data_file("input/data.txt")
    transaksi = load_transaksi_file("input/transaksi.txt")
    OCC("input/data(2).txt", data, transaksi)