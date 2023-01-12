#!/usr/bin/python

# Head ends here

def next_move(posr, posc, board):
    if board[posr][posc]=='d':
        print('CLEAN')
    else: 
        #s+=board[posr]
        s=''
        for c in range(5):
          s+=board[posr][c]
        # check if there are remaining dirty cells in the same row
        if s.find('d')==-1:
          print('DOWN')
        # check all right cells and all left cells for a dirty cell - if found see which one is more close and goto it
        # so avoid far dirty cells - handle dirty cells that are closest first (go opposite direction only if still
        # remining dirty cells in the opposite direction)
        else:
            lft=s[:posc].find('d')
            rt=s[::-1][:4-posc].find('d')
            if lft!=-1:
                if rt==-1:
                    print('LEFT')
                if rt!=-1:
                    if lft <= rt:
                        print('RIGHT')
                    else:
                        print('LEFT')
            else:
                print('RIGHT')
# Tail starts here

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
