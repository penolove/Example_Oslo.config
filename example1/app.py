from __future__ import print_function
from oslo.config import cfg
 
 
opt_group = cfg.OptGroup(name='simple',
                         title='A Simple Example')
 
simple_opts = [
    cfg.BoolOpt('enable', default=False,
                help=('True enables, False disables'))
]
 
loser_opts = [
    cfg.BoolOpt('loser', default=False,
                help=('True enables, False disables'))
]
CONF = cfg.CONF
CONF.register_group(opt_group)
CONF.register_opts(simple_opts, opt_group)
CONF.register_opts(loser_opts)
 
 
if __name__ == "__main__":
    CONF(default_config_files=['app.conf'])
    print(CONF.simple.enable)
    print(CONF.loser)
