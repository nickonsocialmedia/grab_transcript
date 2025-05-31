# grab_transcript

cd ~/grab_transcript  # Assuming grab_transcript is in the home dir

chmod +x run.sh       # Unless you've already made it executable

./run.sh              # nothing further needed


HELLO!!!


I was doing research on a book I'm writing, and instead of transcribing videos for hours on end, I was like I wonder if I can just grab the transcript from YouTube using code. I ended up finding this API,


YouTubeTranscriptApi 


https://github.com/jdepoix/youtube-transcript-api/blob/master/youtube_transcript_api/_transcripts.py


Written by,


https://github.com/jdepoix


Honestly its a great API works awesome, but It stores the output file in the folder I didn't like that so it now stores them in, 


/Documents


I also automate everything so when you run my program it will check all assets are installed, and then will prompt you for the video URL, Transcripts for URLs are printed on the screen and stored in /Documents In a text file and until you enter 'q' it will continue to ask for the next URL, It's not complete but it does the trick was never meant to be a full fledged program. I wrote it to save myself time on note taking. 






