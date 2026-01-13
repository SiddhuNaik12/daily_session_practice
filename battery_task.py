import csv
import json
def create_battery_ranges(csv_file="battery_task.csv",json_file="battery_ranges.json"):
    """Groups vehicles into battery ranges sorts each group  by ID and saves to JSON"""
    ranges={
        "0_to_10":[],
        "11_to_20": [],
        "21_to_30": [],
        "31_to_40": [],
        "41_to_50": [],
        "51_to_60": [],
        "61_to_70": [],
        "71_to_80": [],
        "81_to_90": [],
        "91_to_100": []
    }
    #read csv file
    with open(csv_file,"r") as file:
        reader=csv.DictReader(file)
        for row in reader:
            battery=float(row["battery"])
            #allocate to correct range
            if 0 <= battery <= 10:
                ranges["0_to_10"].append(row)
            elif 11 <= battery <= 20:
                ranges["11_to_20"].append(row)
            elif 21 <= battery <= 30:
                ranges["21_to_30"].append(row)
            elif 31 <= battery <= 40:
                ranges["31_to_40"].append(row)
            elif 41 <= battery <= 50:
                ranges["41_to_50"].append(row)
            elif 51 <= battery <= 60:
                ranges["51_to_60"].append(row)
            elif 61 <= battery <= 70:
                ranges["61_to_70"].append(row)
            elif 71 <= battery <= 80:
                ranges["71_to_80"].append(row)
            elif 81 <= battery <= 90:
                ranges["81_to_90"].append(row)
            elif 91 <= battery <= 100:
                ranges["91_to_100"].append(row)
    #sort list by id
    for key in ranges:
        ranges[key]=sorted(ranges[key],key=lambda x:x["id"])
    #save to json
    with open(json_file,"w") as f:
        json.dump(ranges,f,indent=4)
    print("all battery ranges sorted and saved into battery_ranges.json")
#run the function
create_battery_ranges()
    

