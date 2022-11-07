import json
import csv
import hashlib

# File paths
csvFilePath = 'HNGi9 CSV FILE - Sheet1.csv'
jsonFilePath = 'JSON'
csvOutputPath = 'Output.csv'

def main():

    make_json(csvFilePath='HNGi9 CSV FILE - Sheet1.csv')

    hashed_str = encode(jsonFilePath)

    write_csv(csvFilePath, hashed_str)
    print(hashed_str)

    # Get total rows
    count = 0
    with open(csvFilePath) as csvf:
        csvReader = csv.DictReader(csvf)

        for row in csvReader:
            if 'Series Number' in row:
                count += 1

    for i in range(count):
        result = encode(jsonFilePath + "i")

def make_json(csvFilePath):
   
    # open the csv file
    csv_file = open(csvFilePath, 'r')
    csv_reader = csv.DictReader(csv_file, fieldnames=("Serial number","Filename","Name","Description","Gender","Attributes","UUID"))

    # csv to multiple json files
    count = 0
    for row in csv_reader:
        all_data = json.dumps(row)

        jsonoutput = open('JSON/File' + str(count) + '.json', 'w')
        jsonoutput.write(all_data)
        count += 1

    # close files
    jsonoutput.close()
    csv_file.close()

# Calculate the sha256 of the json file

def encode(json_file):

    json_file = 'JSON'

    result = hashlib.sha256(json_file.encode())
    hashed_code = result.hexdigest()
    return hashed_code
    

# Append to each line of csv(as a filename.output.csv

def write_csv(csvFilePath, hashed_str):

    with open(csvFilePath, 'r') as read_file,\
        open('Output.csv', 'w',newline='') as write_file:
        
            csv_reader = csv.reader(read_file)
            csv_writer = csv.writer(write_file)

            for row in csv_reader:
                row.append(hashed_str)

                csv_writer.writerow(row)


if __name__ == "__main__":
    main()