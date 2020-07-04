import speedtest
st = speedtest.Speedtest()

def opciones(option,optione,optiones):

	if option == 1 and optione == 2 and optiones == 3:
		#print(st.download(), 'b/s')
		mb=(st.download()*1.0E-6)
		print("Velocidad de bajada:","{0:.2f}".format(mb),"mb")
		#print(st.upload(), 'b/s')
		mb2=(st.upload()*1.0E-6)
		print("Velocidad de subida:","{0:.2f}".format(mb2),"mb")
		servernames =[]
		st.get_servers(servernames)
		print("Ping:",st.results.ping,'ms')
	else:
		print("Please enter the correct choice!")

print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
print("Haciendo prueba de velocidad en Python")
opciones(1,2,3)
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")