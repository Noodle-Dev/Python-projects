from pytube import YouTube

link = input("Introduce el link de youtube: ")
yt = YouTube(link)
videos = yt.streams.all()

video = list(enumerate(videos))
for i in video:
    print(i)

print("introduce el formato de descarga")
dn_option = int(input("Introduce la opcion: "))
dn_video = videos[dn_option]
dn_video.download()

print("El video fue descargado exitosamente")