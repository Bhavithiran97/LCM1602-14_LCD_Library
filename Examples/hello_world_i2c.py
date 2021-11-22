# /*******************************************************************************
#  * THIS SOFTWARE IS PROVIDED IN AN "AS IS" CONDITION. NO WARRANTY AND SUPPORT
#  * IS APPLICABLE TO THIS SOFTWARE IN ANY FORM. CYTRON TECHNOLOGIES SHALL NOT,
#  * IN ANY CIRCUMSTANCES, BE LIABLE FOR SPECIAL, INCIDENTAL OR CONSEQUENTIAL
#  * DAMAGES, FOR ANY REASON WHATSOEVER.
#  ********************************************************************************
#  * DESCRIPTION:
#  *
#  * This example show how to connect LCD module with Pico using I2C protocol
#  * 
#  * 
#  * 
#  * CONNECTIONS:
#  * 
#  * Pico SDA 2    - LCD SDA
#  * Pico SCL 3    - LCD SCK
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

from LCD_I2C import *    #import LCD_I2C library
import time

lcd = LCD(sda=2, scl=3)  # Create LCD object with LCD's sda pin connected to PICO's sda pin 2, LCD's sck pin connected to Pico's scl pin 3
lcd.set_cursor(0,0)          # Set the cursor at first column, first row
lcd.write("Hello World")     # Write string to the LCD   
time.sleep(1)               # Delay for 1 second

# scroll functions: scroll both lines right or left by one character cell
for i in range(5):
    lcd.scrollDisplayRight() # scroll message to right of LCD
    time.sleep_ms(200)
time.sleep(1)
for i in range(5):
    lcd.scrollDisplayLeft()  # scroll message back to the left of the LCD
    time.sleep_ms(200)
time.sleep(1)

lcd.off()                    # Off the lcd display without clearing the data
time.sleep(1)

lcd.on()                     # On LCD display without cursor and blink - cursor=False, blink=False - by default
time.sleep(1)

lcd.on(cursor=False, blink=True) # On LCD display without cursor and with blink
time.sleep(1)

lcd.on(cursor=True, blink=False) # On LCD display with cursor and without blink
time.sleep(1)

lcd.on(cursor=True, blink=True)  # On LCD display with cursor and with blink
time.sleep(1.5)

lcd.clear()                 # Clear the data in display
