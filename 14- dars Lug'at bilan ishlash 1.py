#car_0 = {'model': 'ferrari', 'rang': 'qizil'}
#print(car_0['model'])
#print(car_0['rang'])

#en_uz = {'apple':'olma', 'apricot':"o'rik", 'banana':'banan'}
#print(en_uz['apple'])
#mevalar = {'olma':10000, 'tarvuz':9000, 'banan':21000}
#print(mevalar['banan'])
#talaba_0 = {'ism':'olim murodov', 'yosh':20, 't_yil':2000}
#print(f"{talaba_0['ism'].title()},\
     #{talaba_0['t_yil']}-yilda tug'ulgan,\
        # {talaba_0['yosh']} yoshda")
#talaba_0['fakultet'] = 'pedagogika'
#talaba_1 = {}
#talaba_1['ism'] = 'Abdullah'
#talaba_1['yosh'] = 20
#talaba_1['kurs'] = 3
#print(talaba_1)
#print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kursda")
#talaba_1['kurs'] = 4
#print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kursda")
#talaba_0 = {'ism':'olim murodov', 'yosh':20, 't_yil':2000}
#del talaba_0['yosh']
#talaba_0['yosh'] = 20
telefonlar = {  
   'ali': 'iphone 13 pro max',
    'valisher': 'samsung s 21 ultra',
    'sherbek': 'mi 11 pro',
    'jonibek': 'nokia 6233'
    }
phone = telefonlar.get("hasan", 'Bunday ism mavjud emas')
print(phone)