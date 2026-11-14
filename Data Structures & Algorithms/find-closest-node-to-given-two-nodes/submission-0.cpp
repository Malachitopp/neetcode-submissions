class Solution {
public:
    int closestMeetingNode(vector<int>& edges, int node1, int node2) {

        auto n1 {distance(edges, node1)};
        auto n2 {distance(edges, node2)};

        int best_node {-1};
        int best_dist {INT_MAX};

        for (int i {}; i < edges.size(); i ++ )
        {
            if (n1[i] == -1 || n2[i] == -1) continue;

            int worst {std::max(n1[i], n2[i])}; 

            if (worst < best_dist) 
            {
                best_dist = worst; 
                best_node = i; 
            }


        }
        return best_node;
    }


    std::vector<int> distance(vector<int>& edges, int start){

        std:vector<int> dist(edges.size(), -1);

        int current {start};
        int counter {};

        while (current != -1 && dist[current] == -1)
        {
            dist[current] = counter;
            current = edges[current];
            counter++;

        }

        return dist; 

    }
};
