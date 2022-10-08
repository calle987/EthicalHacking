import argparse
import sys
import textwrap


from package.netcat import NetCat



def main():
    parser = argparse.ArgumentParser(
        description='BHP Net Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent('''Example:
          netcat.py -t 192.168.1.108 -p 5555 -l -c # command shell
          netcat.py -t 192.168.1.108 -p 5555 -l -u=mytest.whatisup # upload to file
          netcat.py -t 192.168.1.108 -p 5555 -l -e=\"cat /etc/passwd\" # execute command
          echo 'ABCDEFGHI' | ./netcat.py -t 192.168.1.108 -p 135 # echo local text to server port 135
          netcat.py -t 192.168.1.108 -p 5555 # connect to server
          netcat.py -t 192.168.1.108 -p 5555 -l -c -s 8000
          '''))
    parser.add_argument('-c', '--command', action='store_true', help='initialize command shell')
    parser.add_argument('-e', '--execute', help='execute specified command')
    parser.add_argument('-l', '--listen', action='store_true', help='listen')
    parser.add_argument('-p', '--port', type=int, default=5555, help='specified port')
    parser.add_argument('-t', '--target', default='192.168.1.203', help='specified IP')
    parser.add_argument('-u', '--upload', help='upload file')
    parser.add_argument('-s','--scan',help='scan ports')
    args = parser.parse_args()

    if args.listen:
        buffer = ''
    else:
        buffer = sys.stdin.read()


    nc = NetCat(args, buffer.encode('utf-8'))
    nc.run()

if __name__ == '__main__':
    main()