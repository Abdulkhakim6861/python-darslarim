# -*- coding: utf-8 -*-
"""
Created on Tue May 17 22:27:01 2022

@author: hp
"""

#print("yaqin do'stlaringiz ro'yxatini tuzamiz")
#smlar = []
#n=1
#while True:
 #   savol = f"{n}-do'stingizni ismini kiriting:"
 #   ism = input(savol)
  #  ismlar.append(ism)
  #  takrorlash = input("Yana  ism qo'shasizmi ha/yo'q:")
  #  n+=1
  #  if takrorlash != 'ha':
   #     break
    #
#print("Do'stlaringizni ro'yxati:")
#or ism in ismlar:
 #   print(ism.title())

#print("yaqin dostlaringiz yoshini saqlaymiz")
#dostlar = {}
#ishora = True
#while ishora:
#    ism = input("dostingiz ismini kiriting:")
#    yosh = input(f"{ism.title()}ning yoshini kiriting:")
#    dostlar [ism] = int(yosh)
#    
#    javob = input("Yana malumot qo'shasizmi? (ha/yo'q)")
#    if javob == "yo'q":
#        ishora = False
#for ism, yosh in dostlar.items():
 # print(f"{ism.title()} {yosh} yoshda")  
#cars = ['lacetti', 'nexia', 'jentra', 'malibu', 'nexia', 'audi', 'mers', 'nexia']
#while "nexia" in cars:
#         cars.remove('nexia')
#         print(cars)
talabalar = ['hasan', 'husan', 'ali', 'olim', 'jamol']
baholangan_talabalar = {}
while talabalar:
    talaba = talabalar.pop()
    baho = input(f"{talaba.title()} ning bahosini kiriting: ")
    print(f"{talaba.title()} baholandi")   
    baholangan_talabalar[talaba] = int(baho)

