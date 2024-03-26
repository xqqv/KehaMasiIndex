try:
    print("Tere!")
    
   
    nimi = input("Palun, sisesta oma nimi: ")
    
   
    print(nimi + ", oi kui ilus nimi!")
    
    
    vastus = int(input(nimi + "! Kas leian Sinu keha indeksi? 0-ei, 1-jah "))
    
    if vastus == 1:
      
        pikkus = int(input("Sisesta oma pikkus (cm): "))
        mass = float(input("Sisesta oma mass (kg): "))
        
       
        indeks = mass / ((0.01 * pikkus) ** 2)
        
    
        print(nimi + "! Sinu keha indeks on: {:.1f}".format(indeks))
        
     
        if indeks < 16:
            print("Tervisele ohtlik alakaal")
        elif 16 <= indeks < 19:
            print("Alakaal")
        elif 19 <= indeks < 25:
            print("Normaalkaal")
        elif 25 <= indeks < 30:
            print("Ülekaal")
        elif 30 <= indeks < 35:
            print("Rasvumine")
        elif 35 <= indeks < 40:
            print("Tugev rasvumine")
        else:
            print("Tervisele ohtlik rasvumine")
            
    
    
   
    print("Kohtumiseni, " + nimi + "! ")
    
except ValueError:
    print("Palun sisesta ainult numbreid vastustena!")

