from pytube import *
import os


#make break in else
while True:
    #type the url
    inputted_url = input('Enter the video: ')
    url = inputted_url

    #Get everything after the = in the url
    head, sep, tail = inputted_url.partition('=')

    #put together the url after being seperated
    if inputted_url == 'https://www.youtube.com/watch?v='+ tail:
        the_video = YouTube(url)
        print("--------------------Video Title--------------------")

        #prints the video title
        print(the_video.title)

        #gives the user the best resoultion usally 1080p
        the_video = the_video.streams.get_highest_resolution()

        # Break the loop if they enter a proper url
        break
    else:
        print("Url doesnt seem correct please try again")

print("--------------------Downloading--------------------")

while True:
    # Made the decsion to be able to make a mp4 file
    inputted_decision  = input('Mp4 or Mp3: ')
    if inputted_decision == 'Mp4' or inputted_decision == 'mp4' or inputted_decision == '4':
        original_file = the_video.download()
        break

    # Made the decsion to be able to make a mp3 file
    elif inputted_decision == 'Mp3' or inputted_decision == 'mp3' or inputted_decision == '3':
        original_file = the_video.download()
        base, ext = os.path.splitext(original_file)
        modified_file = base + '.mp3'
        os.rename(original_file, modified_file)
        break

print(" ")
print(" ")

print("--------------------Downloaded--------------------")




#For the understanding of the checker https://bit.ly/3tSpumR that helped me to understand
#Thank you for the help with file management with .gitignore (https://github.com/Ethan-Francolla)
