"""
demo_2.py
Created by dturba at 02/06/2020
"""
from turtle import forward, shape, right, Screen, speed
from typing import Callable

screen = Screen()
screen.setup(1000, 1000)
shape('turtle')
speed(0)


def polygone(side_nbr: int = 4, side_length: int = 100):
    for _ in range(side_nbr):
        forward(side_length)
        right(360 / side_nbr)


def square(side_length=100):
    polygone(4, side_length)


def triangle(side_length=100):
    polygone(3, side_length)


def round_shape(func: Callable = square, side_length: int = 100,
                times: int = 72):
    for _ in range(times):
        func(side_length)
        right(5)


if __name__ == '__main__':
    round_shape(square, 150, 19)
    round_shape(triangle, 110, 72)
    input()
