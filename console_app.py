from DAO import Members, Payments
from DTO import Member, Payment
from os import system

def run_console(members: Members,payments: Payments):
    
    while True:
        system('clear || cls')
        print('------------------ Gym Database Manager -----------------')
        print('Commands: ')
        print('0 - Add Member')
        print('1 - Remove Member')
        print('2 - Add Member Payment')
        print('3 - Remove Member Payment')
        print('4 - Check Member payment for the month')
        
        command = input('Choose an Option: ')
        
        match command:
            case '0':
                command_add_member(members)
            case '1':
                command_remove_member(members)
            case '2':
                command_add_member_payment(members,payments)
            case '3':
                command_remove_member_payment(members,payments)
            case '4':
                command_check_payment(members,payments)
            case _:
                input('Choose a valid option!!')


def command_add_member(members):
    try:
        new_member = Member(
            input('Member Name: '),
            input('Member email: '),
            input('Member CPF: ')
        )
        members.add_member(new_member)
        input(f'Member {new_member.name} added to the database!')
    except Exception as e:
        input(f'Something went wrong: {str(e)}')


def command_remove_member(members):
    try:
        member_cpf = input('Member CPF to remove: ')
        member_id = members.member_id_by_cpf(member_cpf)
        members.remove_member(member_id)
        input('Member removed successfully!')
    except Exception as e:
        input(f'Something went wrong: {str(e)}')


def command_add_member_payment(members, payments):
    try:
        member_id = members.member_id_by_cpf(input('Member CPF: '))
        month = int(input('Month in number: '))
        year = int(input('Year in number: '))
        payments.add_payment(Payment(member_id, month, year, payment_status=True))
        input(f'Member payment added: {month}/{year}')
    except Exception as e:
        input(f'Something went wrong: {str(e)}')


def command_remove_member_payment(members, payments):
    try:
        member_id = members.member_id_by_cpf(input('Member CPF: '))
        month = int(input('Month in number: '))
        year = int(input('Year in number: '))
        payments.remove_payment(member_id, month, year)
        input(f'Member payment removed: {month}/{year}')
    except Exception as e:
        input(f'Something went wrong: {str(e)}')


def command_check_payment(members, payments):
    try:
        member_id = members.member_id_by_cpf(input('Member CPF: '))
        month = int(input('Month in number: '))
        year = int(input('Year in number: '))
        payment = bool(payments.payment_payed(member_id, month, year))
        if payment:
            print("The Member has paid!")
        else:
            print("The Member needs to pay!")
    except Exception as e:
        print(f'Something went wrong: {str(e)}')