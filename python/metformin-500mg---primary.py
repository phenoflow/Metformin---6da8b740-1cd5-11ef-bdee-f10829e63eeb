# Matthew J Carr, Alison K Wright, Lalantha Leelarantha, Hood Thabit, Nicola Milne, Naresh Kanumilli, Darren M Ashcroft, Martin K Rutter, 2024.

import sys, csv, re

codes = [{"code":"34135","system":"gprdproduct"},{"code":"34323","system":"gprdproduct"},{"code":"73285","system":"gprdproduct"},{"code":"60286","system":"gprdproduct"},{"code":"55739","system":"gprdproduct"},{"code":"48149","system":"gprdproduct"},{"code":"53867","system":"gprdproduct"},{"code":"33087","system":"gprdproduct"},{"code":"23","system":"gprdproduct"},{"code":"71198","system":"gprdproduct"},{"code":"55711","system":"gprdproduct"},{"code":"55270","system":"gprdproduct"},{"code":"34598","system":"gprdproduct"},{"code":"52442","system":"gprdproduct"},{"code":"73892","system":"gprdproduct"},{"code":"52221","system":"gprdproduct"},{"code":"72695","system":"gprdproduct"},{"code":"51527","system":"gprdproduct"},{"code":"71012","system":"gprdproduct"},{"code":"34004","system":"gprdproduct"},{"code":"34917","system":"gprdproduct"},{"code":"72052","system":"gprdproduct"},{"code":"72046","system":"gprdproduct"},{"code":"50970","system":"gprdproduct"},{"code":"57457","system":"gprdproduct"},{"code":"34504","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('metformin-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["metformin-500mg---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["metformin-500mg---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["metformin-500mg---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
