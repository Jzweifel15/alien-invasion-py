import pygame
from pygame.sprite import Group

from settings import Settings 
from ship import Ship
from game_stats import GameStats
from button import Button

import game_functions as game_fns

def run_game():
  # Initialize pygame, settings, and screen object.
  pygame.init()
  ai_settings = Settings()
  screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
  pygame.display.set_caption("Alien Invasion")

  # Make the Play button
  play_button = Button(ai_settings, screen, "Play")

  # Create an instance of store game statistics
  stats = GameStats(ai_settings)

  # Make a ship, a group of bullets, and a group of aliens
  ship = Ship(ai_settings, screen)
  bullets = Group()
  aliens = Group()

  # Create the fleet of aliens
  game_fns.create_fleet(ai_settings, screen, ship, aliens)

  # Start the main loop for the game.
  while True:
    game_fns.check_events(ai_settings, screen, stats, play_button, ship, bullets)

    if stats.game_active:
      ship.update()
      game_fns.update_bullets(ai_settings, screen, ship, aliens, bullets)
      game_fns.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

    game_fns.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)


run_game() 
