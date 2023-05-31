import os

def save_extensions(dir_name):
    for filename in os.listdir(dir_name):
        file = os.path.join(dir_name, filename)

        if os.path.isfile(file):
            extension = filename.split(".")[-1]

            if extension not in extensions:
                extensions[extension] = []

            extensions[extension].append(filename)

        elif os.path.isdir(file) and filename!="venv":
            save_extensions(file)

directory = input()
extensions = {}
report = []

try:
    save_extensions(directory)
except FileNotFoundError:
    print(f"Not a valid directory")

extensions = sorted(extensions.items(), key= lambda x :x[0])
for extension, files in extensions:
    report.append(f" .{extension}")
    [report.append(f"---{file}") for file in sorted(files)]

with open(f"{directory}/output.txt", "w") as f:
    f.write("\n".join(report))

#print(extensions.__str__())