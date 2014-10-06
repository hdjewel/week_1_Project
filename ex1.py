import os


def process_list_of_files(path_name):
	
	cmd = "ls -l " + path_name + "/."
	end_of_file = False
	count = 0
	
	list_of_files = os.popen(cmd)

#	for line in list_of_files:
	while end_of_file == False:
		line = list_of_files.readline()

		line = line.strip()
		line = line.split(" ")

		if len(line) == 1:
			end_of_file = True
			print count, "files copied"
			break

		perms = line[0]
		
		file_name = line.pop()
		
		if perms[0] == "-":
			new_path = path_name + "/" + file_name[0] + "/"
			cmd = "cp " + path_name + "/" + file_name + " " + new_path + file_name
			os.popen(cmd)

		count = count + 1

#		print file_name 

def create_directories(path):

    cmd = "rm -rf " + path + "/?"
    os.popen(cmd)

    dirs = "abcdefghijklmnopqrstuvwxyz"
    for i in dirs:
    	cmd = "mkdir " + path + "/" + i
#    	print cmd
    	os.popen(cmd)

def main():
	
	path_name = "/Users/owner/src/week_1_Project/files"
	create_directories(path_name)
	process_list_of_files(path_name) 

#if __name__ == "__MAIN__"
main()
