#%% Functions to update layouts

## Returns a list of parameters
def paramNameList():
    paramNameList = ['Lower Rate Limit       ', 'Upper Rate Limit       ','Maximum Sensor Rate    ','Fixed AV Delay         ','Dynamic AV Delay       ',
                'Sensed AV Delay Offset ','Atrial Amplitude       ','Ventricular Amplitude  ','Atrial Pulse Width     ','Ventricular Pulse Width',
                'Atrial Sensitivity     ','Ventricular Sensitivity','    VRP                ','    ARP                ','    PVARP              ',
                'PVARP Extension        ','  Hysteresis           ',' Rate Smoothing        ','ATR Duration           ','ATR Fallback Mode      ',
                'ATR Fallback Time      ','Activity Threshold     ','Reaction Time          ','Response Factor        ','Recovery Time          ']
    return paramNameList
#Determines which pacing paramters will be active based on the pacing mode
def pacingModePar(paceMode):
    if(paceMode == 'AOO'):
        return [0,1,6,8]
    elif(paceMode == 'VOO'):
        return [0,1,7,9]
    elif(paceMode == 'AAI'):
        return [0,1,6,8,10,13,14,16,17]
    elif(paceMode == 'VVI'):
        return [0,1,7,9,11,12,16,17]

#Updates the visibility of the parameters
'''def updateVisibility():
    paramVisb = pacingModePar(pacingMode)
    for i in paramVisb:
        visbList[i] = True
'''

#Changes the visibility of certain paremters
def changeVisibility(visbiList, window):
    for keyVal in visbiList:
        window[f'-Par{keyVal}-'].Update(visible=True)
        window[f'-ParPrev{keyVal}-'].Update(visible=True)
        window[f'-ParIN{keyVal}-'].Update(visible=False)

#
def changeParameters(visbiList, window):
    for keyVal in visbiList:
        window[f'-ParPrev{keyVal}-'].Update(visible=False)
        window[f'-ParIN{keyVal}-'].Update(visible=True)

#Resets the visibility of all parameter except LR and UP Limit
def resetVisibility(window):
    for keyVal in range(0,len(paramNameList())):
        window[f'-Par{keyVal}-'].Update(visible=False)
        window[f'-ParIN{keyVal}-'].Update(visible=False)
        window[f'-ParPrev{keyVal}-'].Update(visible=False)

#Shows incorrect input text when parameter input is out of range
def paramInputs(window, inputs, reset):
    if (reset):
        window['-FalseParIN-'].Update(visible=False)
        window['-TrueParIN-'].Update(visible=False)
    elif(inputs):
        window['-FalseParIN-'].Update(visible=False)
        window['-TrueParIN-'].Update(visible=True)
    else:
        window['-FalseParIN-'].Update(visible=True)
        window['-TrueParIN-'].Update(visible=False)

#General Function for changing a text element based on key
def updateText(key, parm, window):
   window[key].Update(f"{str(parm)}")

#Clear the data in the corresponding key's input text box
def clrTextInput(key, window):
    for i in key:
        window[i].Update("")

#Create a list of parameter values to clear
def clrParamInputs(pacingMode, window):
    onTerms = pacingModePar(pacingMode)
    lst = []
    for i in onTerms:
        lst.append(f'-ParIN{i}-')
    clrTextInput(lst, window)
        
#Clear Error Messages
def clrErrors(window):
    window['-Incorrect-'].update(visible = False)
    window['-inUse-'].update(visible = False)
    window['-Max-'].update(visible = False)
    window['-Match-'].update(visible = False)
    window['-Incorrect-'].update(visible = False)

#Updates Serial Communication Indicator
def updateSerialInd(deviceAddress, prevDevAdd,window):
    if(True): #temp condition, will be changed once serial communication is added  
        updateText('-serialInd1-', 'No Device Connected', window)
        updateText('-serialInd2-', 'No Device Connected', window)
        updateText('-serIndImg1-', 'serialCross.png', window)
        updateText('-serIndImg2-', 'serialCross.png', window)
        window['-allignText1-'].update('\t\t\t\t\t   ')
        window['-allignText2-'].update('\t\t\t\t\t   ')
    elif(deviceAddress != prevDevAdd):
        updateText('-serialInd1-', f'New Device {deviceAddress} Connected\nOld Device {prevDevAdd}', window)
        updateText('-serialInd2-', f'New Device {deviceAddress} Connected\nOld Device {prevDevAdd}', window)
        updateText('-serIndImg1-', 'serialCheck.png', window)
        updateText('-serIndImg2-', 'serialCheck.png', window)
        window['-allignText1-'].update('\t\t\t  ')
        window['-allignText2-'].update('\t\t\t  ')
    else:
        updateText('-serialInd1-', f'Device {deviceAddress} Connected', window)
        updateText('-serialInd2-', f'Device {deviceAddress} Connected', window)
        updateText('-serIndImg1-', 'serialCheck.png', window)
        updateText('-serIndImg2-', 'serialCheck.png', window)
        window['-allignText1-'].update('\t\t\t\t')
        window['-allignText2-'].update('\t\t\t\t')


#Updates the visibility of buttons in parameter layout, order is change parameters, set parameters, and cancel
def parButtonsUpdate(but1, but2, but3, window):
    window['Change Parameters'].Update(visible=but1)
    window['Set Parameters'].Update(visible=but2)
    window['Cancel'].Update(visible=but3)

#
def cancelErrorReset(mode, window):
     window['-FalseParIN-'].Update(visible=False)
     for keyVal in pacingModePar(mode):
         window[f'-Par{keyVal}-'].update(text_color = 'black')
    
    

