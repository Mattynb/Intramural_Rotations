from player_db import players
import PySimpleGUI as sg

def players_present():
    sg.theme('DarkAmber')

    p_list = [x for x in players]
    print(p_list)
    
    players_here = []
    layout =[]
    
    i = 0
    for x in p_list:
    
        layout.append([sg.Text(f'{x}', key=f'p{i}'), sg.Button('Here', key= f'p{i} T'), sg.Button('Not Here', key= f'p{i} F')])
    
        i += 1

    layout.append([sg.Button('Done', key='Done')])

    win1 = sg.Window('Check In', layout, default_element_size=(12, 1), location=(0,0), size=(800,600), keep_on_top=True)


    while True:

        events, values = win1.read()
        win1.maximize()

        print(events)

        for x in range(len(layout)):
            if events == f'p{x} T':
                n = p_list[x]
                players_here.append(n)
                win1[f'p{x}'].Update(visible=False)
                win1[f'p{x} T'].Update(visible=False)
                win1[f'p{x} F'].Update(visible=False)
        
            if events == f'p{x} F':
                win1[f'p{x}'].Update(visible=False)
                win1[f'p{x} T'].Update(visible=False)
                win1[f'p{x} F'].Update(visible=False)
        
        if events == 'Done':
            win1.close()

            string = ''
           
            for x in players_here:
                string += x + '\n'

            layout2 = [
                [sg.Text('Players Checked in:')],
                [sg.Text('Players Checked in:', visible=False)],
                [sg.Text(f'{string}')],
                [sg.Button('EXIT'), sg.Button('UPDATE')]]   

            win1 = sg.Window('Players Checked in', layout2)  

        if events == 'UPDATE':
            win1.close()
            players_present()
            break

        if events == sg.WIN_CLOSED or events == 'EXIT':
            win1.close()
            break

    print(players_here)
    return players_here


if __name__ == '__main__':
    players_present()
