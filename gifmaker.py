import imageio
import os

clip = os.path.abspath((""))

def gifMaker(inputPath, targetFormat):
    outputPath = os.path.splitext(inputPath)[0] + targetFormat # split the file and extension aprt

    print("Converting file")

    reader = imageio.get_reader(inputPath)
    fps = reader.get_meta_data()['fps']

    writer = imageio.get_writer(outputPath, fps= fps)

    for frames in reader:
        #read img and make gif
        writer.append_data(frames)
       
    print("Completed")
    writer.close()


gifMaker(clip, '.gif')