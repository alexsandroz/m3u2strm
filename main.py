import tools
import logger
import streamClasses
import wget
import sys
import os

ipttvurl = 'http://iptvagora.ddns.net:25461/get.php?username=421441806&password=421441806&type=m3u_plus&output=ts' #replace url with your link, or comment this line out and put the filename in the streamlist below.

filename = 'm3u/iptmovies.m3u'
# if os.path.exists(filename):
#     os.remove(filename)

# print(wget.download(ipttvurl, (filename))) #if not downloading comment out this line.

apollomovies = streamClasses.rawStreamList(filename)

