import speech_recognition
import os
from os import path
from pydub import AudioSegment

class audio_transcription:

        # SYSTEM TRANSCRIBES AUDIO, TAKES MP3 FILE PATH STRING AS INPUT
        def transcribe_audio(self, audio_file):
                '''This function transcribes audio into text'''
                sound = AudioSegment.from_mp3(audio_file)

                # SYSTEM RETRIVES FILENAME FROM THE FILE PATH
                new_filename = (os.path.basename(audio_file))

                # SYSTEM REMOVES FILE EXTENSION FROM FILE NAME
                new_filename = new_filename[:-4]

                # SYSTEM ADDS WAV FILE EXTENSION TO FILE NAME & EXPORTS
                new_filename = (new_filename+".wav")
                sound.export(new_filename, format="wav")

                output_filename = new_filename[:-4]
                output_filename = (output_filename+".txt")
                output_file = open(output_filename, "w")

                # TRANSCRIBE AUDIO
                language_processor = speech_recognition.Recognizer()
                with speech_recognition.AudioFile(new_filename) as source:
                        # SYSTEM READS IN AUDIO FILE
                        audio = language_processor.record(source)
                        output_file.write(language_processor.recognize_google(audio))
                output_file.close()