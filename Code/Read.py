# DSMR P1 uitlezen
# (c) 10-2012 - GJ - gratis te kopieren en te plakken
versie = "1.0"
import sys
import serial

##############################################################################
#Main program
##############################################################################
print ("DSMR P1 uitlezen",  versie)
print ("Control-C om te stoppen")
print ("Pas eventueel de waarde ser.port aan in het python script")

#Set COM port config
ser = serial.Serial()
ser.baudrate = 	115200
ser.bytesize=serial.SEVENBITS
ser.parity=serial.PARITY_EVEN
ser.stopbits=serial.STOPBITS_ONE
ser.xonxoff=0
ser.rtscts=0
ser.timeout=20
ser.port="/dev/ttyUSB0"

#Open COM port
try:
    ser.open()
except:
    sys.exit ("Fout bij het openen van %s. Aaaaarch."  % ser.name)


#Initialize
#p1_teller is mijn tellertje voor van 0 tot 20 te tellen
p1_teller=0
stack=[]

while p1_teller < 20:
    p1_line=''
#Read 1 line van de seriele poort
    try:
        p1_raw = ser.readline()
    except:
        sys.exit ("Seriele poort %s kan niet gelezen worden. Aaaaaaaaarch." % ser.name )
    p1_str=str(p1_raw)
    p1_line=p1_str.strip()
    stack.append(p1_line)
# als je alles wil zien moet je de volgende line uncommenten
    # print (p1_line)
    p1_teller = p1_teller +1

#Initialize
# stack_teller is mijn tellertje voor de 20 weer door te lopen. Waarschijnlijk mag ik die p1_teller ook gebruiken
stack_teller=0

while stack_teller < 20:
   if stack[stack_teller][0:11] == "b'1-0:1.8.1":
    print("daldag     ", stack[stack_teller][12:22])
   elif stack[stack_teller][0:11] == "b'1-0:1.8.2":
    print("piekdag    " , stack[stack_teller][12:22])
# Daltarief, teruggeleverd vermogen 1-0:2.8.1
   elif stack[stack_teller][0:11] == "b'1-0:2.8.1":
    print("dalterug   ", stack[stack_teller][12:22])
# Piek tarief, teruggeleverd vermogen 1-0:2.8.2
   elif stack[stack_teller][0:11] == "b'1-0:2.8.2":
        print("piekterug  ", stack[stack_teller][12:22])
# Huidige stroomafname: 1-0:1.7.0
   elif stack[stack_teller][0:11] == "b'1-0:1.7.0":
        print("afgenomen vermogen      ", int(float(stack[stack_teller][12:18])*1000), " W")
# Huidig teruggeleverd vermogen: 1-0:1.7.0
   elif stack[stack_teller][0:11] == "b'1-0:2.7.0":
        print("teruggeleverd vermogen  ", int(float(stack[stack_teller][12:18])*1000), " W")
# Gasmeter: 0-1:24.3.0
   elif stack[stack_teller][0:11] == "b'0-1:24.3.0":
        print("Gas                     ", int(float(stack[stack_teller+1][1:10])*1000), " dm3")
   else:
    pass
   stack_teller = stack_teller +1

# print(stack, '\n')

#
# add de data to an array for sending to IoT hub
#



#Close port and show status
try:
    ser.close()
except:
    sys.exit ("Oops %s. Programma afgebroken. Kon de seriele poort niet sluiten." % ser.name )
