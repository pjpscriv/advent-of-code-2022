﻿<h2>--- Day 17: Pyroclastic Flow ---</h2><p>Your handheld device has located an alternative exit from the cave for you and the elephants.  The ground is rumbling almost continuously now, but the strange valves bought you some time. It's definitely getting warmer in here, though.</p>
<p>The tunnels eventually open into a very tall, narrow chamber. Large, oddly-shaped rocks are falling into the chamber from above, presumably due to all the rumbling. If you can't work out where the rocks will fall next, you might be <span title="I am the man who arranges the blocks / that descend upon me from up above!">crushed</span>!</p>
<p>The five types of rocks have the following peculiar shapes, where <code>#</code> is rock and <code>.</code> is empty space:</p>
<pre><code>####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##
</code></pre>
<p>The rocks fall in the order shown above: first the <code>-</code> shape, then the <code>+</code> shape, and so on. Once the end of the list is reached, the same order repeats: the <code>-</code> shape falls first, sixth, 11th, 16th, etc.</p>
<p>The rocks don't spin, but they do get pushed around by jets of hot gas coming out of the walls themselves. A quick scan reveals the effect the jets of hot gas will have on the rocks as they fall (your puzzle input).</p>
<p>For example, suppose this was the jet pattern in your cave:</p>
<pre><code>&gt;&gt;&gt;&lt;&lt;&gt;&lt;&gt;&gt;&lt;&lt;&lt;&gt;&gt;&lt;&gt;&gt;&gt;&lt;&lt;&lt;&gt;&gt;&gt;&lt;&lt;&lt;&gt;&lt;&lt;&lt;&gt;&gt;&lt;&gt;&gt;&lt;&lt;&gt;&gt;
</code></pre>
<p>In jet patterns, <code>&lt;</code> means a push to the left, while <code>&gt;</code> means a push to the right. The pattern above means that the jets will push a falling rock right, then right, then right, then left, then left, then right, and so on. If the end of the list is reached, it repeats.</p>
<p>The tall, vertical chamber is exactly <em>seven units wide</em>. Each rock appears so that its left edge is two units away from the left wall and its bottom edge is three units above the highest rock in the room (or the floor, if there isn't one).</p>
<p>After a rock appears, it alternates between <em>being pushed by a jet of hot gas</em> one unit (in the direction indicated by the next symbol in the jet pattern) and then <em>falling one unit down</em>. If any movement would cause any part of the rock to move into the walls, floor, or a stopped rock, the movement instead does not occur. If a <em>downward</em> movement would have caused a falling rock to move into the floor or an already-fallen rock, the falling rock stops where it is (having landed on something) and a new rock immediately begins falling.</p>
<p>Drawing falling rocks with <code>@</code> and stopped rocks with <code>#</code>, the jet pattern in the example above manifests as follows:</p>
<pre><code>The first rock begins falling:
|..@@@@.|
|.......|
|.......|
|.......|
+-------+

Jet of gas pushes rock right:
|...@@@@|
|.......|
|.......|
|.......|
+-------+

Rock falls 1 unit:
|...@@@@|
|.......|
|.......|
+-------+

Jet of gas pushes rock right, but nothing happens:
|...@@@@|
|.......|
|.......|
+-------+

Rock falls 1 unit:
|...@@@@|
|.......|
+-------+

Jet of gas pushes rock right, but nothing happens:
|...@@@@|
|.......|
+-------+

Rock falls 1 unit:
|...@@@@|
+-------+

Jet of gas pushes rock left:
|..@@@@.|
+-------+

Rock falls 1 unit, causing it to come to rest:
|..####.|
+-------+

A new rock begins falling:
|...@...|
|..@@@..|
|...@...|
|.......|
|.......|
|.......|
|..####.|
+-------+

Jet of gas pushes rock left:
|..@....|
|.@@@...|
|..@....|
|.......|
|.......|
|.......|
|..####.|
+-------+

Rock falls 1 unit:
|..@....|
|.@@@...|
|..@....|
|.......|
|.......|
|..####.|
+-------+

Jet of gas pushes rock right:
|...@...|
|..@@@..|
|...@...|
|.......|
|.......|
|..####.|
+-------+

Rock falls 1 unit:
|...@...|
|..@@@..|
|...@...|
|.......|
|..####.|
+-------+

Jet of gas pushes rock left:
|..@....|
|.@@@...|
|..@....|
|.......|
|..####.|
+-------+

Rock falls 1 unit:
|..@....|
|.@@@...|
|..@....|
|..####.|
+-------+

Jet of gas pushes rock right:
|...@...|
|..@@@..|
|...@...|
|..####.|
+-------+

Rock falls 1 unit, causing it to come to rest:
|...#...|
|..###..|
|...#...|
|..####.|
+-------+

A new rock begins falling:
|....@..|
|....@..|
|..@@@..|
|.......|
|.......|
|.......|
|...#...|
|..###..|
|...#...|
|..####.|
+-------+
</code></pre>
<p>The moment each of the next few rocks begins falling, you would see this:</p>
<pre><code>|..@....|
|..@....|
|..@....|
|..@....|
|.......|
|.......|
|.......|
|..#....|
|..#....|
|####...|
|..###..|
|...#...|
|..####.|
+-------+

|..@@...|
|..@@...|
|.......|
|.......|
|.......|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+

|..@@@@.|
|.......|
|.......|
|.......|
|....##.|
|....##.|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+

|...@...|
|..@@@..|
|...@...|
|.......|
|.......|
|.......|
|.####..|
|....##.|
|....##.|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+

|....@..|
|....@..|
|..@@@..|
|.......|
|.......|
|.......|
|..#....|
|.###...|
|..#....|
|.####..|
|....##.|
|....##.|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+

|..@....|
|..@....|
|..@....|
|..@....|
|.......|
|.......|
|.......|
|.....#.|
|.....#.|
|..####.|
|.###...|
|..#....|
|.####..|
|....##.|
|....##.|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+

|..@@...|
|..@@...|
|.......|
|.......|
|.......|
|....#..|
|....#..|
|....##.|
|....##.|
|..####.|
|.###...|
|..#....|
|.####..|
|....##.|
|....##.|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+

|..@@@@.|
|.......|
|.......|
|.......|
|....#..|
|....#..|
|....##.|
|##..##.|
|######.|
|.###...|
|..#....|
|.####..|
|....##.|
|....##.|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+
</code></pre>
<p>To prove to the elephants your simulation is accurate, they want to know how tall the tower will get after 2022 rocks have stopped (but before the 2023rd rock begins falling). In this example, the tower of rocks will be <code><em>3068</em></code> units tall.</p>
<p><em>How many units tall will the tower of rocks be after 2022 rocks have stopped falling?</em></p>

<article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>The elephants are not impressed by your simulation. They demand to know how tall the tower will be after <code><em>1000000000000</em></code> rocks have stopped! Only then will they feel confident enough to proceed through the cave.</p>
<p>In the example above, the tower would be <code><em>1514285714288</em></code> units tall!</p>
<p><em>How tall will the tower be after <code>1000000000000</code> rocks have stopped?</em></p>
