#### This program will automatically send an image from a user,
#### to a device such that it will ensure best use of storage.

import socket
hostname=socket.gethostname()

ip=[]
ip=socket.gethostbyname(hostname)
ip=str(ip)


import pymysql
import datetime
now=[]
now=datetime.datetime.now().strftime("%y-%m-%d-%H-%M")
now=str(now)
            
if __name__=="__main__":
    num = int(input("Enter the number of users: "))
    user_rec = []  
    user_ips = []
    flag = 0

    print("Now please enter the image sizes in each users storage: ")

    for i in range(num):
        temp_list = list(map(int,input("Enter size of images for %d user: " %(i+1)).split()))
        if(len(temp_list) != 0):
            flag = 1
        user_rec.append(temp_list)

    print("Please enter user IP addresses in order of user records: ")

    for j in range(num):
        user_ips.append(input("Enter user %d's IP address: " %(j+1)))

    max_size = int(input("Enter maximum size limit: "))

    num_of_images = int(input("Enter number of images to be transferred: "))
    for m in range(num_of_images):
        img_name = input("Enter image name: ")
        image_size = int(input("Enter size of image that is to be sent: "))

        if(max_size < image_size):
            print("Insufficient Storage")

        if(flag == 0):
            print("App will send your image to user with the following ip address: %s " %user_ips[0])
            user_rec[0].append(image_size)
            print(user_ips[0])
            flag = 1
        else:
            rem_space = [(10 - sum(li)) for li in user_rec]
            dummy = sorted(rem_space)
            for k in range(num):
                if(image_size <=dummy[k]):
                    user = rem_space.index(dummy[k])
                    user_rec[user].append(image_size)
                    print("Image sent to device with the following ip: %s " %user_ips[user])
                    break
            print(user_ips[user])
            db = pymysql.connect("localhost","root","Nikhil@1999","mydb" )

            cursor=db.cursor()
            sql="INSERT INTO SAMPLE(sender_ip,receiver_ip,img_name,img_size,date_time)VALUES(%s,%s,%s,%s,%s)"
            data=ip,user_ips[user],img_name,image_size,now
            cursor.execute(sql,data)
            db.commit()
            
    for nn in range(num):
        print("%s : %s " %(user_ips[nn],user_rec[nn]))

    
