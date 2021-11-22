import machine
import time

COLUMNS = 16
ROWS    = 2

# Instruction Set
CLEARDISPLAY=const(0x01)
CURSORSHIFT=const(0x10)

# display entry mode
ENTRYMODESET=const(0x04)
ENTRYLEFT=const(0x02)
ENTRYRIGHT=const(0x00)
ENTRYSHIFTINCREMENT=const(0x01)
ENTRYSHIFTDECREMENT=const(0x00)

# flags for display/cursor shift
DISPLAYMOVE=const(0x08)
CURSORMOVE=const(0x00)
MOVERIGHT=const(0x04)
MOVELEFT=const(0x00)

# display control
DISPLAYCONTROL=const(0x08)
DISPLAYON=const(0x04)
DISPLAYOFF=const(0x00)
CURSORON=const(0x02)
CURSOROFF=const(0x00)
BLINKON=const(0x01)
BLINKOFF=const(0x00)
SETCGRAMADDR=const(0x40)
SETDDRAMADDR=const(0x80)

# for functionset
FUNCTIONSET=const(0x20)
_5x10DOTS=const(0x04)
_5x8DOTS=const(0x00)
_1LINE=const(0x00)
_2LINE=const(0x08)
_8BITMODE=const(0x10)
_4BITMODE=const(0x00)


class LCD:
    def __init__(self, sda, scl):
        
        self.column = 0
        self.row = 0
        
        self.address = 62
        
        self.command = bytearray(2)

        _sda = machine.Pin(sda)
        _scl = machine.Pin(scl)
        
        if scl == 3 or scl == 7 or scl == 11 or scl == 15 or scl == 19 or scl == 27:
            self.i2c=machine.I2C(1, sda=_sda, scl=_scl, freq=400000)
        else:
            self.i2c=machine.I2C(0, sda=_sda, scl=_scl, freq=400000)
        
        time.sleep_ms(50)
        
        for i in range(3):
            self._command(FUNCTIONSET | _2LINE )
            time.sleep_ms(10)
        
        self.on()
        self.clear()
        
        self._command(ENTRYMODESET | ENTRYLEFT | ENTRYSHIFTDECREMENT)
        
        self.set_cursor(0, 0)
        
    def on(self, cursor=False, blink=False):
        if cursor == False and blink == False:
            self._command(DISPLAYCONTROL | DISPLAYON | CURSOROFF | BLINKOFF)
        elif cursor == False and blink == True:
            self._command(DISPLAYCONTROL | DISPLAYON | CURSOROFF | BLINKON)
        elif cursor == True and blink == False:
            self._command(DISPLAYCONTROL | DISPLAYON | CURSORON | BLINKOFF)
        elif cursor == True and blink == True:
            self._command(DISPLAYCONTROL | DISPLAYON | CURSORON | BLINKON)        
    
    def off(self):
        self._command(DISPLAYCONTROL | DISPLAYOFF | CURSOROFF | BLINKOFF)
        
    def clear(self):
        self._command(CLEARDISPLAY)
        self.set_cursor(0, 0)

    def scrollDisplayRight(self): 
        self._command(CURSORSHIFT | DISPLAYMOVE | MOVERIGHT)

    def scrollDisplayLeft(self): 
        self._command(CURSORSHIFT | DISPLAYMOVE | MOVELEFT)
    
    def set_cursor(self, column, row):
        column = column % COLUMNS
        row = row % ROWS
        if row == 0:
            command = column | 0x80
        else:
            command = column | 0xC0
        self.row = row
        self.column = column
        self._command(command)
    
    def write(self, s):
        for i in range(len(s)):
            time.sleep_ms(10)
            self.i2c.writeto(self.address, b'\x40'+s[i])
            self.column = self.column + 1
            if self.column >= COLUMNS:
                self.set_cursor(0, self.row+1)
        
    def _command(self, value):
        self.command[0] = 0x80
        self.command[1] = value
        self.i2c.writeto(self.address, self.command)
        time.sleep_ms(1)
