import boto3
import urllib.request, urllib.parse, urllib.error
import json
import re
import logging
import os
import copy
import json
import re
import zlib
from collections import OrderedDict


name = "traceur-agg-log-wsj-waf234"
print(name.split("-")[2])