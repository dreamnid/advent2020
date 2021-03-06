# Day 20
Note that you have to set the top left corner manually at the moment

seamonster.txt contents were copied from the site
Because get_file_input() strips out spaces which ruins the image mask, I decided to convert seamonster.txt
to seamonster_form.txt as a file of 0 and 1s. This was generated via: `sed -e 's/ /0/g' -e 's/#/1/g' seamonster.txt > seamonster_form.txt`

## Performance
```bash
(advent2020) ➜  20 git:(master) ✗ time python3 20.py         
Product of corner tiles:  17250897231301
------
['...####...........#.......##...#.#.##...................#...........#.#.#........###......#...##',
 '.........#.........#..#.............#.......O......##...#.#..#.................#...#........#..#',
 '..#........#....#........#O....OO....OO....OOO......#..........#.....#..#.................#...#.',
 '..#..#.....................O..O..O#.O..O..O......#..#.#..#.#..##..##......#.....#...........###.',
 '...#.#..##.#........#...##..#..#...........#.#.#.....#..#...##.#......#O.....#...#.#..#.........',
 '...........#.............#....#..#..#................O#...OO..##OO....OOO...........###.#.......',
 '.#....#.......#...#................#...#...#.#.......#O..O#.O#.O..O..O....#..#..#...........#...',
 '.....##.........#.#.......#..##.................#............#......#................#..........',
 '........#...#..###..#...##....#....#...........#............##.#.#.#...................#.#..#...',
 '.....#.....##...............#.........#......#.#....#............#.....#.#.#....##..#..#..#.#..#',
 '#........#...#.......##.......##.......#.......#..#................##.....##....#..#.......#....',
 '.........#.....##..#..#.#....#......#.#........#..#.........###....#.#..###..#........#.........',
 '..................##.....#..#...#...#..#..##.#....#.....#......#.#.#......#.....#....##..#......',
 '.##......##.........................###.....#....##...#.##...##.......#..................#......',
 '...###..........#............................##..#..#.#...............#...#.#....#.#....#.......',
 '....#.............##..#......##........##.#....##..............#............#..#O#.......#......',
 '...#.##..............#...#...#......#.....#..##.....#...##.#..O..#.OO..#.OO..#.OOO..............',
 '....##..................#.#.O#........##....#..#.#........#...#O..O..O..O..O#.O#.....#.......##.',
 '.......#..O.##.OO....OO....OOO...#........#...........#......#.......##.....#...................',
 '#......#..#O..O..O..O#.O..O......#..#...#.##....##.......#......#........#....#.##..#..#.....#..',
 '..##......#.........##.....#.#.....................####....##...#...#..###..#....#.#O...#.....#.',
 '.......#...#.............###..........#.....#..#..................O#...OO#.#.OO#...OOO#...#.#...',
 '.....#........#..#.............#....O.....#........#..#...#...#...#O..O.#O..O#.O..O..##.........',
 '.....#.#....#.....O....OO.#..OO....OOO....#.......#..#...#..............#...#.....#....#.#..#...',
 '....#......#......#O..O##O..O..O.#O.....#...#...#......##..........##...#.....#.#...#.......#.#.',
 '.........##.........#...#......#....#.......##...#.....#...O......#.##.#....#...##.......#....#.',
 '#..................#.....#.#..#.........#O..#.OO..#.OO...#OOO#.......#......#.##...........#.###',
 '.#......#..#.#...#......##...#..#...#..#..O..O.#O..O.#O..O..#.#..##.......##...#........#..#....',
 '....#...#.#......#.#...#......#..#.#............#....##....#.....#...#..#....#....#......##.....',
 '..#......#........##....####.......#.#.#.#....#.#..#...........#...........#................#...',
 '..#.......#............#.....#............#..#........##.#......#.........##.......#..#.#.#...#.',
 '#..#...#.#......#.#.......#........#.#.....#...#.#.#..#..##...........#.........#.###...........',
 '.........##......#.##...........#.##..#.##...#.........#......#...........#...#....#.#.O##......',
 '.......#.........#.#....#........#........#...#..O...............#...O.#.#OO....OO....OOO..#...#',
 '..##..#........#....O....#.#..#O....OO....OO....OOO##...........#.#..#O.#O..O.#O#.O#.O.......#..',
 '..O....OO...#OO#...OOO..........O..O..O..O.#O..O...........#.......#....#....#...#......#.......',
 '...O..O..O#.O..O#.O#..#........#....#............#.....#.........#.......#..#..#..#..#..#.......',
 '.#.......###.#.##.........#.#...#..#...#......#..........#...............#.##.#...........#.#...',
 '....#...........#..#..........#...#...#..................#...#..#.#.##......#.#..#......#..#....',
 '#.....#.#..........#....#..#..#..#......##.....#........#.#.....#..##.............#O...##...#...',
 '#...#..#....#........#....#..#.......#....#.....O.........#.#....O...#OO....OO...#OOO##.........',
 '......##..##...#.##..#........O....OO..#.OO#.##OOO......#...##.#.#O..O.#O#.O#.O..O......#.#...#.',
 '.#..#...#.#...............#....O..O.#O..O..O..O.......#..#.......#.....#......#.............#...',
 '.......#.#......#..#..#..##........#.....##.#.....#......#...#.......#.#.##.#...#.....#.........',
 '#.#.......#.....##...#....#...#......#............#.#.#......#.....#.......................#....',
 '#....#...#.......#...#.......#..#.#.#.##....O.........#.#.....#.......................#.........',
 '..###.........#.........#.O....OO..#.OO..#.OOO.............#...#..#..........##O................',
 '....##....#...#....#.O.....O..O..O..O..O..O....#...#..##....#O.#..OO....OO...#OOO.............##',
 '...O...#OO.##.OO#.##OOO#.........#............#.#.............O#.O..O..O..O..O.#..#....##..#..##',
 '...#O..O..O..O.#O..O..##.###.#.#...........#...##..........#..##.......#.#.#................#..#',
 '...#...#..........#..........#..................#...#...#.....#.##...#.....#..............#.#...',
 '..#..#.....#.......#......##......##......#................##..........#..#...O.##............#.',
 '...#.....#....#.#........#.......#.........#........#.......O....OO....OO...#OOO.#.#............',
 '#....##........#.#.....#.......##..##......#.....#...#....##.O..O..O..O..O..O#..#......#........',
 '#.........##.#.....##..O.#....#.................##.##.....#..#......#...#.................#.....',
 '..##.O.##.OO#.#.OO....OOO........##........##.....#...#.......#...##............#.....#.#..#...#',
 '.....#O..O..O##O#.O.#O.#.......#......#..##...............##...##.....#......##.##...#..........',
 '..#....#.#...#........##.....#........#...........#....#......#..###...#....#.............#.##..',
 '.....#......#......................##.#.#....#....#...##.........##.....................#...#...',
 '#........##.................#....#....##.......#..#.............#.......#....#..##...#..........',
 '.....##.....#....#.####..#...........#.......#...###..#.#....#.#.#..#.....#.....#...#...........',
 '..#............#...O......#...#.......#......#......#..........#.#.........#.#............#.....',
 '.O....OO#...OO....OOO.....#.#.#....##....................#.#.#.#...............##..#...#........',
 '.#O..O..O..O.#O..O.....#.......#..#..............#.....##........##....##....................#..',
 '........#..#.##.#.#........##...#.........#........#.####.....O.....#....#.....#.#......#..#...#',
 '#...#.....#........#...#....##.#..#....#..#.O....OO##..OO....OOO..............#..........##..##.',
 '#...#..#.......#.........##..#.#..#.......#..O..O..O..O..O#.O......#...#.................#......',
 '.##..........#..........#..#...............#............#......#............#...#...#.#.........',
 '...##.#.#....#.......#....#.....#....#........#...........#....#.......#..#.......###..#........',
 '...#.........#.....#..#.#....................#.......#.#....#....#....##......#......#......#...',
 '.#...........................##..#.#....####............#..#..#.....#..........#..#......#......',
 '..................#.####.................#..........##..#.............#......................#..',
 '......#..................##....#............#.......#......##.#................#...#...#......#.',
 '......#..#.....#.####..........#........##......#..#.....................#........#..#.......###',
 '..#.#................#..#...................#..#................#...#.....................#.##..',
 '#...#..................#...#........#...#.#..#.#..#............#....#..#......#.#......##...#...',
 '..##....#...........................#...#.....#....#...........#.......##..............##.......',
 '.......#.#...........###..#........O....#...#..#......#..........#........#..#....#.............',
 '................#O....OO.#..OO....OOO#......#......#..#..#...........#..#.#....#.....#.....#....',
 '...#.......#....#.O.#O..O..O..O..O.....#..#.#..#.###.......#...............#......#.....#.#....#',
 '#..##......#.#..#........#.......##....#.....#......##........#.#......#................O...#...',
 '...#..#.....#.....#.........#.#.......##..........#....#.#..#......#..O.###OO....OO....OOO......',
 '.#..#.#......#.#................#....#..#....#...#..#......#.....#.....O..O..O#.O..O..O.........',
 '......#.#....##..#.#............#......#....#.........#................................#.#....#.',
 '.#...#...#....####..#..........##.##......O##....##..............##........#......#..#.##.......',
 '#..#.#.#..........#.....O..##OO.##.OO....OOO....#..........#.#..#................#.#............',
 '..............#........#.O..O#.O##O.#O.#O....#..#.........#.......##.#.#................#...##..',
 '.#........#.##...........#.......####........#...#.#..#.......#..#.....#..##......#.............',
 '...........#....#...#............##........#..#..#.....#.#..............#..###........#.#.......',
 '.#..#..............#........#.##............#.#.#.....................#.#......#.......#........',
 '...........#.#...#...#....#....................#......#.#....#....#....#.#.......##...#.#.......',
 '.......#.....#.........O.##....#..#....#.....#....###.#.#..............#......#.#.......#...#..#',
 '.....O....OO....OO..#.OOO...#......#.....##..........#.#........#..#...#....#...........#.#.#...',
 '......O..O#.O..O..O..O.....#...........................#....#..#......#...........###.#......#..',
 '.......#...........#...........#.##.......##..........#...##....##.##........#...#.##.#.#...#...',
 '.........#.................###.....#..#..........#...#..#...###.....#.#..#.....##..#.....#......']
number of dragons 23
answer:  1576
python3 20.py  0.22s user 0.01s system 65% cpu 0.353 total
```
