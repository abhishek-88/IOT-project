import urllib.request

#READ_API_KEY = "S47Z42SUYSK3TB4Z"
#CHANNEL_ID = "890433"


def main():
	#Enable any one, one-by-one


	#Read a channel Field
	conn = urllib.request.urlopen("https://api.thingspeak.com/channels/892782/feeds.csv?api_key=11491HVVNL3DCNX0&results=5")

	response = conn.read()
	print("-----------------------------------")

	print(response)
	print("###################################")
	print("http status code = %s" % (conn.getcode()))
	#print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
	conn.close()

if __name__ == '__main__':
	main()
