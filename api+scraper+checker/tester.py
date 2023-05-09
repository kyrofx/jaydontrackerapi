import subprocess


def check_jaydon():
    process = subprocess.Popen(['scrapy', 'runspider', 'jaydonscraper.py'], stdout=subprocess.PIPE)
    output, error = process.communicate()
    output = output.decode('utf-8')
    # print(output)

    # print(output)
    if "True" in output:
        result = True
    else:
        result = False

    return result


check_jaydon()
