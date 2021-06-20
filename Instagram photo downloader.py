while True:
	filename='pic'+str(random.randint(1, 100000))+'.jpg'
	file_exists = os.path.isfile(filename)

	if not file_exists:
		with open(filename, 'wb+') as handle:
			response = requests.get(string_url, stream=True)
			if not response.ok:
				print(response)
			for block in response.iter_content(1024):
				if not block:
					break
				handle.write(block)
	else:
		continue
	break
print("\n			 downloading completed ..............")
