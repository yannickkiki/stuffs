import warnings


if __name__ == '__main__':
    print('Geeks')

    # displaying the warning message
    warnings.filterwarnings('default')
    warnings.warn('Warning Message: 4', DeprecationWarning)

    print('Geeks !')
