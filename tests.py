import pyaudio
import numpy
import os

FORMAT = pyaudio.paInt16
SAMPLEFREQ = 44100
FRAMESIZE = 1024
NOFFRAMES = 220

p = pyaudio.PyAudio()

for word in ["Hoch", "Tief", "Links", "Rechts"]:
    for i in range(1, 6):

        input(f"Enter drücken und {word} sagen ({i}/5)")

        stream = p.open(
            format=FORMAT,
            channels=1,
            rate=SAMPLEFREQ,
            input=True,
            frames_per_buffer=FRAMESIZE
        )

        print("Aufnahme läuft!")

        data = stream.read(
            NOFFRAMES * FRAMESIZE,
            exception_on_overflow=False
        )

        stream.stop_stream()
        stream.close()

        decoded = numpy.frombuffer(data, dtype=numpy.int16)

        numpy.save(f"data/Testdaten_M/{word}_{i}_M", decoded)

        print("Gespeichert!")

p.terminate()