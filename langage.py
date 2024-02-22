import os
import speech_recognition as sr
import moviepy.editor as mp

def extract_audio_from_video(video_path, audio_path):
    video = mp.VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path)

def identify_spoken_language(audio_path, languages=['en-US', 'fr-FR', 'es-ES', 'de-DE']):
    recognizer = sr.Recognizer()
    transcriptions = {}

    for lang in languages:
        with sr.AudioFile(audio_path) as source:
            audio = recognizer.record(source)
        
        try:
            transcribed_text = recognizer.recognize_google(audio, language=lang)
            transcriptions[lang] = transcribed_text
        except sr.UnknownValueError:
            transcriptions[lang] = ""

    identified_language = max(transcriptions, key=lambda k: len(transcriptions[k]))

    return identified_language, transcriptions[identified_language]

def write_language_to_file(language, output_file):
    with open(output_file, 'w') as file:
        file.write(language)

def main():
    video_name = input("Entrez le chemin du fichier vidéo : ")
    video_path = f"Input_videos/{video_name}"

    if not os.path.exists(video_path):
        print("Erreur : fichier introuvable.")
        return

    audio_path = 'temp_audio.wav'
    extract_audio_from_video(video_path, audio_path)

    identified_language, transcription = identify_spoken_language(audio_path)

    if identified_language:
        print(f"Langue détectée dans la vidéo : {identified_language}")
        print("Transcription :")
        print(transcription)
        identified_language = identified_language[:2]
        # Écrire la langue identifiée dans un fichier
        write_language_to_file(identified_language, 'langue.txt')
        print("Langue identifiée écrite dans identified_language.txt.")
    else:
        print("Échec de l'identification de la langue.")

    os.remove(audio_path)

if __name__ == "__main__":
    main()
