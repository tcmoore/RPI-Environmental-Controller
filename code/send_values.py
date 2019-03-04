# send values to various outputs, like file, RGB LCD, & STDIO

# Todd Moore
# 3.4.19
def save_valuse(now, temp, temp_alarm, humidity, humidity_alarm, moisture, moisture_alarm,
				density, fan_on, atomizer_on)
Main()
# Variables
	CurrentDateTime 	=	CurrentDateTime;
proper_temp 		=	27		# temp should be 27 Deg C
proper_humidity	=	68		# humidity should be 68%
	proper_moisture	=	77		# soil moisture should be 77 % (??)
	CurrentTempValue 	= 	CurrentTempValue 		# measured current temp
	CurrentHumidValue 	= 	CurrentHumidValue 		# measured current humidity
	CurrentMoistureValue = 	CurrentMoistureValue # measured current soil moisture
	IsAlarm		=	IsAlarm		# is there an alarm
	IsFanOn		=	IsFanOn		# is the exhaust fan on

# --------------------------------------------------------------------
# Format
# Date 		Time		Variable	Proper  Current	Alarm	Fan ON
# -----------------------------------------------------------------------------------------------------------
# 12.12.18      05:30:00	T		27	30		Y	Y
# 12.12.18      05:30:00	H		68	50		Y	Y
# 12.12.18      05:30:00	M		77	50		Y	Y

fopen(values.txt, aw);
printf (‘Date’ /t ‘Time’ /t ‘Variable’ /t ‘Proper’ /t  ‘Current’ /t  ‘Alarm’ /t ‘Fan ON’ /n)
	printf(‘------------------------------------------------------------------------------------------------’);
	printf(CurrentDateTime, /t, ‘T’ /t, proper_temp, /t, CurrentTempValue, /t, IsAlarm, /t, IsFanOn, /n);
	printf(CurrentDateTime, /t, ‘H’ /t, proper_humidity, /t, CurrentHumidValue , /t, IsAlarm, /t, IsFanOn, /n);
	printf(CurrentDateTime, /t, ‘H’ /t, proper_moisture, /t, CurrentMoistureValue, /t, IsAlarm, /t, IsFanOn, /n);
fclose(values.txt);
end;
