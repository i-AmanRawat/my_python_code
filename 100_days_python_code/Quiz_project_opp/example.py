class User :    #just following the pascal convention
    def __init__(self , user_id , user_name  ):
        self.id = user_id       #int it is basically using to create the constructor unlike in cpp
        self.name = user_name   #and self is the parameter passed in the methods we create
        self.followers = 0
        self.following = 0

    def follow (self , user) :  #self has decided to follow user so , self +1(into the following list )
        user.followers +=1
        self.following +=1  #basically self ie user01 is following user02 here

    def display_details (self , me):
        print(f"Followers of {me} : ", self.followers)
        print(f"Following of {me} : ", self.following)

aman = User(993923 , "manu")    #for defining the variables we use camel convention
aryan = User(383940 , "onne")
# print(aman.id)
# print(aman.name)
print(aman.followers)
print(aman.following)
aman.follow(aryan)      #aman -->user01 and aryan -->user02 so basically user01 has decided to follow user02
aman.display_details("manu")
aryan.follow(aman)
aman.display_details("manu")
