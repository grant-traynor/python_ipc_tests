# python_ipc_tests
I/O Throughput / Exchange performance tests for various IPCs and Threaded / Multiprocessing methods in python

# Simple Result Overview
```
50,000 Messages                                     Time(s)    /msg(us)   msg/sec
pipetest01 - Protocol.method                          5.9        120        8400
pipetest02 - Protocol.Class - localhost               3.8         77       12950
pipetest03 - Protocol.Class - UDS                     3.1         65       15000
pipetest04 - Protocol.Class - UDS + uvloop            0.4          9      110000
pipetest05 - Protocol.Class - lclhst + uvloop         0.4          9      110000
pipetest06 - coroutines - direct                      0.1          3      350000
pipetest07 - coroutines - direct + uvloop             0.1          3      350000
pipetest08 - function call - no asyncio               0.007        0.1   6723141

threads - ping - deque                                2.9          4.2   1717032
threads - ping - Queue                                2.0          4.1     23600
```
# Machine Spec
8 Cores as follows
```
cat /proc/cpuinfo 
processor	: 0
vendor_id	: GenuineIntel
cpu family	: 6
model		: 45
model name	: Intel(R) Xeon(R) CPU E5-1620 0 @ 3.60GHz
stepping	: 7
microcode	: 0x710
cpu MHz		: 1334.006
cache size	: 10240 KB
physical id	: 0
siblings	: 8
core id		: 0
cpu cores	: 4
apicid		: 0
initial apicid	: 0
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 cx16 xtpr pdcm pcid dca sse4_1 sse4_2 x2apic popcnt tsc_deadline_timer aes xsave avx lahf_lm epb pti tpr_shadow vnmi flexpriority ept vpid xsaveopt dtherm ida arat pln pts
bugs		: cpu_meltdown spectre_v1 spectre_v2
bogomips	: 7182.54
clflush size	: 64
cache_alignment	: 64
address sizes	: 46 bits physical, 48 bits virtual
power management:
```
