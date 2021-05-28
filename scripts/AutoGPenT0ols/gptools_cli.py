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
    parser.add_argument("--show-commands", action='store_true', help="Just show commands")
    parser.add_argument("--path",dest="path", default='/tmp/autorecon/', help="Destination path (default: /tmp/autorecon)")

    std_parser = argparse.ArgumentParser(add_help=False)
    std_parser.add_argument("target", nargs='?', type=str, help="(Target Required *) The target IP(s), range(s), CIDR(s), hostname(s), FQDN(s), file(s) containing a list of targets ")
    scan_parser = argparse.ArgumentParser(add_help=False)
    scan_parser.add_argument(
            '--scanner',
            help='Select scanner (default : full_scanner)',
            nargs='?',
            default = 'full_scanner'
            )

    have_info_parser = argparse.ArgumentParser(add_help=False)
    have_info_parser.add_argument(
            '--tags',
            help='What do you have? [Creds, NoCreds, Hash, Shell] (Default: NoCreds)',
            default = 'NoCreds',
            nargs='?'
            )

    wlist_parser = argparse.ArgumentParser(add_help=False)
    wlist_parser.add_argument("-w", metavar="WORDLIST", dest='wordlist', nargs='+', help="set wordlist  (Default SecList wordlist)")
    
    cred_parser = argparse.ArgumentParser(add_help=False)
    cred_parser.add_argument("-u", metavar="USERNAME", dest='username', nargs='?', default=[], help="username(s) or file(s) containing usernames")
    cred_parser.add_argument("-p", metavar="PASSWORD", dest='password', nargs='?', default=[], help="password(s) or file(s) containing passwords")
    cred_parser.add_argument("-H", metavar="HASH", dest='HASH', nargs='?', default=[], help="Pass The hash")

    subparsers = parser.add_subparsers(title='services', dest='services', description='available options')


    # Arguments Recon

    recon = subparsers.add_parser('recon', help='Initial recon', parents=[std_parser,scan_parser]) ## Get new arguments and can introduce std_parser arguments
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
    
    recon.add_argument(
            '--full',
            help='Full recon scan',
            action='store_true'
            )


    # Arguments WEB

    web = subparsers.add_parser('web', help='Web server scanner', parents = [cred_parser, std_parser,wlist_parser,scan_parser])
    
    web.add_argument(
            '--port',
            help='scan specific port (Default 80)',
            nargs='?',
            default = '80'
            )
    
    web.add_argument(
            '--file-path',
            help='Specify to find the requested resource and start the enumeration with that route (Default / )',
            nargs='?',
            default = '/'
            )
    
    web.add_argument(
            '--ssl',
            help='usage of SSL/HTTPS requests',
            action='store_true'
            )

    web.add_argument(
            '--cms',
            help='What do you have? [Wordpress, Joombla, Drupal] (Default: NoCreds)',
            default = 'NoCreds',
            nargs='?'
            )
    # Arguments SMTP

    smtp = subparsers.add_parser('smtp', help='smtp enumeration')

    # Arguments SMB

    smb = subparsers.add_parser('smb', help='Enum smb', parents = [cred_parser,std_parser,have_info_parser])

    smb.add_argument(
            '--port',
            help='scan specific port (Default 445)',
            nargs='?',
            default = '445'
            )
    
    
    # Arguments FTP
    
    ftp = subparsers.add_parser('ftp', help='FTP enum', parents = [cred_parser,std_parser])

    # Argumets LDAP

    ldap = subparsers.add_parser('ldap', help='LDAP enum', parents = [cred_parser,std_parser,have_info_parser])
    
    ldap.add_argument(
            '--port',
            help='scan specific port (Default 389)',
            nargs='?',
            default = '389'
            )

    # Arguments SNMP
    
    snmp = subparsers.add_parser('snmp', help='Enum SNMP', parents = [cred_parser,std_parser])

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()
    
    check = vars(args)


    if not check['target']:
        if check['services'] == 'recon':
            recon.print_help()
        elif check['services'] == 'web':
            web.print_help()
        elif check['services'] == 'smb':
            smb.print_help()
        elif check['services'] == 'smtp':
            smtp.print_help()
        elif check['services'] == 'ftp':
            ftp.print_help()
        elif check['services'] == 'ldap':
            ldap.print_help()
        elif check['services'] == 'snmp':
            snmp.print_help()
        else: 
            parser.print_help()
        sys.exit(1)

    return args

