from typing import List, Any

import pylightxl as xl
from deepdiff import DeepDiff
diffile = False
# readxl returns a pylightxl database that holds all worksheets and its data
db = xl.readxl(fn='D:/Python/pythonall1/Inst1.xlsx')
lst_ISIN = db.ws(ws='Sheet1').col(col=3)
lst_UP = db.ws(ws='Sheet1').col(col=4)

instFileIP = [
    {'ISIN': n, 'Unit Price': up}
    for n, up in zip(lst_ISIN, lst_UP)
]
instFileIP = instFileIP[1:]
print("INST File", instFileIP)

opdb = xl.readxl(fn='D:/Python/pythonall1/opfile.xlsx')
lst_POSID = opdb.ws(ws='Sheet1').col(col=2)
lst_QNT = opdb.ws(ws='Sheet1').col(col=4)
lst_ISINop = opdb.ws(ws='Sheet1').col(col=3)
lst_totpop = opdb.ws(ws='Sheet1').col(col=5)
opFile = [
    {'Position ID': posi, 'Quantity': qnt}
    for posi, qnt in zip(lst_POSID, lst_QNT)
]
opFile = opFile[1:]
print("OUTFILE: ", opFile)

posdb = xl.readxl(fn='D:/Python/pythonall1/PosDet.xlsx')
lst_POSIDi = posdb.ws(ws='Sheet1').col(col=1)
lst_QNTi = posdb.ws(ws='Sheet1').col(col=3)

posFile = [
    {'Position ID': posi, 'Quantity': qnt}
    for posi, qnt in zip(lst_POSIDi, lst_QNTi)
]
posFile = posFile[1:]
print("Position Details", posFile)

misMatches = DeepDiff(opFile, posFile)

cnt = len(misMatches)

if cnt == 0:
    print("Pass")
else:
    print("FAIL, Number of Mismatches:", cnt, misMatches)
    diffile  = True

opFileFC = [
    {'ISIN': isin, 'Quantity': qnt, "Total Price": totpri}
    for isin, qnt, totpri in zip(lst_ISINop, lst_QNT, lst_totpop)
]
opFileFC = opFileFC[1:]

if diffile:
    print("As the First Test case has failed no pint checking the 2nd One")
else:
    print("Final Check", opFileFC)
    for i in range(len(opFileFC)):
        idn = int(next((j for j, dictionary in enumerate(instFileIP) if dictionary.get('ISIN') == opFileFC[i]['ISIN']), -1))
        if opFileFC[i]['Total Price'] != opFileFC[i]['Quantity'] * instFileIP[idn]['Unit Price']:
            print("Fail", i + 1)
        else:
            print("Pass")
