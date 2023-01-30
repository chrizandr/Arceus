import texttable as tt
import pdb


# Generate table at https://www.tablesgenerator.com/text_tables
# Update paste at https://pastebin.com/3GHySpgg

tb = tt.Texttable(max_width=1000)
#Adding header and rows to the table
rate_sheet = open("rates.csv").read().split("\n")

header = rate_sheet[0].split(",")
tb.header(header)
for r in rate_sheet[1::]:
    if len(r.split(",")) != 6:
        pdb.set_trace()

    tb.add_row(r.split(","))

table_string = tb.draw()
