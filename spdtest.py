import speedtest
#first we need impot speedtest check it how you can do it in your OS

st = speedtest.Speedtest()

def testing(option,option1,option2):

	if option == 1 and option1 == 2 and option2 == 3:
		mb=(st.download()*1.0E-6)
		print("Download speed:","{0:.2f}".format(mb),"mb")

		mb2=(st.upload()*1.0E-6)
		print("Upload  speed:","{0:.2f}".format(mb2),"mb")

		servernames =[]
		st.get_servers(servernames)
		print("Ping:",st.results.ping,'ms')

	else:
		print("Please enter the correct choice!")

print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
print("Test in process please wait...")
testing(1,2,3)
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")