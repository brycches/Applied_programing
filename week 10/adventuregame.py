import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 800, 600
room_width, room_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Dungeon Crawler')

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BROWN = (139, 69, 19)
GRAY = (169, 169, 169)

# Define initial stat points
total_stat_points = 20
stats = {
    "Strength": 0,
    "Dexterity": 0,
    "Intelligence": 0,
    "Speed": 0,
    "Health": 0
}

# Character class
class Character:
    def __init__(self, x, y, stats):
        self.x = x
        self.y = y
        self.size = 50
        self.color = RED
        self.speed = 2 + stats["Speed"]
        self.max_health = 50 + stats["Health"] * 10
        self.health = self.max_health
        self.attack = 5 + stats["Strength"] * 2
        self.dexterity = stats["Dexterity"]
        self.intelligence = stats["Intelligence"]
        self.inventory = []
        self.gold = 0
        self.stats = stats

    def move(self, dx, dy, walls):
        if not self.collides_with_walls(dx, dy, walls):
            self.x += dx
            self.y += dy

    def collides_with_walls(self, dx, dy, walls):
        next_x = self.x + dx
        next_y = self.y + dy
        for wall in walls:
            if wall.colliderect(pygame.Rect(next_x, next_y, self.size, self.size)):
                return True
        return False

    def collides_with_event(self, event_rect):
        if event_rect is None:
            return False
        return event_rect.colliderect(pygame.Rect(self.x, self.y, self.size, self.size))

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.size, self.size))

    def add_item(self, item):
        self.inventory.append(item)
        if item == 'iron sword':
            self.attack += 5

# Room class
class Room:
    def __init__(self, room_type, has_event=True):
        self.room_type = room_type
        self.color = [random.randint(100, 255) for _ in range(3)]
        self.event = self.generate_event() if has_event else None
        self.has_event_object = self.event is not None
        self.walls = self.generate_walls()
        self.event_rect = None
        self.event_triggered = False
        self.random_event_position()
        self.enemies = self.generate_enemies() if has_event and self.event is None else []

    def generate_event(self):
        events = [
            ("There's a goblin, do you punch it?", "Punch it", "Run away", "You punch the goblin.", "goblin"),
            ("You find an iron sword, add to inventory?", "Yes", "No", "You put the sword in your bag, gain +5 attack.", "iron sword"),
            ("You find a treasure chest, do you open it?", "Open it", "Leave it", "You find some gold inside.", "treasure"),
            ("You find a health potion, do you drink it?", "Drink it", "Leave it", "You drink the potion and restore health.", "potion"),
            ("You encounter a trap, do you try to disarm it?", "Disarm it", "Avoid it", "You successfully disarm the trap.", "trap"),
            ("You see a mystic altar, do you approach it?", "Approach it", "Ignore it", "The altar grants you a temporary buff.", "altar"),
            ("You meet a mysterious merchant, do you buy something?", "Buy", "Ignore", "You buy an item from the merchant.", "merchant"),
            ("You find an ancient scroll, do you read it?", "Read it", "Ignore", "You learn a new skill.", "scroll"),
            ("You find a magic fountain, do you drink from it?", "Drink", "Ignore", "You feel rejuvenated.", "fountain"),
            ("You discover a hidden door, do you enter?", "Enter", "Ignore", "You find a secret room.", "hidden door"),
            ("You see a cursed idol, do you touch it?", "Touch it", "Ignore it", "The idol curses you.", "idol"),
            ("You encounter a riddle, do you try to solve it?", "Solve it", "Ignore", "You solve the riddle and gain a reward.", "riddle"),
            ("You find a glowing gem, do you take it?", "Take it", "Leave it", "You feel a surge of power.", "gem"),
            ("A magical barrier blocks your path, do you dispel it?", "Dispel it", "Leave it", "The barrier vanishes.", "barrier"),
            ("You hear strange noises, do you investigate?", "Investigate", "Leave", "You find a hidden passage.", "passage"),
            ("You find a mysterious book, do you read it?", "Read it", "Ignore", "You gain knowledge.", "book")
        ]
        return random.choice(events) if random.random() < 0.5 else None

    def generate_walls(self):
        walls = []
        if random.random() < 0.5:  # 50% chance to have walls
            if self.room_type == "left_wall":
                walls.append(pygame.Rect(room_width // 2 - 10, 0, 20, screen_height))
            elif self.room_type == "right_wall":
                walls.append(pygame.Rect(room_width // 2 - 10, 0, 20, screen_height))
            elif self.room_type == "top_wall":
                walls.append(pygame.Rect(0, room_height // 2 - 10, screen_width, 20))
            elif self.room_type == "bottom_wall":
                walls.append(pygame.Rect(0, room_height // 2 - 10, screen_width, 20))
        return walls

    def random_event_position(self):
        if not self.has_event_object:
            return
        while True:
            x = random.randint(50, room_width - 50)
            y = random.randint(50, room_height - 50)
            event_rect = pygame.Rect(x - 25, y - 25, 50, 50)
            if not any(wall.colliderect(event_rect) for wall in self.walls):
                self.event_rect = event_rect
                break

    def generate_enemies(self):
        enemies = []
        for _ in range(random.randint(1, 2)):  # Random number of enemies per room
            x = random.randint(50, room_width - 50)
            y = random.randint(50, room_height - 50)
            size = random.randint(20, 40)
            speed = random.randint(1, 3)
            enemies.append({"rect": pygame.Rect(x, y, size, size), "speed": speed})
        return enemies

    def draw(self, surface):
        # Draw room walls based on room type
        for wall in self.walls:
            pygame.draw.rect(surface, GRAY, wall)

        # Draw event objects
        if self.has_event_object and not self.event_triggered:
            if self.event[4] == "goblin":
                pygame.draw.circle(surface, GREEN, self.event_rect.center, 25)
            elif self.event[4] == "treasure":
                pygame.draw.rect(surface, YELLOW, self.event_rect)
            elif self.event[4] == "potion":
                pygame.draw.circle(surface, BLUE, self.event_rect.center, 25)
            elif self.event[4] == "altar":
                pygame.draw.rect(surface, BROWN, self.event_rect)
            elif self.event[4] == "merchant":
                pygame.draw.rect(surface, WHITE, self.event_rect)
            elif self.event[4] == "scroll":
                pygame.draw.rect(surface, WHITE, self.event_rect)
            elif self.event[4] == "fountain":
                pygame.draw.circle(surface, BLUE, self.event_rect.center, 30)
            elif self.event[4] == "hidden door":
                pygame.draw.rect(surface, BLACK, self.event_rect)
            elif self.event[4] == "idol":
                pygame.draw.circle(surface, RED, self.event_rect.center, 25)
            elif self.event[4] == "riddle":
                pygame.draw.rect(surface, WHITE, self.event_rect)
            elif self.event[4] == "gem":
                pygame.draw.rect(surface, YELLOW, self.event_rect)
            elif self.event[4] == "barrier":
                pygame.draw.rect(surface, BLUE, self.event_rect)
            elif self.event[4] == "passage":
                pygame.draw.rect(surface, BROWN, self.event_rect)
            elif self.event[4] == "book":
                pygame.draw.rect(surface, WHITE, self.event_rect)

        # Draw enemies
        for enemy in self.enemies:
            pygame.draw.rect(surface, RED, enemy["rect"])

# Create a dungeon
def generate_dungeon(width, height, start_x, start_y):
    room_types = ["empty", "left_wall", "right_wall", "top_wall", "bottom_wall"]
    dungeon = [[Room(random.choice(room_types)) for _ in range(height)] for _ in range(width)]
    
    # Ensure there's a guaranteed staircase in one of the rooms
    staircase_room = dungeon[random.randint(0, width - 1)][random.randint(0, height - 1)]
    staircase_room.event = ("You find a staircase leading down, do you descend?", "Descend", "Stay", "You descend to a new level.", "staircase")
    staircase_room.has_event_object = True
    staircase_room.event_triggered = False
    staircase_room.random_event_position()
    staircase_room.enemies = []  # No enemies in the room with the staircase
    
    # Ensure starting room is safe and doesn't have an event
    dungeon[start_x][start_y] = Room("empty", has_event=False)

    return dungeon

def random_dungeon_size():
    return random.randint(3, 7), random.randint(3, 7)

dungeon_width, dungeon_height = random_dungeon_size()
start_x, start_y = random.randint(0, dungeon_width - 1), random.randint(0, dungeon_height - 1)
dungeon = generate_dungeon(dungeon_width, dungeon_height, start_x, start_y)

# Starting room coordinates
current_room_x, current_room_y = start_x, start_y

# Current dungeon level
current_level = 1

# Create a character instance in the starting room
def create_player(room, stats):
    player = Character(room_width // 2, room_height // 2, stats)
    while player.collides_with_event(room.event_rect) or player.collides_with_walls(0, 0, room.walls):
        player.x = random.randint(0, room_width - player.size)
        player.y = random.randint(0, room_height - player.size)
    return player

player = None

# Set up the clock for controlling the frame rate
clock = pygame.time.Clock()
fps = 60  # Frames per second

# Event handling variables
event_active = False
current_event = None

# Inventory view state
inventory_view_active = False

# Display text
display_text = ""

def handle_event_choice(choice):
    global event_active, dungeon, current_room_x, current_room_y, player, display_text, current_room, dungeon_width, dungeon_height, start_x, start_y, current_level
    if current_event[4] == "goblin":
        if choice == 1:
            if player.attack > 20:  # Check Strength
                gold_found = random.randint(1, 20)
                player.gold += gold_found
                display_text = f"You kill the goblin and find {gold_found} gold."
            else:
                player.health -= 10
                display_text = "The goblin bites you, lose 10 health."
        elif choice == 2:
            display_text = "You run away from the goblin."
    elif current_event[4] == "iron sword":
        if choice == 1:
            player.add_item("iron sword")
            display_text = "You put the sword in your bag, gain +5 attack."
        elif choice == 2:
            display_text = "You leave the sword."
    elif current_event[4] == "treasure":
        if choice == 1:
            gold_found = random.randint(10, 50)
            player.gold += gold_found
            display_text = f"You find {gold_found} gold in the chest."
        elif choice == 2:
            display_text = "You leave the chest."
    elif current_event[4] == "potion":
        if choice == 1:
            health_restored = random.randint(10, 30)
            player.health += health_restored
            if player.health > player.max_health:
                player.health = player.max_health
            display_text = f"You restore {health_restored} health by drinking the potion."
        elif choice == 2:
            display_text = "You leave the potion."
    elif current_event[4] == "trap":
        if choice == 1:
            if player.dexterity > 10:  # Check Dexterity
                gold_found = random.randint(10, 30)
                player.gold += gold_found
                display_text = f"You successfully disarm the trap and find {gold_found} gold."
            else:
                player.health -= 20
                display_text = "You fail to disarm the trap and lose 20 health."
        elif choice == 2:
            display_text = "You avoid the trap."
    elif current_event[4] == "altar":
        if choice == 1:
            if player.intelligence > 10:
                player.attack += 10
                display_text = "The altar grants you a +10 attack buff."
            else:
                player.health -= 20
                display_text = "The altar curses you, lose 20 health."
        elif choice == 2:
            display_text = "You ignore the altar."
    elif current_event[4] == "merchant":
        if choice == 1:
            if player.gold >= 10:
                player.gold -= 10
                player.add_item("mysterious item")
                display_text = "You buy a mysterious item from the merchant."
            else:
                display_text = "You don't have enough gold to buy anything."
        elif choice == 2:
            display_text = "You ignore the merchant."
    elif current_event[4] == "scroll":
        if choice == 1:
            player.attack += 5
            display_text = "You learn a new skill and gain +5 attack."
        elif choice == 2:
            display_text = "You ignore the scroll."
    elif current_event[4] == "fountain":
        if choice == 1:
            player.health = player.max_health
            display_text = "You feel fully rejuvenated after drinking from the fountain."
        elif choice == 2:
            display_text = "You ignore the fountain."
    elif current_event[4] == "hidden door":
        if choice == 1:
            gold_found = random.randint(20, 100)
            player.gold += gold_found
            display_text = f"You find a secret room and gain {gold_found} gold."
        elif choice == 2:
            display_text = "You ignore the hidden door."
    elif current_event[4] == "idol":
        if choice == 1:
            if player.intelligence > 10:
                player.attack += 5
                display_text = "The idol blesses you, gain +5 attack."
            else:
                player.health -= 15
                display_text = "The idol curses you, lose 15 health."
        elif choice == 2:
            display_text = "You ignore the idol."
    elif current_event[4] == "riddle":
        if choice == 1:
            if player.intelligence > 10:  # Check Intelligence
                gold_found = random.randint(10, 50)
                player.gold += gold_found
                display_text = f"You solve the riddle and gain {gold_found} gold."
            else:
                player.health -= 10
                display_text = "You fail to solve the riddle and lose 10 health."
        elif choice == 2:
            display_text = "You ignore the riddle."
    elif current_event[4] == "staircase":
        if choice == 1:
            dungeon_width, dungeon_height = random_dungeon_size()
            start_x, start_y = random.randint(0, dungeon_width - 1), random.randint(0, dungeon_height - 1)
            dungeon = generate_dungeon(dungeon_width, dungeon_height, start_x, start_y)
            current_room_x, current_room_y = start_x, start_y
            current_level += 1
            player = create_player(dungeon[current_room_x][current_room_y], player.stats)
            display_text = "You descend to a new dungeon level."
        elif choice == 2:
            display_text = "You stay on the current level."
    elif current_event[4] == "gem":
        if choice == 1:
            player.attack += 10
            display_text = "You feel a surge of power, gain +10 attack."
        elif choice == 2:
            display_text = "You leave the gem."
    elif current_event[4] == "barrier":
        if choice == 1:
            if player.intelligence > 10:
                display_text = "The barrier vanishes."
            else:
                player.health -= 10
                display_text = "The barrier shocks you, lose 10 health."
        elif choice == 2:
            display_text = "You leave the barrier."
    elif current_event[4] == "passage":
        if choice == 1:
            gold_found = random.randint(10, 50)
            player.gold += gold_found
            display_text = f"You find a hidden passage and gain {gold_found} gold."
        elif choice == 2:
            display_text = "You leave the passage."
    elif current_event[4] == "book":
        if choice == 1:
            player.intelligence += 5
            display_text = "You gain knowledge, gain +5 intelligence."
        elif choice == 2:
            display_text = "You leave the book."
    elif current_event[4] == "fight":
        if choice == 1:
            required_strength = 15 + current_level * 5
            damage_dealt = 15 + current_level * 5
            if player.attack > required_strength:
                gold_found = random.randint(5, 20)
                player.gold += gold_found
                display_text = f"You defeat the enemy and find {gold_found} gold."
                current_room.enemies.remove(current_event[5])
            else:
                player.health -= damage_dealt
                display_text = f"The enemy wounds you, lose {damage_dealt} health."
                if player.health <= 0:
                    display_text += " You have died."
                    event_active = False
                    return end_game()
        elif choice == 2:
            display_text = "You run away from the enemy."
    current_room.event_triggered = True
    event_active = False

def transition_room(new_room_x, new_room_y, dx, dy):
    global current_room_x, current_room_y, player, current_room
    current_room_x = max(0, min(new_room_x, dungeon_width - 1))
    current_room_y = max(0, min(new_room_y, dungeon_height - 1))
    current_room = dungeon[current_room_x][current_room_y]
    if dx != 0:  # Moving left or right
        player.y = max(0, min(player.y, screen_height - player.size))
        if dx > 0:
            player.x = 0
        else:
            player.x = screen_width - player.size
    if dy != 0:  # Moving up or down
        player.x = max(0, min(player.x, screen_width - player.size))
        if dy > 0:
            player.y = 0
        else:
            player.y = screen_height - player.size
    while player.collides_with_walls(0, 0, current_room.walls):
        player.x = random.randint(0, room_width - player.size)
        player.y = random.randint(0, room_height - player.size)

def end_game():
    global running
    running = False
    print("Game Over")

# Character Creation Screen
def character_creation_screen():
    global total_stat_points
    selected_stat = "Strength"
    running = True
    while running:
        screen.fill(BLACK)
        font = pygame.font.Font(None, 36)
        y_offset = 100

        # Display available stat points
        stat_points_text = font.render(f"Stat Points: {total_stat_points}", True, WHITE)
        screen.blit(stat_points_text, (50, 50))

        # Display stats and selection
        for stat in stats:
            stat_text = font.render(f"{stat}: {stats[stat]}", True, WHITE if stat == selected_stat else GRAY)
            screen.blit(stat_text, (50, y_offset))
            y_offset += 50

        # Display instructions
        instructions_text1 = font.render("Use UP/DOWN to select a stat,", True, WHITE)
        instructions_text2 = font.render("LEFT/RIGHT to allocate points,", True, WHITE)
        instructions_text3 = font.render("ENTER to start", True, WHITE)
        screen.blit(instructions_text1, (50, 400))
        screen.blit(instructions_text2, (50, 450))
        screen.blit(instructions_text3, (50, 500))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and total_stat_points == 0:
                    running = False
                elif event.key == pygame.K_UP:
                    selected_stat = list(stats.keys())[max(0, list(stats.keys()).index(selected_stat) - 1)]
                elif event.key == pygame.K_DOWN:
                    selected_stat = list(stats.keys())[min(len(stats) - 1, list(stats.keys()).index(selected_stat) + 1)]
                elif event.key == pygame.K_LEFT and stats[selected_stat] > 0:
                    stats[selected_stat] -= 1
                    total_stat_points += 1
                elif event.key == pygame.K_RIGHT and total_stat_points > 0:
                    stats[selected_stat] += 1
                    total_stat_points -= 1

        pygame.display.flip()
        clock.tick(fps)

# Main game loop
def main_game_loop():
    global running, event_active, current_event, display_text, inventory_view_active
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e and not event_active:
                    inventory_view_active = not inventory_view_active

                if event_active:
                    if event.key == pygame.K_1:  # Player chooses option 1
                        handle_event_choice(1)
                    elif event.key == pygame.K_2:  # Player chooses option 2
                        handle_event_choice(2)

        if event_active:
            # Display the event and choices
            font = pygame.font.Font(None, 36)
            screen.fill(BLACK)  # Clear the screen before drawing text
            text = font.render(current_event[0], True, WHITE)
            screen.blit(text, (50, 50))

            option1 = font.render("1. " + current_event[1], True, WHITE)
            screen.blit(option1, (50, 100))

            option2 = font.render("2. " + current_event[2], True, WHITE)
            screen.blit(option2, (50, 150))
        elif inventory_view_active:
            # Display the inventory and stats
            font = pygame.font.Font(None, 36)
            text_lines = [
                f"Health: {player.health}/{player.max_health}",
                f"Attack: {player.attack}",
                f"Dexterity: {player.dexterity}",
                f"Intelligence: {player.intelligence}",
                f"Gold: {player.gold}",
                "Inventory:"
            ] + player.inventory

            screen.fill(BLACK)
            for i, line in enumerate(text_lines):
                text = font.render(line, True, WHITE)
                screen.blit(text, (50, 50 + i * 40))
        else:
            # Get the set of keys pressed
            keys = pygame.key.get_pressed()

            # Move character based on key input
            if keys[pygame.K_w]:  # Move up
                player.move(0, -player.speed, dungeon[current_room_x][current_room_y].walls)
                if player.y < 0:
                    if current_room_y > 0:
                        transition_room(current_room_x, current_room_y - 1, 0, -1)
                        player.y = screen_height - player.size
                        event_active = False
                        current_event = None
                    else:
                        player.y = 0
            if keys[pygame.K_s]:  # Move down
                player.move(0, player.speed, dungeon[current_room_x][current_room_y].walls)
                if player.y + player.size > screen_height:
                    if current_room_y < dungeon_height - 1:
                        transition_room(current_room_x, current_room_y + 1, 0, 1)
                        player.y = 0
                        event_active = False
                        current_event = None
                    else:
                        player.y = screen_height - player.size
            if keys[pygame.K_a]:  # Move left
                player.move(-player.speed, 0, dungeon[current_room_x][current_room_y].walls)
                if player.x < 0:
                    if current_room_x > 0:
                        transition_room(current_room_x - 1, current_room_y, -1, 0)
                        player.x = screen_width - player.size
                        event_active = False
                        current_event = None
                    else:
                        player.x = 0
            if keys[pygame.K_d]:  # Move right
                player.move(player.speed, 0, dungeon[current_room_x][current_room_y].walls)
                if player.x + player.size > screen_width:
                    if current_room_x < dungeon_width - 1:
                        transition_room(current_room_x + 1, current_room_y, 1, 0)
                        player.x = 0
                        event_active = False
                        current_event = None
                    else:
                        player.x = screen_width - player.size

            # Fill the screen with the current room's color
            current_room = dungeon[current_room_x][current_room_y]
            screen.fill(current_room.color)

            # Draw the room's elements
            current_room.draw(screen)

            # Draw the character
            player.draw(screen)

            # Move enemies towards player
            for enemy in current_room.enemies:
                if enemy["rect"].x < player.x:
                    enemy["rect"].x += enemy["speed"]
                if enemy["rect"].x > player.x:
                    enemy["rect"].x -= enemy["speed"]
                if enemy["rect"].y < player.y:
                    enemy["rect"].y += enemy["speed"]
                if enemy["rect"].y > player.y:
                    enemy["rect"].y -= enemy["speed"]

                # Check for collision with player
                if player.collides_with_event(enemy["rect"]):
                    current_event = ("You are attacked by an enemy! Do you fight back?", "Fight", "Run", "You engage in combat.", "fight", enemy)
                    event_active = True
                    display_text = ""

            # Check for event collision
            if current_room.has_event_object and not current_room.event_triggered and player.collides_with_event(current_room.event_rect):
                current_event = current_room.event
                event_active = True
                display_text = ""

        # Display result text
        if display_text:
            font = pygame.font.Font(None, 36)
            result_text = font.render(display_text, True, WHITE)
            screen.blit(result_text, (50, 500))

        # Update the display
        pygame.display.flip()

        # Limit the frame rate
        clock.tick(fps)

# Run character creation screen first
character_creation_screen()

# Initialize player after character creation
player = create_player(dungeon[current_room_x][current_room_y], stats)

# Run the main game loop
main_game_loop()

# Quit Pygame
pygame.quit()
sys.exit()
