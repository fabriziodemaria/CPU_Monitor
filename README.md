# CPU_Monitor

Graph generator that is able to monitor the CPU usage of a single process in your Linux machine. Uses gnuplot to print the graph of CPU usage and it provides the average value over the time of script execution.

![alt tag](https://raw.githubusercontent.com/fabriziodemaria/CPU_Monitor/master/example/image.png)

## Usage
You need to have gnuplot installed on your machine.
Execute the script:
<pre>python cpu_monitor <PID> <SAMPLES></pre>

Samples represents how many samples are processed before terminating the script and producing the graph. According to your machine, the (number_of_samples/seconds) might be different.
Future work is to include a timer instead of samples as input parameter.
Accuracy of this tool strongly depends on the interval among the samples but it can give a good prospective of the impact of a single program on the CPU in your environment.

The tool has been developed and tested on a Ubuntu machine.
