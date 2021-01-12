import os
os.system("clear")
import amino
client=amino.Client()
email=input("Email: ")
password=input("Password: ")
try:
	client.login(email=email ,password=password)
except:
	print ("Email or Password is Incorrect")
	os._exit(1)

u=input("Host Link: ")
us=client.get_from_code(u)
p=us.objectId
comId=us.path[1:us.path.index('/')]
chatl=input("Chat Link: ")
chatId=client.get_from_code(chatl).objectId
subclient=amino.SubClient(comId=comId, profile=client.profile)

subclient.kick(userId=p ,chatId=chatId, allowRejoin=True)
print ("Done")
os._exit(1)
