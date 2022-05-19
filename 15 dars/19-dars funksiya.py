# -*- coding: utf-8 -*-
"""
Created on Wed May 18 13:01:48 2022

@author: hp
"""

#def salom_ber ():
 #   """Salom beruvchi funksiya"""
  #  print("Assalamu alaykum!")

#salom_ber()
#
#def salom_ber(ism):
#    """Foydalanuvchini ismini qabul qilib,
 #   unga salom beruvchi funksiya"""
  #  print(f"Assalamu alaykum, hurmatli {ism.title()}!")
    
#salom_ber('hasan')
#salom_ber('olim')
#def toliq_ism(ism, familiya):
 #   """Fo'\ydalanuvchini ism va familiyasini jamlab chaqiruvchi funksiya"""
#   print(f"Foydalanuvchi ismi: {ism.title()} \n "
#          f"Foydalanuvchi familiyasi: {familiya.title()}")
#toliq_ism('olim', 'hakimov')
#toliq_ism('hakimov', 'olim')

#def yosh_hisobla(ism, tugilgan_yil):
#    """Foydalanuvchini yoshini hisoblaydigan dastur"""
#    print(f"{ism.title()} {2022-tugilgan_yil} yoshda ")
#yosh_hisobla(ism='olim',tugilgan_yil=1997)


def yosh_hisobla(tugilgan_yil, joriy_yil=2020):
    """Foydalanuvchi tugilgan yilidan uni yoshi hisoblaydi"""
    print(f"siz {joriy_yil-tugilgan_yil} yoshdasiz")
yosh_hisobla(1995,2020)
yosh_hisobla(1993)