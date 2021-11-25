import sys

import pandas as pd

def main():
  file1 = sys.argv[1]
  file2 = sys.argv[2]
  join_on = sys.argv[3]

  df1 = pd.read_csv(file1)
  df2 = pd.read_csv(file2)
  join_fieds = join_on.split(',')

  df = df1.merge(df2, on=join_fieds, how='outer')
  df.to_csv("output.csv")

if __name__ == "__main__":
    main()
