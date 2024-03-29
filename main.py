from Game import (Inventory, Map, Mobile, Engine)

def setup():
    inventory = Inventory()
    #makes an instance of the Inventory class to use as player's inventory
     
    main_map = Map()
    main_map.setup()
    #makes an instance of the Map class and passes it the item dictionary

    player = Mobile(inventory, main_map.all_rooms['tube_room'])
    #makes an instance of the the Mobile class for the player and puts it in the first room


    main_engine = Engine(main_map, player)
    #starts the engine with the map instance

    main_engine.move_into(player.location.label)
    #sets the player's location to the first room and moves into it
    return main_engine

main_engine = setup()
    
while not main_engine.player.victory:
    action = main_engine.prompt()
    main_engine.parse(action)
    
main_engine.victory()