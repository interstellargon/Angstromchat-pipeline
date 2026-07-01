import argparse
import os
from multiprocessing import Pool

from angstromchat.common import get_base_dir


# The URL where the dataset is hosted
BASE_URL = "https://huggingface.co/datasets/karpathy/fineweb-edu-100b-shuffle/resolve/main"
MAX_SHARD = 1822 # the las datashard is shard_01822.parquet
BASE_DIR = get_base_dir()
DATA_DIR = os.path.join(BASE_DIR, "base_data")
os.makedirs(DATA_DIR, exist_ok=True)


def download_single_file(index):

    return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download FineWeb-Edu 100BT dataset")
    parser.add_argument("-n", "--num-shards", type=int, default=-1, help="Number of shards to download, -1 = disable")
    parser.add_argument("-w", "--num-workers", type=int, default=4, help="Number of parallel download workers")
    args = parser.parse_args()

    num = MAX_SHARD + 1 if args.num_shards == -1 else min(args.num_shards, MAX_SHARD + 1)
    ids_to_download = list(range(num))
    print(f"Downloading {len(ids_to_download)} shards using {args.num_workers} workers.")
    print(f"Target directory: {DATA_DIR}")
    print()
    with Pool(processes=args.num_workers) as pool:
        results = pool.map(download_single_file, ids_to_download)

    # Report results
    successful = sum(1 for success in results if success)
    print(f"Downloading is completed, {successful}/{len(ids_to_download)} shards downloaded to {DATA_DIR}")

