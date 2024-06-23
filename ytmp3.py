from pytube import YouTube
import os

def download_mp3(url):
    try:
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        
        destination = '.' 
        print(f"Downloading {yt.title}...")
        
        out_file = audio_stream.download(output_path=destination)
        
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        
        print(f"{yt.title} has been successfully downloaded as MP3.")
        
    except Exception as e:
        print(f"Error downloading {url}: {str(e)}")

def main():
    file_path = 'youtube_urls.txt'  
    
    try:
        with open(file_path, 'r') as file:
            urls = file.read().splitlines()
        
        for url in urls:
            download_mp3(url)
            
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except Exception as e:
        print(f"Error reading URLs from file: {str(e)}")

if __name__ == "__main__":
    main()
