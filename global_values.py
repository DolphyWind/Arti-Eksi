from PyQt5 import QtGui

title_font = QtGui.QFont("Roboto", 36)
normal_font = QtGui.QFont("Segoe UI", 16)
information_font = QtGui.QFont("Segoe UI", 12)
guess_font = QtGui.QFont("Roboto", 18)
windowSize = (300, 400)
mbs = (180, 60)     # Stands for minimum button size
howToPlayStr = "Artı eksi oyunu iki kişi ile oynanır. Bir taraf 4 basamaklı bir\n" \
               "sayı tutar, diğer taraf ise bunu bulmaya çalışır. Sayıyı tutan\n" \
               "oyuncu tutmayana bazı ipuçları verir. Bu ipuçları şu şekildedir:\n" \
               "Eğer tutulan sayı içerisinde tahmin edilen sayının rakamlarından\n" \
               "biri varsa ve aynı basamaklarda iseler artı, farklı basamaklarda\n" \
               "iseler eksi değeri artar. Örneğin tutulan sayı 7168, tahmin edilen\n" \
               "sayı ise 1728 olsun. 1 ve 7 her iki sayıda olduğundan ve farklı\n" \
               "basamaklarda olduklarından, 8 ise hem her iki sayıda hem de aynı\n" \
               "basamakta olduklarından -2 ve +1 ipucu olarak verilecektir."
# howToPlayStr = "Artı eksi oyunu iki kişi ile oynanır. Bir taraf 4 basamaklı bir sayı tutar,\n" \
#                "diğer taraf ise bunu bulmaya çalışır. Sayıyı tutan oyuncu tutmayana bazı ipuçları verir.\n" \
#                "Bu ipuçları şu şekildedir: Eğer tutulan sayı içerisinde tahmin edilen sayının rakamlarından\n" \
#                "biri varsa ve aynı basamaktalarsa artı, farklı basamaklarda iseler eksi değeri artar. Örneğin\n" \
#                "tutulan sayı 7168, tahmin edilen sayı ise 1728 olsun. 1 ve 7 her iki sayıda olduğundan ve farklı\n" \
#                "basamaklarda olduklarından, 8 ise hem her iki sayıda hem de aynı basamakta olduklarından -2 ve +1\n" \
#                "ipucu olarak verilecektir."
