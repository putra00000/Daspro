def Reverse_kata(kalimat): #membuat function untuk reverse per kata
    kata_list = kalimat.split() #kata_list merupakan string dari kalimat yang di split
    return ' '.join([kata [::-1] for kata in kata_list]) #disini setiap kata yang ada di index string yang sudah di split akan di balikan

def urut_kata(kalimat, urutan): #membuat function urutan kalimat
    kata_list = kalimat.split() #kata_list merupakan string dari kalimat yang di split
    return ' '.join([kata_list[i - 1] for i in urutan]) #membuat string baru sesuai dengan urutan yang sudah di berikan dan digabung kembali menjadi string

def ganti_vokal(kalimat, opsi): #membuat function ganti_vokal
    vokalkecil = {'a':'4','i':'1','u':'|_|','e':'3','o':'0'} #vocal kecil yang ada pada list diuabh ke simbol
    vokalbesar = {'A':'4','I':'1','U':'|_|','E':'3','O':'0'} #vocal besar yang ada pada list diubah ke simbol
    hasil = ''#hasil nya sama dengan kosong (karena nanti akan diisi oleh vokal yang di ganti)
    for huruf in kalimat: #untuk huruf dalam kalimat
        if opsi == 1 and huruf in vokalkecil: #jika opsi 1 dan huruf berada di dalam vokalkecil
            hasil += vokalkecil[huruf] #hasil diisi oleh huruf vokalkecil yang sudah diganti
        elif opsi == 2 and huruf in vokalbesar: #jika memilih opsi 2 dan huruf ada di dalam vokalbesar
            hasil += vokalbesar[huruf] #hasil diisi oleh huruf vokalbesar yang sudah diganti
        else: #jika semua opsi tidak dipilih atau tidak ada
            hasil += huruf #maka hasil nya tetap kata dari huruf yang di data
    return hasil #kembali ke hasi

print("Ini adalah output perintah langsung menggunakan print() atau HARDCODE")
print("1. Ubah kata 'AKU CINTA KAMU'")
#print memanggil function Reverse_kata untuk mengubah kalimat "AKU CINTA KAMU" 
print(Reverse_kata("AKU CINTA KAMU")) 
print("2. Urutkan kata 'HARI INI SEDANG BELAJAR PYTHON'")
#print dan memanggil function urut_kata untuk ngeprint hasil susunan kalimat dari kalimat "HARI INI SEDANG BELAJAR PYTHON"
print(urut_kata("HARI INI SEDANG BELAJAR PYTHON", [5,1,4,3,2]))  
print("3. ganti huruf fokal kecil dari kata ""Aku Cinta Kamu")
#mengprint dna mengganti huruf vokalkecil dengan opsi pertama
print(ganti_vokal ("Aku Cinta Kamu", 1))
print("4. ganti huruf vokal besar dari kata" "Aku Cinta Kamu")
#mengprint dan mengganti huruf vokalbesar dengan opsi 2
print(ganti_vokal ("Aku Cinta Kamu", 2))