def umur_nya (umur) :
    if umur <=2 :
        print("maka dia bayi")
    elif umur <=5 :
        print("maka dia balita")
    elif umur <=12 :
        print("maka dia anak_anak")
    elif umur <=17 :
        print("maka dia remaja")
    elif umur >17 and umur <=30 :
        print("maka dia dewasa")
    else:
        print("maka dia orangtua", umur >=30)

print(umur_nya(40))