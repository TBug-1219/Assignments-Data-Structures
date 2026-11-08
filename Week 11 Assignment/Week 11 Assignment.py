import re

def processFile(keyword):
    pattern = re.compile(rf'\b{re.escape(keyword)}\b', re.IGNORECASE)

    with open('Data.txt', 'r') as infile, \
        open('found.txt', 'w') as foundFile, \
        open('notfound.txt', 'w') as notFoundFile, \
        open('details.txt', 'w') as detailsFile:

        for recordNum, line in enumerate(infile, start = 1):
            matches = list(pattern.finditer(line))
            if matches:
                positions = [match.start() for match in matches]
                modifiedLine = pattern.sub(keyword.upper(), line)
                foundFile.write(modifiedLine)
                detailsFile.write(f"Record {recordNum}: positions {positions}\n")
            else:
                notFoundFile.write(line)

if __name__ == "__main__":
    keyword = input("Enter the keyword to search for: ").strip()
    processFile(keyword)