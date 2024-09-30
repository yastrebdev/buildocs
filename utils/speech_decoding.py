# try:
#     import whisper
# except KeyboardInterrupt:
#     print("Didn't have time to import whisper")
#
# from pydub import AudioSegment
#
# def ogg_to_mp3(file):
#     audio = AudioSegment.from_ogg(file)
#     mp3_file = 'audio.mp3'
#     audio.export(mp3_file, format='mp3')
#     return mp3_file
#
#
# def speach_recognition(*, voice, model='small'):
#     model = whisper.load_model(model)
#
#     audio = ogg_to_mp3(voice)
#
#     result = model.transcribe(audio, fp16=False)
#
#     return result["text"]