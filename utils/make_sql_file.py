"""Creates an SQL file, does reading and writing here"""

from utils.warninggenerator import warning_generator


def make_file(start, end):
    """
    creates the file by doing reading and writing
    :param start: start days after today's date
    :param end: end days after today's date
    :return: SQL file gets created
    """
    fo = open("static/downloads/fakewarnings.sql", "w+")

    sql_script = warning_generator(int(start), int(end))

    fo.write("%s" % sql_script)
    fo.close()
