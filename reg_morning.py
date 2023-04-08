import openpyxl

wb = openpyxl.load_workbook("tms.xlsx")
sheet = wb["Sheet1"]

# I subtract 2 because I don't need the last two lines
max_row = sheet.max_row - 2
# =======================================================================

# დაწყება ტერ იდ- დან
x = ""
range = sheet["A1":"A50"]
for cell in range:
    for i in cell:
        if "ტერ. იდ." in str(i.value):
            x = str(i)
            break
x = x.split(".")
numb = x[1].replace(">", "")
numb = numb.replace("A", "")
numb = int(numb) + 1
# ============================================================================

problem_terminals = []

#######################################################





dict_all_sync = {}
dict_all_device_error = {}
dict_all_trans = {}
dict_all_bill = {}
dict_all_coin = {}
dict_all_rf = {}
dict_all_printer = {}

#######################################################

terminal_ID = []
range = sheet["A" + str(numb):"A" + str(max_row)]
for cell in range:
    for i in cell:
        terminal_ID.append(i.value)

#######################################################

# - კრიტიკული რომ არ ამოიღოს.
technician = []

range = sheet["K" + str(numb):"K" + str(max_row)]
for cell in range:
    for i in cell:
        technician.append(i.value)

dict_id_technician = dict(zip(terminal_ID, technician))

critical = []
for i in dict_id_technician.keys():
    if dict_id_technician[i] != None:
        critical.append(i)

#######################################################

noneed = []
rfnoneed = []

Full = []
range12 = sheet["L" + str(numb):"L" + str(max_row)]
for cell in range12:
    for i in cell:
        Full.append(i.value)

dict_id_Full = dict(zip(terminal_ID, Full))

base_inside = []


#######################################################


def Timeredactor(text):
    t = 0
    if len(text) == 7:
        if text[1] == "0" and text[2] == "0":
            t = int(text[3])
        elif text[1] == "0" and text[2] != "0":
            t = int(text[2] + text[3])
        elif text[0] != 0:
            t = int(text[0]) * 60
    elif text == "None":
        t = 0
    elif len(text) > 15:
        t = int(text[0] + text[1]) * 24 * 24

    elif "1 day" in text and text[7] == "0":
        t = (int(text[0]) * 24) * 60
    elif "1 day" in text and text[7] != "0":
        t = (int(text[0]) * 24) * 60 + int(text[7]) * 60
    elif len(text) == 16:
        t = (int(text[0]) * 24) * 60 + int(text[8] + text[9]) * 60
    elif len(text) == 15 and text[8] == "0":
        t = (int(text[0]) * 24) * 60
    elif len(text) == 15 and text[8] != 0:
        t = (int(text[0]) * 24) * 60 + int(text[8]) * 60 + int(text[10] + text[11])
    elif "day" not in text and text == "00:00:00":
        t = 0
    elif "day" not in text and text[0] == "0" and text[1] == "0":
        t = int(text[3] + text[4])
    elif "day" not in text and text[0] == "0" and text[1] != "0":

        t = int(text[1]) * 60 + int(text[3] + text[4])
    elif "day" not in text and text[0] != "0":
        t = int(text[0] + text[1]) * 60 + int(text[3] + text[4])
    return t


def Hourtominut(n):
    if n < 60:
        return (str(n) + "-წთ")
    elif n == 60:
        return ("1 სთ")
    elif n > 60:
        n = n / 60
        n = str(n)
        if len(n) == 3:
            n = n[0] + n[1] + n[2] + "-სთ"
        elif len(n) > 3:
            n = n[0] + n[1] + n[2] + n[3] + "-სთ"
        return n


########################################################################################
category = []
range1 = sheet["C" + str(numb):"C" + str(max_row)]
for cell in range1:
    for i in cell:
        category.append(i.value)

dict_id_categori = dict(zip(terminal_ID, category))
########################################################################################
tr_time = []
range2 = sheet["O" + str(numb):"O" + str(max_row)]
for cell in range2:
    for i in cell:
        tr_time.append(Timeredactor(str(i.value)))

dict_id_tr_time = dict(zip(terminal_ID, tr_time))
########################################################################################
device_eror = []
range3 = sheet["M" + str(numb):"M" + str(max_row)]
for cell in range3:
    for i in cell:
        device_eror.append(str(i.value))
dict_id_device_eror = dict(zip(terminal_ID, device_eror))

########################################################################################
receipt = []
range4 = sheet["S" + str(numb):"S" + str(max_row)]
for cell in range4:
    for i in cell:
        receipt.append(i.value)

dict_id_receipt = dict(zip(terminal_ID, receipt))




sync_time = []
range5 = sheet["N" + str(numb):"N" + str(max_row)]
for cell in range5:
    for i in cell:
        sync_time.append(Timeredactor(str(i.value)))

dict_id_sync_time = dict(zip(terminal_ID, sync_time))

coin_time = []
range6 = sheet["P" + str(numb):"P" + str(max_row)]
for cell in range6:
    for i in cell:
        coin_time.append(Timeredactor(str(i.value)))

dict_id_coin_time = dict(zip(terminal_ID, coin_time))


bill_time = []
range7 = sheet["Q" + str(numb):"Q" + str(max_row)]
for cell in range7:
    for i in cell:
        bill_time.append(Timeredactor(str(i.value)))

dict_id_bill_time = dict(zip(terminal_ID, bill_time))

card_time = []
range8 = sheet["R" + str(numb):"R" + str(max_row)]
for cell in range8:
    for i in cell:
        card_time.append(Timeredactor(str(i.value)))

dict_id_card_time = dict(zip(terminal_ID, card_time))


address = []
range9 = sheet["V" + str(numb):"V" + str(max_row)]
for cell in range9:
    for i in cell:
        address.append(i.value)

dict_id_address = dict(zip(terminal_ID, address))


district = []
range10 = sheet["Y" + str(numb):"Y" + str(max_row)]
for cell in range10:
    for i in cell:
        district.append(i.value)

dict_id_district = dict(zip(terminal_ID, district))


IPadress = []
range10 = sheet["AD" + str(numb):"AD" + str(max_row)]
for cell in range10:
    for i in cell:
        IPadress.append(i.value)

dict_id_IPadress = dict(zip(terminal_ID, IPadress))
##############################################################################

#  device errors
for i in terminal_ID:
    # ეს ლოგიყა ყველა უბანზე მიდის რადგან უბანი მითითებული არ მაქ პირველ if-ს ვგულისხმობ.
    if dict_id_sync_time[i] > 300:
        noneed.append(
            f"{str(i)}  ({dict_id_categori[i]}) {Hourtominut(dict_id_sync_time[i])} __{dict_id_address[i]}")
    elif i in critical:
        noneed.append(i)
    elif  dict_id_sync_time[i] > 15:
        dict_all_sync[i]= (
            f"{str(i)}  ({dict_id_categori[i]}) კავშირი {Hourtominut(dict_id_sync_time[i])}  ")
        problem_terminals.append(i)
    elif  "Stacker" in dict_id_device_eror[i] and dict_id_Full[i] < 600:
        dict_all_device_error[i]=(f'{str(i)}  {"წითელზეა"} ')
    elif  "Cash box" in dict_id_device_eror[i] and dict_id_Full[i] < 600:
        dict_all_device_error[i]=(f'{str(i)}  {"ყვითელზეა"} ')

    elif  "Jammed" in dict_id_device_eror[i]:
        dict_all_device_error[i] =(f'{str(i)}  {"ჩახვევა"}')

    elif  "BILL_ACCEPTOR" in dict_id_device_eror[i]:
        dict_all_device_error[i] =(f'{str(i)}  {"მეის ვერ ხედავს"} ')
        problem_terminals.append(i)
    elif  "COIN" in dict_id_device_eror[i]:
        dict_all_device_error[i] =(f'{str(i)}  {"ქოინს ვერ ხედავს"}')
        problem_terminals.append(i)
    elif  "error 14" in dict_id_device_eror[i]:
        dict_all_device_error[i] =(f'{str(i)}  {"ხურდას აკავებს"} ')
        problem_terminals.append(i)
    elif  "error 16" in dict_id_device_eror[i]:
        dict_all_device_error[i] =(f'{str(i)}  {"ხურდას აკავებს"} ')
        problem_terminals.append(i)
    elif  "registry" in dict_id_device_eror[i]:
        dict_all_device_error[i] =(f'{str(i)}  {"ვინჩესტერის პანიკა"} ')
        problem_terminals.append(i)
    elif  "CashAcceptor" in dict_id_device_eror[i]:
        dict_all_device_error[i] =(f'{str(i)}  {"მეის ვერ ხედავს"} ')
        problem_terminals.append(i)

        #  ტრანზაქციის ლოგიკა
    elif  dict_id_categori[i] == 1 and dict_id_tr_time[i] > 900:
        dict_all_trans[i]=(
            f'{str(i)} ({dict_id_categori[i]})  არ ვაჭრობს {Hourtominut(dict_id_tr_time[i])}')
    elif dict_id_categori[i] == 2 and dict_id_tr_time[i] > 900:
        dict_all_trans[i]=(
            f'{str(i)} ({dict_id_categori[i]})  არ ვაჭრობს {Hourtominut(dict_id_tr_time[i])} ')
    elif  dict_id_categori[i] == 3 and dict_id_tr_time[i] > 1200:
        dict_all_trans[i]=(
            f'{str(i)} ({dict_id_categori[i]}) არ ვაჭრობს {Hourtominut(dict_id_tr_time[i])} ')
    elif  dict_id_categori[i] == 4 and i not in base_inside and \
            dict_id_tr_time[i] > 1500:
        dict_all_trans[i]=(
            f'{str(i)} ({dict_id_categori[i]}) არ ვაჭრობს {Hourtominut(dict_id_tr_time[i])}  ')
    elif dict_id_categori[i] == 5 and i not in base_inside and \
            dict_id_tr_time[i] > 1800:
        dict_all_trans[i]=(
            f'{str(i)} ({dict_id_categori[i]}) არ ვაჭრობს {Hourtominut(dict_id_tr_time[i])}  ')

    #  მონეტის ლოგიკა
    elif dict_id_categori[i] == 1 and i not in base_inside and \
            dict_id_coin_time[i] > 900:
        dict_all_coin[i]=(
            f'{str(i)} ({dict_id_categori[i]}) ხურდა {Hourtominut(dict_id_coin_time[i])} ')
    elif  dict_id_categori[i] == 2 and i not in base_inside and \
            dict_id_coin_time[i] > 900:
        dict_all_coin[i]=(
            f'{str(i)} ({dict_id_categori[i]}) ხურდა {Hourtominut(dict_id_coin_time[i])}')
    elif  dict_id_categori[i] == 3 and i not in base_inside and \
            dict_id_coin_time[i] > 1200:
        dict_all_coin[i]=(
            f'{str(i)} ({dict_id_categori[i]}) ხურდა {Hourtominut(dict_id_coin_time[i])} ')
    elif  dict_id_categori[i] == 4 and i not in base_inside and \
            dict_id_coin_time[i] > 1500:
        dict_all_coin[i]=(
            f'{str(i)} ({dict_id_categori[i]}) ხურდა {Hourtominut(dict_id_coin_time[i])} ')
    elif dict_id_categori[i] == 5 and i not in base_inside and \
            dict_id_coin_time[i] > 1800:
        dict_all_coin[i]=(
            f'{str(i)} ({dict_id_categori[i]}) ხურდა {Hourtominut(dict_id_coin_time[i])}')

    # ----  რფ-ის ლოგიკა >>>>:
    elif dict_id_categori[i] == 1 and i not in base_inside and \
            dict_id_card_time[i] > 1800:
        dict_all_rf[i]=(f'{str(i)} ({dict_id_categori[i]}) rf {dict_id_card_time[i] // 60}-სთ ')
    elif  dict_id_categori[i] == 2 and i not in base_inside and \
            dict_id_card_time[i] > 1800:
        dict_all_rf[i]=(f'{str(i)} ({dict_id_categori[i]}) rf {dict_id_card_time[i] // 60}-სთ ')
    elif  dict_id_categori[i] == 3 and i not in base_inside and \
            dict_id_card_time[i] > 2000 and i not in rfnoneed:
        dict_all_rf[i]=(f'{str(i)} ({dict_id_categori[i]}) rf {dict_id_card_time[i] // 60}-სთ  ')
    elif  dict_id_categori[i] == 4 and i not in base_inside and \
            dict_id_card_time[i] > 3000 and i not in rfnoneed:
        dict_all_rf[i]=(f'{str(i)} ({dict_id_categori[i]}) rf {dict_id_card_time[i] // 60}-სთ ')
    elif  dict_id_categori[i] == 5 and i not in base_inside and \
            dict_id_card_time[i] > 3000 and i not in rfnoneed:
        dict_all_rf[i]=(f'{str(i)} ({dict_id_categori[i]}) rf {dict_id_card_time[i] // 60}-სთ  ')
    #
    #
    # --- პრინტერის ლოგიკა
    elif "Printer" in dict_id_device_eror[i]:
        dict_all_printer[i] =(f'{str(i)} პრინტერი ')


    elif  dict_id_receipt[i] != None and dict_id_receipt[i] < 10:
        dict_all_printer[i] =(f'{str(i)} პრინტერი (კოდი)')



# =======================================================================
print()
print("<<<<<<<<<<<<<<<<<<<<<<<<< ბათუმი, ქედა, შუახევი >>>>>>>>>>>>>>>>>>>>>>>>>")
districts = ["ბათუმი", "ქედა", "შუახევი"]
dicts = [dict_all_sync, dict_all_device_error, dict_all_trans, dict_all_coin, dict_all_rf, dict_all_printer]

for d in dicts:
    for i in terminal_ID:
        if dict_id_district[i] in districts and i in d.keys():
            print(d[i])
    print()
################################################################
print()
print("<<<<<<<<<<<<<<<<<<<<<<<<< ქობულეთი >>>>>>>>>>>>>>>>>>>>>>>>>")
districts = ["ქობულეთი"]
dicts = [dict_all_sync, dict_all_device_error, dict_all_trans, dict_all_coin, dict_all_rf, dict_all_printer]

for d in dicts:
    for i in terminal_ID:
        if dict_id_district[i] in districts and i in d.keys():
            print(d[i])
    print()
################################################################
print()
print("<<<<<<<<<<<<<<<<<<<<<<<<< ოზურგეთი, ლანჩხუთი >>>>>>>>>>>>>>>>>>>>>>>>>")
districts = ["ოზურგეთი","ლანჩხუთი"]
dicts = [dict_all_sync, dict_all_device_error, dict_all_trans, dict_all_coin, dict_all_rf, dict_all_printer]

for d in dicts:
    for i in terminal_ID:
        if dict_id_district[i] in districts and i in d.keys():
            print(d[i])
    print()
################################################################
print()
print("<<<<<<<<<<<<<<<<<<<<<<<<< ფოთი, ურეკი >>>>>>>>>>>>>>>>>>>>>>>>>")
districts = ["ფოთი","ურეკი"]
dicts = [dict_all_sync, dict_all_device_error, dict_all_trans, dict_all_coin, dict_all_rf, dict_all_printer]

for d in dicts:
    for i in terminal_ID:
        if dict_id_district[i] in districts and i in d.keys():
            print(d[i])
    print()
###############################################################
print()
print("<<<<<<<<<<<<<<<<<<<<<<<<< სენაკი, ხობი, აბაშა >>>>>>>>>>>>>>>>>>>>>>>>>")
districts = ["სენაკი", "ხობი", "აბაშა"]
dicts = [dict_all_sync, dict_all_device_error, dict_all_trans, dict_all_coin, dict_all_rf, dict_all_printer]

for d in dicts:
    for i in terminal_ID:
        if dict_id_district[i] in districts and i in d.keys():
            print(d[i])
################################################################
print()
print("<<<<<<<<<<<<<<<<<<<<<<<<< ზუგდიდი, წალენჯიხა, ჩხოროწყუ, ანაკლია >>>>>>>>>>>>>>>>>>>>>>>>>")
districts = ["ზუგდიდი", "წალენჯიხა", "ჩხოროწყუ", "ანაკლია"]
dicts = [dict_all_sync, dict_all_device_error, dict_all_trans, dict_all_coin, dict_all_rf, dict_all_printer]

for d in dicts:
    for i in terminal_ID:
        if dict_id_district[i] in districts and i in d.keys():
            print(d[i])
################################################################
print()
print("<<<<<<<<<<<<<<<<<<<<<<<<< ხონი, მარტვილი >>>>>>>>>>>>>>>>>>>>>>>>>")
districts = ["ხონი", "მარტვილი"]
dicts = [dict_all_sync, dict_all_device_error, dict_all_trans, dict_all_coin, dict_all_rf, dict_all_printer]

for d in dicts:
    for i in terminal_ID:
        if dict_id_district[i] in districts and i in d.keys():
            print(d[i])
################################################################
print()
print("<<<<<<<<<<<<<<<<<<<<<<<<< სამტრედია, ვანი >>>>>>>>>>>>>>>>>>>>>>>>>")
districts = ["სამტრედია", "ვანი"]
dicts = [dict_all_sync, dict_all_device_error, dict_all_trans, dict_all_coin, dict_all_rf, dict_all_printer]

for d in dicts:
    for i in terminal_ID:
        if dict_id_district[i] in districts and i in d.keys():
            print(d[i])
################################################################
print()
print("<<<<<<<<<<<<<<<<<<<<<<<<< ქუთაისი, წყალტუბო, ბაღდათი >>>>>>>>>>>>>>>>>>>>>>>>>")
districts = ["ქუთაისი", "წყალტუბო", "ბაღდათი"]
dicts = [dict_all_sync, dict_all_device_error, dict_all_trans, dict_all_coin, dict_all_rf, dict_all_printer]

for d in dicts:
    for i in terminal_ID:
        if dict_id_district[i] in districts and i in d.keys():
            print(d[i])
################################################################
print()
print("<<<<<<<<<<<<<<<<<<<<<<<<< ზესტაფონი, თერჯოლა >>>>>>>>>>>>>>>>>>>>>>>>>")
districts = ["ზესტაფონი", "თერჯოლა"]
dicts = [dict_all_sync, dict_all_device_error, dict_all_trans, dict_all_coin, dict_all_rf, dict_all_printer]

for d in dicts:
    for i in terminal_ID:
        if dict_id_district[i] in districts and i in d.keys():
            print(d[i])
################################################################
print()
print("<<<<<<<<<<<<<<<<<<<<<<<<< ამბროლაური, ონი, ტყიბული >>>>>>>>>>>>>>>>>>>>>>>>>")
districts = ["ამბროლაური","ონი", "ტყიბული"]
dicts = [dict_all_sync, dict_all_device_error, dict_all_trans, dict_all_coin, dict_all_rf, dict_all_printer]

for d in dicts:
    for i in terminal_ID:
        if dict_id_district[i] in districts and i in d.keys():
            print(d[i])
################################################################
print()
print("<<<<<<<<<<<<<<<<<<<<<<<<< ჭიათურა, საჩხერე >>>>>>>>>>>>>>>>>>>>>>>>>")
districts = ["ჭიათურა", "საჩხერე"]
dicts = [dict_all_sync, dict_all_device_error, dict_all_trans, dict_all_coin, dict_all_rf, dict_all_printer]

for d in dicts:
    for i in terminal_ID:
        if dict_id_district[i] in districts and i in d.keys():
            print(d[i])
################################################################
print("#########################################################################")
print("#########################################################################")
print("#########################################################################")
print()
print("<<<<<<<<<<<<<<<<<<<<<<<<< ხაშური, სურამი >>>>>>>>>>>>>>>>>>>>>>>>>")
districts = ["ხაშური", "სურამი"]
dicts = [dict_all_sync, dict_all_device_error, dict_all_trans, dict_all_coin, dict_all_rf, dict_all_printer]

for d in dicts:
    for i in terminal_ID:
        if dict_id_district[i] in districts and i in d.keys():
            print(d[i])
################################################################
print()
print("<<<<<<<<<<<<<<<<<<<<<<<<< ბორჯომი, ბაკურიანი >>>>>>>>>>>>>>>>>>>>>>>>>")
districts = ["ბორჯომი", "ბაკურიანი"]
dicts = [dict_all_sync, dict_all_device_error, dict_all_trans, dict_all_coin, dict_all_rf, dict_all_printer]

for d in dicts:
    for i in terminal_ID:
        if dict_id_district[i] in districts and i in d.keys():
            print(d[i])
################################################################
print()
print("<<<<<<<<<<<<<<<<<<<<<<<<< ახალციხე, ადიგენი, აბასთუმანი >>>>>>>>>>>>>>>>>>>>>>>>>")
districts = ["ახალციხე","ადიგენი", "აბასთუმანი"]
dicts = [dict_all_sync, dict_all_device_error, dict_all_trans, dict_all_coin, dict_all_rf, dict_all_printer]

for d in dicts:
    for i in terminal_ID:
        if dict_id_district[i] in districts and i in d.keys():
            print(d[i])
################################################################
print()
print("<<<<<<<<<<<<<<<<<<<<<<<<< ახალქალაქი, ნინოწმინდა, ასპინძა >>>>>>>>>>>>>>>>>>>>>>>>>")
districts = ["ახალქალაქი","ნინოწმინდა", "ასპინძა"]
dicts = [dict_all_sync, dict_all_device_error, dict_all_trans, dict_all_coin, dict_all_rf, dict_all_printer]

for d in dicts:
    for i in terminal_ID:
        if dict_id_district[i] in districts and i in d.keys():
            print(d[i])
################################################################
print()
print("<<<<<<<<<<<<<<<<<<<<<<<<< გორი, ქარელი >>>>>>>>>>>>>>>>>>>>>>>>>")
districts = ["გორი", "ქარელი"]
dicts = [dict_all_sync, dict_all_device_error, dict_all_trans, dict_all_coin, dict_all_rf, dict_all_printer]

for d in dicts:
    for i in terminal_ID:
        if dict_id_district[i] in districts and i in d.keys():
            print(d[i])
################################################################
print()
print("<<<<<<<<<<<<<<<<<<<<<<<<< მცხეთა, კასპი >>>>>>>>>>>>>>>>>>>>>>>>>")
districts = ["მცხეთა", "კასპი"]
dicts = [dict_all_sync, dict_all_device_error, dict_all_trans, dict_all_coin, dict_all_rf, dict_all_printer]

for d in dicts:
    for i in terminal_ID:
        if dict_id_district[i] in districts and i in d.keys():
            print(d[i])
################################################################
print()
print("<<<<<<<<<<<<<<<<<<<<<<<<< რუსთავი, გარდაბანი >>>>>>>>>>>>>>>>>>>>>>>>>")
districts = ["რუსთავი", "გარდაბანი"]
dicts = [dict_all_sync, dict_all_device_error, dict_all_trans, dict_all_coin, dict_all_rf, dict_all_printer]

for d in dicts:
    for i in terminal_ID:
        if dict_id_district[i] in districts and i in d.keys():
            print(d[i])
################################################################
print()
print("<<<<<<<<<<<<<<<<<<<<<<<<< მარნეული, თეთრიწყარო, წალკა >>>>>>>>>>>>>>>>>>>>>>>>>")
districts = ["მარნეული", "თეთრიწყარო", "წალკა"]
dicts = [dict_all_sync, dict_all_device_error, dict_all_trans, dict_all_coin, dict_all_rf, dict_all_printer]

for d in dicts:
    for i in terminal_ID:
        if dict_id_district[i] in districts and i in d.keys():
            print(d[i])
################################################################
print()
print("<<<<<<<<<<<<<<<<<<<<<<<<< ბოლნისი, კაზრეთი, დმანისი >>>>>>>>>>>>>>>>>>>>>>>>>")
districts = ["ბოლნისი", "კაზრეთი", "დმანისი"]
dicts = [dict_all_sync, dict_all_device_error, dict_all_trans, dict_all_coin, dict_all_rf, dict_all_printer]

for d in dicts:
    for i in terminal_ID:
        if dict_id_district[i] in districts and i in d.keys():
            print(d[i])
################################################################
print()
print("<<<<<<<<<<<<<<<<<<<<<<<<< საგარეჯო >>>>>>>>>>>>>>>>>>>>>>>>>")
districts = ["საგარეჯო"]
dicts = [dict_all_sync, dict_all_device_error, dict_all_trans, dict_all_coin, dict_all_rf, dict_all_printer]

for d in dicts:
    for i in terminal_ID:
        if dict_id_district[i] in districts and i in d.keys():
            print(d[i])
################################################################
print()
print("<<<<<<<<<<<<<<<<<<<<<<<<< წნორი, სიღნაღი >>>>>>>>>>>>>>>>>>>>>>>>>")
districts = ["წნორი", "სიღნაღი"]
dicts = [dict_all_sync, dict_all_device_error, dict_all_trans, dict_all_coin, dict_all_rf, dict_all_printer]

for d in dicts:
    for i in terminal_ID:
        if dict_id_district[i] in districts and i in d.keys():
            print(d[i])
################################################################
print()
print("<<<<<<<<<<<<<<<<<<<<<<<<< დედოფლისწყარო >>>>>>>>>>>>>>>>>>>>>>>>>")
districts = ["დედოფლისწყარო"]
dicts = [dict_all_sync, dict_all_device_error, dict_all_trans, dict_all_coin, dict_all_rf, dict_all_printer]

for d in dicts:
    for i in terminal_ID:
        if dict_id_district[i] in districts and i in d.keys():
            print(d[i])
################################################################
print()
print("<<<<<<<<<<<<<<<<<<<<<<<<< გურჯაანი >>>>>>>>>>>>>>>>>>>>>>>>>")
districts = ["გურჯაანი"]
dicts = [dict_all_sync, dict_all_device_error, dict_all_trans, dict_all_coin, dict_all_rf, dict_all_printer]

for d in dicts:
    for i in terminal_ID:
        if dict_id_district[i] in districts and i in d.keys():
            print(d[i])
################################################################

print()
print("<<<<<<<<<<<<<<<<<<<<<<<<< თელავი, ახმეტა >>>>>>>>>>>>>>>>>>>>>>>>>")
districts = ["თელავი", "ახმეტა"]
dicts = [dict_all_sync, dict_all_device_error, dict_all_trans, dict_all_coin, dict_all_rf, dict_all_printer]

for d in dicts:
    for i in terminal_ID:
        if dict_id_district[i] in districts and i in d.keys():
            print(d[i])
################################################################
print()
print("<<<<<<<<<<<<<<<<<<<<<<<<< ყვარელი, ლაგოდეხი >>>>>>>>>>>>>>>>>>>>>>>>>")
districts = ["ყვარელი", "ლაგოდეხი"]
dicts = [dict_all_sync, dict_all_device_error, dict_all_trans, dict_all_coin, dict_all_rf, dict_all_printer]

for d in dicts:
    for i in terminal_ID:
        if dict_id_district[i] in districts and i in d.keys():
            print(d[i])
################################################################

print("\n")
print("\n")
print("\n")

for i in problem_terminals:
    print(f"putty.exe -ssh kiosk@{dict_id_IPadress[i]} -pw 123 -m C:\\Users\\gkupreishvili\\Desktop\\t7.txt -t")
