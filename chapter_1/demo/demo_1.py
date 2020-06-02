"""
demo_1.py
Created by dturba at 02/06/2020
"""
from turtle import forward, shape, right, Screen, speed
from typing import Callable

screen = Screen()
screen.setup(1000, 1000)
shape('turtle')
speed(0)


def square(side_length=100):
    for _ in range(4):
        forward(side_length)
        right(90)


def round_shape(func: Callable = square, side_length: int = 100,
                times: int = 72):
    for _ in range(times):
        square(side_length)
        right(5)


if __name__ == '__main__':
    round_shape(square, 150, 72)
    input()
