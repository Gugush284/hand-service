from parser import parser

urls = ["https://hands.ru/company/about", "https://repetitors.info"]

def main():
    phones = []
    for url in urls:
        phones = parser.parse(url) + phones

    print("Потенциальные номера телефона:")
    print (phones)

main()


