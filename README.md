#Music-Visualizer

## TODO this week 1 

- Look into Markdown format
- Look into PIP(pthon package manager)
	- Make sure version I download it for my macos
        - Learn About it
## Music-Visualizer Project Outline

- Figure out to get audio streams into python program
	- Try to get py audio to work on my system 
- Do some simple audio analysis 


- Do a simple visualization(use print function)

## TODO this week 2

- Learn about different bases - 2(binary) - 10(Decimal) - 16(hexadecmial) 

- signed vs unsigned integers & two's compliment
	**bonus** look up how floating point numbers are stored 

	Signed: Signed Binary numbers have one bit dedicated to distingusing whether it is a positve or negative number
	Unsigned: Can not be negative only zero to positive numbers thus not needing or using a desginated bit
	Two's Compliment: take the Binary invert the one's and zero's and add 1 thus getting the negative binary number of 
	any given integer
 
- sample rate
	nyquist theory - this is the justification for the speed at which you should sample something 

	Aliasing: High Frequency signal will appear Low Frequency when sampling at a sampling rate that is too low
	400Hz = 400 cycles of a segement(wave) frequency per second 	
	Nyquist Theorem: Allows you to set a maximum frequency you want to hear and calculate the sampling rate needed to hear it
		-Sampling rate should be double the max frequency 
	Nyquist Rate: Sampling Rate needed to avoid aliasing
	Nyquist Frequency: Maxium Frequency that can be represented given a sampling rate

- Read in a chunk of an audio file & plot using matplotlib
 	Chunk: The format chunk describes how the waveform data is stored and specifies the number of channels, sampling rate, and compression type. 

	Struct: when we read a CHUNK we get a a bunch of data in bytecode. Using struct.unpack() it translates it into int thus making it readible 
## Look into 

- python virtual environments 

- take a look into the struct library

- what is endianess?

## Challenge

Steps to figure out: 
1.data capturing 
2.data analysis - tempo detection etc.. 
2/3.unique ways to diplay it 

Challenge question: why is hexadecmial a great way to compactly represent binary

#TODO this week 3 

#Look Into
plotly and making a 3D plot in real-time(check if possible)
floating vs fixed point


Take the audio signal put a low pass fileter plot on the orginal plot
create a new plot that plots frequency against amplitude(fourier transform) 

averaging filter
low pass filter
median filter
High pass filter etc..
Display different filters to pick out data points 


look into different plotting libraries 

#Plan 
Make a plan for the type of visualtion I wanna create 
find the tools to acomplish this filtering 

Screw around with Game(Look Into) 

