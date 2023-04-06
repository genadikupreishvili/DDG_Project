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
# ===============================================================================
problem_terminals = []

#######################################################
isani_sync = []
isani_device_error = []
isani_trans = []
isani_bill = []
isani_coin = []
isani_rf = []
isani_printer = []

vake_sync = []
vake_device_error = []
vake_trans = []
vake_bill = []
vake_coin = []
vake_rf = []
vake_printer = []

saburtalo_sync = []
saburtalo_device_error = []
saburtalo_trans = []
saburtalo_bill = []
saburtalo_coin = []
saburtalo_rf = []
saburtalo_printer = []

didube_sync = []
didube_device_error = []
didube_trans = []
didube_bill = []
didube_coin = []
didube_rf = []
didube_printer = []

gldani_sync = []
gldani_device_error = []
gldani_trans = []
gldani_bill = []
gldani_coin = []
gldani_rf = []
gldani_printer = []

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
rfnoneed = [14007, 14229, 11094, 11873, 12618, 14196, 14197, 14059, 10313, 12527, 10216, 10467, 12955, 12259, 14242,
            12019, 14137, 14239, 10084, 10403, 11365, 14182, 11792, 14244, 14234, 14059, 12527, 10150, 14175, 10313,
            14272, 14264, 14259, 14275, 14276]

Full = []
range12 = sheet["L" + str(numb):"L" + str(max_row)]
for cell in range12:
    for i in cell:
        Full.append(i.value)

dict_id_Full = dict(zip(terminal_ID, Full))

base_inside = [12282, 10572, 12057, 12270, 12076, 10458, 12942, 12921, 12252, 12576, 11996, 12151, 12703, 12108, 12644,
               12967, 12777, 12698, 12296, 12629, 12987, 12570, 12770, 12067, 14141, 14133, 12520, 11375, 12929, 12751,
               12764, 12418, 14198, 12750, 12240, 11784, 11114, 12760, 11979, 10547, 12793, 12614, 14130, 12839, 12821,
               12869, 12785, 11802, 10155, 14058, 12459, 12933, 12792, 12875, 12065, 12928, 12468, 12421, 12932, 10595,
               12469, 12813, 12781, 12837, 11946, 11102, 12931, 14049, 12663, 12458, 12235, 12627, 12647, 11872, 12705,
               12818, 12738, 10089, 12779, 14162, 14231, 10545, 12596, 11897, 12697, 12787, 12124, 10707, 12519, 12625,
               12790, 12066, 12798, 14117, 12276, 12701, 10082, 11966, 11895, 14246, 11938, 12734, 12709, 12930, 12748,
               14206, 14044, 12850, 12249, 14129, 12257, 10711, 12454, 12261, 14017, 14000, 12131, 14228, 10176, 10396,
               12646, 10410, 10564, 12598, 11090, 12466, 12814, 10391, 14110, 10699, 12871, 10374, 11407, 12599, 12737,
               12595, 12826, 12072, 14230, 12947, 11866, 12961, 10138, 12531, 11208, 12180, 12704, 12872, 12736, 12597,
               12161, 10256, 12283, 12707, 14051, 10531, 14018, 12766, 14224, 12819, 12878, 10687, 14273, 14300]


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

########################################################################################
sync_time = []
range5 = sheet["N" + str(numb):"N" + str(max_row)]
for cell in range5:
    for i in cell:
        sync_time.append(Timeredactor(str(i.value)))

dict_id_sync_time = dict(zip(terminal_ID, sync_time))
########################################################################################
coin_time = []
range6 = sheet["P" + str(numb):"P" + str(max_row)]
for cell in range6:
    for i in cell:
        coin_time.append(Timeredactor(str(i.value)))

dict_id_coin_time = dict(zip(terminal_ID, coin_time))

########################################################################################
bill_time = []
range7 = sheet["Q" + str(numb):"Q" + str(max_row)]
for cell in range7:
    for i in cell:
        bill_time.append(Timeredactor(str(i.value)))

dict_id_bill_time = dict(zip(terminal_ID, bill_time))
########################################################################################
card_time = []
range8 = sheet["R" + str(numb):"R" + str(max_row)]
for cell in range8:
    for i in cell:
        card_time.append(Timeredactor(str(i.value)))

dict_id_card_time = dict(zip(terminal_ID, card_time))

########################################################################################
address = []
range9 = sheet["V" + str(numb):"V" + str(max_row)]
for cell in range9:
    for i in cell:
        address.append(i.value)

dict_id_address = dict(zip(terminal_ID, address))

########################################################################################
district = []
range10 = sheet["Y" + str(numb):"Y" + str(max_row)]
for cell in range10:
    for i in cell:
        district.append(i.value)

dict_id_district = dict(zip(terminal_ID, district))

#################################-----logics gldani-----#######################################################

IPadress = []
range10 = sheet["AD" + str(numb):"AD" + str(max_row)]
for cell in range10:
    for i in cell:
        IPadress.append(i.value)

dict_id_IPadress = dict(zip(terminal_ID, IPadress))


#################################-----logics gldani-----#######################################################



# ასევე მეიგლობალების იპები როწამოგიღოს

# გლდანი device error
for i in terminal_ID:
    if dict_id_sync_time[i] > 900:
        noneed.append(
            f"{str(i)}  ({dict_id_categori[i]}) {Hourtominut(dict_id_sync_time[i])} __{dict_id_address[i]}")
    elif i in critical:
        noneed.append(i)
    elif dict_id_district[i] == 'გლდანი-ნაძალადევი' and dict_id_sync_time[i] > 15:
        gldani_sync.append(
            f"{str(i)}  ({dict_id_categori[i]}) {Hourtominut(dict_id_sync_time[i])} __{dict_id_address[i]}")
        problem_terminals.append(i)
    elif dict_id_district[i] == 'გლდანი-ნაძალადევი' and "Stacker" in dict_id_device_eror[i] and dict_id_Full[i] < 600:
        gldani_device_error.append(f'{str(i)}  {"Stacker Full"}  __{dict_id_address[i]}')
        problem_terminals.append(i)
    elif dict_id_district[i] == 'გლდანი-ნაძალადევი' and "Cash box" in dict_id_device_eror[i] and dict_id_Full[i] < 600:
        gldani_device_error.append(f'{str(i)}  {"Cash box removed"}  __{dict_id_address[i]}')
        problem_terminals.append(i)
    elif dict_id_district[i] == 'გლდანი-ნაძალადევი' and "Jammed" in dict_id_device_eror[i]:
        gldani_device_error.append(f'{str(i)}  {"Mei Jammed "}  __{dict_id_address[i]}')
        problem_terminals.append(i)
    elif dict_id_district[i] == 'გლდანი-ნაძალადევი' and "BILL_ACCEPTOR" in dict_id_device_eror[i]:
        gldani_device_error.append(f'{str(i)}  {"Mei Not Start "}  __{dict_id_address[i]}')
        problem_terminals.append(i)
    elif dict_id_district[i] == 'გლდანი-ნაძალადევი' and "COIN" in dict_id_device_eror[i]:
        gldani_device_error.append(f'{str(i)}  {"Coin Not Started"}  __{dict_id_address[i]}')
        problem_terminals.append(i)
    elif dict_id_district[i] == 'გლდანი-ნაძალადევი' and "error 14" in dict_id_device_eror[i]:
        gldani_device_error.append(f'{str(i)}  {"Coin error 14"}  __{dict_id_address[i]}')
        problem_terminals.append(i)
    elif dict_id_district[i] == 'გლდანი-ნაძალადევი' and "error 16" in dict_id_device_eror[i]:
        gldani_device_error.append(f'{str(i)}  {"Coin error 16"}  __{dict_id_address[i]}')
        problem_terminals.append(i)
    elif dict_id_district[i] == 'გლდანი-ნაძალადევი' and "registry" in dict_id_device_eror[i]:
        gldani_device_error.append(f'{str(i)}  {"Error registry file"}  __{dict_id_address[i]}')
        problem_terminals.append(i)
    elif dict_id_district[i] == 'გლდანი-ნაძალადევი' and "CashAcceptor" in dict_id_device_eror[i]:
        gldani_device_error.append(f'{str(i)}  {"CashAcceptor not  start"}  __{dict_id_address[i]}')
        problem_terminals.append(i)
    ###-----
    # --- გლდანი ტრანზაქციის ლოგიკა
    elif dict_id_district[i] == 'გლდანი-ნაძალადევი' and dict_id_categori[i] == 1 and dict_id_tr_time[i] > 720:
        gldani_trans.append(
            f'{str(i)} ({dict_id_categori[i]}) {Hourtominut(dict_id_tr_time[i])} __{dict_id_address[i]}')
    elif dict_id_district[i] == 'გლდანი-ნაძალადევი' and dict_id_categori[i] == 2 and dict_id_tr_time[i] > 780:
        gldani_trans.append(
            f'{str(i)} ({dict_id_categori[i]}) {Hourtominut(dict_id_tr_time[i])} __{dict_id_address[i]}')
    elif dict_id_district[i] == 'გლდანი-ნაძალადევი' and dict_id_categori[i] == 3 and dict_id_tr_time[i] > 780:
        gldani_trans.append(
            f'{str(i)} ({dict_id_categori[i]}) {Hourtominut(dict_id_tr_time[i])} __{dict_id_address[i]}')
    elif dict_id_district[i] == 'გლდანი-ნაძალადევი' and dict_id_categori[i] == 4 and i not in base_inside and \
            dict_id_tr_time[i] > 900:
        gldani_trans.append(
            f'{str(i)} ({dict_id_categori[i]}) {Hourtominut(dict_id_tr_time[i])} __{dict_id_address[i]}')
    elif dict_id_district[i] == 'გლდანი-ნაძალადევი' and dict_id_categori[i] == 5 and i not in base_inside and \
            dict_id_tr_time[i] > 1140:
        gldani_trans.append(
            f'{str(i)} ({dict_id_categori[i]}) {Hourtominut(dict_id_tr_time[i])} __{dict_id_address[i]}')

    # --- გლდანი მონეტის ლოგიკა
    elif dict_id_district[i] == 'გლდანი-ნაძალადევი' and dict_id_categori[i] == 1 and i not in base_inside and \
            dict_id_coin_time[i] > 720:
        gldani_coin.append(
            f'{str(i)} ({dict_id_categori[i]}) {Hourtominut(dict_id_coin_time[i])} __{dict_id_address[i]}')
    elif dict_id_district[i] == 'გლდანი-ნაძალადევი' and dict_id_categori[i] == 2 and i not in base_inside and \
            dict_id_coin_time[i] > 780:
        gldani_coin.append(
            f'{str(i)} ({dict_id_categori[i]}) {Hourtominut(dict_id_coin_time[i])} __{dict_id_address[i]}')
    elif dict_id_district[i] == 'გლდანი-ნაძალადევი' and dict_id_categori[i] == 3 and i not in base_inside and \
            dict_id_coin_time[i] > 780:
        gldani_coin.append(
            f'{str(i)} ({dict_id_categori[i]}) {Hourtominut(dict_id_coin_time[i])} __{dict_id_address[i]}')
    elif dict_id_district[i] == 'გლდანი-ნაძალადევი' and dict_id_categori[i] == 4 and i not in base_inside and \
            dict_id_coin_time[i] > 900:
        gldani_coin.append(
            f'{str(i)} ({dict_id_categori[i]}) {Hourtominut(dict_id_coin_time[i])} __{dict_id_address[i]}')
    elif dict_id_district[i] == 'გლდანი-ნაძალადევი' and dict_id_categori[i] == 5 and i not in base_inside and \
            dict_id_coin_time[i] > 1140:
        gldani_coin.append(
            f'{str(i)} ({dict_id_categori[i]}) {Hourtominut(dict_id_coin_time[i])} __{dict_id_address[i]}')

    # ---- გლდანი რფ-ის ლოგიკა >>>>:
    elif dict_id_district[i] == 'გლდანი-ნაძალადევი' and dict_id_categori[i] == 1 and i not in base_inside and \
            dict_id_card_time[i] > 720 and i not in rfnoneed:
        gldani_rf.append(f'{str(i)} ({dict_id_categori[i]}) {dict_id_card_time[i] // 60}-სთ {dict_id_address[i]} ')
    elif dict_id_district[i] == 'გლდანი-ნაძალადევი' and dict_id_categori[i] == 2 and i not in base_inside and \
            dict_id_card_time[i] > 780 and i not in rfnoneed:
        gldani_rf.append(f'{str(i)} ({dict_id_categori[i]}) {dict_id_card_time[i] // 60}-სთ {dict_id_address[i]} ')
    elif dict_id_district[i] == 'გლდანი-ნაძალადევი' and dict_id_categori[i] == 3 and i not in base_inside and \
            dict_id_card_time[i] > 780 and i not in rfnoneed:
        gldani_rf.append(f'{str(i)} ({dict_id_categori[i]}) {dict_id_card_time[i] // 60}-სთ {dict_id_address[i]} ')
    elif dict_id_district[i] == 'გლდანი-ნაძალადევი' and dict_id_categori[i] == 4 and i not in base_inside and \
            dict_id_card_time[i] > 900 and i not in rfnoneed:
        gldani_rf.append(f'{str(i)} ({dict_id_categori[i]}) {dict_id_card_time[i] // 60}-სთ {dict_id_address[i]} ')
    elif dict_id_district[i] == 'გლდანი-ნაძალადევი' and dict_id_categori[i] == 5 and i not in base_inside and \
            dict_id_card_time[i] > 1140 and i not in rfnoneed:
        gldani_rf.append(f'{str(i)} ({dict_id_categori[i]}) {dict_id_card_time[i] // 60}-სთ {dict_id_address[i]} ')

    # ----გლდანი პრინტერის ლოგიკა
    elif dict_id_district[i] == 'გლდანი-ნაძალადევი' and "Printer" in dict_id_device_eror[i]:
        gldani_printer.append(f'{str(i)}  {dict_id_address[i]}')
    elif dict_id_district[i] == 'გლდანი-ნაძალადევი' and dict_id_receipt[i] < 10:
        gldani_printer.append(f'{str(i)}  {dict_id_address[i]}')

    #################################-----<<<<    დიდუბის ლოგიკები  >>>>-----#######################################################

    # დიდუბე device error
    elif dict_id_district[i] == 'დიდუბე-ჩუღურეთი' and dict_id_sync_time[i] > 15:
        didube_sync.append(
            f"{str(i)}  ({dict_id_categori[i]}) {Hourtominut(dict_id_sync_time[i])} __{dict_id_address[i]}")
        problem_terminals.append(i)
    elif dict_id_district[i] == 'დიდუბე-ჩუღურეთი' and "Stacker" in dict_id_device_eror[i] and dict_id_Full[i] < 600:
        didube_device_error.append(f'{str(i)}  {"Stacker Full"}  __{dict_id_address[i]}')
        problem_terminals.append(i)
    elif dict_id_district[i] == 'დიდუბე-ჩუღურეთი' and "Cash box" in dict_id_device_eror[i] and dict_id_Full[i] < 600:
        didube_device_error.append(f'{str(i)}  {"Cash box removed"}  __{dict_id_address[i]}')
        problem_terminals.append(i)
    elif dict_id_district[i] == 'დიდუბე-ჩუღურეთი' and "Jammed" in dict_id_device_eror[i]:
        didube_device_error.append(f'{str(i)}  {"Mei Jammed "}  __{dict_id_address[i]}')
        problem_terminals.append(i)
    elif dict_id_district[i] == 'დიდუბე-ჩუღურეთი' and "BILL_ACCEPTOR" in dict_id_device_eror[i]:
        didube_device_error.append(f'{str(i)}  {"Mei Not Start "}  __{dict_id_address[i]}')
        problem_terminals.append(i)
    elif dict_id_district[i] == 'დიდუბე-ჩუღურეთი' and "COIN" in dict_id_device_eror[i]:
        didube_device_error.append(f'{str(i)}  {"Coin Not Started"}  __{dict_id_address[i]}')
        problem_terminals.append(i)
    elif dict_id_district[i] == 'დიდუბე-ჩუღურეთი' and "error 14" in dict_id_device_eror[i]:
        didube_device_error.append(f'{str(i)}  {"Coin error 14"}  __{dict_id_address[i]}')
        problem_terminals.append(i)
    elif dict_id_district[i] == 'დიდუბე-ჩუღურეთი' and "error 16" in dict_id_device_eror[i]:
        didube_device_error.append(f'{str(i)}  {"Coin error 16"}  __{dict_id_address[i]}')
        problem_terminals.append(i)
    elif dict_id_district[i] == 'დიდუბე-ჩუღურეთი' and "registry" in dict_id_device_eror[i]:
        didube_device_error.append(f'{str(i)}  {"Error registry file"}  __{dict_id_address[i]}')
        problem_terminals.append(i)
    elif dict_id_district[i] == 'დიდუბე-ჩუღურეთი' and "CashAcceptor" in dict_id_device_eror[i]:
        didube_device_error.append(f'{str(i)}  {"CashAcceptor not  start"}  __{dict_id_address[i]}')
        problem_terminals.append(i)
    # --- დიდუბე ტრანზაქციის ლოგიკა >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    elif dict_id_district[i] == 'დიდუბე-ჩუღურეთი' and dict_id_categori[i] == 1 and dict_id_tr_time[i] > 720:
        didube_trans.append(
            f'{str(i)} ({dict_id_categori[i]}) {Hourtominut(dict_id_tr_time[i])} __{dict_id_address[i]}')
    elif dict_id_district[i] == 'დიდუბე-ჩუღურეთი' and dict_id_categori[i] == 2 and dict_id_tr_time[i] > 780:
        didube_trans.append(
            f'{str(i)} ({dict_id_categori[i]}) {Hourtominut(dict_id_tr_time[i])} __{dict_id_address[i]}')
    elif dict_id_district[i] == 'დიდუბე-ჩუღურეთი' and dict_id_categori[i] == 3 and dict_id_tr_time[i] > 780:
        didube_trans.append(
            f'{str(i)} ({dict_id_categori[i]}) {Hourtominut(dict_id_tr_time[i])} __{dict_id_address[i]}')
    elif dict_id_district[i] == 'დიდუბე-ჩუღურეთი' and dict_id_categori[i] == 4 and i not in base_inside and \
            dict_id_tr_time[i] > 900:
        didube_trans.append(
            f'{str(i)} ({dict_id_categori[i]}) {Hourtominut(dict_id_tr_time[i])} __{dict_id_address[i]}')
    elif dict_id_district[i] == 'დიდუბე-ჩუღურეთი' and dict_id_categori[i] == 5 and i not in base_inside and \
            dict_id_tr_time[i] > 1140:
        didube_trans.append(
            f'{str(i)} ({dict_id_categori[i]}) {Hourtominut(dict_id_tr_time[i])} __{dict_id_address[i]}')
    # --- დიდუბე მონეტის ლოგიკა------------------------------------------------------------------------------------------------------
    elif dict_id_district[i] == 'დიდუბე-ჩუღურეთი' and dict_id_categori[i] == 1 and i not in base_inside and \
            dict_id_coin_time[i] > 720:
        didube_coin.append(
            f'{str(i)} ({dict_id_categori[i]}) {Hourtominut(dict_id_coin_time[i])} __{dict_id_address[i]}')
    elif dict_id_district[i] == 'დიდუბე-ჩუღურეთი' and dict_id_categori[i] == 2 and i not in base_inside and \
            dict_id_coin_time[i] > 780:
        didube_coin.append(
            f'{str(i)} ({dict_id_categori[i]}) {Hourtominut(dict_id_coin_time[i])} __{dict_id_address[i]}')
    elif dict_id_district[i] == 'დიდუბე-ჩუღურეთი' and dict_id_categori[i] == 3 and i not in base_inside and \
            dict_id_coin_time[i] > 780:
        didube_coin.append(
            f'{str(i)} ({dict_id_categori[i]}) {Hourtominut(dict_id_coin_time[i])} __{dict_id_address[i]}')
    elif dict_id_district[i] == 'დიდუბე-ჩუღურეთი' and dict_id_categori[i] == 4 and i not in base_inside and \
            dict_id_coin_time[i] > 900:
        didube_coin.append(
            f'{str(i)} ({dict_id_categori[i]}) {Hourtominut(dict_id_coin_time[i])} __{dict_id_address[i]}')
    elif dict_id_district[i] == 'დიდუბე-ჩუღურეთი' and dict_id_categori[i] == 5 and i not in base_inside and \
            dict_id_coin_time[i] > 1140:
        didube_coin.append(
            f'{str(i)} ({dict_id_categori[i]}) {Hourtominut(dict_id_coin_time[i])} __{dict_id_address[i]}')

    # ---- დიდუბე რფ-ის ლოგიკა >>>>:
    elif dict_id_district[i] == 'დიდუბე-ჩუღურეთი' and dict_id_categori[i] == 1 and i not in base_inside and \
            dict_id_card_time[i] > 720 and i not in rfnoneed:
        didube_rf.append(f'{str(i)} ({dict_id_categori[i]}) {dict_id_card_time[i] // 60}-სთ {dict_id_address[i]} ')
    elif dict_id_district[i] == 'დიდუბე-ჩუღურეთი' and dict_id_categori[i] == 2 and i not in base_inside and \
            dict_id_card_time[i] > 780 and i not in rfnoneed:
        didube_rf.append(f'{str(i)} ({dict_id_categori[i]}) {dict_id_card_time[i] // 60}-სთ {dict_id_address[i]} ')
    elif dict_id_district[i] == 'დიდუბე-ჩუღურეთი' and dict_id_categori[i] == 3 and i not in base_inside and \
            dict_id_card_time[i] > 780 and i not in rfnoneed:
        didube_rf.append(f'{str(i)} ({dict_id_categori[i]}) {dict_id_card_time[i] // 60}-სთ {dict_id_address[i]} ')
    elif dict_id_district[i] == 'დიდუბე-ჩუღურეთი' and dict_id_categori[i] == 4 and i not in base_inside and \
            dict_id_card_time[i] > 900 and i not in rfnoneed:
        didube_rf.append(f'{str(i)} ({dict_id_categori[i]}) {dict_id_card_time[i] // 60}-სთ {dict_id_address[i]} ')
    elif dict_id_district[i] == 'დიდუბე-ჩუღურეთი' and dict_id_categori[i] == 5 and i not in base_inside and \
            dict_id_card_time[i] > 1140 and i not in rfnoneed:
        didube_rf.append(f'{str(i)} ({dict_id_categori[i]}) {dict_id_card_time[i] // 60}-სთ {dict_id_address[i]} ')

    # ----დიდუბე პრინტერის ლოგიკა
    elif dict_id_district[i] == 'დიდუბე-ჩუღურეთი' and "Printer" in dict_id_device_eror[i]:
        didube_printer.append(f'{str(i)}  {dict_id_address[i]}')
    elif dict_id_district[i] == 'დიდუბე-ჩუღურეთი' and dict_id_receipt[i] < 10:
        didube_printer.append(f'{str(i)}  {dict_id_address[i]}')

    # ს ------- საბურთალო device eror
    elif dict_id_district[i] == 'საბურთალო' and dict_id_sync_time[i] > 15:
        saburtalo_sync.append(
            f"{str(i)}  ({dict_id_categori[i]}) {Hourtominut(dict_id_sync_time[i])} __{dict_id_address[i]}")
        problem_terminals.append(i)
    elif dict_id_district[i] == 'საბურთალო' and "Stacker" in dict_id_device_eror[i] and dict_id_Full[i] < 600:
        saburtalo_device_error.append(f'{str(i)}  {"Stacker Full"}  __{dict_id_address[i]}')
        problem_terminals.append(i)
    elif dict_id_district[i] == 'საბურთალო' and "Cash box" in dict_id_device_eror[i] and dict_id_Full[i] < 600:
        saburtalo_device_error.append(f'{str(i)}  {"Cash box removed"}  __{dict_id_address[i]}')
        problem_terminals.append(i)
    elif dict_id_district[i] == 'საბურთალო' and "Jammed" in dict_id_device_eror[i]:
        saburtalo_device_error.append(f'{str(i)}  {"Mei Jammed "}  __{dict_id_address[i]}')
        problem_terminals.append(i)
    elif dict_id_district[i] == 'საბურთალო' and "BILL_ACCEPTOR" in dict_id_device_eror[i]:
        saburtalo_device_error.append(f'{str(i)}  {"Mei Not Start "}  __{dict_id_address[i]}')
        problem_terminals.append(i)
    elif dict_id_district[i] == 'საბურთალო' and "COIN" in dict_id_device_eror[i]:
        saburtalo_device_error.append(f'{str(i)}  {"Coin Not Started"}  __{dict_id_address[i]}')
        problem_terminals.append(i)
    elif dict_id_district[i] == 'საბურთალო' and "error 14" in dict_id_device_eror[i]:
        saburtalo_device_error.append(f'{str(i)}  {"Coin error 14"}  __{dict_id_address[i]}')
        problem_terminals.append(i)
    elif dict_id_district[i] == 'საბურთალო' and "error 16" in dict_id_device_eror[i]:
        saburtalo_device_error.append(f'{str(i)}  {"Coin error 16"}  __{dict_id_address[i]}')
        problem_terminals.append(i)
    elif dict_id_district[i] == 'საბურთალო' and "registry" in dict_id_device_eror[i]:
        saburtalo_device_error.append(f'{str(i)}  {"Error registry file"}  __{dict_id_address[i]}')
        problem_terminals.append(i)
    elif dict_id_district[i] == 'საბურთალო' and "CashAcceptor" in dict_id_device_eror[i]:
        saburtalo_device_error.append(f'{str(i)}  {"CashAcceptor not  start"}  __{dict_id_address[i]}')
        problem_terminals.append(i)


    # --- საბურთალო ტრანზაქციის ლოგიკა
    elif dict_id_district[i] == 'საბურთალო' and dict_id_categori[i] == 1 and dict_id_tr_time[
        i] > 720 and i not in rfnoneed:
        saburtalo_trans.append(
            f'{str(i)} ({dict_id_categori[i]}) {Hourtominut(dict_id_tr_time[i])} __{dict_id_address[i]}')
    elif dict_id_district[i] == 'საბურთალო' and dict_id_categori[i] == 2 and dict_id_tr_time[
        i] > 780 and i not in rfnoneed:
        saburtalo_trans.append(
            f'{str(i)} ({dict_id_categori[i]}) {Hourtominut(dict_id_tr_time[i])} __{dict_id_address[i]}')
    elif dict_id_district[i] == 'საბურთალო' and dict_id_categori[i] == 3 and dict_id_tr_time[
        i] > 780 and i not in rfnoneed:
        saburtalo_trans.append(
            f'{str(i)} ({dict_id_categori[i]}) {Hourtominut(dict_id_tr_time[i])} __{dict_id_address[i]}')
    elif dict_id_district[i] == 'საბურთალო' and dict_id_categori[i] == 4 and i not in base_inside and dict_id_tr_time[
        i] > 900 and i not in rfnoneed:
        saburtalo_trans.append(
            f'{str(i)} ({dict_id_categori[i]}) {Hourtominut(dict_id_tr_time[i])} __{dict_id_address[i]}')
    elif dict_id_district[i] == 'საბურთალო' and dict_id_categori[i] == 5 and i not in base_inside and dict_id_tr_time[
        i] > 1140 and i not in rfnoneed:
        saburtalo_trans.append(
            f'{str(i)} ({dict_id_categori[i]}) {Hourtominut(dict_id_tr_time[i])} __{dict_id_address[i]}')

    # --- საბურთალო მონეტის ლოგიკა
    elif dict_id_district[i] == 'საბურთალო' and dict_id_categori[i] == 1 and i not in base_inside and dict_id_coin_time[
        i] > 720:
        saburtalo_coin.append(
            f'{str(i)} ({dict_id_categori[i]}) {Hourtominut(dict_id_coin_time[i])} __{dict_id_address[i]}')
    elif dict_id_district[i] == 'საბურთალო' and dict_id_categori[i] == 2 and i not in base_inside and dict_id_coin_time[
        i] > 780:
        saburtalo_coin.append(
            f'{str(i)} ({dict_id_categori[i]}) {Hourtominut(dict_id_coin_time[i])} __{dict_id_address[i]}')
    elif dict_id_district[i] == 'საბურთალო' and dict_id_categori[i] == 3 and i not in base_inside and dict_id_coin_time[
        i] > 780:
        saburtalo_coin.append(
            f'{str(i)} ({dict_id_categori[i]}) {Hourtominut(dict_id_coin_time[i])} __{dict_id_address[i]}')
    elif dict_id_district[i] == 'საბურთალო' and dict_id_categori[i] == 4 and i not in base_inside and dict_id_coin_time[
        i] > 900:
        saburtalo_coin.append(
            f'{str(i)} ({dict_id_categori[i]}) {Hourtominut(dict_id_coin_time[i])} __{dict_id_address[i]}')
    elif dict_id_district[i] == 'საბურთალო' and dict_id_categori[i] == 5 and i not in base_inside and dict_id_coin_time[
        i] > 1140:
        saburtalo_coin.append(
            f'{str(i)} ({dict_id_categori[i]}) {Hourtominut(dict_id_coin_time[i])} __{dict_id_address[i]}')

    # ---- საბურთალო რფ-ის ლოგიკა >>>>:
    elif dict_id_district[i] == 'საბურთალო' and dict_id_categori[i] == 1 and i not in base_inside and dict_id_card_time[
        i] > 720 and i not in rfnoneed:
        saburtalo_rf.append(f'{str(i)} ({dict_id_categori[i]}) {dict_id_card_time[i] // 60}-სთ {dict_id_address[i]} ')
    elif dict_id_district[i] == 'საბურთალო' and dict_id_categori[i] == 2 and i not in base_inside and dict_id_card_time[
        i] > 780 and i not in rfnoneed:
        saburtalo_rf.append(f'{str(i)} ({dict_id_categori[i]}) {dict_id_card_time[i] // 60}-სთ {dict_id_address[i]} ')
    elif dict_id_district[i] == 'საბურთალო' and dict_id_categori[i] == 3 and i not in base_inside and dict_id_card_time[
        i] > 780 and i not in rfnoneed:
        saburtalo_rf.append(f'{str(i)} ({dict_id_categori[i]}) {dict_id_card_time[i] // 60}-სთ {dict_id_address[i]} ')
    elif dict_id_district[i] == 'საბურთალო' and dict_id_categori[i] == 4 and i not in base_inside and dict_id_card_time[
        i] > 900 and i not in rfnoneed:
        saburtalo_rf.append(f'{str(i)} ({dict_id_categori[i]}) {dict_id_card_time[i] // 60}-სთ {dict_id_address[i]} ')
    elif dict_id_district[i] == 'საბურთალო' and dict_id_categori[i] == 5 and i not in base_inside and dict_id_card_time[
        i] > 1140 and i not in rfnoneed:
        saburtalo_rf.append(f'{str(i)} ({dict_id_categori[i]}) {dict_id_card_time[i] // 60}-სთ {dict_id_address[i]} ')

    # ----საბურთალო პრინტერის ლოგიკა
    elif dict_id_district[i] == 'საბურთალო' and "Printer" in dict_id_device_eror[i]:
        saburtalo_printer.append(f'{str(i)}  {dict_id_address[i]}')
    elif dict_id_district[i] == 'საბურთალო' and dict_id_receipt[i] < 10:
        saburtalo_printer.append(f'{str(i)}  {dict_id_address[i]}')

    # ----------------------------------------------------------------------------------------------------------------
    # ვაკე-ვერა-მთაწმინა device error

    elif dict_id_district[i] == 'ვაკე-ვერა-მთაწმინდა' and dict_id_sync_time[i] > 15:
        vake_sync.append(
            f"{str(i)}  ({dict_id_categori[i]}) {Hourtominut(dict_id_sync_time[i])} __{dict_id_address[i]}")
        problem_terminals.append(i)

    elif dict_id_district[i] == 'ვაკე-ვერა-მთაწმინდა' and "Stacker" in dict_id_device_eror[i] and dict_id_Full[i] < 600:
        vake_device_error.append(f'{str(i)}  {"Stacker Full"}  __{dict_id_address[i]}')
        problem_terminals.append(i)
    elif dict_id_district[i] == 'ვაკე-ვერა-მთაწმინდა' and "Cash box" in dict_id_device_eror[i] and dict_id_Full[
        i] < 600:
        vake_device_error.append(f'{str(i)}  {"Cash box removed"}  __{dict_id_address[i]}')
        problem_terminals.append(i)
    elif dict_id_district[i] == 'ვაკე-ვერა-მთაწმინდა' and "Jammed" in dict_id_device_eror[i]:
        vake_device_error.append(f'{str(i)}  {"Mei Jammed "}  __{dict_id_address[i]}')
        problem_terminals.append(i)
    elif dict_id_district[i] == 'ვაკე-ვერა-მთაწმინდა' and "BILL_ACCEPTOR" in dict_id_device_eror[i]:
        vake_device_error.append(f'{str(i)}  {"Mei Not Start "}  __{dict_id_address[i]}')
        problem_terminals.append(i)
    elif dict_id_district[i] == 'ვაკე-ვერა-მთაწმინდა' and "COIN" in dict_id_device_eror[i]:
        vake_device_error.append(f'{str(i)}  {"Coin Not Started"}  __{dict_id_address[i]}')
        problem_terminals.append(i)
    elif dict_id_district[i] == 'ვაკე-ვერა-მთაწმინდა' and "error 14" in dict_id_device_eror[i]:
        vake_device_error.append(f'{str(i)}  {"Coin error 14"}  __{dict_id_address[i]}')
        problem_terminals.append(i)
    elif dict_id_district[i] == 'ვაკე-ვერა-მთაწმინდა' and "error 16" in dict_id_device_eror[i]:
        vake_device_error.append(f'{str(i)}  {"Coin error 16"}  __{dict_id_address[i]}')
        problem_terminals.append(i)
    elif dict_id_district[i] == 'ვაკე-ვერა-მთაწმინდა' and "registry" in dict_id_device_eror[i]:
        vake_device_error.append(f'{str(i)}  {"Error registry file"}  __{dict_id_address[i]}')
        problem_terminals.append(i)
    elif dict_id_district[i] == 'ვაკე-ვერა-მთაწმინდა' and "CashAcceptor" in dict_id_device_eror[i]:
        vake_device_error.append(f'{str(i)}  {"CashAcceptor not  start"}  __{dict_id_address[i]}')
        problem_terminals.append(i)

    # --- ვაკე-ვერა-მთაწმინა ტრანზაქციის ლოგიკა
    elif dict_id_district[i] == 'ვაკე-ვერა-მთაწმინდა' and dict_id_categori[i] == 1 and dict_id_tr_time[i] > 720:
        vake_trans.append(f'{str(i)} ({dict_id_categori[i]}) {Hourtominut(dict_id_tr_time[i])} __{dict_id_address[i]}')
    elif dict_id_district[i] == 'ვაკე-ვერა-მთაწმინდა' and dict_id_categori[i] == 2 and dict_id_tr_time[i] > 780:
        vake_trans.append(f'{str(i)} ({dict_id_categori[i]}) {Hourtominut(dict_id_tr_time[i])} __{dict_id_address[i]}')
    elif dict_id_district[i] == 'ვაკე-ვერა-მთაწმინდა' and dict_id_categori[i] == 3 and dict_id_tr_time[i] > 780:
        vake_trans.append(f'{str(i)} ({dict_id_categori[i]}) {Hourtominut(dict_id_tr_time[i])} __{dict_id_address[i]}')
    elif dict_id_district[i] == 'ვაკე-ვერა-მთაწმინდა' and dict_id_categori[i] == 4 and i not in base_inside and \
            dict_id_tr_time[i] > 900:
        vake_trans.append(f'{str(i)} ({dict_id_categori[i]}) {Hourtominut(dict_id_tr_time[i])} __{dict_id_address[i]}')
    elif dict_id_district[i] == 'ვაკე-ვერა-მთაწმინდა' and dict_id_categori[i] == 5 and i not in base_inside and \
            dict_id_tr_time[i] > 1140:
        vake_trans.append(f'{str(i)} ({dict_id_categori[i]}) {Hourtominut(dict_id_tr_time[i])} __{dict_id_address[i]}')

    # --- ვაკე-ვერა-მთაწმინა მონეტის ლოგიკა
    elif dict_id_district[i] == 'ვაკე-ვერა-მთაწმინდა' and dict_id_categori[i] == 1 and i not in base_inside and \
            dict_id_coin_time[i] > 720:
        vake_coin.append(f'{str(i)} ({dict_id_categori[i]}) {Hourtominut(dict_id_coin_time[i])} __{dict_id_address[i]}')
    elif dict_id_district[i] == 'ვაკე-ვერა-მთაწმინდა' and dict_id_categori[i] == 2 and i not in base_inside and \
            dict_id_coin_time[i] > 780:
        vake_coin.append(f'{str(i)} ({dict_id_categori[i]}) {Hourtominut(dict_id_coin_time[i])} __{dict_id_address[i]}')
    elif dict_id_district[i] == 'ვაკე-ვერა-მთაწმინდა' and dict_id_categori[i] == 3 and i not in base_inside and \
            dict_id_coin_time[i] > 780:
        vake_coin.append(f'{str(i)} ({dict_id_categori[i]}) {Hourtominut(dict_id_coin_time[i])} __{dict_id_address[i]}')
    elif dict_id_district[i] == 'ვაკე-ვერა-მთაწმინდა' and dict_id_categori[i] == 4 and i not in base_inside and \
            dict_id_coin_time[i] > 900:
        vake_coin.append(f'{str(i)} ({dict_id_categori[i]}) {Hourtominut(dict_id_coin_time[i])} __{dict_id_address[i]}')
    elif dict_id_district[i] == 'ვაკე-ვერა-მთაწმინდა' and dict_id_categori[i] == 5 and i not in base_inside and \
            dict_id_coin_time[i] > 1140:
        vake_coin.append(f'{str(i)} ({dict_id_categori[i]}) {Hourtominut(dict_id_coin_time[i])} __{dict_id_address[i]}')

    # ---- ვაკე-ვერა-მთაწმინა რფ-ის ლოგიკა >>>>:
    elif dict_id_district[i] == 'ვაკე-ვერა-მთაწმინდა' and dict_id_categori[i] == 1 and i not in base_inside and \
            dict_id_card_time[i] > 720 and i not in rfnoneed:
        vake_rf.append(f'{str(i)} ({dict_id_categori[i]}) {dict_id_card_time[i] // 60}-სთ {dict_id_address[i]} ')
    elif dict_id_district[i] == 'ვაკე-ვერა-მთაწმინდა' and dict_id_categori[i] == 2 and i not in base_inside and \
            dict_id_card_time[i] > 780 and i not in rfnoneed:
        vake_rf.append(f'{str(i)} ({dict_id_categori[i]}) {dict_id_card_time[i] // 60}-სთ {dict_id_address[i]} ')
    elif dict_id_district[i] == 'ვაკე-ვერა-მთაწმინდა' and dict_id_categori[i] == 3 and i not in base_inside and \
            dict_id_card_time[i] > 780 and i not in rfnoneed:
        vake_rf.append(f'{str(i)} ({dict_id_categori[i]}) {dict_id_card_time[i] // 60}-სთ {dict_id_address[i]} ')
    elif dict_id_district[i] == 'ვაკე-ვერა-მთაწმინდა' and dict_id_categori[i] == 4 and i not in base_inside and \
            dict_id_card_time[i] > 900 and i not in rfnoneed:
        vake_rf.append(f'{str(i)} ({dict_id_categori[i]}) {dict_id_card_time[i] // 60}-სთ {dict_id_address[i]} ')
    elif dict_id_district[i] == 'ვაკე-ვერა-მთაწმინდა' and dict_id_categori[i] == 5 and i not in base_inside and \
            dict_id_card_time[i] > 1140 and i not in rfnoneed:
        vake_rf.append(f'{str(i)} ({dict_id_categori[i]}) {dict_id_card_time[i] // 60}-სთ {dict_id_address[i]} ')

    # ----ვაკე-ვერა-მთაწმინა პრინტერის ლოგიკა
    elif dict_id_district[i] == 'ვაკე-ვერა-მთაწმინდა' and "Printer" in dict_id_device_eror[i]:
        vake_printer.append(f'{str(i)}  {dict_id_address[i]}')
    elif dict_id_district[i] == 'ვაკე-ვერა-მთაწმინდა' and dict_id_receipt[i] < 10:
        vake_printer.append(f'{str(i)}  {dict_id_address[i]}')

    # ისანი-სამგორი device error

    elif dict_id_district[i] == 'ისანი-სამგორი' and dict_id_sync_time[i] > 15:
        isani_sync.append(
            f"{str(i)}  ({dict_id_categori[i]}) {Hourtominut(dict_id_sync_time[i])} __{dict_id_address[i]}")

    elif dict_id_district[i] == 'ისანი-სამგორი' and "Stacker" in dict_id_device_eror[i] and dict_id_Full[i] < 600:
        isani_device_error.append(f'{str(i)}  {"Stacker Full"}  __{dict_id_address[i]}')
    elif dict_id_district[i] == 'ისანი-სამგორი' and "Cash box" in dict_id_device_eror[i] and dict_id_Full[i] < 600:
        isani_device_error.append(f'{str(i)}  {"Cash box removed"}  __{dict_id_address[i]}')
    elif dict_id_district[i] == 'ისანი-სამგორი' and "Jammed" in dict_id_device_eror[i]:
        isani_device_error.append(f'{str(i)}  {"Mei Jammed "}  __{dict_id_address[i]}')
    elif dict_id_district[i] == 'ისანი-სამგორი' and "BILL_ACCEPTOR" in dict_id_device_eror[i]:
        isani_device_error.append(f'{str(i)}  {"Mei Not Start "}  __{dict_id_address[i]}')
    elif dict_id_district[i] == 'ისანი-სამგორი' and "COIN" in dict_id_device_eror[i]:
        isani_device_error.append(f'{str(i)}  {"Coin Not Started"}  __{dict_id_address[i]}')
    elif dict_id_district[i] == 'ისანი-სამგორი' and "error 14" in dict_id_device_eror[i]:
        isani_device_error.append(f'{str(i)}  {"Coin error 14"}  __{dict_id_address[i]}')
    elif dict_id_district[i] == 'ისანი-სამგორი' and "error 16" in dict_id_device_eror[i]:
        isani_device_error.append(f'{str(i)}  {"Coin error 16"}  __{dict_id_address[i]}')
    elif dict_id_district[i] == 'ისანი-სამგორი' and "registry" in dict_id_device_eror[i]:
        isani_device_error.append(f'{str(i)}  {"Error registry file"}  __{dict_id_address[i]}')
    elif dict_id_district[i] == 'ისანი-სამგორი' and "CashAcceptor" in dict_id_device_eror[i]:
        isani_device_error.append(f'{str(i)}  {"CashAcceptor not  start"}  __{dict_id_address[i]}')

    # --- ისანი-სამგორი ტრანზაქციის ლოგიკა
    elif dict_id_district[i] == 'ისანი-სამგორი' and dict_id_categori[i] == 1 and dict_id_tr_time[i] > 720:
        isani_trans.append(f'{str(i)} ({dict_id_categori[i]}) {Hourtominut(dict_id_tr_time[i])} __{dict_id_address[i]}')
        problem_terminals.append(i)
    elif dict_id_district[i] == 'ისანი-სამგორი' and dict_id_categori[i] == 2 and dict_id_tr_time[i] > 780:
        isani_trans.append(f'{str(i)} ({dict_id_categori[i]}) {Hourtominut(dict_id_tr_time[i])} __{dict_id_address[i]}')
        problem_terminals.append(i)
    elif dict_id_district[i] == 'ისანი-სამგორი' and dict_id_categori[i] == 3 and dict_id_tr_time[i] > 780:
        isani_trans.append(f'{str(i)} ({dict_id_categori[i]}) {Hourtominut(dict_id_tr_time[i])} __{dict_id_address[i]}')
        problem_terminals.append(i)
    elif dict_id_district[i] == 'ისანი-სამგორი' and dict_id_categori[i] == 4 and i not in base_inside and \
            dict_id_tr_time[i] > 900:
        isani_trans.append(f'{str(i)} ({dict_id_categori[i]}) {Hourtominut(dict_id_tr_time[i])} __{dict_id_address[i]}')
        problem_terminals.append(i)
    elif dict_id_district[i] == 'ისანი-სამგორი' and dict_id_categori[i] == 5 and i not in base_inside and \
            dict_id_tr_time[i] > 1140:
        isani_trans.append(f'{str(i)} ({dict_id_categori[i]}) {Hourtominut(dict_id_tr_time[i])} __{dict_id_address[i]}')
        problem_terminals.append(i)

    # --- ისანი-სამგორი მონეტის ლოგიკა
    elif dict_id_district[i] == 'ისანი-სამგორი' and dict_id_categori[i] == 1 and i not in base_inside and \
            dict_id_coin_time[i] > 720:
        isani_coin.append(
            f'{str(i)} ({dict_id_categori[i]}) {Hourtominut(dict_id_coin_time[i])} __{dict_id_address[i]}')
    elif dict_id_district[i] == 'ისანი-სამგორი' and dict_id_categori[i] == 2 and i not in base_inside and \
            dict_id_coin_time[i] > 780:
        isani_coin.append(
            f'{str(i)} ({dict_id_categori[i]}) {Hourtominut(dict_id_coin_time[i])} __{dict_id_address[i]}')
    elif dict_id_district[i] == 'ისანი-სამგორი' and dict_id_categori[i] == 3 and i not in base_inside and \
            dict_id_coin_time[i] > 780:
        isani_coin.append(
            f'{str(i)} ({dict_id_categori[i]}) {Hourtominut(dict_id_coin_time[i])} __{dict_id_address[i]}')
    elif dict_id_district[i] == 'ისანი-სამგორი' and dict_id_categori[i] == 4 and i not in base_inside and \
            dict_id_coin_time[i] > 900:
        isani_coin.append(
            f'{str(i)} ({dict_id_categori[i]}) {Hourtominut(dict_id_coin_time[i])} __{dict_id_address[i]}')
    elif dict_id_district[i] == 'ისანი-სამგორი' and dict_id_categori[i] == 5 and i not in base_inside and \
            dict_id_coin_time[i] > 1140:
        isani_coin.append(
            f'{str(i)} ({dict_id_categori[i]}) {Hourtominut(dict_id_coin_time[i])} __{dict_id_address[i]}')

    # ---- ისანი-სამგორი რფ-ის ლოგიკა >>>>:
    elif dict_id_district[i] == 'ისანი-სამგორი' and dict_id_categori[i] == 1 and i not in base_inside and \
            dict_id_card_time[i] > 720 and i not in rfnoneed:
        isani_rf.append(f'{str(i)} ({dict_id_categori[i]}) {dict_id_card_time[i] // 60}-სთ {dict_id_address[i]} ')
    elif dict_id_district[i] == 'ისანი-სამგორი' and dict_id_categori[i] == 2 and i not in base_inside and \
            dict_id_card_time[i] > 780 and i not in rfnoneed:
        isani_rf.append(f'{str(i)} ({dict_id_categori[i]}) {dict_id_card_time[i] // 60}-სთ {dict_id_address[i]} ')
    elif dict_id_district[i] == 'ისანი-სამგორი' and dict_id_categori[i] == 3 and i not in base_inside and \
            dict_id_card_time[i] > 780 and i not in rfnoneed:
        isani_rf.append(f'{str(i)} ({dict_id_categori[i]}) {dict_id_card_time[i] // 60}-სთ {dict_id_address[i]} ')
    elif dict_id_district[i] == 'ისანი-სამგორი' and dict_id_categori[i] == 4 and i not in base_inside and \
            dict_id_card_time[i] > 900 and i not in rfnoneed:
        isani_rf.append(f'{str(i)} ({dict_id_categori[i]}) {dict_id_card_time[i] // 60}-სთ {dict_id_address[i]} ')
    elif dict_id_district[i] == 'ისანი-სამგორი' and dict_id_categori[i] == 5 and i not in base_inside and \
            dict_id_card_time[i] > 1140 and i not in rfnoneed:
        isani_rf.append(f'{str(i)} ({dict_id_categori[i]}) {dict_id_card_time[i] // 60}-სთ {dict_id_address[i]} ')

    # ----ისანი-სამგორი პრინტერის ლოგიკა
    elif dict_id_district[i] == 'ისანი-სამგორი' and "Printer" in dict_id_device_eror[i]:
        isani_printer.append(f'{str(i)}  {dict_id_address[i]}')
    elif dict_id_district[i] == 'ისანი-სამგორი' and dict_id_receipt[i] < 10:
        isani_printer.append(f'{str(i)}  {dict_id_address[i]}')
#
# gldani = []
# for i in(terminal_ID):
#
#
#
#
#
# print("გლდანის ერეფის პრობლემები:",*gldani, sep = "\n")

#
# #len------------------------------
# print("time len", len(tr_time))
# print("dict id tr len",len(dict_id_tr_time))
# print("terminal id",len(terminal_ID))
# print('category',len(category))
# print("dict id category", len(dict_id_categori))
# print(len(device_eror))
# print(len(receipt))
# print(len(sync_time))
# print(len(coin_time))
# print(len(bill_time))
# print(len(card_time))
# print(len(address))
# print(len(district))
#
#
# #dicts---------------------------
# print(dict_id_tr_time)
# print(dict_id_categori)
# print(dict(zip(terminal_ID,device_eror)))
# print(dict_id_receipt)
# print(dict_id_sync_time)
# print(dict_id_coin_time)
# print(dict_id_bill_time)
# print(dict_id_card_time)
# print(dict_id_address)
# print(dict_id_district)

# ----------------------------------
# print(terminal_ID)
# print(tr_time)
# print(category)
# print(device_eror)
# print(sync_time)
# print(coin_time)
# print(bill_time)
# print(card_time)
# print(address)
# print(district)
# print(base_inside)


# ==============================================================================
isani_summ = len(isani_sync) + len(isani_device_error) + len(isani_trans) + len(isani_bill) + len(isani_coin) + len(
    isani_rf) + len(isani_printer)

vake_summ = len(vake_sync) + len(vake_device_error) + len(vake_trans) + len(vake_bill) + len(vake_coin) + len(
    vake_rf) + len(vake_rf) + len(vake_printer)

saburtalo_summ = len(saburtalo_sync) + len(saburtalo_device_error) + len(saburtalo_trans) + len(saburtalo_bill) + len(
    saburtalo_coin) + len(saburtalo_rf) + len(saburtalo_printer)

didube_summ = len(didube_sync) + len(didube_device_error) + len(didube_trans) + len(didube_bill) + len(
    didube_coin) + len(didube_rf) + len(didube_printer)

gldani_summ = len(gldani_sync) + len(gldani_device_error) + len(gldani_trans) + len(gldani_bill) + len(
    gldani_coin) + len(gldani_rf) + len(gldani_printer)
tbilisi_summ = gldani_summ + didube_summ + saburtalo_summ + vake_summ + isani_summ

print("""

""")
print("თბილისი - პრობლემების საერთო რაოდენობა: ", tbilisi_summ)
print("_______________________________________________________")
print("\n""გლდანი-ნაძალადევი - ", gldani_summ)
print("დიდუბე-ჩუღურეთი - ", didube_summ)
print("საბურთალო - ", saburtalo_summ)
print("ვაკე-ვერა-მთაწმინდა - ", vake_summ)
print("ისანი-სამგორი - ", isani_summ)
print("_______________________________________________________")

print("""

""")

# ==============================================================================

#
print("\n""\n""@<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< გლდანი-ნაძალადევი >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>@")
#
if len(gldani_sync) > 0:
    print("\n""კავშირის პრობლემა:", *gldani_sync, sep="\n")
if len(gldani_device_error) > 0:
    print("\n""მოწყობილობის შეცდომა:", *gldani_device_error, sep="\n")
if len(gldani_trans) > 0:
    print("\n""ტრანზაქციის პობლემა:", *gldani_trans, sep="\n")
if len(gldani_coin) > 0:
    print("\n""მონეტის პრობლემა:", *gldani_coin, sep="\n")
if len(gldani_rf) > 0:
    print("\n""RF-ის პრობლემა:", *gldani_rf, sep="\n")
if len(gldani_printer) > 0:
    print("\n""პრინტერის პრობლემა:", *gldani_printer, sep="\n")

print("\n""\n""\n""@<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<დიდუბე ჩუღურეთი>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>@")

if len(didube_sync) > 0:
    print("\n""კავშირის პრობლემა:", *didube_sync, sep="\n")
if len(didube_device_error) > 0:
    print("\n""მოწყობილობის შეცდომა:", *didube_device_error, sep="\n")
if len(didube_trans) > 0:
    print("\n""ტრანზაქციის პობლემა:", *didube_trans, sep="\n")
if len(didube_coin) > 0:
    print("\n""მონეტის პრობლემა:", *didube_coin, sep="\n")
if len(didube_rf) > 0:
    print("\n""RF-ის პრობლემა:", *didube_rf, sep="\n")
if len(didube_printer) > 0:
    print("\n""პრინტერის პრობლემა:", *didube_printer, sep="\n")

print("\n""\n""\n""@<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<საბურთალო>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>@")

if len(saburtalo_sync) > 0:
    print("\n""კავშირის პრობლემა:", *saburtalo_sync, sep="\n")
if len(saburtalo_device_error) > 0:
    print("\n""მოწყობილობის შეცდომა:", *saburtalo_device_error, sep="\n")
if len(saburtalo_trans) > 0:
    print("\n""ტრანზაქციის პობლემა:", *saburtalo_trans, sep="\n")
if len(saburtalo_coin) > 0:
    print("\n""მონეტის პრობლემა:", *saburtalo_coin, sep="\n")
if len(saburtalo_rf) > 0:
    print("\n""RF-ის პრობლემა:", *saburtalo_rf, sep="\n")
if len(saburtalo_printer) > 0:
    print("\n""პრინტერის პრობლემა:", *saburtalo_printer, sep="\n")

print("\n""\n""\n""@<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< ვაკე-ვერა-მთაწმინა>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>@")

if len(vake_sync) > 0:
    print("\n""კავშირის პრობლემა:", *vake_sync, sep="\n")
if len(vake_device_error) > 0:
    print("\n""მოწყობილობის შეცდომა:", *vake_device_error, sep="\n")
if len(vake_trans) > 0:
    print("\n""ტრანზაქციის პობლემა:", *vake_trans, sep="\n")
if len(vake_coin) > 0:
    print("\n""მონეტის პრობლემა:", *vake_coin, sep="\n")
if len(vake_rf) > 0:
    print("\n""RF-ის პრობლემა:", *vake_rf, sep="\n")
if len(vake_printer) > 0:
    print("\n""პრინტერის პრობლემა:", *vake_printer, sep="\n")

print("\n""\n""\n""@<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< ისანი-სამგორი >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>@")

if len(isani_sync) > 0:
    print("\n""კავშირის პრობლემა:", *isani_sync, sep="\n")
if len(isani_device_error) > 0:
    print("\n""მოწყობილობის შეცდომა:", *isani_device_error, sep="\n")
if len(isani_trans) > 0:
    print("\n""ტრანზაქციის პობლემა:", *isani_trans, sep="\n")
if len(isani_coin) > 0:
    print("\n""მონეტის პრობლემა:", *isani_coin, sep="\n")
if len(isani_rf) > 0:
    print("\n""RF-ის პრობლემა:", *isani_rf, sep="\n")
if len(isani_printer) > 0:
    print("\n""პრინტერის პრობლემა:", *isani_printer, sep="\n")

# =======================================================================
print("\n")
print("\n")
print("\n")

for i in problem_terminals:
    print(f"putty.exe -ssh kiosk@{dict_id_IPadress[i]} -pw 123 -m C:\\Users\\gkupreishvili\\Desktop\\t7.txt -t")



# ======================================================================
# isani_sync = []
# isani_device_error = []
# isani_trans = []
# isani_bill = []
# isani_coin = []
# isani_rf = []
# isani_printer = []

#
# gldani_sync = []
# gldani_device_error = []
# gldani_trans = []
# gldani_bill = []
# gldani_coin = []
# gldani_rf = []
# gldani_printer = []

# saburtalo_sync = []
# saburtalo_device_error = []
# saburtalo_trans = []
# saburtalo_bill = []
# saburtalo_coin = []
# saburtalo_rf = []
# saburtalo_printer = []
#
# vake_sync = []
# vake_device_error = []
# vake_trans = []
# vake_bill = []
# vake_coin = []
# vake_rf = []
# vake_printer = []


# didube_sync = []
#device_eror = []
# didube_trans = []
# didube_bill = []
# didube_coin = []
# didube_rf = []
# didube_printer = []



