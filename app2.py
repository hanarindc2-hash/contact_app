import sys


contacts = []

def print_menu():
    menu = "1) 보기 2) 추가 3) 삭제 4) 종료"
    print(menu)

def select_menu():
        sel = input('선택> ')
        sel = int(sel)
        return sel

def print_contact():
     print("보기 실행")
     for contact in contacts:
          print(f"이름: {contact['name']}")
          print(f"전화번호: {contact['phone']}")
          print(f"주소: {contact['address']}")
          print(f"이메일: {contact['email']}")

def input_contact():
     
     name=input("이름: ")
     phone=input("전화번호: ")
     address=input("주소: ")
     email=input("이메일: ")
     contact = {
          "name": name,
          "phone": phone,
          "address": address,
          "email": email
     }
     return contact


def add_contact():
     contact = input_contact()

     contacts.append(contact)

def delete_contact():
     print("삭제 실행")

def confirm(question):
     answer = input(question + '[Y/n]')
     if answer == '':
          return True
     answer = answer.lower()
     if answer == 'y':
          True
     else:
          return False

     return answer

     
def exit():
     answer = confirm('종료할까요')
     if answer:
          print("종료합니다.")
          sys.exit(0)
          


def run_menu(sel):

    if sel == 1:
         print_contact()
    elif sel == 2:
         add_contact()
    elif sel == 3:
         delete_contact()
    elif sel == 4:
         exit()
    else:
         print("입력이 잘못되었습니다. 다시 입력해주세요.")



def main():

    while True:
        print_menu()
        sel = select_menu()
        if run_menu(sel) == 1:
             break
        
    

main()
