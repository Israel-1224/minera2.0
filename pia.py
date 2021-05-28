import requests
import io
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate
from typing import Tuple, List
import re
from datetime import datetime
import plotly
import plotly.graph_objects as go

df = pd.read_csv('C:\Users\Admin\Documents\semestre\mineria\Adidas_Vs_Nike.csv')
df.head()