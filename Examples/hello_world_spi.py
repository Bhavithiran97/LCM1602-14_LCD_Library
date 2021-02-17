# /*******************************************************************************
#  * THIS SOFTWARE IS PROVIDED IN AN "AS IS" CONDITION. NO WARRANTY AND SUPPORT
#  * IS APPLICABLE TO THIS SOFTWARE IN ANY FORM. CYTRON TECHNOLOGIES SHALL NOT,
#  * IN ANY CIRCUMSTANCES, BE LIABLE FOR SPECIAL, INCIDENTAL OR CONSEQUENTIAL
#  * DAMAGES, FOR ANY REASON WHATSOEVER.
#  ********************************************************************************
#  * DESCRIPTION:
#  *
#  * This example show how to connect LCD module with Pico using SPI protocol
#  * 
#  * 
#  * 
#  * CONNECTIONS:
#  * 
#  * Pico TX 2     - LCD SDA
#  * Pico SCK 3    - LCD SCK
#  * Pico CSn 5    - LCD CS
#  * Pico 3V3(OUT) - LCD VDD
#  * Pico GND      - LCD VSS
#  * 
#  *
#  *
#  * AUTHOR   : Bhavithiran
#  * COMPANY  : Cytron Technologies Sdn Bhd
#  * WEBSITE  : www.cytron.io
#  * EMAIL    : support@cytron.io
#  *
#  *******************************************************************************/

from LCD_SPI import *    #import LCD_SPI library

lcd = LCD(sck=2, tx=3, cs=5)  # Create LCD object with LCD's sck pin connected to PICO's sck pin 2, LCD's sda pin connected to Pico's tx pin 3, LCD's cs pin connected to Pico's CSn pin 5
lcd.set_cursor(0,0)          # Set the cursor at first column, first row
lcd.write("Hello World")     # Write string to the LCD   
utime.sleep(1)               # Delay for 1 second

lcd.off()                    # Off the lcd display without clearing the data
utime.sleep(1)

lcd.on()                     # On LCD display without cursor and blink - cursor=False, blink=False - by default
utime.sleep(1)

lcd.on(cursor=False, blink=True) # On LCD display without cursor and with blink
utime.sleep(1)

lcd.on(cursor=True, blink=False) # On LCD display with cursor and without blink
utime.sleep(1)

lcd.on(cursor=True, blink=True)  # On LCD display with cursor and with blink
utime.sleep(1.5)

lcd.clear()                 # Clear the data in display
