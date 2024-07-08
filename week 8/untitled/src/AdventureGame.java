import java.util.*;

class Room {
    String description;
    HashMap<String, Room> exits;
    HashMap<String, String> items;
    String puzzle;
    String puzzleAnswer;

    public Room(String description, String puzzle, String puzzleAnswer) {
        this.description = description;
        this.exits = new HashMap<>();
        this.items = new HashMap<>();
        this.puzzle = puzzle;
        this.puzzleAnswer = puzzleAnswer;
    }
}

class Player {
    Room currentRoom;
    HashMap<String, String> inventory;
    HashMap<String, Integer> itemLookCount;

    public Player(Room currentRoom) {
        this.currentRoom = currentRoom;
        this.inventory = new HashMap<>();
        this.itemLookCount = new HashMap<>();
    }
}

public class AdventureGame {
    public static void main(String[] args) {
        Room room1 = new Room("You are in room 1.", null, null);
        Room room2 = new Room("You are in room 2. There is a locked door to the east.", "What is the square root of 144?", "12");
        Room room3 = new Room("You are in room 3.", null, null);

        room1.exits.put("north", room2);
        room2.exits.put("south", room1);
        room2.exits.put("east", room3);
        room3.exits.put("west", room2);

        room1.items.put("key", "A small, rusty key.");
        room1.items.put("rock", "It's just a rock.");
        room1.items.put("table", "A sturdy wooden table. Too heavy to pick up.");
        room1.items.put("chair", "A wooden chair. It's bolted to the floor.");
        room1.items.put("lamp", "An old lamp. It doesn't work.");
        room1.items.put("rug", "A dusty rug. It's too big to carry.");
        room2.items.put("map", "A map of the dungeon.");
        room2.items.put("candle", "A candle. It's not lit.");
        room2.items.put("book", "A book. The pages are blank.");
        room2.items.put("pen", "A pen. It's out of ink.");
        room2.items.put("paper", "A piece of paper. It's blank.");
        room2.items.put("cup", "A cup. It's empty.");
        room3.items.put("chest", "A large chest. It's locked.");
        room3.items.put("table", "A wooden table. There's something on it.");
        room3.items.put("chair", "A wooden chair. It's bolted to the floor.");
        room3.items.put("lamp", "An old lamp. It doesn't work.");
        room3.items.put("rug", "A dusty rug. It's too big to carry.");

        Player player = new Player(room1);

        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.println(player.currentRoom.description);
            System.out.println("Available commands: go [direction], get [item], inventory, look [direction/item/room], use [item]");
            String command = scanner.nextLine();

            String[] parts = command.split(" ");
            if (parts[0].equals("go")) {
                if (player.currentRoom.exits.containsKey(parts[1])) {
                    if (player.currentRoom.puzzle != null && player.currentRoom.puzzleAnswer != null) {
                        System.out.println("The door is locked. There is a puzzle: " + player.currentRoom.puzzle);
                    } else {
                        player.currentRoom = player.currentRoom.exits.get(parts[1]);
                    }
                } else {
                    System.out.println("There is no exit in that direction.");
                }
            } else if (parts[0].equals("get")) {
                if (player.currentRoom.items.containsKey(parts[1]) && !parts[1].equals("table") && !parts[1].equals("chest")) {
                    player.inventory.put(parts[1], player.currentRoom.items.get(parts[1]));
                    player.currentRoom.items.remove(parts[1]);
                    System.out.println("You picked up " + parts[1] + ".");
                } else {
                    System.out.println("You can't pick up that item.");
                }
            } else if (parts[0].equals("inventory")) {
                System.out.println("You are carrying: " + String.join(", ", player.inventory.keySet()));
            } else if (parts[0].equals("look")) {
                if (parts[1].equals("east") || parts[1].equals("west") || parts[1].equals("north") || parts[1].equals("south")) {
                    if (player.currentRoom.exits.containsKey(parts[1])) {
                        System.out.println("You see a door to the " + parts[1] + ".");
                    } else {
                        System.out.println("There is no door to the " + parts[1] + ".");
                    }
                } else if (player.inventory.containsKey(parts[1])) {
                    int count = player.itemLookCount.getOrDefault(parts[1], 0);
                    player.itemLookCount.put(parts[1], count + 1);
                    if (parts[1].equals("rock") && count >= 1) {
                        System.out.println("You look at the rock again. You notice something odd... The answer to the puzzle is a number between 10 and 15.");
                    } else {
                        System.out.println("You look at the " + parts[1] + ". " + player.inventory.get(parts[1]));
                    }
                } else if (parts[1].equals("room")) {
                    System.out.println("You see: " + String.join(", ", player.currentRoom.items.keySet()));
                } else {
                    System.out.println("You don't have that item.");
                }
            } else if (parts[0].equals("use")) {
                if (parts[1].equals("key") && player.inventory.containsKey("key") && player.currentRoom.items.containsKey("chest")) {
                    player.currentRoom.items.remove("chest");
                    player.currentRoom.items.put("open chest", "The chest is open. There's treasure inside!");
                    System.out.println("You use the key to open the chest.");
                } else if (parts[1].equals("puzzle") && player.currentRoom.puzzle != null) {
                    System.out.println("Enter the answer to the puzzle:");
                    String answer = scanner.nextLine();
                    if (player.currentRoom.puzzleAnswer.equals(answer)) {
                        player.currentRoom.puzzleAnswer = null;
                        System.out.println("The door unlocks!");
                    } else {
                        System.out.println("That's not the correct answer.");
                    }
                } else {
                    System.out.println("You can't use that item here.");
                }
            } else {
                System.out.println("Invalid command.");
            }
        }
    }
}