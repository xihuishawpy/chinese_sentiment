from pathlib import Path
import os
import jieba


def build_data_file(directory, samples_path, label, mode_str):
    for sample_path in samples_path:
        with Path(f'{directory}/{sample_path}').open() as f:
            words = [' '.join(jieba.cut(line.strip(), cut_all=False, HMM=True)) for line in f if line.strip() != '']
            with Path(f'{mode_str}.words.txt').open('a') as g:
                g.write(f"{' '.join(words)}\n")
            with Path(f'{mode_str}.labels.txt').open('a') as h:
                h.write(f'{label}\n')


if __name__ == '__main__':
    pos_dir = Path('raw_data/fix_pos')
    neg_dir = Path('raw_data/fix_neg')
    pos_samples = os.listdir(pos_dir)
    neg_samples = os.listdir(neg_dir)
    num_pos = len(pos_samples)
    num_neg = len(neg_samples)
    build_data_file(pos_dir, pos_samples[:num_pos - num_pos // 5], 'POS', 'train')
    build_data_file(pos_dir, pos_samples[(num_pos - num_pos // 5):], 'POS', 'eval')
    build_data_file(neg_dir, neg_samples[:num_neg - num_neg // 5], 'NEG', 'train')
    build_data_file(neg_dir, neg_samples[(num_neg - num_neg // 5):], 'NEG', 'eval')