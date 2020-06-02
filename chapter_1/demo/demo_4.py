"""
demo_4.py
Created by dturba at 03/06/2020
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


def star(side_length=100):
    for _ in range(5):
        forward(side_length)
        right(720 / 5)


def add(x, y):
    return x + y


def mul(x, y):
    return x * y


def add_mul(x, y):
    return x + x * y


def round_shape(func: Callable = square, side_length: int = 100,
                times: int = 72, side_length_increase: float = 0,
                increase_mode: Callable = add):
    for _ in range(times):
        func(side_length)
        side_length = increase_mode(side_length, side_length_increase)
        right(5)


if __name__ == '__main__':
    round_shape(star, 20, 150, 1.68 / 90, add_mul)
    input()
