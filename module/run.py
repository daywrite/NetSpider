#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2016-7-25
@author: huaihuai
'''
import click
from module.fetcher.tornado_fetcher import *

@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    ctx.invoke(fetcher)


@cli.command()
@click.pass_context
def scheduler(ctx):
    print('scheduler')

@cli.command()
@click.pass_context
def fetcher(ctx):
    print('开始执行module.fetcher.tornado_fetcher.fetcher')
    _fetcher=Fetcher()
    _fetcher.run()

@cli.command()
@click.pass_context
def all(ctx):
    print('开始执行all方法，开启线程执行各个模块')

    g = ctx.obj

    threads = []



def main():
    cli()


if __name__ == '__main__':
    main()
