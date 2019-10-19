HTML_page_header = '''
<!DOCTYPE html>
<html>
<script src="http://d3js.org/d3.v3.min.js"></script>
<script src="d3.layout.cloud.js"></script>
<head>
    <title>Nube de Palabras</title>
</head>
<style>
    body {
        font-family:"Lucida Grande","Droid Sans",Arial,Helvetica,sans-serif;
    }
    .legend {
        border: 1px solid #555555;
        border-radius: 5px 5px 5px 5px;
        font-size: 0.8em;
        margin: 10px;
        padding: 8px;
    }
    .bld {
        font-weight: bold;
    }
</style>
<body>

</body>
<script>

    var frequency_list = [
'''

HTML_page_body ='''
          ];


    var color = d3.scale.linear()
            .domain([0,1,2,3,4,5,6,10,15,20,100])
            .range(["#ddd", "#ccc", "#bbb", "#aaa", "#999", "#888", "#777", "#666", "#555", "#444", "#333", "#222"]);

    d3.layout.cloud().size([850, 300])
            .words(frequency_list)
            .rotate(0)
            .fontSize(function(d) { return d.size; })
            .on("end", draw)
            .start();

    function draw(words) {
        d3.select("body").append("svg")
                .attr("width", 900)
                .attr("height", 350)
                .attr("class", "wordcloud")
                .append("g")
                // without the transform, words words would get cutoff to the left and top, they would
                // appear outside of the SVG area
                .attr("transform", "translate(370,200)")
                .selectAll("text")
                .data(words)
                .enter().append("text")
                .style("font-size", function(d) { return d.size + "px"; })
                .style("fill", function(d, i) { return color(i); })
                .attr("transform", function(d) {
                    return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
                })
                .text(function(d) { return d.text; });
    }
</script>

<div style="width: 40%;">
    <div class="legend">
        Las palabras de uso común son más grandes y ligeramente claras. Las palabras menos comunes son más pequeñas y más oscuras.
    </div>

</div>


</html>
'''


def read_words(file_name):
    result = []
    # put your code here
    TweetsFile = open(file_name, "r", encoding="utf-8");
    for line in TweetsFile:
        Elementos = line.split(" ");
        Cupla = (Elementos[0], int(Elementos[1]));
        result.append(Cupla);

    TweetsFile.close();
    return result


def get_top_words(words, n=100):
    sorted_by_second = sorted(words, key=lambda tup: tup[1]);
    words.reverse();
    Top = [];
    Counter0 = len(words)-1;
    Counter1 = 0;
    while (Counter1 < n)and(Counter0>=0):
      Top.append(words[Counter0]);
      Counter0 -= 1;
      Counter1 +=1;
    return Top


def get_top_hashtags(words, n=20):
    TextualAnalisis = [];
    Counter2 = 0;
    while (Counter2 < len(words)):
        TextualAnalisis.append((list(words[Counter2][0]), (words[Counter2][1])));
        Counter2 += 1;
    Candidates = [];
    Counter3 = 0;
    while (Counter3 < len(TextualAnalisis)):
        Counter4 = 0;
        while (Counter4 < len(TextualAnalisis[Counter3][0])):
             if "#" == TextualAnalisis[Counter3][0][Counter4]:
                 Candidates.append(words[Counter3]);
             Counter4 += 1;
        Counter3 += 1;

    sorted_by_second = sorted(Candidates, key=lambda tup: tup[1]);
    Candidates.reverse();
    Top = [];
    Counter0 = len(Candidates)-1;
    Counter1 = 0;
    while (Counter1 < n)and(Counter0>=0):
      Top.append(Candidates[Counter0]);
      Counter0 -= 1;
      Counter1 +=1;
    return Top


def get_top_users(words, n=20):
    TextualAnalisis = [];
    Counter2 = 0;
    while (Counter2 < len(words)):
        TextualAnalisis.append((list(words[Counter2][0]), (words[Counter2][1])));
        Counter2 += 1;
    Candidates = [];
    Counter3 = 0;
    while (Counter3 < len(TextualAnalisis)):
        Counter4 = 0;
        while (Counter4 < len(TextualAnalisis[Counter3][0])):
             if "@" == TextualAnalisis[Counter3][0][Counter4]:
                 Candidates.append(words[Counter3]);
             Counter4 += 1;
        Counter3 += 1;

    sorted_by_second = sorted(Candidates, key=lambda tup: tup[1]);
    Candidates.reverse();
    Top = [];
    Counter0 = len(Candidates)-1;
    Counter1 = 0;
    while (Counter1 < n)and(Counter0>=0):
      Top.append(Candidates[Counter0]);
      Counter0 -= 1;
      Counter1 +=1;

    return Top


def generate_cloud(words, scale, file_name):
    with open(file_name, 'w') as outfile:
        outfile.write(HTML_page_header)
        for w, f in words:
            outfile.write("{text: '" + w + "', size:" + str(f * scale) + "},")
        outfile.write("{text: 'none', size: 0}\n")
        outfile.write(HTML_page_body)

words = read_words('words.txt')
generate_cloud(get_top_words(words, 100), 0.3, 'word_cloud.html')
generate_cloud(get_top_hashtags(words, 20), 5, 'hashtag_cloud.html')
generate_cloud(get_top_users(words, 30), 3, 'user_cloud.html')
