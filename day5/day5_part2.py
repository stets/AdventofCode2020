# https://adventofcode.com/2020/day/5

boarding_passes = open("boarding_passes.txt", "r").read().split('\n')

def gen_rows():
    rows_range = []
    for each in range(0,128):
        rows_range.append(each)
    return rows_range

def gen_cols():
    cols_range = []
    for each in range(0,8):
        cols_range.append(each)
    return cols_range


# back half 
#row_range[int(len(b) / 2 ):][-1]

# front half
#row_range[:int(len(b) / 2 )][-1]

seat_ids = []

for boarding_pass in boarding_passes:
    seat_row = boarding_pass[0:7]
    seat_col = boarding_pass[7:]
    row_range = gen_rows()
    col_range = gen_cols()
    seat_id = 0
    
    for location in seat_row:
        if location == 'F':
            row_range = row_range[:int(len(row_range) / 2 )]

        elif location == 'B':    
            row_range = row_range[int(len(row_range) / 2 ):]
        
        else: pass
            

    for location in seat_col:
        if location == 'L':
            col_range = col_range[:int(len(col_range) / 2 )]

        elif location == 'R':
            col_range = col_range[int(len(col_range) / 2 ):]
        
        else: pass

    print(f'Col for seat is {col_range}')   
    print(f'Row for seat is {row_range}')
    seat_id = (row_range[0] * 8) + col_range[0]
    print(f'Seat ID is {seat_id}')
    seat_ids.append(seat_id)

seat_ids.sort()
print(f"The highest seat ID on the above boarding passes is {max(seat_ids)}")


print(seat_ids)

for idx, each in enumerate(seat_ids):
    if (seat_ids[idx]) - seat_ids[idx-1] == 2:
        print(f'Missing seat is {seat_ids[idx] - 1}')
    
# 557 is missing