import sys

contacts = []


def init():
    for i in range(10):
        contact = {
            "name": f"hong{i:02}",
            "phone": f"{str(i)*3}-{str(i)*4}-{str(i)*4}",
            "address": f"서울시",
            "email": f"hong{i:02}@gmail.com",
        }
        contacts.append(contact)


def print_menu():
    print("1) 보기 2) 추가 3) 삭제 4) 종료")


def select_menu():
    sel = input("선택>")
    sel = int(sel)
    return sel


def print_contact():
    # print(f"이름:{contact['name']}")
    # print(f"휴대전화:{contact['phone']}")
    # print(f"집 주소:{contact['address']}")
    # print(f"e- mail:{contact['email']}")
    print(f"no.", "이름", "휴대전화    ", "집 주소", "e-mail") # no. 이름   휴대전화 집 주소 e-mail
    print("--------------------------------")
    for index, values in enumerate(contacts):
        print(
            f"{index+1} {values['name']} {values['phone']} {values['address']} {values['email']}"
        )                                                 # 1   홍길동 111-1111-1111 서울시 hong00@gmail.com
    print("--------------------------------")
    print(len(contacts))


def input_contact():
    name = input("이름: ")
    phone = input("휴대전화: ")
    address = input("집 주소: ")
    email = input("e- mail: ")

    contact = {"name:name", "phone:phone", "address:address", "email:email"}
    return contact


def add_contact():
    contact = input_contact()
    contacts.append(contact)


def del_contact():
    print("삭제 실행")


def confirm(question):
    answer = input(question + "[Y/n]")
    if answer == "":
        return True

    answer = answer.lower()
    if answer == "y":
        return True
    else:
        return False


def exit():
    answer = confirm("정말 종료하시겠습니까?")
    if answer:
        print("종료합니다.")
        sys.exit(0)


def execute_menu(sel):
    if sel == 1:
        print_contact()
    elif sel == 2:
        add_contact()
    elif sel == 3:
        del_contact()
    elif sel == 4:
        exit()
    else:
        print("잘못된 선택입니다.")


def main():
    init()
    while True:
        print_menu()
        sel = select_menu()
        execute_menu(sel)


main()
