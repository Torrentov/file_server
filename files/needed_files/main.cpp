#include <iostream>
#include <vector>
using namespace std;


int main()
{
    int tops, pillows, a, b, c;
    cin >> tops >> pillows;
    int edges[tops][tops];
    vector<int> ans;
    for (int i = 0; i < tops; i++)
    {
        for (int j = 0; j < tops; j++)
        {
            edges[i][j] = 0;
        }
    }
    int pills[pillows][3];
    for (int i = 0; i < pillows; i++)
    {
        cin >> a >> b >> c;
        pills[i][0] = a;
        pills[i][1] = b;
        pills[i][2] = c;
        a--;
        b--;
        c--;
        edges[a][b] = 1;
        edges[a][c] = 1;
        edges[b][a] = 1;
        edges[c][a] = 1;
        edges[b][c] = 1;
        edges[c][b] = 1;
    }
    for (int i = 0; i < pillows; i++)
    {
        a = pills[i][0];
        b = pills[i][1];
        c = pills[i][2];
        edges[a][b] = 0;
        edges[b][a] = 0;
        edges[c][b] = 0;
        edges[b][c] = 0;
        edges[a][c] = 0;
        edges[c][a] = 0;
        vector<int> wave_front;
        vector<int> new_front;
        wave_front.push_back(pills[i][0]);
        int used[tops];
        for (int it = 0; it < tops; it++)
        {
            used[tops] = 0;
        }
        int res = 0;
        while (wave_front.size() > 0)
        {
            for (int u = 0; u < wave_front.size(); u++)
            {
                for (int j = 0; j < tops; j++)
                {
                    if ((edges[wave_front[u]][j] == 1) && (used[j] == 0))
                    {
                        new_front.push_back(j);
                        used[j] = 1;
                    }
                    if (wave_front[u] == b)
                    {
                        res++;
                        edges[a][b] = 1;
                    }
                    if (wave_front[u] == c)
                    {
                        res++;
                        edges[a][c] = 1;
                    }
                }
            }
            wave_front.clear();
            for (int i = 0; i < new_front.size(); i++)
            {
                wave_front.push_back(new_front[i]);
            }
            new_front.clear();
        }
        if (res == 2)
        {
            ans.push_back(i + 1);
        }
    }
    int length = ans.size();
    cout << length << endl;
    for (int i = 0; i < length; i++)
    {
        cout << ans[i] << endl;
    }
    return 0;
}
