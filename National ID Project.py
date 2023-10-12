x = str (input("enter your name : "))
y = input ("entar password : ")


try :
      
        
       if len(y) < 10 :
                  print ("Password should have a minimum length of 10 characters")
                  print ("try agin")
       else :
        s=  input("enter your national ID : ")
       
        if len(s) != 14 or not s.isdigit () :
                   print ("Invalid national ID")
        else :
               
              
               first_elments = s[0]
               sacend_elments = s[1]
               third_elment = s[2]
               elments_four = s[3]
               elments_three = s [4]
               elments_five = s [5]
               elments_six = s[6]
               elments_seven = s[7]
               elments_aight = s[8]
               elments_nine = s[9] , s[10] , s[11]
               elments_11 = s[12]

               if len(s) == 14 :
                                print ("wait......")
               if first_elments == '3' :
                                print ("you were born in the twenty-first century")
                                print ("you were born in  20" + sacend_elments + third_elment )
                                print ("The number you chose while registering in the civil registry is " + str(elments_nine))  
               if first_elments == '2':
                                print ("you were born in the twentieth century")
                                print ("you were born in  19" + sacend_elments + third_elment )
                                print ("The number you chose while registering in the civil registry is " + str(elments_nine))  




               if elments_three == '1' :
                                print ("you were born in January " + elments_five + elments_six)
               if elments_three == '2' :
                                print ("you were born in February " + elments_five + elments_six)
               if elments_three == '3' :
                                print ("you were born in March " + elments_five + elments_six)
               if elments_three == '4' :
                                print ("you were born in April " + elments_five + elments_six)
               if elments_three == '5' :
                                print ("you were born in May " + elments_five + elments_six)
               if elments_three == '6' :
                                print ("you were born in June " + elments_five + elments_six)
               if elments_three == '7' :
                                print ("you were born in July "+ elments_five + elments_six)
               if elments_three == '8' :
                                print ("you were born in August " + elments_five + elments_six)
               if elments_three == '9' :
                                print ("you were born in September " + elments_five + elments_six)
               if elments_three == '0' :
                                print ("you were born in October " + elments_five + elments_six)
               if  elments_four =='1' and elments_three == '1' :
                                print ("you were born in November " + elments_five + elments_six)
               if elments_four == '1' and elments_three == '2' :
                                print ("you were born in December " + elments_five + elments_six)


               if elments_seven == '0' and elments_aight == '1' :
                                print ("The governorate in which you were born is Cairo")
               if elments_seven == '0' and elments_aight == '2' :
                                print ("The governorate in which you were born is Alexandria")
               if elments_seven == '0' and elments_aight == '3' :
                                print ("The governorate in which you were born is Port Said")
               if elments_seven == '0' and elments_aight == '4' :
                                print ("The governorate in which you were born is Suez")
               if elments_seven == '1' and elments_aight == '1' :
                                print ("The governorate in which you were born is Damietta")
               if elments_seven == '1' and elments_aight == '2' :
                                print ("The governorate in which you were born is Dakahlia")
               if elments_seven == '1' and elments_aight == '3' :
                                print ("The governorate in which you were born is Eastern")
               if elments_seven == '1' and elments_aight == '4' :
                                print ("The governorate in which you were born is Qalyubia")
               if elments_seven == '1' and elments_aight == '5' :
                                print ("The governorate in which you were born is Kafr El-Sheikh")
               if elments_seven == '1' and elments_aight == '6' :
                                print ("The governorate in which you were born is algharbiah")
               if elments_seven == '1' and elments_aight == '7' :
                                print ("The governorate in which you were born is Menoufia")
               if elments_seven == '1' and elments_aight == '8' :
                                print ("The governorate in which you were born is el beheira")
               if elments_seven == '1' and elments_aight == '9' :
                                print ("The governorate in which you were born is Ismailia")
               if elments_seven == '2' and elments_aight == '1' :
                                print ("The governorate in which you were born is Giza")
               if elments_seven == '2' and elments_aight == '2' :
                                print ("The governorate in which you were born is Bani Sweif")
               if elments_seven == '2' and elments_aight == '3' :
                                print ("The governorate in which you were born is Fayoum")
               if elments_seven == '2' and elments_aight == '4' :
                                print ("The governorate in which you were born is Minya")
               if elments_seven == '2' and elments_aight == '5' :
                                print ("The governorate in which you were born is Asyut")
               if elments_seven == '2' and elments_aight == '6' :
                                print ("The governorate in which you were born is Sohag")
               if elments_seven == '2' and elments_aight == '7' :
                                print ("The governorate in which you were born is Qena")
               if elments_seven == '2' and elments_aight == '8' :
                                print ("The governorate in which you were born is Aswan")
               if elments_seven == '2' and elments_aight == '9' :
                                print ("The governorate in which you were born is alaqasr")
               if elments_seven == '3' and elments_aight == '1' :
                                print ("The governorate in which you were born is albahr alahmir")
               if elments_seven == '3' and elments_aight == '2' :
                                print ("The governorate in which you were born is alwadi aljadid")
               if elments_seven == '3' and elments_aight == '3' :
                                print ("The governorate in which you were born is matruh")
               if elments_seven == '3' and elments_aight == '4' :
                                print ("The governorate in which you were born is shamal sina'")
               if elments_seven == '3' and elments_aight == '5' :
                                print ("The governorate in which you were born is janub sina'")
               if elments_seven == '8' and elments_aight == '8' :
                                print ("The governorate in which you were born is Outside the republic")

   
            
               if  elments_11 == ('2') :
                              print ("The owner of this card is female")
               if  elments_11 == ('4') :
                              print ("The owner of this card is female")
               if  elments_11 == ('6') :
                              print ("The owner of this card is female")
               if  elments_11 == ('8') :
                              print ("The owner of this card is female")
               if elments_11 == '1':
                             print ("The owner of this card is mail") 
               if elments_11 == '3':
                             print ("The owner of this card is mail") 
               if elments_11 == '5':
                             print ("The owner of this card is mail") 
               if elments_11 == '7':
                             print ("The owner of this card is mail") 
               if elments_11 == '9':
                             print ("The owner of this card is mail") 

        
 
            
except ValueError as err :
                          print (err)



                     
    

            

       
       





