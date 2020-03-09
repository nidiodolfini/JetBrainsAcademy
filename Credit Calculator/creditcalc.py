import math
import sys
import argparse

args = sys.argv
values_positive = True


def diff(args):
    print('diff', args)


def annuity(args):
    print('annuity', args)


def check_positive(value):
    return_value = int(value)
    if return_value <= 0:
        global values_positive
        values_positive = False

    return return_value


def check_positive_float(value):
    return_value = float(value)
    if return_value <= 0:
        global values_positive
        values_positive = False
    return return_value


if len(args) == 5:
    ap = argparse.ArgumentParser()
    ap.add_argument("-t", "--type", required=True)
    ap.add_argument("-p", "--principal", type=check_positive)
    ap.add_argument("-i", "--interest", type=check_positive_float)
    ap.add_argument("-m", "--payment", type=check_positive)
    ap.add_argument("-mo", "--periods", type=check_positive)
    args = vars(ap.parse_args())
    # print(ap)
    # print(len(args))
    if values_positive and not (args['type'] == 'diff' and args['payment'] is not None) and args['interest'] is not None:
        if args['type'] == 'annuity':
            annuity(args)
        elif args['type'] == 'diff':
            diff(args)
        else:
            print('Incorrect parameters')
    else:
        print('Incorrect parameters')
else:
    print('Incorrect parameters')
