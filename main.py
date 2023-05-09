import scrapy
from flask import Flask, jsonify
import subprocess


def check_jaydon():
    process = subprocess.Popen(['python', 'jaydonscraper.py'], stdout=subprocess.PIPE)
    output, error = process.communicate()
    output = output.decode('utf-8')
    if "Found Jaydon!" in output:
        result = {'jaydon': True}
    else:
        result = {'jaydon': False}
    print(result)



check_jaydon()