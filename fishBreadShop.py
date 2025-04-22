# START

stock = {"팥붕어빵": 10, "슈크림붕어빵": 8, "초코붕어빵": 5}

order = {"팥붕어빵": 0, "슈크림붕어빵": 0, "초코붕어빵": 0}


def orderBread():
    while True:
        breadType = input("주문할 붕어빵을 선택하세요 - 팥붕어빵, 슈크림붕어빵, 초코붕어빵(만약 끝내고 싶다면 '종료'를 작성해 주세요): ")
        if breadType == "종료":
            break
        
        breadCount = int(input("주문할 수량을 입력하세요(숫자만)."))
        

def admin():
    pass


while True:
    mode = input("원하는 모드를 선택하세요(주문, 관리자, 종료): ")

    if mode == "종료":
        break
    elif mode == "주문":
        orderBread()
    elif mode == "관리자":
        admin()
