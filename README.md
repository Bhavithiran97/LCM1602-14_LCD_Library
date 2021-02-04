# LCM1602A-14 LCD Library for MicroPython
This library supports LCM1602A-14 LCD module I2C and SPI communication with Raspberry Pi Pico. 
**The library file must be saved inside the Raspberry Pi Pico before uploading user's code**

![1](https://user-images.githubusercontent.com/34527010/106834022-980a3000-66cf-11eb-9ffe-f6febd25de34.PNG)

## Import LCD_SPI Library

 - Import LCD_SPI library
 
 `from LCD_SPI import *`

## Import LCD_I2C Library

 - Import LCD_I2C library
 
`from LCD_I2C import *`

## Create Object for SPI

 -  Create object using the class
 -  Create LCD object with LCD's sck pin connected to PICO's sck pin 2, LCD's sda pin 	connected to Pico's tx pin 3
 
 `lcd = LCD(sck=2, scl=3)  `

## Create Object for I2C
 -  Create object using the class
 - Create LCD object with LCD's sda pin connected to PICO's sda pin 2, LCD's sck pin connected to Pico's scl pin 3
 
`lcd = LCD(sda=2, scl=3)`

## Set cursor

 - Set the cursor to a specific position
 - First parameter sets the column, second parameter sets the row
 - Set the cursor to column 0 (first column) and row 0 (first row)
 
 `lcd.set_cursor(0,0) `

## On LCD Display

 - Turn on the LCD Display without clearing the data
 - Cursor and Blink is Off by default
 
`lcd.on()`

 - Cursor On, Blink Off
 
`lcd.on(cursor=True, blink=False)`

 - Cursor Off, Blink On
 
`lcd.on(cursor=False, blink=True) `

 - Cursor On, Blink On
 
`lcd.on(cursor=True, blink=True) `

## Off LCD Display

 - Turn off the LCD Display without clearing the data
 
`lcd.off() `

## Write to LCD Display

 - Write string to the LCD  
 
`lcd.write("Hello World")`

## Clear LCD Display

 - Clear the data on the display
 
 `lcd.clear() `
