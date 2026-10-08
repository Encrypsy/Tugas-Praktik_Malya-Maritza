from django.shortcuts import render
import json
from pathlib import Path

# Create your views here.
def home(request):
    jenis_barang = [
        'Buku',
        'Pulpen',
        'Pensil',
        'Penghapus'
    ]
    
    jenis_barang.sort()
    
    context = {
        'jenis_barang' : jenis_barang
    }
    
    if request.method == 'POST':
        nama = request.POST.get('nama')
        no_hp = request.POST.get('no_hp')
        barang = request.POST.get('barang')
        jumlah = int(request.POST.get('jumlah'))
        
        def total_tagihan(harga, jumlah):
            total = harga * jumlah
            
            if total > 50000:
                return total - (total * 0.1)
            elif total <= 50000:
                return total
        
        if barang == 'Buku':
            harga = 5000
        elif barang == 'Pulpen':
            harga = 3000
        elif barang == 'Pensil':
            harga = 2000
        elif barang == 'Penghapus':
            harga = 1500
            
        total_harga = total_tagihan(
            harga,
            jumlah
        )
        
        data_pesanan = {
            'nama' : nama,
            'no_hp' : no_hp,
            'barang' : barang,
            'jumlah' : jumlah,
            'total_harga' : total_harga
        }
        
        # inisialisasi variabel tempat folder untuk menyimpan data
        data_dir = Path('data')
                
        # inisialisasi variabel file data.json
        data_file = data_dir / 'data.json'
                
        # mengambil data yang lama
        if data_file.exists():
            # jika file tersebut mempunyai data, sistem akan membaca nya
            with open(data_file, 'r') as file:
                # data yang lama akan dibaca menggunakan function laod()
                # dan data tersebut akan di simpan kedalam variabel 'data'
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    data = []
        else:
            # jika file tersebut tidak mempunyai data, maka akan disimpan ke dalam list kosong
            data = []
                
        # tambahkan data baru ke dalam file data.json
        data.append(data_pesanan)
                
        # object python (data_pesanan) akan disimpan dalam bentuk JSON
        with open(data_file, 'w') as file:
            json.dump(data, file, indent=4)
            
        context.update({
            'nama' : nama,
            'no_hp' : no_hp,
            'barang' : barang,
            'jumlah' : jumlah,
            'total_harga' : total_harga
        })
    
    return render(request, 'base.html', context)