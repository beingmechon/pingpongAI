# PingPong AI with NEAT and Pygame

This project implements an AI for playing PingPong using NEAT (NeuroEvolution of Augmenting Topologies) and Pygame.

## Requirements

- Python 3.x
- Pygame
- NEAT Python
- argparse

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/pong-ai-neat.git
   cd pong-ai-neat
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Training the AI

To train the AI using NEAT, run the following command:
```bash
python main.py --mode train --config_path ./config/config.txt --checkpoint ./checkpoints/neat-checkpoint-
```
- `--config_path`: Path to the NEAT configuration file.
- `--checkpoint`: Optional. Path to a NEAT checkpoint for resuming training.

### Playing with the AI

To play PingPong against the trained AI, run:
```bash
python main.py --mode play --model_path ./model/best.pickle
```
- `--model_path`: Path to the trained model pickle file.

During gameplay:
- Use 'W' key to move the paddle upwards.
- Use 'S' key to move the paddle downwards.

### Configuration

The NEAT configuration file (`config.txt`) defines the genetic algorithm parameters such as population size, mutation rates, and activation functions. Modify this file to experiment with different settings.

## Files

- `main.py`: Main script to train or play with the PingPong AI.
- `PongGameAI.py`: Contains the `PongGame` class for game logic and AI interactions.
- `config/config.txt`: NEAT configuration file.
- `model/best.pickle`: Trained model saved as a pickle file.

## Acknowledgements

- [NEAT Python](https://neat-python.readthedocs.io/)
- [Pygame Documentation](https://www.pygame.org/docs/)
- [Creative Commons Attribution-NonCommercial License](https://creativecommons.org/licenses/by-nc/4.0/legalcode) for non-commercial use.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
