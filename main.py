import time
from skill_class import Skill
from entity_class import entity

#pygame initialization
import pygame
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

background = pygame.image.load("BOBackground.jpeg").convert()
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Player intialization
player_skill1 = Skill(4, 4, 3, "Player Skill 1", 3) # Base power 4, Coin power 4, 3 coins, 3 uses
player_skill2 = Skill(5, 5, 3, "Player Skill 2", 2) # Base power 5, Coin power 5, 3 coins, 2 uses
player_skill3 = Skill(8, 6, 2, "Player Skill 3", 1) # Base power 8, Coin power 6, 2 coins, 1 use
player_skills = [player_skill1, player_skill2, player_skill3]
player = entity(100, player_skills)

# Enemy initialization
enemy_skill1 = Skill(3, 3, 4, "Enemy Skill 1", 3) # Base power 3, Coin power 3, 4 coins, 3 uses
enemy_skill2 = Skill(4, 4, 4, "Enemy Skill 2", 2) # Base power 4, Coin power 4, 4 coins, 2 uses
enemy_skill3 = Skill(6, 5, 3, "Enemy Skill 3", 1) # Base power 6, Coin power 5, 3 coins, 1 use
enemy_skills = [enemy_skill1, enemy_skill2, enemy_skill3]
enemy = entity (100, enemy_skills)
testing = True

def clashing(p_skill, e_skill):
    global player
    global enemy
    p_coins = p_skill.initial_coins()
    e_coins = e_skill.initial_coins()
    clash = True
    while clash:
        p_num = p_skill.calculate(p_coins)
        e_num = e_skill.calculate(e_coins)
        print("Player rolls a " + str(p_num))
        if not testing:
            time.sleep(0.5)
        print("Enemy rolls a " + str(e_num))
        if not testing:
            time.sleep(0.5)
        if p_num > e_num:
            e_coins -= 1
            if not testing:
                time.sleep(0.5)
            print("Enemy loses 1 coin and has " + str(e_coins) + " remaining!")
        elif e_num > p_num:
            p_coins -= 1
            if not testing:
                time.sleep(0.5)
            print("Player loses 1 coin and has " + str(p_coins) + " remaining!")
        if not testing:
            time.sleep(1)
        print(" ")
        #nobody loses coins if roll same number
        if e_coins == 0:
            loser = enemy
            damage_num = p_skill.calculate(p_coins)
            skill_name = p_skill.get_name()
            print("Player attacks with " + str(p_coins) + " coins!")
            print("Player has " + str(p_skill.get_uses()) + " uses of " + str(p_skill.get_name()) + " remaining!")
            clash = False
        elif p_coins == 0:
            loser = player
            damage_num = e_skill.calculate(e_coins)
            skill_name = e_skill.get_name()
            print("Enemy attacks with " + str(e_coins) + " coins!")
            print("Enemy has " + str(e_skill.get_uses()) + " uses of " + str(e_skill.get_name()) + " remaining!")
            clash = False
        p_skill.change_uses(False)
        e_skill.change_uses(False)
        #take damage returns the health after calculations
        loser_health = loser.take_damage(damage_num)
    return loser, damage_num, skill_name, loser_health

def print_clash_results(results):
    loser, damage_to_take, skills_name, loser_hp = results
    print(print(loser + " takes " + str(damage_to_take) + " damage to " + skills_name + "!"))

def player_select_skill():
    list_of_skills = player.get_skills()
    print("Here are your skills: \n")
    for skill in list_of_skills:
        print(skill.__read__())
        print(" ")
    print("Reminder: Your skill uses will refresh once all your skills are used \n")
    selecting = True
    while selecting:
        request = int(input("Please enter the skill you would like to use as an integer (1, 2, or 3): "))
        selected = player.get_skill(request - 1)
        if selected.get_uses() <= 0:
            print("Please select a skill with uses remaining")
        else:
            selecting = False
    return selected

def skill_refreshing(player_or_enemy):
    skills = player_or_enemy.get_skills()
    refresh_skills = True
    for skill in skills:
        if skill.get_uses() > 0:
            refresh_skills = False
    if refresh_skills == True:
        for skill in skills:
            skill.change_uses(True)

def draw_text(text, font, color, x, y, center=False):
    """Utility function to draw text on the screen."""
    text_surface = font.render(text, True, color)
    if center:
        rect = text_surface.get_rect(center=(x, y))
        screen.blit(text_surface, rect)
    else:
        screen.blit(text_surface, (x, y))

def draw_health_bar(entity_obj, x, y, width, height, color):
    """Draws a health bar for the entity."""
    # Background (Max HP)
    pygame.draw.rect(screen, RED, (x, y, width, height), 0, 5) 
    
    # Current HP
    current_health_width = (entity_obj.get_hp() / entity_obj.max_hp) * width
    pygame.draw.rect(screen, color, (x, y, current_health_width, height), 0, 5)

    # Outline
    pygame.draw.rect(screen, BLACK, (x, y, width, height), 2, 5)
    
    # HP text
    hp_text = f"HP: {entity_obj.get_hp()}/{entity_obj.max_hp}"
    draw_text(hp_text, font_small, BLACK, x + width/2, y + 5, center=True)


def draw_ui():
    """Draws the main game user interface."""
    
    # Draw Health Bars
    draw_health_bar(player, 50, 50, 300, 30, GREEN)
    draw_health_bar(enemy, 450, 50, 300, 30, GREEN)
    draw_text("PLAYER", font_medium, BLACK, 50, 10)
    draw_text("ENEMY", font_medium, BLACK, 450, 10)

    # Draw Placeholders for Sprites
    pygame.draw.rect(screen, BLUE, (100, 150, 150, 200), 0, 10) # Player
    pygame.draw.rect(screen, RED, (550, 150, 150, 200), 0, 10) # Enemy
    draw_text("PLAYER", font_medium, WHITE, 175, 250, center=True)
    draw_text("ENEMY", font_medium, WHITE, 625, 250, center=True)
    
    # Draw Information based on State
    if GAME_STATE == "SELECT_SKILL":
        draw_text("Select Skill (Press 1, 2, or 3)", font_medium, BLACK, 400, 400, center=True)
        # Display available skills
        skills = player.get_skills()
        for i, skill in enumerate(skills):
             draw_text(f"[{i+1}] {skill.get_name()} (Uses: {skill.get_uses()})", 
                       font_small, BLACK, 100, 450 + i * 30)
             # Highlight if uses are zero
             if skill.get_uses() <= 0:
                 draw_text("NO USES", font_small, RED, 300, 450 + i * 30)

    elif GAME_STATE == "CLASH_RESULT" and current_clash_result:
        loser_name, damage_to_take, skill_name, _, _ = current_clash_result
        
        # Display the result
        result_text = f"{loser_name} takes {damage_to_take} damage from {skill_name}!"
        draw_text(result_text, font_medium, BLACK, 400, 450, center=True)
        
        # Check and display refresh notification
        player_refreshed = skill_refreshing(player)
        enemy_refreshed = skill_refreshing(enemy)
        
        if player_refreshed or enemy_refreshed:
             draw_text("SKILLS REFRESHED!", font_medium, BLUE, 400, 500, center=True)
             
        draw_text("Press SPACE to Continue", font_small, BLACK, 400, 550, center=True)
    
    elif GAME_STATE == "GAME_OVER":
        winner = "PLAYER" if enemy.get_hp() <= 0 else "ENEMY"
        draw_text("GAME OVER!", font_large, RED, 400, 200, center=True) 
        draw_text(f"{winner} WINS!", font_large, BLUE, 400, 250, center=True)
        draw_text("Press ESC to exit", font_small, BLACK, 400, 300, center=True)


# --- MAIN GAME LOOP ---

def game_loop():
    """Main function that handles events, logic, and drawing."""
    global GAME_STATE, current_clash_result, player, enemy

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if GAME_STATE == "SELECT_SKILL":
                    selected_skill_index = -1
                    if event.key == pygame.K_1:
                        selected_skill_index = 0
                    elif event.key == pygame.K_2:
                        selected_skill_index = 1
                    elif event.key == pygame.K_3:
                        selected_skill_index = 2
                    
                    if selected_skill_index != -1:
                        p_skill = player.get_skill(selected_skill_index)
                        
                        # Only proceed if the skill is valid and has uses
                        if p_skill and p_skill.get_uses() > 0:
                            # Enemy always uses skill 1 for this demo
                            e_skill = enemy_skill1 
                            
                            # CARRY OUT CLASH
                            current_clash_result = clashing(p_skill, e_skill)
                            
                            # Check for game over immediately after clash
                            if player.get_hp() <= 0 or enemy.get_hp() <= 0:
                                GAME_STATE = "GAME_OVER"
                            else:
                                GAME_STATE = "CLASH_RESULT"
                        else:
                            print("Skill has no uses or invalid selection.")
                            
                elif GAME_STATE == "CLASH_RESULT" and event.key == pygame.K_SPACE:
                    # After seeing the results, go back to the selection screen
                    GAME_STATE = "SELECT_SKILL"
                    current_clash_result = None
                
                elif GAME_STATE == "GAME_OVER" and event.key == pygame.K_ESCAPE:
                    running = False

        # B. LOGIC UPDATE 
        
        # C. DRAWING / RENDERING
        screen.blit(background, (0, 0))
        draw_ui()

        # D. DISPLAY UPDATE
        pygame.display.flip()
        
        # E. FRAME RATE CONTROL
        clock.tick(60) 

    pygame.quit()

if __name__ == "__main__":
    game_loop()

while True:
    selected_skill = player_select_skill()
    print_clash_results(clashing(selected_skill, enemy_skill1))
    skill_refreshing(player)
    skill_refreshing(enemy)