import argparse
import logging
from pathlib import Path


import attr

import pandas as pd
import spacy
import pyinflect

from english_exercises.data.create_exercises_dataset import create_exercises_dataset
from english_exercises.data.load_dataset import load_data


def main():
    logging.basicConfig(level=logging.INFO)
    argparser = argparse.ArgumentParser()
    model = spacy.load('en_core_web_sm')
    argparser.add_argument('--text', type=str)
    argparser.add_argument('--output', type=str)
    args = argparser.parse_args()
    path = Path(args.text).expanduser()
    output = Path(args.output).expanduser()
    sentences = load_data(path, model)
    exercises = create_exercises_dataset(sentences)
    df = pd.DataFrame(attr.asdict(e) for e in exercises)

    df.to_csv(output, index=False)



if __name__ == '__main__':
    main()