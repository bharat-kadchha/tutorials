import csv, os

parent_dir = "E:/GitHub/1) Git_Tutorials_Repo_Projects/core-python/Core_Python/ExCsvFiles"

with open(os.path.join(parent_dir, "ReadCsvWithDict.csv")) as software_csv:
    reader = csv.DictReader(software_csv)
    for row in reader:
        print(("{} has {} users").format(row["name"], row["users"]))

