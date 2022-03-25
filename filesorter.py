import os
files = os.listdir()
extensions = list()
for file in files:
	if "." in file and os.path.basename(__file__) != file and os.path.isfile(file):
		extensions.append(file.split(".")[-1])

extensions = list(dict.fromkeys(extensions))
for ext in extensions:
	try:
		os.mkdir(f"x.{ext}")
	except:
		pass
for file in files:
	for ext in extensions:
		if file.split(".")[-1] == ext:
			try:
				os.rename(file, f"x.{ext}/{file}")
			except Exception as e:
				print(f"Failed {file} to move: {e}")
input("Done!")