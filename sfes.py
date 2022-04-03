import os
import sys
from getopt import *
from colorama import init
from termcolor import colored

def sort(prefix):
	files = os.listdir()
	extensions = list()
	for file in files:
		if "." in file and os.path.basename(__file__) != file and os.path.isfile(file) and file != "desktop.ini" and file != "cfg.sfes":
			extensions.append(file.split(".")[-1])

	extensions = list(dict.fromkeys(extensions))
	for ext in extensions:
		try:
			os.mkdir(f"{prefix}{ext}")
		except:
			pass
	for file in files:
		for ext in extensions:
			if file.split(".")[-1] == ext:
				try:
					os.rename(file, f"{prefix}{ext}/{file}")
				except Exception as e:
					print(colored(f"Failed {file} to move: {e}", "red"))
	print(colored("Done!", "yellow"))
	with open("cfg.sfes", "w") as file:
		file.write(prefix)
	print(colored("Do not delete or edit cfg.sfes file if you will need to unsort your files!", "yellow"))
	sys.exit()


def unsort(prefix):
	try:
		with open("cfg.sfes") as file:
			prefix = file.readlines()[0]
	except FileNotFoundError:
		print(colored("Error: cfg.sfes not found, cannot resort", "red"))
		sys.exit()
	files = os.listdir()
	folders = list()
	extensions = list()
	for file in files:
		if prefix in file and os.path.isdir(file):
			folders.append(file)
			extensions.append(file.split(".")[-1])
	for folder in folders:
		files = os.listdir(folder)
		for file in files:
			try:
				os.rename(f"{folder}/{file}", f"{file}")
			except Exception as e:
				print(colored(f"Failed {file} to move: {e}", "red"))
		try:
			os.rmdir(folder)
		except Exception as e:
			print(colored(f"Failed {file} to delete: {e}", "red"))
	print(colored("Done!", "yellow"))
	sys.exit()


def help():
	print(colored("Usage:\n-p (prefix) - sets prefixes for folders like '(prefix)txt' or '(prefix)doc'\n-n - create folders named by just extensions\n-r - sorts unsorted files in existant folders using previous prefix\n-h - shows this message\n-c - unsort, bring files back from folders (also deleting folders)", "yellow"))
	sys.exit()


def main():
	print("Simple File Extension Sorter. Made by Rivus (Utoog) 2022 v1.1\n")
	if len(sys.argv) == 1:
		help()
	try:
		optlist, args = getopt(sys.argv[1:], 'np:hcr')
	except GetoptError as e:
		print(colored("Error: " + str(e) + ", use 'sfes -h' for help", "red"))
		sys.exit()

	for opt, a in optlist:
		if opt == "-h":
			help()
		elif opt == "-n":
			yn = input("Are you sure that you want to have no prefix? You wont be able to unsort your files using sfes in the future!\n(yes or no? y/n): ")
			if yn.lower() == "y":
				sort("")
			elif yn.lower() == "n":
				sys.exit()
			else:
				print("I`ll take that as no")
				sys.exit()
		elif opt == "-p":
			if a not in "+=[]:;«,./\\:*? «<>|":
				yn = input("Proceed? (yes or no? y/n): ")
				if yn.lower() == "y":
					sort(a)
				elif yn.lower() == "n":
					sys.exit()
				else:
					print("I`ll take that as no")
					sys.exit()
			else:
				print(colored("Error: Can't create folders with this prefix!", "red"))
				sys.exit()
		elif opt == "-c":
			unsort(a)
		elif opt == "-r":
			try:
				yn = input("Proceed? (yes or no? y/n): ")
				if yn.lower() == "y":
					with open("cfg.sfes") as file:
						sort(file.readlines()[0])
				elif yn.lower() == "n":
					sys.exit()
				else:
					print("I`ll take that as no")
					sys.exit()
			except FileNotFoundError:
				print(colored("Error: cfg.sfes not found, cannot resort", "red"))
				sys.exit()

	


if __name__ == "__main__":
	main()