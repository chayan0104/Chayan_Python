data = {
    "DERF": 0,
    "POENKN": 10,
    "DD": 7,
    "MAINDATA": [
        {
            "IDD": "d3454355",
            "BDD": "5678hfjhjh",
            "LINKID": 4,
            "HeaderFields": [
                {"FieldTypeName": "H1", "Value": "false"},
                {"FieldTypeName": "H2", "Value": "148877564"},
                {"FieldTypeName": "H3", "Value": "20230930"},
                {"FieldTypeName": "H4", "Value": "20231130"},
                {"FieldTypeName": "H5", "Value": "2441.56"},
                {"FieldTypeName": "H6", "Value": "0.00"},
                {"FieldTypeName": "H7", "Value": "2411.56"},
                {"FieldTypeName": "H8", "Value": "EUR"},
                {"FieldTypeName": "H9", "Value": "00115190035"},
                {"FieldTypeName": "H10", "Value": ""},
                {"FieldTypeName": "H11", "Value": "4500575382"},
                {"FieldTypeName": "H12", "Value": "0.00"},
                {"FieldTypeName": "H13", "Value": ""},
                {"FieldTypeName": "H14", "Value": ""},
                {"FieldTypeName": "H15", "Value": "F0"},
                {"FieldTypeName": "H16", "Value": "87"},
                {"FieldTypeName": "H17", "Value": "0.00"},
                {"FieldTypeName": "H18", "Value": ""},
                {"FieldTypeName": "H19", "Value": ""},
                {"FieldTypeName": "H20", "Value": "No"}
            ],
            "CodingLines": [],
            "Tables": [
                {"N1": "233553", "N2": "3555", "N3": "ASDDDD", "N4": "334324", "N5": "900.00", "N6": "1.29", "N7": "387.00", "N8": "", "N9": "0.00", "N10": "", "N11": "", "N12": "", "N13": "", "N14": ""},
                {"N1": "765765", "N2": "67657657", "N3": "ADFDFF)", "N4": "667657", "N5": "1000.00", "N6": "1.94", "N7": "1940.00", "N8": "", "N9": "0.00", "N10": "", "N11": "", "N12": "", "N13": "", "N14": ""},
                {"N1": "67657", "N2": "76576576576", "N3": "SFDFFDFSDF", "N4": "7667676", "N5": "1000.00", "N6": "0.11456", "N7": "114.56", "N8": "", "N9": "0.00", "N10": "", "N11": "", "N12": "", "N13": "", "N14": ""}
            ],
            "INININ": "148877564",
            "SDRER": "null"
        },
        {
            "IDD": "frret5",
            "BDD": "5trtry4566",
            "LINKID": 4,
            "HeaderFields": [
                {"FieldTypeName": "H1", "Value": "false"},
                {"FieldTypeName": "H2", "Value": "ICI2300397"},
                {"FieldTypeName": "H3", "Value": "20231219"},
                {"FieldTypeName": "H4", "Value": "20240331"},
                {"FieldTypeName": "H5", "Value": "76.44"},
                {"FieldTypeName": "H6", "Value": "0.00"},
                {"FieldTypeName": "H7", "Value": "76.44"},
                {"FieldTypeName": "H8", "Value": "INR"},
                {"FieldTypeName": "H9", "Value": "56676765"},
                {"FieldTypeName": "H10", "Value": ""},
                {"FieldTypeName": "H11", "Value": "0.00"},
                {"FieldTypeName": "H12", "Value": ""},
                {"FieldTypeName": "H13", "Value": ""},
                {"FieldTypeName": "H14", "Value": "F1"},
                {"FieldTypeName": "H15", "Value": "87"},
                {"FieldTypeName": "H16", "Value": "0.00"},
                {"FieldTypeName": "H17", "Value": ""},
                {"FieldTypeName": "H18", "Value": ""}
            ],
            "CodingLines": [
                {
                    "CODE1": 0.0,
                    "CODE2": 76.44,
                    "CODE3": "5645654",
                    "CODE4": "",
                    "CodingFields": [
                        {"FieldName": "COL1", "Value": "223DD666"},
                        {"FieldName": "COL2", "Value": "3454545"},
                        {"FieldName": "COL3", "Value": ""},
                        {"FieldName": "COL5", "Value": ""},
                        {"FieldName": "COL5", "Value": ""}
                    ]
                }
            ],
            "Tables": [],
            "INININ": "DER3434",
            "SDRER": "null"
        }
    ],
    "Final": "JKHJKLH0909908"
}


# Initialize counter
count = 0

# Traverse the "MAINDATA" list
for record in data["MAINDATA"]:
    for field in record["HeaderFields"]:
         if "FieldTypeName" in field:
             count +=1
         else:
             count =1

# Print the count
print(f"The count of 'FieldTypeName' is: {count}")