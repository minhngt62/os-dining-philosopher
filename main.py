import time
from dining_philosophers import ArbitratorTable

def main():
    dining_table = ArbitratorTable()
    dining_table.start_dining()

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("-" * 5, f"{end - start:.4f}s", "-" * 5)