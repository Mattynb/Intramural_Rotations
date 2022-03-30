import time, PySimpleGUI as sg
from pygame import mixer
from players_present import players_present


def createTextlay(lay, x):
    lay += [sg.Text('x')]

def main():
    playa_here = players_present()

    t_time = 48 # minutes
    p_t_time = int(t_time/len(playa_here)) * 5
    sub_t = round(t_time/len(playa_here), 1)
    print(f'p_t_time is: {p_t_time}, there should be a substitution every {sub_t} min.')
    
    input('to start the clock press any key')
    t = time.time()
    m = 0

    c_lineup = []
    for x in range(0, 5):
        y = playa_here.pop(0)
        c_lineup.append(y)
    

    str12 = ''
    lay = []
    for x in c_lineup:
        if x == c_lineup[len(c_lineup)-1]:
            str12 += ' and ' + x 
        else:
            str12 += x + ', '

        lay.append( [sg.Text(f'{x}')])
    
    str12 += '\b' 
    start_win = sg.Window('starters', lay)
    
    while True:
        event, valueee = start_win.read()
        if event == sg.WIN_CLOSED:
            start_win.close()
            break

    print(f'\n starting lineup is: {str12}')

    while m < t_time:
        m = round((time.time() - t)/60 , 2)
        
        if m >= sub_t:
            i = 0
            for i in range(2):
                h = c_lineup.pop(i)
                playa_here.append(h)
                h2 = playa_here.pop(i)
                c_lineup.append(h)
                call(h2, h)
                i += 1
            
            sub_t = sub_t + sub_t 
        

def mix(file):
    mixer.init()
    mixer.music.load(file)
    mixer.music.set_volume(1.3)
    mixer.music.play()


def call(pin, pout):
    
    sg.theme('DarkAmber')

    layout = [
        [sg.Text(f'{pin} please ask to sub in for {pout}', s=(10,10), expand_x=True, expand_y=True)],
        [sg.Button('OK')]
        ]

    win = sg.Window('SUBSTITUTION ALERT', layout, margins=(400, 400), auto_size_text=True, auto_close_duration= 6, scaling=True, auto_size_buttons=True )
    mix('./sounds/lets.wav') 

    while True:

        event, values = win.read()
        

        if event == 'OK' or event == sg.WIN_CLOSED:
            mix('./sounds/hell.wav')
            win.close()
            break


if __name__ == '__main__':
    main()
