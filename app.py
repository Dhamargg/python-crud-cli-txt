import os

t_pegawai = './database/t_pegawai.txt'

list_jk = [
    'Laki-laki',
    'Perempuan'
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def back_to_menu():
    print("\n")
    input("Tekan Enter untuk kembali...")
    show_menu()

def get_data(file_path):
    try:
        with open(file_path, 'r') as file:
            data = []
            for line in file:
                data.append(line.strip().split(','))
        return data
    except FileNotFoundError:
        return []
    
def set_data(file_path, data):
    with open(file_path, 'w') as file:
        for item in data:
            file.write(','.join(item) + '\n')

def sort_asc(arr, index):
    try:
        for i in range(len(arr) - 1):
            for j in range(len(arr) - 1 - i):
                if arr[j][index] > arr[j + 1][index]:
                    temp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1]=temp

        return arr
    except ValueError:
        return arr

def show_pegawai():
    file_path = t_pegawai
    data = sort_asc(get_data(file_path),0)
    
    header = ['ID','NAMA','JK']
    print(f"{header[0]:<3} {header[1]:<30} {header[2]}")
    print("-"*50)
    if (len(data) > 0):
        no = 1
        for row in data:
            print(f"{no:<3} {row[0]:<30} {row[1]}")
            no+=1
    else:
        print("Tidak ada data!")

def add_pegawai():
    print("Tambah Data Pegawai")
    file_path = t_pegawai
    data = sort_asc(get_data(file_path),0)
    nama = input('Masukan Nama: ')
    print('Pilih Jenis Kelamin: ')
    print(f"1. {list_jk[0]}")
    print(f"2. {list_jk[1]}")
    jk = int(input('Masukan Jenis Kelamin: '))-1
    if jk == 0 or jk == 1:
        data.append([nama,list_jk[jk]])
        set_data(file_path, data)
    else:
        print('\n')
        print("gagal menambah data")
        print("harap pilih sesuai pilihan yang tersedia!")

def update_pegawai():
    show_pegawai()
    file_path = t_pegawai
    data = sort_asc(get_data(file_path),0)
    if(len(data) > 0):
        print("Edit Data Pegawai")
        index = (int(input('Masukan ID : '))-1)
        if len(data[index]) >= 0:
            data[index][0] = input('Masukan Nama: ')
            print('Pilih Jenis Kelamin: ')
            print(f"1. {list_jk[0]}")
            print(f"2. {list_jk[1]}")
            jk = int(input('Masukan Jenis Kelamin: '))-1
            if jk == 0 or jk == 1:
                data[index][1] = list_jk[jk]
                set_data(file_path, data)
            else:
                print('\n')
                print("gagal menambah data")
                print("harap pilih sesuai pilihan yang tersedia!")
        else:
            print('id tidak ditemukan')
    else:
        print("gagal ubah data")

def delete_pegawai():
    show_pegawai()
    file_path = t_pegawai
    data = sort_asc(get_data(file_path),0)
    if(len(data) > 0):
        print("Hapus Data Pegawai")
        index = (int(input('Masukan ID : '))-1)
        if len(data[index]) >= 0 and data[index]:
            data.remove(data[index])
            set_data(file_path, data)
            print(f"berhasil menghapus data")
        else:
            print('id tidak ditemukan')
    else:
        print("gagal menghapus data")
    
def search_pegawai():
    show_pegawai()
    file_path = t_pegawai
    data = sort_asc(get_data(file_path),0)
    if(len(data) > 0):
        nama = input('Masukan Nama : ')
        header = ['ID','NAMA','JK']
        print(f"{header[0]:<3} {header[1]:<30} {header[2]}")
        print("-"*50)
        no = 1
        for row in data:
            if row[0] == nama or nama in row[0]:
                print(f"{no:<3} {row[0]:<30} {row[1]}")
                no+=1
            elif len(data) == no :
                print('data tidak ditemukan')
    else:
        print("tidak ada data!")

def show_menu():
    clear_screen()
    print("=== Aplikasi Pegawai ===")
    print("[1] Lihat Data Pegawai")
    print("[2] Tambah Data Pegawai")
    print("[3] Edit Data Pegawai")
    print("[4] Hapus Data Pegawai")
    print("[5] Cari Data Pegawai")
    print("[0] Exit")
    print("------------------------")
    selected_menu = input("Pilih menu> ")
    if selected_menu == '1' :
        clear_screen()
        show_pegawai()
        back_to_menu()
    elif selected_menu == '2':
        clear_screen()
        add_pegawai()
        back_to_menu()
    elif selected_menu == '3':
        clear_screen()
        update_pegawai()
        back_to_menu()
    elif selected_menu == '4':
        clear_screen()
        delete_pegawai()
        back_to_menu()
    elif selected_menu == '5':
        clear_screen()
        search_pegawai()
        back_to_menu()
    elif(selected_menu == "0"):
        exit()

show_menu()