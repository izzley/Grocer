#!/bin/bash

cd ~/repos/Grocer/
PATH = $PATH:.venv/bin
export PATH
scrapy crawl woolies
