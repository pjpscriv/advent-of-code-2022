﻿<h2>--- Day 22: Monkey Map ---</h2><p>The monkeys take you on a surprisingly easy trail through the jungle. They're even going in roughly the right direction according to your handheld device's Grove Positioning System.</p>
<p>As you walk, the monkeys explain that the grove is protected by a <em>force field</em>. To pass through the force field, you have to enter a password; doing so involves tracing a specific <em>path</em> on a strangely-shaped board.</p>
<p>At least, you're pretty sure that's what you have to do; the elephants aren't exactly fluent in monkey.</p>
<p>The monkeys give you notes that they took when they last saw the password entered (your puzzle input).</p>
<p>For example:</p>
<pre><code>        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5
</code></pre>
<p>The first half of the monkeys' notes is a <em>map of the board</em>. It is comprised of a set of <em>open tiles</em> (on which you can move, drawn <code>.</code>) and <em>solid walls</em> (tiles which you cannot enter, drawn <code>#</code>).</p>
<p>The second half is a description of <em>the path you must follow</em>. It consists of alternating numbers and letters:</p>
<ul>
<li>A <em>number</em> indicates the <em>number of tiles to move</em> in the direction you are facing. If you run into a wall, you stop moving forward and continue with the next instruction.</li>
<li>A <em>letter</em> indicates whether to turn 90 degrees <em>clockwise</em> (<code>R</code>) or <em><span title="Or &quot;anticlockwise&quot;, if you're anti-counterclockwise.">counterclockwise</span></em> (<code>L</code>). Turning happens in-place; it does not change your current tile.</li>
</ul>
<p>So, a path like <code>10R5</code> means "go forward 10 tiles, then turn clockwise 90 degrees, then go forward 5 tiles".</p>
<p>You begin the path in the leftmost open tile of the top row of tiles. Initially, you are facing <em>to the right</em> (from the perspective of how the map is drawn).</p>
<p>If a movement instruction would take you off of the map, you <em>wrap around</em> to the other side of the board. In other words, if your next tile is off of the board, you should instead look in the direction opposite of your current facing as far as you can until you find the opposite edge of the board, then reappear there.</p>
<p>For example, if you are at <code>A</code> and facing to the right, the tile in front of you is marked <code>B</code>; if you are at <code>C</code> and facing down, the tile in front of you is marked <code>D</code>:</p>
<pre><code>        ...#
        .#..
        #...
        ....
...#.<em>D</em>.....#
........#...
<em>B</em>.#....#...<em>A</em>
.....<em>C</em>....#.
        ...#....
        .....#..
        .#......
        ......#.
</code></pre>
<p>It is possible for the next tile (after wrapping around) to be a <em>wall</em>; this still counts as there being a wall in front of you, and so movement stops before you actually wrap to the other side of the board.</p>
<p>By drawing the <em>last facing you had</em> with an arrow on each tile you visit, the full path taken by the above example looks like this:</p>
<pre><code>        &gt;&gt;v#    
        .#v.    
        #.v.    
        ..v.    
...#...v..v#    
&gt;&gt;&gt;v...<em>&gt;</em>#.&gt;&gt;    
..#v...#....    
...&gt;&gt;&gt;&gt;v..#.    
        ...#....
        .....#..
        .#......
        ......#.
</code></pre>
<p>To finish providing the password to this strange input device, you need to determine numbers for your final <em>row</em>, <em>column</em>, and <em>facing</em> as your final position appears from the perspective of the original map. Rows start from <code>1</code> at the top and count downward; columns start from <code>1</code> at the left and count rightward. (In the above example, row 1, column 1 refers to the empty space with no tile on it in the top-left corner.) Facing is <code>0</code> for right (<code>&gt;</code>), <code>1</code> for down (<code>v</code>), <code>2</code> for left (<code>&lt;</code>), and <code>3</code> for up (<code>^</code>). The <em>final password</em> is the sum of 1000 times the row, 4 times the column, and the facing.</p>
<p>In the above example, the final row is <code>6</code>, the final column is <code>8</code>, and the final facing is <code>0</code>. So, the final password is 1000 * 6 + 4 * 8 + 0: <code><em>6032</em></code>.</p>
<p>Follow the path given in the monkeys' notes. <em>What is the final password?</em></p>

<article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>As you reach the force field, you think you hear some Elves in the distance. Perhaps they've already arrived?</p>
<p>You approach the strange <em>input device</em>, but it isn't quite what the monkeys drew in their notes. Instead, you are met with a large <em>cube</em>; each of its six faces is a square of 50x50 tiles.</p>
<p>To be fair, the monkeys' map <em>does</em> have six 50x50 regions on it. If you were to <em>carefully fold the map</em>, you should be able to shape it into a cube!</p>
<p>In the example above, the six (smaller, 4x4) faces of the cube are:</p>
<pre><code>        1111
        1111
        1111
        1111
222233334444
222233334444
222233334444
222233334444
        55556666
        55556666
        55556666
        55556666
</code></pre>
<p>You still start in the same position and with the same facing as before, but the <em>wrapping</em> rules are different. Now, if you would walk off the board, you instead <em>proceed around the cube</em>. From the perspective of the map, this can look a little strange. In the above example, if you are at A and move to the right, you would arrive at B facing down; if you are at C and move down, you would arrive at D facing up:</p>
<pre><code>        ...#
        .#..
        #...
        ....
...#.......#
........#..<em>A</em>
..#....#....
.<em>D</em>........#.
        ...#..<em>B</em>.
        .....#..
        .#......
        ..<em>C</em>...#.
</code></pre>
<p>Walls still block your path, even if they are on a different face of the cube. If you are at E facing up, your movement is blocked by the wall marked by the arrow:</p>
<pre><code>        ...#
        .#..
     <em>--&gt;#</em>...
        ....
...#..<em>E</em>....#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.
</code></pre>
<p>Using the same method of drawing the <em>last facing you had</em> with an arrow on each tile you visit, the full path taken by the above example now looks like this:</p>
<pre><code>        &gt;&gt;v#    
        .#v.    
        #.v.    
        ..v.    
...#..<em>^</em>...v#    
.&gt;&gt;&gt;&gt;&gt;^.#.&gt;&gt;    
.^#....#....    
.^........#.    
        ...#..v.
        .....#v.
        .#v&lt;&lt;&lt;&lt;.
        ..v...#.
</code></pre>
<p>The final password is still calculated from your final position and facing from the perspective of the map. In this example, the final row is <code>5</code>, the final column is <code>7</code>, and the final facing is <code>3</code>, so the final password is 1000 * 5 + 4 * 7 + 3 = <code><em>5031</em></code>.</p>
<p>Fold the map into a cube, <em>then</em> follow the path given in the monkeys' notes. <em>What is the final password?</em></p>
