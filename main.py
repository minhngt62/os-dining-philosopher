from dining_philosophers import ArbitratorTable, HierachyTable


def main():
    # dining_table = ArbitratorTable()
    dining_table = HierachyTable()
    dining_table.start_dining()


if __name__ == "__main__":
    main()