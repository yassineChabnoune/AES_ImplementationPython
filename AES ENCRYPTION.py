import numpy as np
S_box = [
    ['63', '7c', '77', '7b', 'f2', '6b', '6f', 'c5', '30', '01', '67', '2b', 'fe', 'd7', 'ab', '76'],
    ['ca', '82', 'c9', '7d', 'fa', '59', '47', 'f0', 'ad', 'd4', 'a2', 'af', '9c', 'a4', '72', 'c0'],
    ['b7', 'fd', '93', '26', '36', '3f', 'f7', 'cc', '34', 'a5', 'e5', 'f1', '71', 'd8', '31', '15'],
    ['04', 'c7', '23', 'c3', '18', '96', '05', '9a', '07', '12', '80', 'e2', 'eb', '27', 'b2', '75'],
    ['09', '83', '2c', '1a', '1b', '6e', '5a', 'a0', '52', '3b', 'd6', 'b3', '29', 'e3', '2f', '84'],
    ['53', 'd1', '00', 'ed', '20', 'fc', 'b1', '5b', '6a', 'cb', 'be', '39', '4a', '4c', '58', 'cf'],
    ['d0', 'ef', 'aa', 'fb', '43', '4d', '33', '85', '45', 'f9', '02', '7f', '50', '3c', '9f', 'a8'],
    ['51', 'a3', '40', '8f', '92', '9d', '38', 'f5', 'bc', 'b6', 'da', '21', '10', 'ff', 'f3', 'd2'],
    ['cd', '0c', '13', 'ec', '5f', '97', '44', '17', 'c4', 'a7', '7e', '3d', '64', '5d', '19', '73'],
    ['60', '81', '4f', 'dc', '22', '2a', '90', '88', '46', 'ee', 'b8', '14', 'de', '5e', '0b', 'db'],
    ['e0', '32', '3a', '0a', '49', '06', '24', '5c', 'c2', 'd3', 'ac', '62', '91', '95', 'e4', '79'],
    ['e7', 'c8', '37', '6d', '8d', 'd5', '4e', 'a9', '6c', '56', 'f4', 'ea', '65', '7a', 'ae', '08'],
    ['ba', '78', '25', '2e', '1c', 'a6', 'b4', 'c6', 'e8', 'dd', '74', '1f', '4b', 'bd', '8b', '8a'],
    ['70', '3e', 'b5', '66', '48', '03', 'f6', '0e', '61', '35', '57', 'b9', '86', 'c1', '1d', '9e'],
    ['e1', 'f8', '98', '11', '69', 'd9', '8e', '94', '9b', '1e', '87', 'e9', 'ce', '55', '28', 'df'],
    ['8c', 'a1', '89', '0d', 'bf', 'e6', '42', '68', '41', '99', '2d', '0f', 'b0', '54', 'bb', '16']
]
s_box = np.array(
   [[" ",    "0",    "1",    "2",    "3",    "4",    "5",    "6",    "7",    "8",    "9",    "a",    "b",    "c",    "d",    "e",    "f"],
    ["0", "0x63", "0x7c", "0x77", "0x7b", "0xf2", "0x6b", "0x6f", "0xc5", "0x30", "0x01", "0x67", "0x2b", "0xfe", "0xd7", "0xab", "0x76" ],
    ["1", "0xca", "0x82", "0xc9", "0x7d", "0xfa", "0x59", "0x47", "0xf0", "0xad", "0xd4", "0xa2", "0xaf", "0x9c", "0xa4", "0x72", "0xc0" ],
    ["2", "0xb7", "0xfd", "0x93", "0x26", "0x36", "0x3f", "0xf7", "0xcc", "0x34", "0xa5", "0xe5", "0xf1", "0x71", "0xd8", "0x31", "0x15" ],
    ["3", "0x04", "0xc7", "0x23", "0xc3", "0x18", "0x96", "0x05", "0x9a", "0x07", "0x12", "0x80", "0xe2", "0xeb", "0x27", "0xb2", "0x75" ],
    ["4", "0x09", "0x83", "0x2c", "0x1a", "0x1b", "0x6e", "0x5a", "0xa0", "0x52", "0x3b", "0xd6", "0xb3", "0x29", "0xe3", "0x2f", "0x84" ],
    ["5", "0x53", "0xd1", "0x00", "0xed", "0x20", "0xfc", "0xb1", "0x5b", "0x6a", "0xcb", "0xbe", "0x39", "0x4a", "0x4c", "0x58", "0xcf" ],
    ["6", "0xd0", "0xef", "0xaa", "0xfb", "0x43", "0x4d", "0x33", "0x85", "0x45", "0xf9", "0x02", "0x7f", "0x50", "0x3c", "0x9f", "0xa8" ],
    ["7", "0x51", "0xa3", "0x40", "0x8f", "0x92", "0x9d", "0x38", "0xf5", "0xbc", "0xb6", "0xda", "0x21", "0x10", "0xff", "0xf3", "0xd2" ],
    ["8", "0xcd", "0x0c", "0x13", "0xec", "0x5f", "0x97", "0x44", "0x17", "0xc4", "0xa7", "0x7e", "0x3d", "0x64", "0x5d", "0x19", "0x73" ],
    ["9", "0x60", "0x81", "0x4f", "0xdc", "0x22", "0x2a", "0x90", "0x88", "0x46", "0xee", "0xb8", "0x14", "0xde", "0x5e", "0x0b", "0xdb" ],
    ["a", "0xe0", "0x32", "0x3a", "0x0a", "0x49", "0x06", "0x24", "0x5c", "0xc2", "0xd3", "0xac", "0x62", "0x91", "0x95", "0xe4", "0x79" ],
    ["b", "0xe7", "0xc8", "0x37", "0x6d", "0x8d", "0xd5", "0x4e", "0xa9", "0x6c", "0x56", "0xf4", "0xea", "0x65", "0x7a", "0xae", "0x08" ],
    ["c", "0xba", "0x78", "0x25", "0x2e", "0x1c", "0xa6", "0xb4", "0xc6", "0xe8", "0xdd", "0x74", "0x1f", "0x4b", "0xbd", "0x8b", "0x8a" ],
    ["d", "0x70", "0x3e", "0xb5", "0x66", "0x48", "0x03", "0xf6", "0x0e", "0x61", "0x35", "0x57", "0xb9", "0x86", "0xc1", "0x1d", "0x9e" ],
    ["e", "0xe1", "0xf8", "0x98", "0x11", "0x69", "0xd9", "0x8e", "0x94", "0x9b", "0x1e", "0x87", "0xe9", "0xce", "0x55", "0x28", "0xdf" ],
    ["f", "0x8c", "0xa1", "0x89", "0x0d", "0xbf", "0xe6", "0x42", "0x68", "0x41", "0x99", "0x2d", "0x0f", "0xb0", "0x54", "0xbb", "0x16" ]])

def text_to_hex(string):
    list = []
    for i in range(0, len(string), 1):
        temp = hex(ord(string[i]))
        list.append(temp)
    return list


def subbyte(strList):
    list=[]
    for i in strList:
        y = s_box[:, 0].tolist()
        x = s_box[0, :].tolist()
        findx = x.index(str(i[-2]))
        findy = y.index(str(i[-1]))
        list.append((s_box[findx][findy]))
    arr = np.array(list)
    newarr = arr.reshape(4, 4)
    newarr = np.transpose(newarr)
    return newarr


    return list

def mixCol(A):
  e_table = np.load('E_Table.npy')
  B = np.zeros((4,4),dtype=int)
  for row in range(4):
    for col in range(4):
      sub_row , sub_col = A[row,col]//16,A[row,col]%16
      B[row,col] = e_table[sub_row,sub_col]
  return B


def hex_to_text(hexa):
    list=[]
    for i in hexa:
        temp = chr(int(i,16))
        list.append(temp)
        chaine="".join(map(str,list))
    return chaine


# ===================================================
# =                  SHIFT ROW                      =
# ===================================================
def shifting(lamatrice):
    list=[]
    list = lamatrice.tolist()
    newlist=[]
    for i in range(len(list)):
        if i==0:
            newlist.append(list[i])
        else:
            var= list[i][i:]
            var2= list[i][:i]
            #var.append(var2)
            var= var+var2
            newlist.append(var)
    arr=np.array(newlist)
    newarr = arr.reshape(4,4)
    return newarr
L= text_to_hex("yassneshshewowna")
# print(shifting(subbyte(L)))
shifted =shifting(subbyte(L))


mc = [
    ["02", "03", "01", "01"],
    ["01", "02", "03", "01"],
    ["01", "01", "02", "03"],
    ["03", "01", "01", "02"]
]

def addroundkey(matrice,key):
    list=[]
    for i in range(0,4):
        for j in range(0,4):
            elem =int(matrice[i][j],16)
            k = int(key[i][j],16)
            res = hex(elem ^ k)
            list.append(res)
    roundkey= np.array(list)
    return roundkey.reshape(4,4)

rcon = np.array([
    ["01","02","04","08","10","20","40","80","18","36",],
    ["00","00","00","00","00","00","00","00","00","00",],
    ["00","00","00","00","00","00","00","00","00","00",],
    ["00","00","00","00","00","00","00","00","00","00",],
    ])


def keygen(key):
    # transformation de la clef vers une matrice
    list = text_to_hex(key)
    matrice = np.array(list)
    # key state
    matrice = matrice.reshape(4,4)
    print(matrice)
    # on prend la derniere colone puis on fait le rotword
    lastlINE = matrice[3].tolist()
    R = rotword(lastlINE)
    # on fait le subbyte pour la colone qui etait rotworder
    LRS = subbytekey(R)
    # creation de la premiere colone dans la matrice du key1
    count =0
    # on prend la premiere colone et la derniere et la premiere colone de rcon et on fait le xor
    firstLine = matrice[0][:].tolist()
    Ckey1= xoringLRS(firstLine,LRS,count)
    keylist1= []
    keylist1.append(Ckey1) #ajout de la colone dans une liste
    #boucle pour stocker toute la matrice Key1 dans la liste
    for i in range(3):
        keylist1.append(xoringCol(matrice[i+1],keylist1[i]))
    print('key list number 1 ----------------------------------')
    key1 = np.array(keylist1)
    key1 = key1.transpose()
    print(key1)
    print('**************8')
    print(key1[:,3])
    count=1

    #creation du deuxieme matrice key2
    lastlINE = key1[:,3].tolist()
    print('last colone is ')
    print(lastlINE)
    R = rotword(lastlINE)
    LRS = subbytekey(R)
    firstLine=key1[:,0].tolist()
    print('first colone is ')
    print(firstLine)
    Ckey1=xoringLRS(firstLine,LRS,1)
    print('premiere line dans la deuxieme matrice')
    print(Ckey1)
    print('---------------------')
    keylist2=[]
    keylist2.append(Ckey1)
    for i in range(3):
        keylist2.append(xoringCol(key1[:,i + 1], keylist2[i]))
    print(keylist2)
    key2 = np.array(keylist2)
    key2 = key2.transpose()
    print('----la cle 2 ------------')
    print(key2)
def xoringLRS(list,lrs,count):
    rc = rcon.transpose()
    rc =  rc[count]
    tmplist=[]
    for i in range (4):
        item1= int(list[i],16)
        item2= int(lrs[i],16)
        item3= int(rc[i],16)
        tmplist.append(hex(item1 ^ item2 ^ item3))

    return tmplist



def xoringCol(col1,col2):
    ncol=[]
    for i in range(4):
        c1=int(col1[i],16)
        c2= int(col2[i],16)
        ncol.append(hex(c1 ^ c2))
    return ncol


def subbytekey(strList):
    list = []
    for i in strList:
        y = s_box[:, 0].tolist()
        x = s_box[0, :].tolist()
        findx = x.index(str(i[-2]))
        findy = y.index(str(i[-1]))
        list.append((s_box[findx][findy]))
    return list

def rotword(line):
    liste=[]
    liste=line[1:]
    liste.append(line[0])
    return liste
print(type(keygen('TEAMSCORPIAN1234')))

