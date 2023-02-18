from utils.csv_ import HandleCSV
def file():
    bar= HandleCSV.read_entire_csv()

    for k in bar:
        if int(k['SALARY']) > 9000:
            name=k["FIRST_NAME"]
            lname=k["LAST_NAME"]
            email=k["EMAIL"]
            phone=k["PHONE_NUMBER"].replace(".","")

            print(f"name:{name} {lname}")
            print(f"email:{email}")
            print(f"phone_no:{phone}")

if __name__=="__main__":
    file()

