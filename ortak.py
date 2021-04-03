
def fiyat_temizle(formatli_fiyat):
    # noktalama işaretli, sonunda TL olan fiyatı temizleme
    bosluk_yeri = formatli_fiyat.find(' ')

    fiyat = formatli_fiyat[:bosluk_yeri]

    # 1.255.256,94

    nokta_yeri = fiyat.find(".")

    while nokta_yeri >= 0:
        fiyat = fiyat[0:nokta_yeri] + fiyat[nokta_yeri + 1:]

        # 1255.256,94

        nokta_yeri = fiyat.find(".")

    # 1255256,94

    # float'a çevirirken virgüllü sayı kabul etmez.
    # python da ondalık işareti nokta
    # virgül varsa noktaya çeviriyoruz.
    fiyat = fiyat.replace(",", ".")

    fiyat = float(fiyat)
    return fiyat
