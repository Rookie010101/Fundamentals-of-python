print("This is a menu driven telecom calling system. \n")
print('''Press 1 to continue in English
Press 2 to continue in Hindi
Press 3 to continue in Gujrati''')
num = int(input("Press the number to continue in your desired language: "))
match num:
    case 1:
        print('''\nPress 1 to know about our products
Press 2 to know number of active stores in Gujarat''')
        Eng_info = int(input("Enter the Code to know the details."))
        match Eng_info:
            case 1:
                print("We deal in all types of car parts and accessories.")
            case 2:
                print("There are total 25 active stores in Gujarat")
            case _:
                print("Invalid Code")
    case 2:
        print('''\nहमारे उत्पादों के बारे में जानने के लिए 1 दबाएँ
गुजरात में सक्रिय स्टोर्स की संख्या जानने के लिए 2 दबाएँ''')
        Hin_info = int(input("जानकारी जानने के लिए कोड दर्ज करें: "))
        match Hin_info:
            case 1:
                print("हम सभी प्रकार के कार पार्ट्स और एक्सेसरीज में व्यापार करते हैं.")
            case 2:
                print("गुजरात में कुल 25 सक्रिय स्टोर हैं.")
            case _:
                print("Invalid Code")

    case 3:
        print('''\nઅમારા ઉત્પાદનો વિશે જાણવા માટે 1 દબાવો
ગુજરાતમાં સક્રિય સ્ટોરોની સંખ્યા જાણવા માટે 2 દબાવો''')
        Guj_info = int(input("વિગતો જાણવા માટે કોડ દાખલ કરો: "))
        match Guj_info:
            case 1:
                print("અમે તમામ પ્રકારના કાર પાર્ટ્સ અને એસેસરીઝમાં વ્યવહાર કરીએ છીએ")
            case 2:
                print("ગુજરાતમાં કુલ 25 સક્રિય સ્ટોર્સ છે.")
            case _:
                print("Invalid Code")
