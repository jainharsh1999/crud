from django.shortcuts import render

# Create your views here.
def register(requset):
    if requset.method == 'POST':
        Username=requset.post.get('username')
        Email=requset.post.get('Email')
        city=requset.post.get('city')
        address=requset.post.get('address')
        pincode=requset.post.get('pincode')
        Password=requset.post.get('Password')
        
        
        log=customer(name=Username, Email=Email, city=city, address=address, pincode=pincode, Password=Password)
        
        log.save()
    
        return render(requset, register.html)