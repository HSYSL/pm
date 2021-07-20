import os
import re
def find_files() -> list:
	for file in os.listdir("."):
		pm_files = list()
		if file.endswith(".txt"):
			pm_files.append(file)

	return pm_files

codes = ["1450", "1600", "1601", "1602", "1500", "1501", "1502", "1503", "1504"]
tag_regex = re.compile(r"[0-9]{2}-[FIT]{2}-[0-9]{3}[ABC]?")



