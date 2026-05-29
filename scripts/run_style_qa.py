import argparse
import pandas as pd
from evaluators.style_rules import validate_row

DEFAULT_INPUT_CSV = "data/processed/sft_augmented_dataset_promptC2_sample150_20260529.csv"
DEFAULT_OUTPUT_CSV = "experiments/qa_results/style_validation_promptC2_sample150_20260529.csv"


def main(input_csv, output_csv):
    df = pd.read_csv(input_csv)
    results = [validate_row(row) for row in df.to_dict("records")]

    result_df = pd.DataFrame(results)
    result_df.to_csv(output_csv, index=False, encoding="utf-8-sig")

    print(result_df.groupby("persona")["score"].describe())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_csv", default=DEFAULT_INPUT_CSV)
    parser.add_argument("--output_csv", default=DEFAULT_OUTPUT_CSV)
    args = parser.parse_args()

    main(args.input_csv, args.output_csv)