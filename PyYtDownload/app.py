from crypt import methods
from flask import Flask, render_template, request, Response, redirect, send_file
import os
from os import remove
import pafy
import moviepy.editor as mp

app = Flask(__name__)

path = os.getcwd() + "/output"

@app.route('/')
def route():
    return render_template('index.html')

#Cuidado con la sangria(TAB)
@app.route('/envia', methods=['GET', 'POST'])
def envia():  #Esto debe tener esta posicion
        if request.method == 'POST':
            url = request.form['url']
            video= pafy.new(url)
            best = video.getbest(preftype="MP4")
            best.download(path)
            p = path + video.tilte + ".mp4"
        
        return send_file(p,as_attachment=True)

@app.route('/envia2', methods=['GET','POST'])
def envia2():
    if request.method == 'POST':
            url = request.form['url']
            video= pafy.new(url)
            best = video.getbest(preftype="MP4")
            best.download(path)
            name = path + video.tilte + ".mp4"
            clip = mp.VideoFileClip(name)
            clip.audio.write_audiofile(path+ video.tilte + ".mp3")
            p = path + video.tilte + ".mp3"
            
    return send_file(p, as_attachment=True)
if __name__ == '__main__':
    app.run(host='localhost')