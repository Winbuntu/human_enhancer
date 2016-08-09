'''
This script read data downloaded from http://enhancer.lbl.gov/frnt_page_n.shtml , Vista enhancer broswer
only output human enhancers, and bed files are coded in hg19 coordinates
'''


def process_cord(cord):
	chrs = cord.split(":")
	co = chrs[1].split("-")
	return [chrs[0].strip(),co[0].strip(),co[1].strip()]



def main():
	bedout = open("human_enhancer_hg19.bed","w")
	with open("enhancer_origional_data.txt","r") as filein:
		for line in filein:
			if line[0] == ">" and line[1:6] == "Human":
				elements = line[1:].strip().split("|")

				bedout.write("\t".join(process_cord(elements[1])) + "\t" + elements[2].strip().replace(" ","_") + "\t" +elements[3].strip() + "\n")
				#print "\t".join(elements[0:4])
			else:
				continue

			


if __name__ == "__main__":
	#print process_cord("chr11:16913136-16917745")
	main()