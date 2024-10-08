"""
--------------------------------------------------------------------------
Blink USR3 Program
--------------------------------------------------------------------------
License:   
Copyright 2024 - Mustafa Latif

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, 
this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE 
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE 
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF 
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN 
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF 
THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------

Blink USR3 program that will 
  - Blink USR3 LED at 5HZ
    - (5 full on/off cycles per second)
  - reset pin state when program exits

--------------------------------------------------------------------------
"""

# imports
import Adafruit_BBIO.GPIO as GPIO
import time

# define variables and setup USR3 LED as GPIO output
USR3 = "USR3"
GPIO.setup(USR3, GPIO.OUT)

try:
    while True:
        # LED turns on for 0.1 seconds
        GPIO.output(USR3, GPIO.HIGH)
        time.sleep(0.1)
        # LED turns off for 0.1 seconds
        GPIO.output(USR3, GPIO.LOW)
        time.sleep(0.1)
except KeyboardInterrupt:
    # resets LED to "off" state when function interrupted
    GPIO.output(USR3, GPIO.LOW)
    pass

GPIO.cleanup()
    