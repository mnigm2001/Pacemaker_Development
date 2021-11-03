#%% Import Libraries
import PySimpleGUI as sg
from userVerify import verify, register
from layouts import layout
from layoutFunctions import updateSerialInd, pacingModePar, updateText, cancelErrorReset, changeVisibility, changeParameters,paramInputs, updateText, clrParamInputs, clrTextInput, parButtonsUpdate, clrErrors, resetVisibility
from inputVerify import inputValues, inputVerify

#%% Display/Run app 
# keys for inputs of different screens
prevDevice = 'address'
loginKeys = ["-User-", "-Pass-"]
signupKeys = ['-newUser-', '-newPass-', '-verifyPass-']

# define app layout
layout = [[sg.Column(layout('login'), visible = True, key='-COL1-'),
           sg.Column(layout('signup'), visible=False, key='-COL2-'),
           sg.Column(layout('select'), visible = False, key='-COL3-'), 
           sg.Column(layout('mode'), visible=False, key='-COL4-')]]

window = sg.Window('Pace Maker', layout, margins=(10,10))
layout = 1

while True:
    event, values = window.read()
    print('event = ', event, end='\n');
    if event == sg.WIN_CLOSED:
        break
    
    ## Go to register screen
    if (event == 'New User? Register here '):
        clrErrors(window)
        window[f'-COL{layout}-'].update(visible = False)
        layout = 2
        clrTextInput(loginKeys, window)
        window[f'-COL{layout}-'].update(visible = True)
    
    ## Verify Login
    if (event == 'Login'):
        clrErrors(window)
        if (verify(values['-User-'], values['-Pass-']) == True):
            clrTextInput(loginKeys, window)
            window[f'-COL{layout}-'].update(visible = False)
            layout = 3
            window[f'-COL{layout}-'].update(visible = True)
            updateSerialInd('deviceAddress',prevDevice, window)
        else:
            window["-Incorrect-"].update(visible = True)
            
    ## Verify Registration        
    if event == "Sign Up":
        clrErrors(window)
        verifyReg = register(values['-newUser-'], values['-newPass-'], values['-verifyPass-'])
        if(verifyReg == [False, False]):
            window['-Max-'].update(visible = True)
        elif (verifyReg == [True, False]):
            window['-inUse-'].update(visible = True)
        elif (verifyReg == [False, True]):
            window['-Match-'].update(visible = True)
        else:
            clrTextInput(signupKeys, window)
            window[f'-COL{layout}-'].update(visible=False)
            layout = 1
            window[f'-COL{layout}-'].update(visible=True)
    
    ## Open mode screen  
    if event in ['AOO', 'VOO', 'AAI', 'VVI']:
        mode = event
        paramInputs(window, False, True)
        updateText('-ParTitle-', f'{event} Parameters', window)
        updateText('-ParSubTitle-',  f'Existing Parameters for {event}', window)
        parButtonsUpdate(True, False, False, window)
        pacingMode = event
        changeVisibility(pacingModePar(event), window)
        for keyVal in pacingModePar(mode):
            window[f'-Par{keyVal}-'].update(text_color = 'black')
        window[f'-COL{layout}-'].update(visible=False)
        layout = 4
        window[f'-COL{layout}-'].update(visible=True)
    
    ## Go to previous page
    if event == 'Go Back':
        resetVisibility(window)
        clrParamInputs(pacingMode, window)
        parButtonsUpdate(True, False, False, window)
        window[f'-COL{layout}-'].update(visible=False)
        layout = layout-1
        window[f'-COL{layout}-'].update(visible=True)
    
    ## Go back to login screen
    if (event == "Logout" or event == "Back to Login"):
        if event == "Back to Login":
            clrTextInput(signupKeys, window)
        clrErrors(window)
        window[f'-COL{layout}-'].update(visible=False)
        layout = 1
        window[f'-COL{layout}-'].update(visible=True)
    
    ##Change Preset Parameters
    if(event == "Change Parameters"):
        changeParameters(pacingModePar(mode), window)
        updateText('-ParSubTitle-',  'Set Parameters Using Dropdowns\t', window)
        parButtonsUpdate(False, True, True, window)
    
    ##Cancel the changes
    if(event == 'Cancel'):
        updateText('-ParSubTitle-',  f'Existing Parameters for {mode}\t', window)
        changeVisibility(pacingModePar(mode), window)
        parButtonsUpdate(True, False, False, window)
        cancelErrorReset(mode, window)
                
    ## Set Parameters
    if(event == "Set Parameters"):
        print("\n\n Set Paremters \n\n")
        if (False in inputVerify(mode, window, values)):
            paramInputs(window, False, False)
        else:
            paramInputs(window, True, False)
            updateText('-ParSubTitle-',  f'Existing Parameters for {mode}', window)
            parButtonsUpdate(True, False, False, window)
            changeVisibility(pacingModePar(mode), window)
            

window.close()
