import tkinter as tk
import logging
import random

logging.basicConfig(level=logging.INFO, filename='log.txt')

colors = ['#00cc99', '#330099', '#336699', '#990099', '#660033', 'pink', '#00ff66', '#00ffcc', '#9932CD', '#70DB93', '#ffcc99', '#ffff33']


class Position:
    def __init__(self):
        self.position_x = 100
        self.position_y = 100

    def up(self):
        if self.position_y == 0:
            self.position_y = 200
            c.create_line(self.position_x, self.position_y, self.position_x, self.position_y-4, fill=colors[ random.randint(0, len(colors)-1)], width=5)
            logging.info('up: linia od punktu (%s,%s) do punktu (%s, %s)', self.position_x, self.position_y, self.position_x, self.position_y-4)
        else:
            c.create_line(self.position_x, self.position_y, self.position_x, self.position_y - 4,
                          fill=colors[random.randint(0, len(colors) - 1)], width=5)
            logging.info('up: linia od punktu (%s,%s) do punktu (%s, %s)', self.position_x, self.position_y,
                         self.position_x, self.position_y - 4)
        self.position_y -= 4

    def down(self):
        if self.position_y == 200:
            self.position_y = 0
            c.create_line(self.position_x, self.position_y, self.position_x, self.position_y + 4,
                          fill=colors[random.randint(0, len(colors) - 1)], width=5)
            logging.info('down: linia od punktu (%s,%s) do punktu (%s, %s)', self.position_x, self.position_y,
                         self.position_x,
                         self.position_y + 4)
        else:
            c.create_line(self.position_x, self.position_y, self.position_x, self.position_y+4, fill=colors[ random.randint(0, len(colors)-1)], width=5)
            logging.info('down: linia od punktu (%s,%s) do punktu (%s, %s)', self.position_x, self.position_y, self.position_x,
                         self.position_y + 4)
        self.position_y += 4

    def left(self):
        if self.position_x == 0:
            self.position_x = 200
            c.create_line(self.position_x, self.position_y, self.position_x - 4, self.position_y,
                          fill=colors[random.randint(0, len(colors) - 1)], width=5)
            logging.info('left: linia od punktu (%s,%s) do punktu (%s, %s)', self.position_x, self.position_y,
                         self.position_x - 4,
                         self.position_y)
        else:
            c.create_line(self.position_x, self.position_y, self.position_x-4, self.position_y, fill=colors[ random.randint(0, len(colors)-1)], width=5)
            logging.info('left: linia od punktu (%s,%s) do punktu (%s, %s)', self.position_x, self.position_y, self.position_x -4,
                         self.position_y )
        self.position_x -= 4

    def right(self):
        if self.position_x == 200:
            self.position_x = 0
            c.create_line(self.position_x, self.position_y, self.position_x + 4, self.position_y,
                          fill=colors[random.randint(0, len(colors) - 1)], width=5)
            logging.info('right: linia od punktu (%s,%s) do punktu (%s, %s)', self.position_x, self.position_y,
                         self.position_x + 4,
                         self.position_y)
        else:
            c.create_line(self.position_x, self.position_y, self.position_x+4, self.position_y, fill=colors[ random.randint(0, len(colors)-1)], width=5)
            logging.info('right: linia od punktu (%s,%s) do punktu (%s, %s)', self.position_x, self.position_y, self.position_x+4,
                         self.position_y )
        self.position_x += 4


root = tk.Tk()
position = Position()
tk.Button(root, text='left', command=position.left).grid(row=0, column=0)
tk.Button(root, text='right', command=position.right).grid(row=0, column=1)
tk.Button(root, text='up', command=position.up).grid(row=0, column=2)
tk.Button(root, text='down', command=position.down).grid(row=0, column=3)

c = tk.Canvas(root, width=200, height=200)
c.grid(row=1, column=0, columnspan=4)

root.mainloop()