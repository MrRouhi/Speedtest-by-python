from speedtest import Speedtest

obj = Speedtest()
print(f'Download Speed : {obj.download()}')
print(f'Upload Speed : {obj.upload()}')