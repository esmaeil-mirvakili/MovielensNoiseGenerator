import argparse
import pandas as pd
import noise
import csv


def main(dataset_path='./', out='./out', noise_models=None, noise_levels=None, columns=None):
    if noise_models is None:
        noise_models = []
    if noise_levels is None:
        noise_levels = []
    if columns is None:
        columns = []
    dataset = pd.read_csv(dataset_path, sep='::', header=None)
    for index in range(len(columns)):
        col = columns[index]
        noise_method = getattr(noise, noise_models[index])
        dataset.iloc[:, int(col)] = dataset.iloc[:, int(col)].apply(lambda x: noise_method(x, noise_levels[index]))
    with open(out, 'w') as f:
        for index, row in dataset.iterrows():
            f.write('::'.join([str(elem) for elem in row]))
            f.write('\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Personal information')
    parser.add_argument('--path', dest='path', type=str, default='/.', help='Path to dataset files.')
    parser.add_argument('--out', dest='out', type=str, default='./out.dat', help='Output path.')
    parser.add_argument('--noise_model', dest='noise_models', action='append', type=str, help='Noise model to use.')
    parser.add_argument('--noise_level', dest='noise_levels', action='append', type=int, help='Noise level.')
    parser.add_argument('--column', dest='columns', action='append', type=str,
                        help='Column names for noise generation.')
    args = parser.parse_args()
    main(
        dataset_path=args.path,
        out=args.out,
        noise_models=args.noise_models,
        noise_levels=args.noise_levels,
        columns=args.columns
    )
