with open('ports.txt', 'a') as file:
    for i in range(1024, 5000):
    	file.write(f"{i}\n")
