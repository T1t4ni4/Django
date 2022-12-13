from django.shortcuts import render
from dashboard.forms import FormBarang
from .models import Barang 
# Create your views here

def tambah_barang(request):
    form=FormBarang()
    konteks={
        'form':form,
    }
    return render(request,'tambah_barang.html',konteks)

def produk(request):
    titelnya="Produk"
    konteks = {
        'titel':titelnya,
    }
    return render(request,'jualan.html',konteks)

def Barang_View(request):
    barangs=Barang.objects.all()

    konteks={
        'barangs':barangs,
    }
    return render(request,'tampil_brg.html',konteks)

