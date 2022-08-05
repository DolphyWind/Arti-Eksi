from PyQt5 import QtGui

title_font = QtGui.QFont("Roboto", 36)
normal_font = QtGui.QFont("Segoe UI", 16)
information_font = QtGui.QFont("Segoe UI", 12)
guess_font = QtGui.QFont("Roboto", 18)
windowSize = (300, 400)
mbs = (180, 60)     # Stands for minimum button size
howToPlayStr = "Artı eksi oyunu iki kişi ile oynanır. Bir taraf 4 basamaklı rakamları farklı bir\n" \
               "sayı tutar, diğer taraf ise bunu bulmaya çalışır. Sayıyı tutan oyuncu tutmayan\n" \
               "oyuncuya bazı ipuçları verir. Bu ipuçları şu şekildedir: Eğer tutulan sayı\n" \
               "içerisinde tahmin edilen sayının rakamlarından biri varsa ve aynı basamaklarda\n" \
               "iseler artı, farklı basamaklarda iseler eksi değeri artar. Örneğin tutulan sayı\n" \
               "7168, tahmin edilen sayı ise 1728 olsun. 1 ve 7 her iki sayıda olduğundan ve de farklı\n" \
               "basamaklarda olduklarından, 8 ise hem her iki sayıda hem de aynı basamakta\n" \
               "olduklarından -2 ve +1 ipucu olarak verilecektir."
