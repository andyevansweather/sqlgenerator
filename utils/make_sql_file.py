from utils.warninggenerator import warning_generator


def make_file(start, end):
    fo = open("static/downloads/fakewarnings.sql", "w+")

    sql_script = warning_generator(int(start), int(end))

    fo.write("%s" % sql_script)
    fo.close()
