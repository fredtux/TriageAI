import yaml
from yaml.loader import SafeLoader
import numpy as np   
import networkx as nx  
import matplotlib.pyplot as plt

graph = {}

def get_story_checkpoint(step):
    if "checkpoint" in step:
        return step["checkpoint"]
    else:
        return "greet"

if __name__ == '__main__':
    with open("rasa/data/stories.yml") as f:
        stories = yaml.load(f, Loader=SafeLoader)["stories"]
        
        graph["greet"] = []
                
        for story in stories:
            story_chkpt = get_story_checkpoint(story["steps"][0])
            # graph[story["story"]] = []
            # graph[story_chkpt].append(story["story"])
            
            for i in range(1, len(story["steps"])):
                if "checkpoint" in story["steps"][i]:
                    new_chkpt = story["steps"][i]["checkpoint"]
                    if new_chkpt not in graph:
                        graph[new_chkpt] = []
                    
                    
                    graph[story_chkpt].append(new_chkpt)
                
                if "action" in story["steps"][i].keys() and story["steps"][i]["action"] in ["utter_red_code", "utter_orange_code", "utter_yellow_code", "utter_green_code", "utter_blue_code"]:
                    graph[story_chkpt].append(story["steps"][i]["action"])
        
        G = nx.DiGraph()
        
        gkeys = graph.keys()
        for key in gkeys:
            G.add_node(key)
            
            for value in graph[key]:
                G.add_edge(key, value)
                
        G.add_nodes_from(["utter_red_code", "utter_orange_code", "utter_yellow_code", "utter_green_code", "utter_blue_code"])
        
        # Check if each node has a path to utter_red_code
        color_map = []
        for node in G.nodes:
            if node != "utter_red_code":
                if nx.has_path(G, node, "utter_red_code"):
                    color_map.append("green")
                    continue
                    
            if node != "utter_orange_code":
                if nx.has_path(G, node, "utter_orange_code"):
                    color_map.append("green")
                    continue
                    
            if node != "utter_yellow_code":
                if nx.has_path(G, node, "utter_yellow_code"):
                    color_map.append("green")
                    continue
                    
            if node != "utter_green_code":
                if nx.has_path(G, node, "utter_green_code"):
                    color_map.append("green")
                    continue
                    
            if node != "utter_blue_code":
                if nx.has_path(G, node, "utter_blue_code"):
                    color_map.append("green")
                    continue
                
            if node in ["utter_red_code", "utter_orange_code", "utter_yellow_code", "utter_green_code", "utter_blue_code"]:
                color_map.append("blue")
                continue
                
            color_map.append("red")
                
        node_pose = nx.spring_layout(G)
        nx.draw_networkx(G,pos=node_pose, node_color=color_map)
        plt.show()
        
                        
        