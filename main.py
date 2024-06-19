import time
import neat
import pickle
import pygame
import argparse

from PongGameAI import PongGame

def eval_genomes(genomes, config):
    width, height = 700, 500
    window = pygame.display.set_mode((width, height))

    for i, (genome_id1, genome1) in enumerate(genomes):
        if i == len(genomes) - 1:
            break

        genome1.fitness = 0
        for (genome_id2, genome2) in genomes[i+1:]:
            genome2.fitness = 0 if genome2.fitness == None else genome2.fitness
            game = PongGame(window, width, height)

            game.train_ai(genome1, genome2, config)                


def run_neat(config=None, checkpoint=None, model_path="./model/best.pickle"):
    # if config is None or checkpoint is None:
    #     print("No configuration or checkpoint provided")
    
    if config is None and checkpoint:
        print(f"Using checkpoint {checkpoint}")
        p = neat.Checkpointer.restore_checkpoint(checkpoint)
    
    if checkpoint is None and config:
        print("No checkpoint provided, so defaulting to train from scratch.")
        p = neat.Population(config)

    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(1, filename_prefix='checkpoints/neat-checkpoint-'))

    winner = p.run(eval_genomes, 50)

    with open(model_path, "wb") as f:
        pickle.dump(winner, f)


def test(config, model_path):
    if config is None or model_path is None:
        print("Please provide configuration and model path")

    width, height = 700, 500
    window = pygame.display.set_mode((width, height))

    with open(model_path, "rb") as f:
        winner = pickle.load(f)

    game = PongGame(window, width, height)
    game.test_ai(winner, config)


def main(args):
    mode = args.mode
    config_path = args.config_path
    checkpoint = args.checkpoint
    model_path = args.model_path

    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction, 
                neat.DefaultSpeciesSet, neat.DefaultStagnation, 
                config_path)

    if mode == "train":
        run_neat(config, checkpoint)
    if mode == "play":
        print("Please use 'W' to move updwards and 'S' to move downwards! Have fun!")
        time.sleep(3)
        test(config, model_path)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='PingPong AI')
    parser.add_argument('--config_path', default="./config/config.txt")
    parser.add_argument('--checkpoint', default=None)
    parser.add_argument('--model_path', default="./model/best.pickle")
    parser.add_argument('--mode', default="train", choices=["train", "play"])

    args = parser.parse_args()
    main(args)

    # local_dir = os.path.dirname(__file__)
    # config_path = os.path.join(local_dir, "./config/config.txt")
    # pickle_path = "best.pickle"
    # checkpoint = "neat-checkpoint-29"
    # config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction, 
    #                      neat.DefaultSpeciesSet, neat.DefaultStagnation, 
    #                      config_path)
    # run_neat(config)
    # test(config, pickle_path)