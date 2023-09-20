def NULL_not_found(variable):
    try:
        if variable is None:
            print(f'Nothing: {variable}', type(variable))
        elif isinstance(variable, float) and (variable != variable):
            print(f'Cheese: {variable}', type(variable))
        elif isinstance(variable, bool) and (variable is False):
            print(f'Fake: {variable}', type(variable))
        elif isinstance(variable, int) and (variable == 0):
            print(f'Zero: {variable}', type(variable))
        elif isinstance(variable, str) and variable == '':
            print('Empty: ', type(variable))
        else:
            print('Type not Found')
            return 1
        return 0
    except Exception as e:
        print(f"Exception: {e}")
