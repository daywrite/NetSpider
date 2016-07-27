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
    ctx.invoke(all)


@cli.command()
@click.pass_context
def scheduler(ctx):
    print('scheduler')


@cli.command()
@click.pass_context
def fetcher(ctx):
    print('开始执行module.fetcher.tornado_fetcher.fetcher')

    g = ctx.obj

    _fetcher = Fetcher()

    g.instances.append(fetcher)

    _fetcher.run()


@cli.command()
@click.option('--fetcher-num', default=1, help='instance num of fetcher')
@click.option('--run-in', default='subprocess', type=click.Choice(['subprocess', 'thread']),
              help='run each components in thread or subprocess. '
                   'always using thread for windows.')
@click.pass_context
def all(ctx, fetcher_num, run_in):
    print('开始执行all方法，开启线程执行各个模块')

    g = ctx.obj

    threads = []

    try:
        # fetcher
        fetcher_config = g.config.get('fetcher', {})
        fetcher_config.setdefault('xmlrpc_host', '127.0.0.1')
        for i in range(fetcher_num):
            threads.append(run_in(ctx.invoke, fetcher, **fetcher_config))
    finally:
        # exit components run in threading
        for each in g.instances:
            each.quit()

        # exit components run in subprocess
        for each in threads:
            if not each.is_alive():
                continue
            if hasattr(each, 'terminate'):
                each.terminate()
            each.join()


def main():
    cli()


if __name__ == '__main__':
    main()
