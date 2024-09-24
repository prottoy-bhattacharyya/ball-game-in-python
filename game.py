import pygame
import time

pygame.init()
pygame.mouse.set_visible(False)
disp_info = pygame.display.Info()
screen_width = disp_info.current_w
screen_height = disp_info.current_h

screen = pygame.display.set_mode((screen_width, screen_height))

# pygame.display.set_caption("Pong")

bg_color = (52,86,48)
white = (255, 255, 255)
paddle_width = 10
paddle_height = 200
ball_radius = 10
paddle_speed = 5
high_score = 0


paddle1 = pygame.Rect(0, screen_height // 2 - paddle_height // 2, paddle_width, paddle_height)
paddle2 = pygame.Rect(screen_width - paddle_width, screen_height // 2 - paddle_height // 2, paddle_width, paddle_height)
ball = pygame.Rect(screen_width // 2 - ball_radius, screen_height // 2 - ball_radius, ball_radius * 2, ball_radius * 2)



def game():
    ball_speed_x = 1
    ball_speed_y = 1
    score = 0
    global high_score
    

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if score > high_score:
            high_score = score
        
        # Paddle Movement
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and paddle1.top >= 0:
            paddle1.y -= paddle_speed
            paddle2.y -= paddle_speed
        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and paddle1.bottom <= screen_height:
            paddle2.y += paddle_speed
            paddle1.y += paddle_speed
        if keys[pygame.K_ESCAPE]:
            pygame.quit()

        # Ball Movement
        ball.x += ball_speed_x
        ball.y += ball_speed_y

        # Ball Collisions
        if ball.top <= 0 or ball.bottom >= screen_height:
            ball_speed_y = -ball_speed_y
        if ball.colliderect(paddle1) or ball.colliderect(paddle2):
            ball_speed_x = -ball_speed_x
            score += 1 # Update Score

        # Check for game over
        if ball.left <= 0 or ball.right >= screen_width:
            font = pygame.font.Font(None, 35)
            game_over = font.render(str("Game Over"), True, white)
            disp_score = font.render(str("Your Score : ") + str(score), True, white)
            screen.blit(game_over, (screen_width // 2, screen_height // 2))
            screen.blit(disp_score, (screen_width // 2, screen_height // 2 + 40))
            pygame.display.update()
            time.sleep(2.0)
            ball.x = screen_width//2
            ball.y = screen_height//2
            game()
            
        else:
            # Draw Objects
            screen.fill(bg_color)
            pygame.draw.rect(screen, white, paddle1)
            pygame.draw.rect(screen, white, paddle2)
            pygame.draw.circle(screen, white, ball.center, ball_radius)

            # Draw Score
            font = pygame.font.Font(None, 36)
            text1 = font.render(str("Score: ") + str(score), True, white)
            text2 = font.render(str("High Score: ") + str(high_score), True, white)
            screen.blit(text1, (screen_width // 4 , 20))
            screen.blit(text2, (screen_width // 4 * 3, 20))
            pygame.display.update()

game()
