import matplotlib.pyplot as plt
import numpy as np
import pandas

months = { 'January' : 0, 
'February' : 0, 
'March' : 0, 
'April' : 0, 
'May' : 0, 
'June' : 0, 
'July' : 0, 
'August' : 0, 
'September' : 0, 
'October' : 0, 
'November' : 0, 
'December' : 0} 

def zerostr(height):
   #function to prevent 0s from showing up as labels on the bad graph
   if height==0:
      return ''
   else:
      return int(height)

def plot_bar_x(number):
    # this is for plotting a bar graph
    index = np.arange(len(months))
    mybars=plt.bar(index, months.values())
    plt.xticks(index, months.keys(), fontsize=6, rotation=45, color='gray')
    plt.tick_params(right=False, top=False, left=False, bottom=False, labelleft=False, labelbottom=True)
    plt.box(False)
    #set top limit to max number of tweets
    plt.ylim(top=4800)
    for bari in mybars:
      height = bari.get_height()
      plt.gca().text(bari.get_x() + bari.get_width()/2, bari.get_height()*1.01, str(zerostr(height)), 
      ha='center', color='gray', fontsize=6)
    #save the images to desktop > twprog > twgraphxxx.png
    plt.savefig('~/Desktop/twproj/twgraph{}.png'.format(number))
    plt.clf()

if __name__ == "__main__":
    
    #read tweets.csv from Desktop
    df = pandas.read_csv('~/Desktop/ref docs/tweets.csv', parse_dates=['timestamp'])
    df_mthonly = df['timestamp'].apply(lambda x: x.strftime('%B'))

    twcount = 0
    imgcount = 0

    #loop mths column in reverse, call graph generator every 100 tweets/end of line
    for i in reversed(df_mthonly):
       months[i] = months[i]+1
       twcount=twcount+1
       #call the graphing function every 100 tweets, and on the last tweet
       if (twcount%100==0 and twcount<df_mthonly.size) or (twcount==df_mthonly.size):
          imgcount = imgcount+1
          plot_bar_x(imgcount)

'''
In order to put the tweet graphs all into one video, you'll need to install ffmpeg, and call it with the following parameters:
ffmpeg -f image2 -framerate 60 -i /path/to/input/folders/twgraph%01d.png -c:v mpeg4 -q 2 -y /path/to/output/filename.mp4
ffmpeg -f image2 -framerate 60 -i ~/Desktop/twproj/twgraph%01d.png -c:v mpeg4 -q 2 -y ~/Desktop/twproj/twgraph60fps.mp4

-f image2        : calls image demuxer
-framerate 60    : sets framerate of result to 60fps
-c:v mpeg4       : sets format of output to mpeg4
-q 2             : set quality to 2
-i               : input path
-y               : output path
'''
