''''''
import time

'''PONDICHERRY'''
print("!!..Welcome to Pondicherry..!")
time.sleep(3)
print("What do you wanna rent??")
print("1.Two wheeler \n2.Four Wheeler")
rent = int(input())
def booking():
    amount = price * days
    print("Your Booking Details are as follows....")
    print("------------------------------------------")
    print("Vehicle : ",vehicle)
    print("Amount per day : ", price)
    print("Number of days : ", days)
    print("Your Aadhar number is : ", aadhar)
    print("Your Driving License Number is : ", dl)
    print("Total Amount : ", amount)
    print("------------------------------------------")
    print("Do you want to continue??")
    print("1.Yes \n2.No")
    confirm = int(input())
    if (confirm == 1):
        print("Congratulations....!\nYour Booking has been Confirmed..!!")
        time.sleep(3)
        print("Please pay at the time of pick-up by providing your Documents")
        print("Enjoyy your Trip!!!!")
    else:
        print("Your Booking has been cancelled!!! ")


if(rent == 1):
    print("1.Bike \n2.scooter")
    two = int(input())

    if(two == 1):
        print("Select a bike below..")
        print("1.Royal Enfield Bullet 350 \n2.Royal Enfield Bullet 500 \n3.Bajaj Avenger crusie 220 \n4.Yamaha FZ V3 \n5.Yamaha MT 15")
        bike = int(input())
        print("For how many days do you want to rent bike??")
        days = int(input())
        print("Enter your Aadhar Number")
        aadhar = int(input())
        print("Enter your Driving License Number")
        dl = int(input())

        if(bike == 1):
            price = 2050
            vehicle = "Royal Enfield Bullet 350"
            booking()
        elif(bike == 2):
            price = 2550
            vehicle = "Royal Enfield Bullet 500"
            booking()
        elif(bike == 3):
            price = 1700
            vehicle = "Bajaj Avenger crusie 220"
            booking()
        elif(bike == 4):
            price = 2300
            vehicle = "Yamaha FZ V3"
            booking()
        elif(bike == 5):
            price = 2100
            vehicle = "Yamaha MT 15"
            booking()
        else:
            print("Please select a valid option..")

    elif(two == 2):
        print("Select a scooter below..")
        print("1.Vespa 125 \n2.Yamaha Aerox \n3.Suzuki Access 125 \n4.Yamaha Fascino \n5.TVS Ntorq 125")
        scooter = int(input())
        print("For how many days do you want to rent bike??")
        days = int(input())
        print("Enter your Aadhar Number")
        aadhar = int(input())
        print("Enter your Driving License Number")
        dl = int(input())

        if(scooter == 1):
            price = 750
            vehicle = "Vespa 125"
            booking()
        elif(scooter == 2):
            price = 850
            vehicle = "Yamaha Aerox"
            booking()
        elif(scooter == 3):
            price = 1200
            vehicle = "Suzuki Access 125"
            booking()
        elif(scooter == 4):
            price = 1000
            vehicle = "Yamaha Fascino"
            booking()
        elif(scooter == 5):
            price = 650
            vehicle = "TVS Ntorq 125"
            booking()
        else:
            print("Please select a valid option..")
    else:
        print("Please select a valid option..")

elif(rent == 2):
    print("Select a car below..")
    print("1.Tata Punch \n2.Tata Nexon \n3.Mahindra XUV 300 \n4.Maruti Suzuki Swift \n5.Hyundai i20")
    car = int(input())
    print("For how many days do you want to rent car??")
    days = int(input())
    print("Enter your Aadhar Number")
    aadhar = int(input())
    print("Enter your Driving License Number")
    dl = int(input())
    if(car == 1):
        price = 2500
        vehicle = "Tata Punch"
        booking()
    elif(car == 2):
        price = 3000
        vehicle = "Tata Nexon"
        booking()
    elif(car == 3):
        price = 3200
        vehicle = "Mahindra XUV 300"
        booking()
    elif(car == 4):
        price = 2000
        vehicle = "Maruti Suzuki Swift"
        booking()
    elif(car == 5):
        price = 1900
        vehicle = "Hyundai i20"
        booking()
    else:
        print("Please select a valid option..")
else:
    print("Please select a valid option..")