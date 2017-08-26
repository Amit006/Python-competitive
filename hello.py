import click

 @click.command()
 @click.option('---string', default='world')
 def cli(string):
 	print 'hello %s!' % string 
  	print 'hello world'

        


import os
dir(os)
        
