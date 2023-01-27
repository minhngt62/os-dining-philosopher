import time

from dining_philosophers import ArbitratorTable, HierachyTable, CMTable, LimitDiners


def main():
    # dining_table = LimitDiners()
    # dining_table = ArbitratorTable()
    dining_table = HierachyTable()
    # dining_table = CMTable()
    
    dining_table.start_dining()

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("-" * 5, f"{end - start:.4f}s", "-" * 5)