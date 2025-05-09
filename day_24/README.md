﻿<h2>--- Day 24: Blizzard Basin ---</h2><p>With everything replanted for next year (and with elephants and monkeys to tend the grove), you and the Elves leave for the extraction point.</p>
<p>Partway up the mountain that shields the grove is a flat, open area that serves as the extraction point. It's a bit of a climb, but nothing the expedition can't handle.</p>
<p>At least, that would normally be true; now that the mountain is covered in snow, things have become more difficult than the Elves are used to.</p>
<p>As the expedition reaches a valley that must be traversed to reach the extraction site, you find that strong, turbulent winds are pushing small <em>blizzards</em> of snow and sharp ice around the valley. It's a good thing everyone packed warm clothes! To make it across safely, you'll need to find a way to avoid them.</p>
<p>Fortunately, it's easy to see all of this from the entrance to the valley, so you make a map of the valley and the blizzards (your puzzle input). For example:</p>
<pre><code>#.#####
#.....#
#&gt;....#
#.....#
#...v.#
#.....#
#####.#
</code></pre>
<p>The walls of the valley are drawn as <code>#</code>; everything else is ground. Clear ground - where there is currently no blizzard - is drawn as <code>.</code>. Otherwise, blizzards are drawn with an arrow indicating their direction of motion: up (<code>^</code>), down (<code>v</code>), left (<code>&lt;</code>), or right (<code>&gt;</code>).</p>
<p>The above map includes two blizzards, one moving right (<code>&gt;</code>) and one moving down (<code>v</code>). In one minute, each blizzard moves one position in the direction it is pointing:</p>
<pre><code>#.#####
#.....#
#.&gt;...#
#.....#
#.....#
#...v.#
#####.#
</code></pre>
<p>Due to <span title="I think, anyway. Do I look like a theoretical blizzacist?">conservation of blizzard energy</span>, as a blizzard reaches the wall of the valley, a new blizzard forms on the opposite side of the valley moving in the same direction. After another minute, the bottom downward-moving blizzard has been replaced with a new downward-moving blizzard at the top of the valley instead:</p>
<pre><code>#.#####
#...v.#
#..&gt;..#
#.....#
#.....#
#.....#
#####.#
</code></pre>
<p>Because blizzards are made of tiny snowflakes, they pass right through each other. After another minute, both blizzards temporarily occupy the same position, marked <code>2</code>:</p>
<pre><code>#.#####
#.....#
#...2.#
#.....#
#.....#
#.....#
#####.#
</code></pre>
<p>After another minute, the situation resolves itself, giving each blizzard back its personal space:</p>
<pre><code>#.#####
#.....#
#....&gt;#
#...v.#
#.....#
#.....#
#####.#
</code></pre>
<p>Finally, after yet another minute, the rightward-facing blizzard on the right is replaced with a new one on the left facing the same direction:</p>
<pre><code>#.#####
#.....#
#&gt;....#
#.....#
#...v.#
#.....#
#####.#
</code></pre>
<p>This process repeats at least as long as you are observing it, but probably forever.</p>
<p>Here is a more complex example:</p>
<pre><code>#.######
#&gt;&gt;.&lt;^&lt;#
#.&lt;..&lt;&lt;#
#&gt;v.&gt;&lt;&gt;#
#&lt;^v^^&gt;#
######.#
</code></pre>
<p>Your expedition begins in the only non-wall position in the top row and needs to reach the only non-wall position in the bottom row. On each minute, you can <em>move</em> up, down, left, or right, or you can <em>wait</em> in place. You and the blizzards act <em>simultaneously</em>, and you cannot share a position with a blizzard.</p>
<p>In the above example, the fastest way to reach your goal requires <code><em>18</em></code> steps. Drawing the position of the expedition as <code>E</code>, one way to achieve this is:</p>
<pre><code>Initial state:
#<em>E</em>######
#&gt;&gt;.&lt;^&lt;#
#.&lt;..&lt;&lt;#
#&gt;v.&gt;&lt;&gt;#
#&lt;^v^^&gt;#
######.#
<br/>
Minute 1, move down:
#.######
#<em>E</em>&gt;3.&lt;.#
#&lt;..&lt;&lt;.#
#&gt;2.22.#
#&gt;v..^&lt;#
######.#
<br/>
Minute 2, move down:
#.######
#.2&gt;2..#
#<em>E</em>^22^&lt;#
#.&gt;2.^&gt;#
#.&gt;..&lt;.#
######.#
<br/>
Minute 3, wait:
#.######
#&lt;^&lt;22.#
#<em>E</em>2&lt;.2.#
#&gt;&lt;2&gt;..#
#..&gt;&lt;..#
######.#
<br/>
Minute 4, move up:
#.######
#<em>E</em>&lt;..22#
#&lt;&lt;.&lt;..#
#&lt;2.&gt;&gt;.#
#.^22^.#
######.#
<br/>
Minute 5, move right:
#.######
#2<em>E</em>v.&lt;&gt;#
#&lt;.&lt;..&lt;#
#.^&gt;^22#
#.2..2.#
######.#
<br/>
Minute 6, move right:
#.######
#&gt;2<em>E</em>&lt;.&lt;#
#.2v^2&lt;#
#&gt;..&gt;2&gt;#
#&lt;....&gt;#
######.#
<br/>
Minute 7, move down:
#.######
#.22^2.#
#&lt;v<em>E</em>&lt;2.#
#&gt;&gt;v&lt;&gt;.#
#&gt;....&lt;#
######.#
<br/>
Minute 8, move left:
#.######
#.&lt;&gt;2^.#
#.<em>E</em>&lt;&lt;.&lt;#
#.22..&gt;#
#.2v^2.#
######.#
<br/>
Minute 9, move up:
#.######
#&lt;<em>E</em>2&gt;&gt;.#
#.&lt;&lt;.&lt;.#
#&gt;2&gt;2^.#
#.v&gt;&lt;^.#
######.#
<br/>
Minute 10, move right:
#.######
#.2<em>E</em>.&gt;2#
#&lt;2v2^.#
#&lt;&gt;.&gt;2.#
#..&lt;&gt;..#
######.#
<br/>
Minute 11, wait:
#.######
#2^<em>E</em>^2&gt;#
#&lt;v&lt;.^&lt;#
#..2.&gt;2#
#.&lt;..&gt;.#
######.#
<br/>
Minute 12, move down:
#.######
#&gt;&gt;.&lt;^&lt;#
#.&lt;<em>E</em>.&lt;&lt;#
#&gt;v.&gt;&lt;&gt;#
#&lt;^v^^&gt;#
######.#
<br/>
Minute 13, move down:
#.######
#.&gt;3.&lt;.#
#&lt;..&lt;&lt;.#
#&gt;2<em>E</em>22.#
#&gt;v..^&lt;#
######.#
<br/>
Minute 14, move right:
#.######
#.2&gt;2..#
#.^22^&lt;#
#.&gt;2<em>E</em>^&gt;#
#.&gt;..&lt;.#
######.#
<br/>
Minute 15, move right:
#.######
#&lt;^&lt;22.#
#.2&lt;.2.#
#&gt;&lt;2&gt;<em>E</em>.#
#..&gt;&lt;..#
######.#
<br/>
Minute 16, move right:
#.######
#.&lt;..22#
#&lt;&lt;.&lt;..#
#&lt;2.&gt;&gt;<em>E</em>#
#.^22^.#
######.#
<br/>
Minute 17, move down:
#.######
#2.v.&lt;&gt;#
#&lt;.&lt;..&lt;#
#.^&gt;^22#
#.2..2<em>E</em>#
######.#
<br/>
Minute 18, move down:
#.######
#&gt;2.&lt;.&lt;#
#.2v^2&lt;#
#&gt;..&gt;2&gt;#
#&lt;....&gt;#
######<em>E</em>#
</code></pre>
<p><em>What is the fewest number of minutes required to avoid the blizzards and reach the goal?</em></p>

<article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>As the expedition reaches the far side of the valley, one of the Elves looks especially dismayed:</p>
<p>He <em>forgot his snacks</em> at the entrance to the valley!</p>
<p>Since you're so good at dodging blizzards, the Elves humbly request that you go back for his snacks. From the same initial conditions, how quickly can you make it from the start to the goal, then back to the start, then back to the goal?</p>
<p>In the above example, the first trip to the goal takes <code>18</code> minutes, the trip back to the start takes <code>23</code> minutes, and the trip back to the goal again takes <code>13</code> minutes, for a total time of <code><em>54</em></code> minutes.</p>
<p><em>What is the fewest number of minutes required to reach the goal, go back to the start, then reach the goal again?</em></p>
