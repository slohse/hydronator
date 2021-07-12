#!/usr/bin/env python3

import smbus
from time import sleep
import click
import relay_lib

@click.command()
@click.option('--bus', type=int, default=0, help='I2C bus')
@click.option('--p1', type=int, default=0, help='Run Pump 1 for n seconds')
@click.option('--p2', type=int, default=0, help='Run Pump 2 for n seconds')
@click.option('--p3', type=int, default=0, help='Run Pump 3 for n seconds')
@click.option('--p4', type=int, default=0, help='Run Pump 4 for n seconds')
def water(bus, p1, p2, p3, p4):
    """Hydronator waters your plants to your specifications."""
    i2c = smbus.SMBus(bus)
    if p1 > 0:
        relay_lib.relay_on(1, i2c)
        sleep(p1)
        relay_lib.relay_off(1, i2c)
    if p2 > 0:
        relay_lib.relay_on(2, i2c)
        sleep(p2)
        relay_lib.relay_off(2, i2c)
    if p3 > 0:
        relay_lib.relay_on(3, i2c)
        sleep(p3)
        relay_lib.relay_off(3, i2c)
    if p4 > 0:
        relay_lib.relay_on(4, i2c)
        sleep(p4)
        relay_lib.relay_off(4, i2c)

if __name__ == '__main__':
    water()
