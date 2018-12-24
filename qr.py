import qrcode,sys
import os
delimetr = {'linux':'/','win32':'\\'}
def make_qr(lst,fpath):
    for k,item in enumerate(lst):
        if os.path.exists(fpath):
            img = qrcode.make(item)
            img.save('{}{}{}.png'.format(fpath,delimetr.get(sys.platform),k))
        else:
            print('Path is invalid')
            exit()


def parse_str(string,number):
    substr_len = round(len(string)/number)
    parsed = []
    last_ind = 0
    for i in range (1,number+1):
        parsed.append(string[last_ind:i*substr_len])
        last_ind = i*substr_len
    return parsed

def main():
    string = ''
    if os.path.exists(sys.argv[1]):
        with open(sys.argv[1],'r') as f:
            string = f.read().rstrip()

    parsed = parse_str(string,int(sys.argv[3]))
    make_qr(parsed,sys.argv[2])






if __name__ == '__main__':
    main()
