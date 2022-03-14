from pytube import *
import os

#make break in else 

#type the url
inputted_url = input('Enter the video: ')
url = inputted_url

#Get everything after the = in the url
head, sep, tail = inputted_url.partition('=')

#put together the url after being seperated 
if inputted_url == 'https://www.youtube.com/watch?v='+ tail:
    the_video = YouTube(url)
    print("*********************Video Title************************")

    #prints the video title
    print(the_video.title)
    
    #gives the user the best resoultion usally 1080p
    the_video = the_video.streams.get_highest_resolution()

    print("*********************Downloading************************")

    inputted_decision  = input('Mp4 or Mp3: ')
    original_file = the_video.download()


    if inputted_decision == 'Mp4' 'mp4' '4':
        the_video.download()

    elif inputted_decision == 'Mp3' 'mp3' '3':
        the_video.download()
        base, ext = os.path.splitext(original_file)
        modified_file = base + '.mp3'
        os.rename(original_file, modified_file)
        os.remove(original_file + ".mp4")
    print(" ")
    print(" ")

    print("*********************Downloaded************************")



else:
    print("Url doesnt seem correct please try again")
    inputted_url = input('Enter the video: ')
    
    



   
