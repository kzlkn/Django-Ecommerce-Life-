from .sepet import Sepet

def sepet(request):# para
    # parametre request olaca
    
    
    sepet = Sepet(request)
    # sepet nesnesi request prametresi ile
    # olusturulmus
    #rerurn et sepeti bize sepeti
    return {'sepet': sepet}

#bütün templates boyunca uygun olacak