#car0 = {
  #      'model':'lacetti',
  #      'rang':'oq',
  #      'yil':2019,
  #      'narh':13000,
  #      'masofa':50000,
   #     'karobka':'avtomat'
  #      }

#car1 = {
  #      'model':'Nexia',
  #      'rang':'qora',
  #      'yil':2011,
  #      'narh':9000,
  #      'masofa':89000,
   #     'karobka':'mexanika'
   #     }

#car2 = {
 #       'model':'gentra',
  #      'rang':'qizil',
   #     'yil':2021,
    #    'narh':12000,
     #   'masofa':95000,
      #  'karobka':'avtomat'
#}
#car = car2
#print(f"{car['model'].title()},\
  #{car['rang']} rang,\
  #{car['masofa']} masofa,\
 # {car['yil']}-yil, {car['narh']}$")
#cars = [car0, car1, car2]
#for car in cars:
#    print(f"{car['model'].title()},\
 #     {car['rang']} rang,\
  #    {car['masofa']} masofa,\
 #     {car['yil']}-yil, {car['narh']}$")
#print(f"{cars[2]['rang'].title()} "
 #     f"{cars[2]['model']}" )

#malibus=[]
#for n in range(10):
#    new_car = {
#        'model':'malibu',
#        'rang':None,
#        'yil':2022,
#        'narh':None,
#        'km':0,
#        'karobka':'avto'
#        }
#    malibus.append(new_car)
#for malibu in malibus[:3]:
#    malibu['rang']='qizil'
#    
      
#for malibu in malibus[3:6]:
#    malibu['rang']='qora'
    
#for malibu in malibus[6:]:
#        malibu['rang']='qora'
#        malibu["karobka"]="avtomat"
       # for malibu in malibus:
        #    print(malibu)
#for malibu in malibus:
#    if malibu['karobka']=='avto':
#        malibu['narh']=40000
#    else:
#        malibu['narh']=35000
#for malibu in malibus:
#     print(malibu)
            
            
#dasturchilar = {
#    'ali':['python','c++'],
#    'vali':['html','css','js'],
#    'hasan':['php','sql'],
#    'husan':['python','php'],
#    'maryam':['c++','c#']
#    }
#for ism, tillar in dasturchilar.items():
#    print(f"\n{ism.title()} quydagi dasturlash tillarini biladi:")
#    for til in tillar:
 #       print(til.upper())
 #       
 #       for ism, tillar in dasturchilar.items():
 #           print(f"\n{ism.title()} quydagi dasturlash tillarini biladi:")
 #           for til in tillar:
 #               print(f'{til.upper()} ', end='')
#hamkasblar = {
#    'ali':{'familiya':'valiyev',
#           'tyil':1995,
#           'malumot':'oliy',
#           'tillar':['python','c++']
#           },
#    'vali':{'familiya':'aliyev',
#            'tyil':2001,
#            'malumot':"o'rta-maxsus",
#           'tillar':['html', 'css', 'js']},
#    'hasan':{'familiya':'husanov',
 #            'tyil':1999,
#             'malumot':'maxsus',
#             'tillar':['python','php']}
#    }
#for ism, info in hamkasblar.items():
#    print(f"\n{ism.title()} {info['familiya'].title()}, "
#          f"{info['tyil']}-yilda tug'ulgan "
#         f"Ma'lumoti: {info['malumot']}. \n"
#          "Quyidagi dasturlash tillarini biladi:")    
#    for tillar in info['tillar']:
#        print(tillar.upper())
buxoriy = {
    "ism": "Abu Abdulloh Muhammad ibn Ismoil",
    "tyil": 810,
    "vyil": 870,
    "tjoy": "Buxoro",
}

qodiriy = {"ism": "Abdulla Qodiriy", "tyil": 1894, "vyil": 1938, "tjoy": "Toshkent"}

vohidov = {"ism": "Erkin Vohidov", "tyil": 1936, "vyil": 2016, "tjoy": "Farg'ona"}

navoiy = {"ism": "Alisher Navoiy", "tyil": 1441, "vyil": 1501, "tjoy": "Xirot"}

shaxslar = [buxoriy, qodiriy, vohidov, navoiy]

for shaxs in shaxslar:
    ism = shaxs["ism"]
    tyil = shaxs["tyil"]
    vyil = shaxs["vyil"]
    tjoy = shaxs["tjoy"]
    print(
        f"{ism} {tyil}-yilda {tjoy}da tavallud topgan. " f"{vyil-tyil} yil umr ko'rgan."
    )
    
kinolar = {
    "ali": ["Terminator", "Rambo", "Titanic"],
    "vali": ["Tenet", "Inception", "Interstellar"],
    "hasan": ["Abdullajon", "Bomba", "Shaytanat"],
    "husan": ["Mahallada duv-duv gap", "John Wick"],
    }
for ism, kinolar in kinolar.items():
    print(f"\n{ism.title()}ning sevimli kinolari:")
    for kino in kinolar:
        print(kino)
      