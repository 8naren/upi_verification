import requests

def main(lines,n):
    new_lines = []
    for num in lines:
        number = num.rstrip("\n")
        if number not in new_lines:
            new_lines.append(number)
    if n not in new_lines:
        print(n)
        new_lines.append(n)
    return new_lines

with open(r"C:\Users\bogem\Downloads\numbers.txt","r") as file:
    number_list = []
    data = file.readlines()
    for number in data:
        number_list.append(int(number[:-1]))
    
    for number in number_list:

        upi = [
            str(number)+"@apl",
            str(number)+"@ybl",
            str(number)+"@oksbi",
            str(number)+"@okhdfcbank",
            str(number)+"@axl",
            str(number)+"@paytm",
            str(number)+"@ibl",
            str(number)+"@upi",
            str(number)+"@icici",
            str(number)+"@sbi",
            str(number)+"@kotak",
            str(number)+"@postbank",
            str(number)+"@axisbank",
            str(number)+"@okicici",
            str(number)+"@okaxis",
            str(number)+"@dbs",
            str(number)+"@barodampay",
            str(number)+"@idfcbank"
        ]
    for num in upi:
            response = requests.post('https://upibankvalidator.com/api/upiValidation', params={"upi":num})
            try:
                if '"isUpiRegistered":true' in response.text:
                    if "@ybl" in num or "@yapl" in num or "@yesbank" in num:
                        with open("Yesbank.txt","a") as file:
                            file.write(num+"\n")
                        
                    elif ("@axl" in num or "@abfspay" in num or "@axisb" in num or "@okaxis" in num or "@axisbank" in num or "@jupiteraxis"
                            in num or"@pingpay" in num or "@sliceaxis" in num or "@waaxis" in num ):
                        with open("Axisbank.txt","a") as file:
                            file.write(num+"\n")
                            
                    elif "@fbl" in num:
                        with open("federalbank.txt","a") as file:
                            file.write(num+"\n")
                        
                    elif "@idfcbank" in num:
                        with open("idfcbank.txt","a") as file:
                            file.write(num+"\n")
                            
                    elif "@icici" in num or "@okicici" in num or "@ibl" in num or "@tapicici" in num or "@waicici" in num:
                        with open("icici.txt", "r") as fp:
                            lines = fp.readlines()
                            a = main(lines,num)
                            if len(a)==len(lines):
                                pass
                            else:
                                with open("icici.txt","w") as file:
                                    file.writelines("\n".join(a))
                            
                    elif "@okhdfcbank" in num or "@ikwik" in num or "@wahdfcbank" in num:
                        with open("hdfc.txt","a") as file:
                            file.write(num+"\n")
                            
                    elif "@oksbi" in num or "@wasbi" in num:
                        with open("sbi.txt","a") as file:
                            file.write(num+"\n")
                            
                    elif "@indus" in num:
                        with open("indusbank.txt","a") as file:
                            file.write(num+"\n")
                            
                    elif "@kmbl" in num:
                        with open("kotalmahidrabank.txt","a") as file:
                            file.write(num+"\n")
                            
            except Exception as E:
                print(E)