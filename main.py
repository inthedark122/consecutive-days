from seed import res as incoming_data

from app import ConsecutiveDays
    

def main():
  consecutive_days = ConsecutiveDays(incoming_data)
  df_days = consecutive_days.process()
  consecutive_days.print(df_days)

if __name__ == "__main__":
  main()