#libraries
import random as rd

#inputs
ask_draw = int(input('How many draw (1.000.000 recommanded)? '))
ask_sim = int(input('How many simulation (1.000 recommanded)? '))

#loops
sim = 1
while sim <= ask_sim:
    #print('sim', sim)
    red = 1
    blue = 1
    draw = 1
    while draw <= (ask_draw-2):
        #print('draw', draw)
        if rd.randint(1,(red+blue)) <= red:
            red += 1
        else:
            blue += 1
        draw += 1
    #print('P(red) =', red ,'/', (red+blue), '=', red / (red+blue))
    save = open('/home/fernandez/Bureau/launey.csv', 'a')
    save.write(str(sim)+','+str(red/(red+blue))+'\n')
    save.close()
    sim += 1

