﻿<h2>--- Day 18: Boiling Boulders ---</h2><p>You and the elephants finally reach fresh air. You've emerged near the base of a large volcano that seems to be actively erupting! Fortunately, the lava seems to be flowing away from you and toward the ocean.</p>
<p>Bits of lava are still being ejected toward you, so you're sheltering in the cavern exit a little longer. Outside the cave, you can see the lava landing in a pond and hear it loudly hissing as it solidifies.</p>
<p>Depending on the specific compounds in the lava and speed at which it cools, it might be forming <a href="https://en.wikipedia.org/wiki/Obsidian" target="_blank">obsidian</a>! The cooling rate should be based on the surface area of the lava droplets, so you take a quick scan of a droplet as it flies past you (your puzzle input).</p>
<p>Because of how quickly the lava is moving, the scan isn't very good; its resolution is quite low and, as a result, it approximates the shape of the lava droplet with <em>1x1x1 <span title="Unfortunately, you forgot your flint and steel in another dimension.">cubes</span> on a 3D grid</em>, each given as its <code>x,y,z</code> position.</p>
<p>To approximate the surface area, count the number of sides of each cube that are not immediately connected to another cube. So, if your scan were only two adjacent cubes like <code>1,1,1</code> and <code>2,1,1</code>, each cube would have a single side covered and five sides exposed, a total surface area of <code><em>10</em></code> sides.</p>
<p>Here's a larger example:</p>
<pre><code>2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5
</code></pre>
<p>In the above example, after counting up all the sides that aren't connected to another cube, the total surface area is <code><em>64</em></code>.</p>
<p><em>What is the surface area of your scanned lava droplet?</em></p>

<article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>Something seems off about your calculation. The cooling rate depends on exterior surface area, but your calculation also included the surface area of air pockets trapped in the lava droplet.</p>
<p>Instead, consider only cube sides that could be reached by the water and steam as the lava droplet tumbles into the pond. The steam will expand to reach as much as possible, completely displacing any air on the outside of the lava droplet but never expanding diagonally.</p>
<p>In the larger example above, exactly one cube of air is trapped within the lava droplet (at <code>2,2,5</code>), so the exterior surface area of the lava droplet is <code><em>58</em></code>.</p>
<p><em>What is the exterior surface area of your scanned lava droplet?</em></p>
