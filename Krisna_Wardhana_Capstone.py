mobil = [
    {
        'plat' : 'B1234ZFN',
        'model' : 'honda HRV',
        'tahun' : '2014',
        'warna' : 'putih',
        'ketersediaan' : 'tersedia'
    },
    {
        'plat' : 'B3621EOH',
        'model' : 'toyota raize',
        'tahun' : '2021',
        'warna' : 'hitam',
        'ketersediaan' : 'tersedia',
    },
    {
        'plat' : 'B5824ESA',
        'model' : 'suzuki baleno',
        'tahun' : '2019',
        'warna' : 'merah',
        'ketersediaan' : 'tersedia'
    }
]

def menu_utama():
    print("SELAMAT DATANG DI APLIKASI LIST MOBIL RENTAL\n\nMenu:")
    print("1. menampilkan list mobil rental")
    print("2. menambah mobil rental")
    print("3. mengupdate mobil rental")
    print("4. menghapus mobil rental")
    print("5. keluar")

def menu_1():
    print("\n--------------------MENU 1--------------------\n")
    print("1. menampilkan semua list mobil rental")
    print("2. menampilkan mobil berdasarkan nomor plat")
    print("3. keluar")

def menu_2():
    print("\n--------------------MENU 2--------------------\n")
    print("1. menambahkan list mobil")
    print("2. keluar")

def menu_3():
    print("\n--------------------MENU 3--------------------\n")
    print("1. mengubah data mobil")
    print("2. keluar")

def menu_4():
    print("\n--------------------MENU 4--------------------\n")
    print("1. menghapus data mobil")
    print("2. keluar")

def list_mobil(mobil):
    print("PLAT\t\t|JENIS MOBIL\t|TAHUN\t|WARNA\t|KETERSEDIAAN")
    for i in range(len(mobil)):
        print(f"{mobil[i]['plat']}\t|{mobil[i]['model']}\t|{mobil[i]['tahun']}\t|{mobil[i]['warna']}\t|{mobil[i]['ketersediaan']}\t")

def pilih_menu():
    pilih = int(input("masukkan pilihan anda : "))
    return pilih

def sub_menu_1_2():
    pilih = (input("\ncari mobil dengan memasukkan plat nomor : "))
    pilih = pilih.upper()   
    cek_plat = []
    for i in range(len(mobil)):
        cek_plat.append(mobil[i]['plat'])
    if pilih in cek_plat:
        index_pilih = cek_plat.index(pilih)
        print("\ndata ditemukan!\n")
        print("\nPLAT\t\t|JENIS MOBIL\t|TAHUN\t|WARNA\t|KETERSEDIAAN")
        print(f"{mobil[index_pilih]['plat']}\t|{mobil[index_pilih]['model']}\t|{mobil[index_pilih]['tahun']}\t|{mobil[index_pilih]['warna']}\t|{mobil[index_pilih]['ketersediaan']}")   
    else:
        print("data nomor plat yang anda masukkan tidak ada pada sistem!")
    
def tambah_mobil(mobil):
    list_mobil(mobil)
    plat = input("masukkan nomor plat mobil : ")
    plat = plat.upper()
    for i in range(len(mobil)):
        if plat == mobil[i]['plat']:
            print("nomor plat yang anda masukkan sudah ada dalam data!")
            break
        else:
            model = input("masukkan model mobil : ")
            model = model.lower()
            tahun = int(input("masukkan tahun mobil : "))
            warna = input("masukkan warna mobil : ")
            warna = warna.lower()
            konfirmasi = int(input("\napakah anda yakin ingin menambahkan data ini?\n1. YES\n2. NO\n"))
            if konfirmasi == 1:
                mobil.append(
                    {
                        'plat' : plat,
                        'model' : model,
                        'tahun' : tahun,
                        'warna' : warna,
                        'ketersediaan' : 'tersedia'
                    }
                )
                print("\ndata berhasil ditambahkan!\n")
                list_mobil(mobil)
                break
            elif konfirmasi == 2:
                print("penambahan data dibatalkan")
                break
            else:
                print("pilihan anda tidak ada dalam opsi")
    return
                
def update():
    pilih = (input("\nmasukkan nomor plat mobil yang ingin diubah : "))
    pilih = pilih.upper()   
    cek_plat = []
    for i in range(len(mobil)):
        cek_plat.append(mobil[i]['plat'])
    if pilih in cek_plat:
        index_pilih = cek_plat.index(pilih)
        print("\nPLAT\t\t|JENIS MOBIL\t|TAHUN\t|WARNA\t|KETERSEDIAAN")
        print(f"{mobil[index_pilih]['plat']}\t|{mobil[index_pilih]['model']}\t|{mobil[index_pilih]['tahun']}\t|{mobil[index_pilih]['warna']}\t|{mobil[index_pilih]['ketersediaan']}")
        konfirmasi = int(input("\napakah anda yakin ingin melanjutkan update data ini?\n1. YES\n2. NO\n"))
        if konfirmasi == 1:
            print("\n1. mengubah nomor plat mobil")
            print("2. mengubah model mobil")
            print("3. mengubah tahun mobil")
            print("4. mengubah warna mobil")
            pilih_kolom = int(input("\npilih kolom data yang akan diubah : "))
            while True:
                if pilih_kolom == 1:
                    plat = input("masukkan nomor plat baru mobil : ")
                    plat = plat.upper()
                    konfirmasi = int(input("\napakah anda yakin ingin mengubah data ini?\n1. YES\n2. NO\n"))
                    if konfirmasi == 1:
                        mobil[index_pilih]['plat'] = plat
                        print("data telah berhasil diubah!")
                        break
                    elif konfirmasi == 2:
                        print("\nperubahan data dibatalkan!")
                        break
                    else:
                        print("\npilihan anda tidak ada dalam opsi")
                        break                   
                elif pilih_kolom == 2:
                    model = input("masukkan model baru mobil : ")
                    konfirmasi = int(input("\napakah anda yakin ingin mengubah data ini?\n1. YES\n2. NO\n"))
                    if konfirmasi == 1:
                        mobil[index_pilih]['model'] = model
                        print("data telah berhasil diubah!")
                        break
                    elif konfirmasi == 2:
                        print("\nperubahan data dibatalkan!")
                        break
                    else:
                        print("\npilihan anda tidak ada dalam opsi")
                        break                    
                elif pilih_kolom == 3:
                    tahun = input("masukkan tahun baru mobil : ")
                    konfirmasi = int(input("\napakah anda yakin ingin mengubah data ini?\n1. YES\n2. NO\n"))
                    if konfirmasi == 1:
                        mobil[index_pilih]['tahun'] = tahun
                        print("data telah berhasil diubah!")
                        break
                    elif konfirmasi == 2:
                        print("\nperubahan data dibatalkan!")
                        break
                    else:
                        print("\npilihan anda tidak ada dalam opsi")
                        break                    
                elif pilih_kolom == 4:
                    warna = input("masukkan warna baru mobil : ")
                    konfirmasi = int(input("\napakah anda yakin ingin mengubah data ini?\n1. YES\n2. NO\n"))
                    if konfirmasi == 1:
                        mobil[index_pilih]['warna'] = warna
                        print("data telah berhasil diubah!")
                        break
                    elif konfirmasi == 2:
                        print("\nperubahan data dibatalkan!")
                        break
                    else:
                        print("\npilihan anda tidak ada dalam opsi")
                        break                    
                else:
                    print("pilihan anda tidak ada dalam opsi")
                    continue
                    
        elif konfirmasi == 2:
            print("penambahan data dibatalkan")
            
        else:
            print("pilihan anda tidak ada dalam opsi")
    else:
        print("data nomor plat yang anda masukkan tidak ada pada sistem!")
    return

def hapus():
    pilih = (input("\nmasukkan nomor plat mobil yang ingin dihapus : "))
    pilih = pilih.upper()   
    cek_plat = []
    for i in range(len(mobil)):
        cek_plat.append(mobil[i]['plat'])
    if pilih in cek_plat:
        index_pilih = cek_plat.index(pilih)
        print("\nPLAT\t\t|JENIS MOBIL\t|TAHUN\t|WARNA\t|KETERSEDIAAN")
        print(f"{mobil[index_pilih]['plat']}\t|{mobil[index_pilih]['model']}\t|{mobil[index_pilih]['tahun']}\t|{mobil[index_pilih]['warna']}\t|{mobil[index_pilih]['ketersediaan']}")
        #PROGRAM
        konfirmasi = int(input("\napakah anda yakin ingin menghapus data ini?\n1. YES\n2. NO\n"))
        if konfirmasi == 1:
            del mobil[index_pilih]
            print("\nmobil berhasil dihapus!\n")
            list_mobil(mobil)
    else:
        print("\ndata nomor plat yang anda masukkan tidak ada pada sistem!\n")

while True:
    menu_utama()
    pilih = int(input("\npilih menu yang akan dijalankan : "))

    if pilih == 1:
        while True:
            menu_1()
            pilih = pilih_menu()
            if pilih == 1:
                while True:
                    list_mobil(mobil)
                    break
            elif pilih == 2:
                while True:
                    sub_menu_1_2()
                    break
            elif pilih == 3:
                konfirmasi = int(input("apakah yakin ingin keluar?\n1. ya\n2. tidak\n"))
                if konfirmasi == 1:
                    break
                elif konfirmasi == 2:
                    continue
                else:
                    print("menu yang dipilih tidak ada, silahkan masukkan nomor menu dengan benar!")
                    continue
            else:
                print("menu yang dipilih tidak ada, silahkan masukkan nomor menu dengan benar!")
                continue
    
    elif pilih == 2:
        while True:
            menu_2()
            pilih = pilih_menu()
            if pilih == 1:
                while True:
                    tambah_mobil(mobil)
                    break
            elif pilih == 2:
                konfirmasi = int(input("apakah yakin ingin keluar?\n1. ya\n2. tidak\n"))
                if konfirmasi == 1:
                    break
                elif konfirmasi == 2:
                    continue
                else:
                    print("menu yang dipilih tidak ada, silahkan masukkan nomor menu dengan benar!")
                    continue
            else:
                print("menu yang dipilih tidak ada, silahkan masukkan nomor menu dengan benar!")
                continue

    elif pilih == 3:
        while True:
            menu_3()
            pilih = pilih_menu()
            if pilih == 1:
                while True:
                    update()
                    break
            elif pilih == 2:
                konfirmasi = int(input("apakah yakin ingin keluar?\n1. ya\n2. tidak\n"))
                if konfirmasi == 1:
                    break
                elif konfirmasi == 2:
                    continue
                else:
                    print("menu yang dipilih tidak ada, silahkan masukkan nomor menu dengan benar!")
                    continue
            else:
                print("menu yang dipilih tidak ada, silahkan masukkan nomor menu dengan benar!")
                continue

    elif pilih == 4:
        while True:
            menu_4()
            pilih = pilih_menu()
            if pilih == 1:
                while True:
                    hapus()
                    break
            elif pilih == 2:
                konfirmasi = int(input("apakah yakin ingin keluar?\n1. ya\n2. tidak\n"))
                if konfirmasi == 1:
                    break
                elif konfirmasi == 2:
                    continue
                else:
                    print("menu yang dipilih tidak ada, silahkan masukkan nomor menu dengan benar!")
                    continue
            else:
                print("menu yang dipilih tidak ada, silahkan masukkan nomor menu dengan benar!")
                continue

    elif pilih == 5:
        break

    else:
        print("menu yang dipilih tidak ada, silahkan masukkan nomor menu dengan benar!\n")
        continue

##--------------------------------------------SELESAI-------------------------------------------


            




        
        
               

                

