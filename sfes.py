import os
import sys
from getopt import *

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def colored(text, color):
	match color:
		case "header":
			return bcolors.HEADER+text+bcolors.ENDC
		case "okblue":
			return bcolors.OKBLUE+text+bcolors.ENDC
		case "okcyan":
			return bcolors.OKCYAN+text+bcolors.ENDC
		case "okgreen":
			return bcolors.OKGREEN+text+bcolors.ENDC
		case "warning":
			return bcolors.WARNING+text+bcolors.ENDC
		case "fail":
			return bcolors.FAIL+text+bcolors.ENDC
		case "bold":
			return bcolors.BOLD+text+bcolors.ENDC
		case "underline":
			return bcolors.UNDERLINE+text+bcolors.ENDC
		case _:
			return text

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
					print(colored(f"Failed {file} to move: {e}", "fail"))
	print(colored("Done!", "okgreen"))
	with open("cfg.sfes", "w") as file:
		file.write(prefix)
	print(colored("Do not delete or edit cfg.sfes file if you will need to unsort your files!", "warning"))
	sys.exit()


def unsort(prefix):
	try:
		with open("cfg.sfes") as file:
			prefix = file.readlines()[0]
	except FileNotFoundError:
		print(colored("Error: cfg.sfes not found, cannot resort", "fail"))
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
				print(colored(f"Failed {file} to move: {e}", "fail"))
		try:
			os.rmdir(folder)
		except Exception as e:
			print(colored(f"Failed {file} to delete: {e}", "fail"))
	print(colored("Done!", "okgreen"))
	sys.exit()


def help():
	print(colored("Usage:\n-p (prefix) - sets prefixes for folders like '(prefix)txt' or '(prefix)doc'\n-n - create folders named by just extensions\n-r - sorts unsorted files in existant folders using previous prefix\n-h - shows this message\n-c - unsort, bring files back from folders (also deleting folders)", "warning"))
	sys.exit()


def main():
	print(colored("Simple File Extension Sorter v1.12\n", "header"))
	if len(sys.argv) == 1:
		help()
	try:
		optlist, args = getopt(sys.argv[1:], 'np:hcr')
	except GetoptError as e:
		print(colored("Error: " + str(e) + ", use 'sfes -h' for help", "fail"))
		sys.exit()

	for opt, a in optlist:
		if opt == "-h":
			help()
		elif opt == "-n":
			yn = input(colored("Are you sure that you want to have no prefix? You wont be able to unsort your files using sfes in the future!\n(yes or no? y/n): ", "warning"))
			if yn.lower() == "y":
				sort("")
			elif yn.lower() == "n":
				sys.exit()
			else:
				print("I`ll take that as no")
				sys.exit()
		elif opt == "-p":
			if a not in "+=[]:;«,./\\:*? «<>|":
				sort(a)
			else:
				print(colored("Error: Can't create folders with this prefix!", "fail"))
				sys.exit()
		elif opt == "-c":
			unsort(a)
		elif opt == "-r":
			try:
				with open("cfg.sfes") as file:
					sort(file.readlines()[0])
			except FileNotFoundError:
				print(colored("Error: cfg.sfes not found, cannot resort", "fail"))
				sys.exit()

	


if __name__ == "__main__":
	main()