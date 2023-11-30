from pydub import AudioSegment
import os
import glob

currentdir = os.getcwd()

for i in range(1, 4):
    currentfiles = glob.glob(f"{currentdir}/AllScenes/Scene{i}/*.wav")
    currentfolder = os.listdir(f"{currentdir}/AllScenes/Scene{i}")

    # Count the number of files in the folder
    file_count = len(currentfolder)
    print(f"Number of files in Scene{i}: {file_count}")

    # Convert each WAV file to MP3
    for file_path in currentfiles:
        # Extracting the file name without extension
        file_name = os.path.splitext(os.path.basename(file_path))[0]
        output_path = f"{currentdir}/output/{file_name}.mp3"

        # Load the WAV file and export as MP3
        AudioSegment.from_wav(file_path).export(output_path, format="mp3")

        print(f"Converted: {file_path} to {output_path}")
