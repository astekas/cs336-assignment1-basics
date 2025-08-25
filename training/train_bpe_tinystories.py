from tests.adapters import run_train_bpe
from time import perf_counter
from scalene import scalene_profiler


if __name__ == '__main__':
    train_path = 'data/TinyStoriesV2-GPT4-valid.txt'
    start = perf_counter()
    # Turn profiling on
    scalene_profiler.start()

    # your code
    vocab, merges = run_train_bpe(train_path, vocab_size=300, special_tokens=['<|endoftext|>'])
    print(f'TRAINING COMPLETE, timing: {perf_counter() - start}')
    # Turn profiling off
    scalene_profiler.stop()