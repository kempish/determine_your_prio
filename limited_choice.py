from msvcrt import getwch

def limited_choice(*args):
    while True:
        ask = getwch()
        if ask.capitalize() in args:
            return ask.capitalize()
        else:
            arguments = ' | '.join(args)
            print(f'You entered wrong data\n'
                f'Enter: {arguments}')
            # limited_choice(*args) # when function is repeated - there is no value here (*args return None) | improve limited_choice_int as well


def limited_choice_int(*args):
    while True:
        ask = getwch()

        try:
            ask = int(ask)
        except:
            ask = str(ask)

        if ask in args:
            return int(ask)
        else:
            str_args = tuple(map(lambda x: str(x), args))
            arguments = ' | '.join(str_args)
            print(f'You entered wrong data\n'
                f'Enter: {arguments}')