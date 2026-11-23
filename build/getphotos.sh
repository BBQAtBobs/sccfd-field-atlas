B=https://www.sccfd.org/wp-content/uploads
while read n p; do curl -sL -m 60 -o "raw_$n.jpg" "$B/$p" && echo "$n $(stat -c%s raw_$n.jpg)"; done <<'L'
70 2025/07/Casa-de-Fruta.jpg
81 2021/11/Campbell-1200x800-1.jpg
71 2021/11/Cupertino-1200x800-1.jpg
74 2021/11/El-Monte-1200x800-1.jpg
75 2021/11/Los_Altos-07387.jpg
76 2021/11/Loyola-.jpg
83 2021/11/Los-Gatos-1200x800-1.jpg
68 2025/07/Masten.jpg
77 2021/11/Monte-Vista-1200x800-1.jpg
78 2023/08/Image-7800-Quito-Station.jpg
84 2024/02/SCC_3336.jpg
73 2021/11/Saratoga-1200x800-1.jpg
72 2021/11/Seven-Springs-1200x800-1.jpg
82 2021/11/Shannon2-1200x800-1.jpg
80 2021/11/Sunnyoaks-07107.jpg
69 2025/07/Treehaven.jpg
67 2025/07/Vineyard.jpg
85 2021/11/Winchester2-1200x800-1.jpg
79 2021/11/West-Valley-08450-1200x800-1.jpg
L
