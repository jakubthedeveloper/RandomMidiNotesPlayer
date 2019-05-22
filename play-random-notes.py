import rtmidi
import random
import time

midiout = rtmidi.RtMidiOut()
ports = range(midiout.getPortCount())

if ports:
    print("Available MIDI output ports:")
    
    for i in ports:
        print(str(i) + ': ' + midiout.getPortName(i))
    
else:
    print('No MIDI output ports available')
    exit()
    
midiPort = int(input("Select a port: "))

if (midiPort < 0 or midiPort > len(ports)):
    print('Invalid port. Bye.')
    exit()

midiChannel = int(input("Select MIDI Channel (default 1): "))
if (midiChannel < 0 or midiChannel > 16):
    print('Invalid channel. Bye.')
    exit()

midiout.openPort(midiPort)

try:
    count = 100
    while count > 0:
        keyNumber = int(random.random() * 128)
        velocity = int(random.random() * 128)
        
        midiout.sendMessage(rtmidi.MidiMessage.noteOn(midiChannel, keyNumber, velocity))
        ts = random.random() * 0.5
        time.sleep(ts)
        midiout.sendMessage(rtmidi.MidiMessage.noteOff(midiChannel, keyNumber))
        count = count - 1
except KeyboardInterrupt:
    midiout.sendMessage(rtmidi.MidiMessage.allNotesOff(midiChannel))
    print("\nWhy did you stop?")


