###[ SIMPLE CODING ]###

###[ ANDA TOBAT DI HARI INI ]###
import os, sys, time, json, random, platform, requests, rich, re
from datetime import datetime
from os import system as sis
from time import time as tim
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
###[ IMPORT PANEL AND RICH ]###
from rich.panel import Panel
from rich import print as prints

###----------[ WARNA PRINT RICH ]---------- ###
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
###----------[ WARNA PRINT RICH ]---------- ###
os.system('clear')
prints(Panel(f"""{P2}[{M2}01{P2}] Sholawatan jibril
{P2}[{M2}02{P2}] Sholawatan solla alaikallahu
{P2}[{M2}03{P2}] Sholawatan syaikona
{P2}[{M2}04{P2}] Sholawatan robi qola
{P2}[{M2}05{P2}] Sholawatan dhiyaahu""",title=f'{B2}SHOLAWATAN'))
prints(Panel(f"""{P2}[{H2}06{P2}] Ceramah V1
[{H2}07{P2}] Ceramah V2
[{H2}08{P2}] Ceramah V3""",title=f'{B2} CERAMAH'))
watan = input(f'(?) pilih : ')
if watan in ['1','01']:
    cetak(nel("""[green]SEDANG MEMUTAR SHOLAWAT"""))
    os.popen('play-audio jibril.mp3')
    ra = input('[enter untuk kembali]')
elif watan in ['2','02']:
            cetak(nel("""[green]SEDANG MEMUTAR SHOLAWAT"""))
            os.popen('play-audio alai.mp3')
            ra = input(f'[enter untuk kembali]')
elif watan in ['3','03']:
        cetak(nel("""[green]SEDANG MEMUTAR SHOLAWAT...."""))
        os.popen('play-audio syaikona.mp3')
        ina = input(f'[{M} ENTER UNTUK KEMBALI {P}]')
elif watan in ['4','04']:
    cetak(nel("""[green]SEDANG MEMUTAR SHOLAWAT...."""))
    os.popen('play-audio robiqola.mp3')
    ras = input('[teken enter untuk kembali]')
elif watan in ['5','05']:
	cetak(nel("""[green]SEDANG MEMUTAR SHOLAWAT...."""))
	os.popen('play-audio dhiyaahu.mp3')
	rasu = input(f'{P}[{M} ENTER UNTUK KEMBALI {P}]')
elif watan in ['6','06']:
	cetak(nel("""[green]SEDANG MEMUTAR CERAMAH...."""))
	aaa = input(f'{P}[{M} ENTER UNTUK KEMBALI {P}]')
	os.popen('play-audio cermahV1.mp3')
elif watan in ['7','07']:
	cetak(nel("""[green]SEDANG MEMUTAR CERAMAH...."""))
	os.popen('play-audio ceramahV2.mp3')
elif watan in ['08','8']:
	cetak(nel("""[green]SEDANG MEMUTAR CERAMAH"""))
	os.popen('play-audio ceramahV3.mp3')