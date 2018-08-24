compiler = 'C:\\Users\\Public\\Documents\\Mikroelektronika\\mikroC PRO for PIC\\mikroCPIC1618.exe'

settings = {
    'cmdln0': '"{compiler}" -MSF -DBG -p{device} -GC -DL -O11111110 -fo{clock} -N"{project}" "{filename}"',
    'cmdlnSP': '-SP"{path}"',
    'cmdlnIP': '-IP"{path}"',
    'cmdlnLIBS': '"__Lib_Math.mcl" "__Lib_MathDouble.mcl" "__Lib_System.mcl" "__Lib_Delays.mcl" "__Lib_CType.mcl" "__Lib_CString.mcl" "__Lib_CStdlib.mcl" "__Lib_CMath.mcl" "__Lib_MemManager.mcl" "__Lib_Conversions.mcl" "__Lib_Sprinti.mcl" "__Lib_Sprintl.mcl" "__Lib_Time.mcl" "__Lib_Trigonometry.mcl" "__Lib_Button.mcl" "__Lib_Keypad4x4.mcl" "__Lib_Manchester.mcl" "__Lib_OneWire.mcl" "__Lib_PS2.mcl" "__Lib_Sound.mcl" "__Lib_SoftI2C.mcl" "__Lib_SoftSPI.mcl" "__Lib_SoftUART.mcl" "__Lib_EEPROM.mcl" "__Lib_LcdConsts.mcl" "__Lib_Lcd.mcl" "__Lib_S1D13700.mcl"',
}