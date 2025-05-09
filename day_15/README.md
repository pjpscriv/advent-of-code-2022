﻿<h2>--- Day 15: Beacon Exclusion Zone ---</h2><p>You feel the ground rumble again as the distress signal leads you to a large network of subterranean tunnels. You don't have time to search them all, but you don't need to: your pack contains a set of deployable <em>sensors</em> that you imagine were originally built to locate lost Elves.</p>
<p>The sensors aren't very powerful, but that's okay; your handheld device indicates that you're close enough to the source of the distress signal to use them. You pull the emergency sensor system out of your pack, hit the big button on top, and the sensors zoom off down the tunnels.</p>
<p>Once a sensor finds a spot it thinks will give it a good reading, it attaches itself to a hard surface and begins monitoring for the nearest signal source <em>beacon</em>. Sensors and beacons always exist at integer coordinates. Each sensor knows its own position and can <em>determine the position of a beacon precisely</em>; however, sensors can only lock on to the one beacon <em>closest to the sensor</em> as measured by the <a href="https://en.wikipedia.org/wiki/Taxicab_geometry" target="_blank">Manhattan distance</a>. (There is never a tie where two beacons are the same distance to a sensor.)</p>
<p>It doesn't take long for the sensors to report back their positions and closest beacons (your puzzle input). For example:</p>
<pre><code>Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
</code></pre>
<p>So, consider the sensor at <code>2,18</code>; the closest beacon to it is at <code>-2,15</code>. For the sensor at <code>9,16</code>, the closest beacon to it is at <code>10,16</code>.</p>
<p>Drawing sensors as <code>S</code> and beacons as <code>B</code>, the above arrangement of sensors and beacons looks like this:</p>
<pre><code>               1    1    2    2
     0    5    0    5    0    5
 0 ....S.......................
 1 ......................S.....
 2 ...............S............
 3 ................SB..........
 4 ............................
 5 ............................
 6 ............................
 7 ..........S.......S.........
 8 ............................
 9 ............................
10 ....B.......................
11 ..S.........................
12 ............................
13 ............................
14 ..............S.......S.....
15 B...........................
16 ...........SB...............
17 ................S..........B
18 ....S.......................
19 ............................
20 ............S......S........
21 ............................
22 .......................B....
</code></pre>
<p>This isn't necessarily a comprehensive map of all beacons in the area, though. Because each sensor only identifies its closest beacon, if a sensor detects a beacon, you know there are no other beacons that close or closer to that sensor. There could still be beacons that just happen to not be the closest beacon to any sensor. Consider the sensor at <code>8,7</code>:</p>
<pre><code>               1    1    2    2
     0    5    0    5    0    5
-2 ..........#.................
-1 .........###................
 0 ....S...#####...............
 1 .......#######........S.....
 2 ......#########S............
 3 .....###########SB..........
 4 ....#############...........
 5 ...###############..........
 6 ..#################.........
 7 .#########<em>S</em>#######S#........
 8 ..#################.........
 9 ...###############..........
10 ....<em>B</em>############...........
11 ..S..###########............
12 ......#########.............
13 .......#######..............
14 ........#####.S.......S.....
15 B........###................
16 ..........#SB...............
17 ................S..........B
18 ....S.......................
19 ............................
20 ............S......S........
21 ............................
22 .......................B....
</code></pre>
<p>This sensor's closest beacon is at <code>2,10</code>, and so you know there are no beacons that close or closer (in any positions marked <code>#</code>).</p>
<p>None of the detected beacons seem to be producing the distress signal, so you'll need to <span title="&quot;When you have eliminated all which is impossible, then whatever remains, however improbable, must be where the missing beacon is.&quot; - Sherlock Holmes">work out</span> where the distress beacon is by working out where it <em>isn't</em>. For now, keep things simple by counting the positions where a beacon cannot possibly be along just a single row.</p>
<p>So, suppose you have an arrangement of beacons and sensors like in the example above and, just in the row where <code>y=10</code>, you'd like to count the number of positions a beacon cannot possibly exist. The coverage from all sensors near that row looks like this:</p>
<pre><code>                 1    1    2    2
       0    5    0    5    0    5
 9 ...#########################...
<em>10 ..####B######################..</em>
11 .###S#############.###########.
</code></pre>
<p>In this example, in the row where <code>y=10</code>, there are <code><em>26</em></code> positions where a beacon cannot be present.</p>
<p>Consult the report from the sensors you just deployed. <em>In the row where <code>y=2000000</code>, how many positions cannot contain a beacon?</em></p>

<article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>Your handheld device indicates that the distress signal is coming from a beacon nearby. The distress beacon is not detected by any sensor, but the distress beacon must have <code>x</code> and <code>y</code> coordinates each no lower than <code>0</code> and no larger than <code>4000000</code>.</p>
<p>To isolate the distress beacon's signal, you need to determine its <em>tuning frequency</em>, which can be found by multiplying its <code>x</code> coordinate by <code>4000000</code> and then adding its <code>y</code> coordinate.</p>
<p>In the example above, the search space is smaller: instead, the <code>x</code> and <code>y</code> coordinates can each be at most <code>20</code>. With this reduced search area, there is only a single position that could have a beacon: <code>x=14, y=11</code>. The tuning frequency for this distress beacon is <code><em>56000011</em></code>.</p>
<p>Find the only possible position for the distress beacon. <em>What is its tuning frequency?</em></p>
