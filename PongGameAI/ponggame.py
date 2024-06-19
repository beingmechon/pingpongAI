from .game import Game

import neat
import pygame

class PongGame:
    def __init__(self, window, width, height, FPS=60) -> None:
        self.FPS = FPS
        self.game = Game(window, width, height)
        self.left_paddle = self.game.left_paddle
        self.right_paddle = self.game.right_paddle
        self.ball = self.game.ball

    def test_ai(self, genome, config):
        net = neat.nn.FeedForwardNetwork.create(genome, config)

        run = True
        clock = pygame.time.Clock()

        while run:
            clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type ==  pygame.QUIT:
                    run = False
                    break

            keys = pygame.key.get_pressed()

            if keys[pygame.K_w]:
                self.game.move_paddle(left=True, up=True)
            if keys[pygame.K_s]:
                self.game.move_paddle(left=True, up=False)

            # Uncomment below to enable UP Arrow and down Arrow key for the play
            # if keys[pygame.K_UP]:
            #     self.game.move_paddle(left=False, up=True)
            # if keys[pygame.K_DOWN]:
            #     self.game.move_paddle(left=False, up=False)

            output = net.activate((self.right_paddle.y, self.ball.y, abs(self.right_paddle.x - self.ball.x)))
            descision = output.index(max(output))
            # print(output, descision)

            if descision == 0:
                pass
            elif descision == 1:
                self.game.move_paddle(left=False, up=True)
            else:
                self.game.move_paddle(left=False, up=False)

            game_info = self.game.loop()
            self.game.draw(True, False)
            pygame.display.update()

        pygame.quit()

    def train_ai(self, genome1, genome2, config):
        net1 = neat.nn.FeedForwardNetwork.create(genome1, config)
        net2 = neat.nn.FeedForwardNetwork.create(genome2, config)

        run = True
        while run:
            for event in pygame.event.get():
                if event.type ==  pygame.QUIT:
                    quit()

            output1 = net1.activate((self.left_paddle.y, self.ball.y, abs(self.left_paddle.x - self.ball.x)))
            descision1 = output1.index(max(output1))

            if descision1 == 0:
                pass
            elif descision1 == 1:
                self.game.move_paddle(left=True, up=True)
            else:
                self.game.move_paddle(left=True, up=False)

            output2 = net2.activate((self.right_paddle.y, self.ball.y, abs(self.right_paddle.x - self.ball.x)))
            descision2 = output2.index(max(output2))

            if descision2 == 0:
                pass
            elif descision2 == 1:
                self.game.move_paddle(left=False, up=True)
            else:
                self.game.move_paddle(left=False, up=False)

            
            game_info = self.game.loop()
            self.game.draw(draw_score=False, draw_hits=True)
            pygame.display.update()

            if game_info.left_score >=1 or game_info.right_score >= 1 or game_info.left_hits > 50:
                self.calculate_fitness(genome1, genome2, game_info)
                break

    def calculate_fitness(self, genome1, genome2, game_info):
        genome1.fitness += game_info.left_hits
        genome2.fitness += game_info.right_hits
