def envoltura(regalo):
    def papel():
        print("🎁🔖")
        regalo()
        print("🎁")
    return papel

@envoltura
def pelota():
    print("⚽")

@envoltura
def chocolate():
    print ("🍫")

pelota()
chocolate()