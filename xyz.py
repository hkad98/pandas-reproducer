import pandas as pd
import random
import string
from memory_profiler import profile


def random_string():
    return ''.join(random.choices(string.ascii_letters, k=7))


@profile
def main():
    records_count = 63531
    df = pd.DataFrame(
        {
            "A": random.choices([random_string() for _ in range(24)], k=records_count),
            "B": random.choices([random_string() for _ in range(14580)], k=records_count),
            "C": random.choices([random_string() for _ in range(9)], k=records_count),
            "D": random.choices([random_string() for _ in range(2311)], k=records_count),
            "E": random.choices([random_string() for _ in range(2)], k=records_count),
            "F": random.choices([random_string() for _ in range(280)], k=records_count),
            "M": random.sample(range(0, records_count), records_count)
        }
    )

    grouped_df = df.groupby(["A", "B", "C", "D", "E", "F"], dropna=False)[["M"]].sum(min_count=1, numeric_only=False)
    grouped_df.unstack("F")


if __name__ == "__main__":
    main()