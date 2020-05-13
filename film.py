from requests import get
import re,html,json,os
from threading import Thread as td
urllist = """http://ok.ru/video/1591322479169 1
http://ok.ru/video/1591325624897 2
http://ok.ru/video/1591328705089 3
http://ok.ru/video/1591337749057 4
http://ok.ru/video/1591338994241 5
http://ok.ru/video/1591348234817 6
http://ok.ru/video/1591363701313 7
http://ok.ru/video/1591365536321 8
http://ok.ru/video/1591368550977 9
http://ok.ru/video/1591370320449 10
http://ok.ru/video/1591322479169 11
http://ok.ru/video/1591325624897 12
http://ok.ru/video/1591328705089 13
http://ok.ru/video/1591337749057 14
http://ok.ru/video/1591338994241 15
http://ok.ru/video/1591348234817 16
http://ok.ru/video/1591363701313 17
http://ok.ru/video/1591365536321 18
http://ok.ru/video/1591368550977 19
http://ok.ru/video/1591370320449 20
http://ok.ru/video/1591322479169 21
http://ok.ru/video/1591328705089 22
http://ok.ru/video/1591337749057 23
http://ok.ru/video/1591338994241 24
http://ok.ru/video/1591348234817 25
http://ok.ru/video/1591363701313 26
http://ok.ru/video/1591365536321 27
http://ok.ru/video/1591368550977 28 
http://ok.ru/video/1591370320449 29
http://ok.ru/video/1591322479169 30"""


def sizes(size):
	for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
		if size < 1024.0:
			return "%3.1f %s" % (size, x)
		size /= 1024.0
	return size
def getb(f,episod):
	x = get(f)
	xx = open(f"Umar_Bin_Khatab_Episode_{episod}.mp4","wb")
	xx.write(x.content)
	return x.content
def gas(u,episode):
	bb = bytearray()
	if len(u) != 0:
			r = get(u.split()[0],headers={"User-agent":"Mozilla/5.0 (Linux; Android 9; Redmi Note 5A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36"})
			v = re.search(r'data\-video\=\"(.*?)\"',r.text).group(1)
			data = json.loads(html.unescape(v))
			ur = data["videoSrc"]
			x = get(ur,headers={"User-agent":"Mozilla/5.0 (Linux; Android 9; Redmi Note 5A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36"})
			u = re.findall(r'http[s]:\/\/.*?\/video\/',x.text)
			print("mengambil frame..")
			y = get(u[0]).text
			z = re.findall(r'LOWEST.*?.ts',y)
			print("banyaknya frame: ",len(z))
			n = 1
			for f in z:
				print(f"mendownload frame \033[92m{n}\033[0m..",end="")
				b = getb(u[0]+f,episode)
				bb += b
				print(f" sukses! \033[92m({sizes(len(bb))})\033[0m")
				n+=1
if __name__=='__main__':
	os.system("clear")
	print("""
\033[92mok.ru video downloader\033[0m
\033[93mhttps://t.me/om_karjok\033[0m
""")
	print("pilih episode")
	urll = []
	for i in urllist.split("\n"):
		i = i.split()
		print(f"\033[92m{i[1]}. \033[0mEpisode ",i[1])
		urll.append(i[0])
	ux = int(input("nomor: ")) -1
	print("mengakses video episode ",ux+1)
	print("mengambil informasi video..")
	gas(urll[ux],str(ux+1))
