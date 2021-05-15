import argparse
import sys
from argparse import RawTextHelpFormatter
from lib.core.__version__ import __version__
from helpers.logger import highlight

def gen_cli_args():

    VERSION  = __version__
    CODENAME = 'CapitanJ4ck'


    parser = argparse.ArgumentParser(description="""


                           #                                                 
                           ##                                ###             
  ###### #######  ######## ###  ## ######## ####### #######  ###         ####
 ###           ##          #### ##    ###   ##   ##       ## ###        ###  
 ###  ##  ######   ####### #######    ###   ##   ##  ##   ## ###        ###  
 ###  ##  ###      ###     ### ###    ###   ##   ##  ##   ## ###        ###  
  ######  ###      ####### ###  ##    ###   #######   #####  ####### #####   
                                 #                                           

                                 {}: {}
                                 {}: {}
""".format(highlight('Version', 'red'),
           highlight(VERSION),
           highlight('Codename', 'red'),
           highlight(CODENAME)),

                                    formatter_class=RawTextHelpFormatter,
                                    epilog="We are in... Let the hacking begin!")

    parser.add_argument("-t", type=int, dest="threads", default=100, help="set how many concurrent threads to use (default: 100)")
    parser.add_argument("--verbose", action='store_true', help="enable verbose output")
    parser.add_argument("--path",dest="path", default='/tmp/autorecon/', help="Destination path (default: /tmp/autorecon)")

    std_parser = argparse.ArgumentParser(add_help=False)
    std_parser.add_argument("target", nargs='*', type=str, help="the target IP(s), range(s), CIDR(s), hostname(s), FQDN(s), file(s) containing a list of targets, NMap XML or .Nessus file(s)")
    
    cred_parser = argparse.ArgumentParser(add_help=False)
    cred_parser.add_argument("-u", metavar="USERNAME", dest='username', nargs='+', default=[], help="username(s) or file(s) containing usernames")
    cred_parser.add_argument("-p", metavar="PASSWORD", dest='password', nargs='+', default=[], help="password(s) or file(s) containing passwords")

    subparsers = parser.add_subparsers(title='services', dest='services', description='available options')


    # Arguments Recon

    recon = subparsers.add_parser('recon', help='Initial recon', parents=[std_parser])
    recon.add_argument(
            '--all-ports',
            help='scan all ports',
            action='store_true'
            )

    recon.add_argument(
            '--ports',
            help='scan specific ports',
            nargs='?'
            )

    # Arguments WEB

    web = subparsers.add_parser('web', help='Web server scanner', parents = [cred_parser,std_parser])


    # Arguments SMTP

    smtp = subparsers.add_parser('smtp', help='smtp enumeration')

    # Arguments SMB

    smb = subparsers.add_parser('smb', help='Enum smb', parents = [cred_parser,std_parser])
    smb.add_argument(
            '--null-session',
            help='Null Sessions',
            action='store_true'
            )
    
    # Arguments FTP
    
    ftp = subparsers.add_parser('ftp', help='FTP enum', parents = [cred_parser,std_parser])

    # Argumets LDAP

    ldap = subparsers.add_parser('ldap', help='LDAP enum', parents = [cred_parser,std_parser])
    
    # Arguments SNMP
    
    snmp = subparsers.add_parser('snmp', help='Enum SNMP', parents = [cred_parser,std_parser])

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()

    return args

