#!/usr/bin/python

import argparse, random, sys, string

class shuffle:
    def __init__(self, lines, input_range, head_count, repeat):
        self.lines = lines
        self.input_range = input_range
        self.head_count = head_count
        self.repeat = repeat
        
        
    def shuffle(self):

        if self.repeat == True:
            if self.input_range == -1: #-i was not inputted
                while True:
                    print(random.choice(self.lines))
                    
            else:
                random.shuffle(self.lines)
                for i in range(int(self.head_count)):
                    print (self.lines[i])
         
        else:
            if self.input_range == -1:
                random.shuffle(self.lines)
                if int(self.head_count) > int(len(self.lines)):
                    numlines = int(len(self.lines))
                    for i in range(numlines):
                        print(self.lines[i])
                else:
                    for i in range(int(self.head_count)):
                        print(self.lines[i])
                        
            else:
                random.shuffle(self.lines)
                for i in range(int(self.head_count)):
                    print(self.lines[i])
        
    
def main():

    parser = argparse.ArgumentParser()
    
    parser.add_argument("filename", nargs='?')
    parser.add_argument("-i", "--input-range", action="store", default=-1, help="treat input as a range from LO-HI")
    parser.add_argument("-n", "--head-count", action="store", default=sys.maxsize, help="Output at most count lines")
    parser.add_argument("-r", "--repeat", action="store_true", default=None,  help="repeat output values")
    args = parser.parse_args()
    
    
    if args.input_range != -1 and args.filename:
        print("Too many arguments")
        sys.exit(1)

    if args.head_count and int(args.head_count) < 0:
        print("Invalid input")
        sys.exit(1)
        
    
    if args.input_range != -1:
        lines =  []
        lo,hi = args.input_range.split('-',1)
        lo = int(lo)
        hi = int(hi)

        if lo > hi:
            print("Invalid input")
            sys.exit(1)
        while(lo < hi + 1):
            lines.append(str(lo) + "\n")
            lo+=1
    else:
        if args.filename  == "" or args.filename == "-":
            lines = sys.stdin.readlines()
            
        else:
            f = open(args.filename, 'r')
            lines = f.readlines()
            f.close()
    
    lines = [x.replace("\n",'') for x in lines]
    generator = shuffle(lines, args.input_range, args.head_count, args.repeat)
    generator.shuffle()

    
if __name__ == '__main__':
    main()
