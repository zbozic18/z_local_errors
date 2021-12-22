import datetime


def save_error(error: str):
    """
    Save an error locally on errors.txt file.

    :param error: required
    :type error: string
    :return:
    """

    current_time = datetime.datetime.now()
    file1 = open('errors.txt', 'a')
    file1.write(f'{current_time}: {error} \n')
    file1.close()
