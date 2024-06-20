import pickle
import sys
sys.path.append('../')

from graph_modules.graph.graph import Graph, Node, Edge, saveObject

def getKitchenRelation():
    relations = [
        ['cereal', 'bowl'],
        ['cereal', 'box'],
        ['teabag', 'water'],
        ['teabag', 'table'],
        ['bun', 'sandwich'],
        ['bun', 'butter'],
        ['butter', 'bread'],
        ['butter', 'pan'],
        ['butter', 'box'],
        ['butter', 'sandwich'],
        ['egg', 'pan'],
        ['egg', 'plate'],
        ['egg', 'sandwich'],
        ['egg', 'pancake'],
        ['saltnpepper', 'sandwich'],
        ['saltnpepper', 'egg'],
        ['saltnpepper', 'salad'],
        ['sugar', 'pancake'],
        ['sugar', 'tea'],
        ['sugar', 'coffee'],
        ['pancake', 'pan'],
        ['dough', 'table'],
        ['dough', 'pancake'],
        ['dough', 'bowl'],
        ['flour', 'dough'],
        ['flour', 'pancake'],
        ['sandwich', 'table'],
        ['sandwich', 'plate'],
        ['topping', 'salad'],
        ['fruit', 'table'],
        ['fruit', 'bowl'],
        ['milk', 'pancake'],
        ['milk', 'cereal'],
        ['milk', 'bowl'],
        ['milk', 'cup'],
        ['milk', 'bottle'],
        ['milk', 'tea'],
        ['milk', 'coffee'],
        ['water', 'cup'],
        ['water', 'bottle'],
        ['water', 'tea'],
        ['tea', 'cup'],
        ['oil', 'pan'],
        ['oil', 'bottle'],
        ['spoon', 'table'],
        ['knife', 'table'], 
        ['pan', 'table'],
        ['plate', 'table'],
        ['spoon', 'plate'],
        ['spoon', 'bowl'],
        ['bottle', 'table'],
        ['orange', 'fruit'],
        ['orange', 'table'],
        ['squeezer', 'table'],
        ['juice', 'glass'],
        ['juice', 'bottle'],
        ['cereal', 'bowl'],
        ['coffee', 'glass'],
        ['coffee', 'cup'],
        ['pan', 'stove'],
        ['pan', 'table'],
        ['milk', 'glass'],
        ['water', 'glass'],
        ['powder', 'spoon'],
        ['oil', 'spoon'],
        ['person', 'knife'],
        ['person', 'bottle'],
        ['person', 'glass'],
        ['person', 'plate'],
        ['person', 'cup'],
        ['person', 'table'],
        ['butter', 'ingredients'],
        ['egg', 'ingredients'],
        ['saltnpepper', 'ingredients'],
        ['sugar', 'ingredients'],
        ['dough', 'ingredients'],
        ['milk', 'ingredients'],
        ['oil', 'ingredients'],
        ['flour', 'ingredients'],
        ['vinegar', 'ingredients'],
        ['tomato', 'ingredients'],
        ['lettuce', 'ingredients'],
        ['cucumber', 'ingredients'],
        ['cheese', 'ingredients'],
        ['salt', 'ingredients'],
        ['salt', 'egg'],
        ['salt', 'sandwich'],
        ['salt', 'salad'],
        ['pepper', 'ingredients'],
        ['pepper', 'egg'],
        ['pepper', 'sandwich'],
        ['pepper', 'salad'],
        ['tomato', 'vegetable'],
        ['lettuce', 'vegetable'],
        ['cucumber', 'vegetable'],
        ['tomato', 'table'],
        ['lettuce', 'table'],
        ['cucumber', 'table'],
        ['peeler', 'table']
    ]

    affordances = [
        ['milk', 'pour'],
        ['milk', 'stir'],
        ['water', 'pour'],
        ['oil', 'pour'],
        ['juice', 'pour'],
        ['glass', 'contain'],
        ['cup', 'contain'],
        ['pan', 'contain'],
        ['bowl', 'contain'],
        ['tea', 'pour'],
        ['orange', 'squeeze'],
        ['orange', 'cut'],
        ['orange', 'peel'],
        ['coffee', 'pour'],
        ['coffee', 'stir'],
        ['cereal', 'pour'],
        ['cereal', 'stir'],
        ['sandwich', 'cut'],
        ['teabag', 'add'],
        ['fruit', 'cut'],
        ['fruit', 'put'],
        ['fruit', 'peel'],
        ['fruit', 'stir'],
        ['bun', 'cut'],
        ['bun', 'put together'],
        ['topping', 'put'],
        ['topping', 'take'],
        ['egg', 'fry'],
        ['egg', 'crack'],
        ['egg', 'stirfry'],
        ['egg', 'stir'],
        ['egg', 'pour'],
        ['egg', 'boil'],
        ['egg', 'put'],
        ['butter', 'smear'],
        ['buter', 'put'],
        ['buter', 'add'],
        ['water', 'boil'],
        ['milk', 'boil'],
        ['spoon', 'grasp'],
        ['knife', 'grasp'],
        ['pan', 'grasp'],
        ['plate', 'grasp'], 
        ['plate', 'take'],
        ['bottle', 'grasp'],
        ['dough', 'pour'],
        ['dough', 'stir'],
        ['flour', 'spoon'],
        ['flour', 'pour'],
        ['powder', 'spoon'],
        ['pancake', 'fry'],
        ['pancake', 'put'],
        ['saltnpepper', 'add'],
        ['sugar', 'spoon'],
        ['sugar', 'add'],
        ['sugar', 'pour'],
        ['bowl', 'take'],
        ['squeezer', 'take'],
        ['person', 'walk in'],
        ['person', 'walk out'],
        ['cereal', 'eat'],
        ['orange', 'eat'],
        ['egg', 'eat'],
        ['salad', 'eat'],
        ['cereal', 'eat'],
        ['bun', 'eat'],
        ['vegetable', 'cook'],
        ['vegetable', 'eat'],
        ['sugar', 'eat'],
        ['pancake', 'eat'],
        ['sandwich', 'eat'], 
        ['water', 'drink'],       
        ['tea', 'drink'],       
        ['coffee', 'drink'],
        ['juice', 'drink'],       
        ['milk', 'drink'],   
        ['cup', 'take'],
        ['cup', 'grasp'],
        ['tea', 'stir'],
        ['flour', 'pour'],
        ['ingredients', 'cut'],
        ['ingredients', 'mix'],
        ['ingredients', 'add'],
        ['dressing', 'prepare'],
        ['dressing', 'add'],
        ['dressing', 'mix'],
        ['salad', 'serve'],
        ['cheese', 'cut'],
        ['cucumber', 'cut'],
        ['cucumber', 'peel'],
        ['tomato', 'cut'],
        ['lettuce', 'cut'],
        ['cucumber', 'grasp'],
        ['tomato', 'grasp'],
        ['lettuce', 'grasp'],
        ['vinegar', 'add'],
        ['vinegar', 'pour'],
        ['oil', 'add'],
        ['salt', 'add'],
        ['pepper', 'add'],
        ['cheese', 'place'],
        ['tomato', 'place'],
        ['lettuce', 'place'],
        ['cucumber', 'place'],
        ['cheese', 'eat'],
        ['tomato', 'eat'],
        ['lettuce', 'eat'],
        ['cucumber', 'eat'],
        ['pancake', 'cook'],
        ['egg', 'cook'],
        ['sandwich', 'cook'],
    ]

    tools = [
        ['cut', 'knife'],
        ['pour', 'pan'],
        ['pour', 'bowl'],
        ['put', 'plate'],
        ['put', 'bowl'],
        ['add', 'bowl'],
        ['add', 'plate'],
        ['put', 'pan'],
        ['peel', 'peeler'],
        ['fry', 'pan'],
        ['stirfry', 'pan'],
        ['stir', 'spatula'],
        ['squeeze', 'squeezer'],
        ['serve', 'plate'],
        ['serve', 'bowl'],
        ['place', 'bowl'],
        # implicit ones: 
        ['grasp', 'person'],
        ['boil', 'stove'],
        # add for contains 
        # check these -->
        # ['eat', 'spoon'],
        # ['eat', 'person'],
        ['eat', 'bowl'],
        ['eat', 'plate'],
        ['drink', 'glass'],
        ['drink', 'cup'],
        # ['drink', 'bowl'],
    ]
    actions = [
        ['cut_tomato', 'cut'],
        ['cut_tomato', 'tomato'],
        ['cut_onion', 'cut'],
        ['cut_onion', 'onion'],
        ['cut_cucumber', 'cut'],
        ['cut_cucumber', 'cucumber'],
        ['cut_lettuce', 'cut'],
        ['cut_lettuce', 'lettuce'],
        ['cut_cheese', 'cut'],
        ['cut_cheese', 'cheese'],
        ['cut_bun', 'cut'],
        ['cut_bun', 'bun'],
        ['cut_bread', 'cut'],
        ['cut_bread', 'bread'],
        ['cut_orange', 'cut'],
        ['cut_orange', 'orange'],
        ['cut_fruit', 'cut'],
        ['cut_fruit', 'fruit'],
        ['cut_sandwich', 'cut'],
        ['cut_sandwich', 'sandwich'],
        ['cut_salad', 'cut'],
        ['cut_salad', 'salad'],
        ['cut_butter', 'cut'],
        ['cut_butter', 'butter'],
        ['break_egg', 'break'],
        ['break_egg', 'egg'],
        ['cut_pancake', 'cut'],
        ['cut_pancake', 'pancake'],
        ['cut_dough', 'cut'],
        ['cut_dough', 'dough'],
        ['prepare_dressing', 'prepare'],
        ['prepare_dressing', 'dressing'],
        ['serve_salad', 'serve'],
        ['serve_salad', 'salad'],
        ['mix_ingredients', 'mix'],
        ['mix_ingredients', 'ingredients'],
        ['add_pepper','add'],
        ['add_pepper','pepper'],
        ['cut_and_mix_ingredients', 'cut'],
        ['cut_and_mix_ingredients', 'mix'],
        ['cut_and_mix_ingredients', 'ingredients'],
        ['prepare_dressing', 'prepare'],
        ['prepare_dressing', 'dressing'],
        ['serve_salad', 'serve'],
        ['serve_salad', 'salad'],
        ['cut_cheese', 'cut'],
        ['cut_cheese', 'cheese'],
        ['cut_tomato', 'cut'],
        ['cut_tomato', 'tomato'],
        ['cut_lettuce', 'cut'],
        ['cut_lettuce', 'lettuce'],
        ['peel_cucumber', 'peel'],
        ['peel_cucumber', 'cucumber'],
        ['cut_cucumber', 'cut'],
        ['cut_cucumber', 'cucumber'],
        ['add_vinegar', 'add'],
        ['add_vinegar', 'vinegar'],
        ['add_oil', 'add'],
        ['add_oil', 'oil'],
        ['add_salt', 'add'],
        ['add_salt', 'salt'],
        ['add_pepper', 'add'],
        ['add_pepper', 'pepper'],
        ['mix_ingredients', 'mix'],
        ['mix_ingredients', 'ingredients'],
        ['serve_salad_onto_plate', 'serve'],
        ['serve_salad_onto_plate', 'salad'],
        ['serve_salad_onto_plate', 'plate'],
        ['place_cheese_into_bowl', 'place'],
        ['place_cheese_into_bowl', 'cheese'],
        ['place_cheese_into_bowl', 'bowl'],
        ['place_tomato_into_bowl', 'place'],
        ['place_tomato_into_bowl', 'tomato'],
        ['place_tomato_into_bowl', 'bowl'],
        ['place_lettuce_into_bowl', 'place'],
        ['place_lettuce_into_bowl', 'lettuce'],
        ['place_lettuce_into_bowl', 'bowl'],
        ['place_cucumber_into_bowl', 'place'],
        ['place_cucumber_into_bowl', 'cucumber'],
        ['place_cucumber_into_bowl', 'bowl'],
        ['mix_dressing', 'mix'],
        ['mix_dressing', 'dressing'],
        ['add_dressing', 'add'],
        ['add_dressing', 'dressing'],
        ['take_cup', 'take'],
        ['take_cup', 'cup'],
        ['pour_coffee', 'pour'],
        ['pour_coffee', 'coffee'],
        ['pour_milk', 'pour'],
        ['pour_milk', 'milk'],
        ['cut_orange', 'cut'],
        ['cut_orange', 'orange'],
        ['squeeze_orange', 'squeeze'],
        ['squeeze_orange', 'orange'],
        ['pour_juice', 'pour'],
        ['pour_juice', 'juice'],
        ['butter_pan', 'put'],
        ['butter_pan', 'butter'],
        ['butter_pan', 'pan'],
        ['crack_egg', 'crack'],
        ['crack_egg', 'egg'],
        ['fry_egg', 'fry'],
        ['fry_egg', 'egg'],
        ['put_egg2plate', 'put'],
        ['put_egg2plate', 'egg'],
        ['put_egg2plate', 'plate'],
        ['spoon_powder', 'spoon'],
        ['spoon_powder', 'powder'],
        ['stir_milk', 'stir'],
        ['stir_milk', 'milk'],
        ['add_teabag', 'add'],
        ['add_teabag', 'teabag'],
        ['pour_water', 'pour'],
        ['pour_water', 'water'],
        ['pour_cereals', 'pour'],
        ['pour_cereals', 'cereal'],
        ['cut_bun', 'cut'],
        ['cut_bun', 'bun'],
        ['smear_butter', 'smear'],
        ['smear_butter', 'butter'],
        ['take_topping', 'take'],
        ['take_topping', 'topping'],
        ['put_toppingOnTop', 'put'],
        ['put_toppingOnTop', 'topping'],
        ['spoon_flour', 'spoon'],
        ['spoon_flour', 'flour'],
        ['stir_dough', 'stir'],
        ['stir_dough', 'dough'],
        ['pour_dough2pan', 'pour'],
        ['pour_dough2pan', 'dough'],
        ['pour_dough2pan', 'pan'],
        ['fry_pancake', 'fry'],
        ['fry_pancake', 'pancake'],
        ['take_plate', 'take'],
        ['take_plate', 'plate'],
        ['put_pancake2plate', 'put'],
        ['put_pancake2plate', 'pancake'],
        ['put_pancake2plate', 'plate'],
        ['peel_fruit', 'peel'],
        ['peel_fruit', 'fruit'],
        ['cut_fruit', 'cut'],
        ['cut_fruit', 'fruit'],
        ['put_fruit2bowl', 'put'],
        ['put_fruit2bowl', 'fruit'],
        ['put_fruit2bowl', 'bowl'],
        ['stirfry_egg', 'stirfry'],
        ['stirfry_egg', 'egg'],
        ['add_saltnpepper', 'add'],
        ['add_saltnpepper', 'saltnpepper'],
        ['take_glass', 'take'],
        ['take_glass', 'glass'],
        ['take_squeezer', 'take'],
        ['take_squeezer', 'squeezer'],
        ['pour_oil', 'pour'],
        ['pour_oil', 'oil'],
        ['walk_out', 'walk out'],
        ['take_bowl', 'take'],
        ['take_bowl', 'bowl'],
        ['stir_egg', 'stir'],
        ['stir_egg', 'egg'],
        ['pour_egg2pan', 'pour'],
        ['pour_egg2pan', 'egg'],
        ['pour_egg2pan', 'pan'],
        ['pour_sugar', 'pour'],
        ['pour_sugar', 'sugar'],
        ['take_knife', 'take'],
        ['take_knife', 'knife'],
        ['stir_cereals', 'stir'],
        ['stir_cereals', 'cereal'],
        ['put_bunTogether', 'put together'],
        ['put_bunTogether', 'bun'],
        ['walk_in', 'walk in'],
        ['stir_coffee', 'stir'],
        ['stir_coffee', 'coffee'],
        ['spoon_sugar', 'spoon'],
        ['spoon_sugar', 'sugar'],
        ['stir_tea', 'stir'],
        ['stir_tea', 'tea'],
        ['take_eggs', 'take'],
        ['take_eggs', 'egg'],
        ['pour_flour', 'pour'],
        ['pour_flour', 'flour'],
        ['take_butter', 'take'],
        ['take_butter', 'butter'],
        ['stir_fruit', 'stir'],
        ['stir_fruit', 'fruit'],
        ['stirfry_eg', 'stirfry'],
        ['stirfry_eg', 'egg'],

    ]

    return relations, affordances, tools, actions

def makeGraph():
    relations, affordances, tools ,actions = getKitchenRelation()

    graph = Graph()

    for relation in relations:
        object1, object2 = relation
        
        if not graph.checkNodeNameExists(object1, 'object'): 
            graph.addNode(object1, 'object')

        if not graph.checkNodeNameExists(object2, 'object'):
            graph.addNode(object2, 'object')

        if not graph.checkEdgeNameExists(object1, object2)[0]:
            object1_idx = graph.getNode(object1)
            object2_idx = graph.getNode(object2)
            graph.addEdge(object1_idx, object2_idx)

    for affordance in affordances:
        object1, affordance2 = affordance

        if not graph.checkNodeNameExists(object1, 'object'):
            graph.addNode(object1, 'object')

        if not graph.checkNodeNameExists(affordance2, 'affordance'):
            graph.addNode(affordance2, 'affordance')

        if not graph.checkEdgeNameExists(object1, affordance2)[0]:
            object1_idx = graph.getNode(object1)
            object2_idx = graph.getNode(affordance2)
            graph.addEdge(object1_idx, object2_idx)

    for tool in tools:
        affordance1, object2 = tool
        
        if not graph.checkNodeNameExists(affordance1, 'affordance'):
            graph.addNode(affordance1, 'affordance')

        if not graph.checkNodeNameExists(object2, 'object'):
            graph.addNode(object2, 'object')

        if not graph.checkEdgeNameExists(affordance1, object2)[0]:
            object1_idx = graph.getNode(affordance1)
            object2_idx = graph.getNode(object2)
            graph.addEdge(object1_idx, object2_idx)
    
    for action_idx in actions:
        action, object2 = action_idx
        
        if not graph.checkNodeNameExists(action, 'action'):
            graph.addNode(action, 'action')

        if not graph.checkNodeNameExists(object2):
            graph.addNode(object2, 'object')

        if not graph.checkEdgeNameExists(action, object2)[0]:
            object1_idx = graph.getNode(action)
            object2_idx = graph.getNode(object2)
            graph.addEdge(object1_idx, object2_idx)

    # graph.printNodes()
    graph.writeNodes('nodelist_kitchen.csv')
    # graph.printEdges()
    print (graph.n_total_nodes, graph.n_total_edges)

    saveObject(graph, 'graph_kitchen.pkl')
        
if (__name__ == '__main__'):
    makeGraph()

