import math
import sys
import argparse

args = sys.argv
values_positive = True


def check_positive(value):
    return_value = int(value)
    if return_value <= 0:
        global values_positive
        values_positive = False

    return return_value

def diff(principal_arg, periods_arg, interest_arg):
    principal = principal_arg
    periods = periods_arg
    interest = interest_arg
    total = 0
    annuity_payment = math.ceil(principal / periods + interest * (principal - principal *(1 - 1) / periods))
    for i in range(1, periods+1):
        annuity_payment = math.ceil(principal / periods + interest * (principal - principal *(i - 1) / periods))
        total += annuity_payment
        print(f'Month {i}: paid out {annuity_payment}')
    print(f'Overpayment = {total - principal}')


def annuity(principal_arg, periods_arg, interest_arg):
    principal = principal_arg
    periods = periods_arg
    interest = interest_arg
    pow_i_n = math.pow(1 + interest, periods)
    annuity_payment = math.ceil(principal * ((interest * pow_i_n) / (pow_i_n - 1)))
    print(f'Your annuity payment = {annuity_payment}!')
    print(f'Overpayment = {(annuity_payment * periods) - principal}')

def annuity_monthly(monthly_payment_arg, periods_arg, interest_arg):
    monthly_payment = monthly_payment_arg
    periods = periods_arg
    interest = interest_arg
    pow_i_n = math.pow(1 + interest, periods)
    principal = math.floor(monthly_payment / ((interest * pow_i_n) / (pow_i_n - 1)))
    print(f'Your credit principal = {principal}!')
    print(f'Overpayment = {(monthly_payment * periods) - principal}')

def annuity_monthly_payment(principal_arg, monthly_payment_arg, interest_arg):
    principal = principal_arg
    monthly_payment = monthly_payment_arg
    interest = interest_arg
    month_count = math.ceil(math.log(monthly_payment / (monthly_payment - interest * principal), (1 + interest)))
    months = month_count % 12
    years = month_count // 12
    text = f'{months} month{"s" if months != 1 else ""} to replay the credit'
    if years > 0:
        text = f'{years} year{"s" if years != 1 else ""} and ' + text
    print(f'It takes ' + text)
    print(f'Overpayment = {(monthly_payment * month_count) - principal}')
def check_positive_float(value):
    return_value = float(value)
    if return_value <= 0:
        global values_positive
        values_positive = False
    return return_value / 1200


if len(args) == 5:
    ap = argparse.ArgumentParser()
    ap.add_argument("-t", "--type", required=True)
    ap.add_argument("-p", "--principal", type=check_positive)
    ap.add_argument("-i", "--interest", type=check_positive_float)
    ap.add_argument("-m", "--payment", type=check_positive)
    ap.add_argument("-mo", "--periods", type=check_positive)
    args = vars(ap.parse_args())
    if values_positive and not (args['type'] == 'diff' and args['payment'] is not None) and args[
        'interest'] is not None:
        # print('deu certo')
        if args['type'] == 'annuity':
            if args['payment'] is not None and args['periods'] is not None:
                annuity_monthly(args['payment'], args['periods'], args['interest'])
            elif args['periods'] is None:
                annuity_monthly_payment(args['principal'], args['payment'], args['interest'])
            else:
                # print(args['principal'], args['periods'], args['interest'])
                annuity(args['principal'], args['periods'], args['interest'])
        elif args['type'] == 'diff':
            # print('diff')
            diff(args['principal'], args['periods'], args['interest'])
        else:
            print('Incorrect parameters')
    else:
        print('Incorrect parameters')
else:
    print('Incorrect parameters')
